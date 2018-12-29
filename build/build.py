#! /usr/bin/env python

import argparse
import functools
import glob
import os
import multiprocessing
import subprocess
import shutil
import sys

def __projects() :

	configFiles = glob.glob( "*/config.py" )
	return sorted( [ os.path.split( f )[0] for f in configFiles ] )

def __loadConfig( project, buildDir ) :

	# Load file. Really we want to use JSON to
	# enforce a "pure data" methodology, but JSON
	# doesn't allow comments so we use Python
	# instead. Because we use `eval` and don't expose
	# any modules, there's not much beyond JSON
	# syntax that we can use in practice.

	with open( project + "/config.py" ) as f :
		config =f.read()

	config = eval( config )

	# Apply platform-specific config overrides.

	platform = "platform:osx" if sys.platform == "darwin" else "platform:linux"
	platformOverrides = config.pop( platform, {} )
	for key, value in platformOverrides.items() :

		if isinstance( value, dict ) and key in config :
			config[key].update( value )
		else :
			config[key] = value

	# Apply variable substitutions.

	variables = config.get( "variables", {} ).copy()
	variables.update( {
		"buildDir" : buildDir,
		"jobs" : multiprocessing.cpu_count(),
		"path" : os.environ["PATH"],
	} )

	def __substitute( o ) :

		if isinstance( o, dict ) :
			return { k : __substitute( v ) for k, v in o.items() }
		elif isinstance( o, list ) :
			return [ __substitute( x ) for x in o ]
		elif isinstance( o, tuple ) :
			return tuple( __substitute( x ) for x in o )
		elif isinstance( o, str ) :
			while True :
				s = o.format( **variables )
				if s == o :
					return s
				else :
					o = s

	return __substitute( config )

def __loadConfigs( buildDir ) :

	result = {}
	for project in __projects() :
		result[project] = __loadConfig( project, buildDir )

	return result

def __decompress( archive ) :

	command = "tar -xvf {archive}".format( archive=archive )
	sys.stderr.write( command + "\n" )
	files = subprocess.check_output( command, stderr=subprocess.STDOUT, shell = True )
	files = [ f for f in files.split( "\n" ) if f ]
	files = [ f[2:] if f.startswith( "x " ) else f for f in files ]
	dirs = { f.split( "/" )[0] for f in files }
	assert( len( dirs ) ==  1 )
	return next( iter( dirs ) )

def __preserveCurrentDirectory( f ) :

	@functools.wraps( f )
	def decorated( *args, **kw ) :
		d = os.getcwd()
		try :
			return f( *args, **kw )
		finally :
			os.chdir( d )

	return decorated

@__preserveCurrentDirectory
def __buildProject( project, config, buildDir ) :

	archiveDir = project + "/archives"
	if not os.path.exists( archiveDir ) :
		os.makedirs( archiveDir )

	archives = []
	for download in config["downloads"] :

		archivePath = os.path.join( archiveDir, os.path.basename( download ) )
		archives.append( archivePath )

		if os.path.exists( archivePath ) :
			continue

		downloadCommand = "curl -L {0} > {1}".format( download, archivePath )
		sys.stderr.write( downloadCommand + "\n" )
		subprocess.check_call( downloadCommand, shell = True )

	workingDir = project + "/working"
	if os.path.exists( workingDir ) :
		shutil.rmtree( workingDir )
	os.makedirs( workingDir )
	os.chdir( workingDir )

	decompressedArchives = [ __decompress( "../../" + a ) for a in archives ]
	os.chdir( decompressedArchives[0] )

	if config["license"] is not None :
		licenseDir = os.path.join( buildDir, "doc/licenses" )
		if not os.path.exists( licenseDir ) :
			os.makedirs( licenseDir )
		if os.path.isfile( config["license"] ) :
			shutil.copy( config["license"], os.path.join( licenseDir, project ) )
		else :
			shutil.copytree( config["license"], os.path.join( licenseDir, project ) )

	for patch in glob.glob( "../../patches/*.patch" ) :
		subprocess.check_call( "patch -p1 < {patch}".format( patch = patch ), shell = True )

	environment = os.environ.copy()
	for k, v in config.get( "environment", {} ).items() :
		environment[k] = os.path.expandvars( v )

	for command in config["commands"] :
		sys.stderr.write( command + "\n" )
		subprocess.check_call( command, shell = True, env = environment )

	for link in config.get( "symbolicLinks", [] ) :
		if os.path.exists( link[0] ) :
			os.remove( link[0] )
		os.symlink( link[1], link[0] )

def __buildProjects( projects, configs, buildDir ) :

	built = set()
	def walk( project, configs, buildDir ) :

		if project in built :
			return

		for dependency in configs[project].get( "dependencies", [] ) :
			walk( dependency, configs, buildDir )

		__buildProject( project, configs[project], buildDir )
		built.add( project )

	for project in projects :
		walk( project, configs, buildDir )

parser = argparse.ArgumentParser()

parser.add_argument(
	"--projects",
	choices = __projects(),
	nargs = "+",
	default = __projects(),
	help = "The projects to build."
)

parser.add_argument(
	"--buildDir",
	required = True,
	help = "The directory to put the builds in."
)

args = parser.parse_args()

configs = __loadConfigs( args.buildDir )
__buildProjects( args.projects, configs, args.buildDir )

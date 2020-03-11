{

	"downloads" : [

		"https://github.com/AcademySoftwareFoundation/openvdb/archive/v7.0.0.tar.gz"

	],

	"license" : "LICENSE",

	"dependencies" : [ "Blosc", "TBB", "OpenEXR", "Python" ],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"commands" : [

		"mkdir build",
		"cd build && cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D OPENVDB_BUILD_PYTHON_MODULE=ON"
			" -D PYOPENVDB_INSTALL_DIRECTORY={buildDir}/python"
			" .."
		,

		"cd build && make VERBOSE=1 -j {jobs} && make install",

	],

	"manifest" : [

		"include/openvdb",
		"include/pyopenvdb.h",
		"lib/libopenvdb*{sharedLibraryExtension}*",
		"python/pyopenvdb*",

	],

}

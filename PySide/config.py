{

	"downloads" : [

		"http://download.qt.io/official_releases/QtForPython/pyside2/PySide2-5.12.0-src/pyside-setup-everywhere-src-5.12.0.tar.xz"

	],

	"license" : "LICENSE.LGPLv3",

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"PATH" : "{buildDir}/bin:{path}",

	},

	"commands" : [

		# We build clang so we can compile LLVM bitcode during the OSL build.
		# But having this clang on the path breaks the PySide build, which needs
		# to be done with the system clang. Remove our custom clang.
		"rm -f {buildDir}/bin/clang*",
		"python setup.py --ignore-git --skip-docs --skip-modules=QtWebChannel --parallel {jobs} install",

	],

}

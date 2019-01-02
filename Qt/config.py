{

	"downloads" : [

		"http://download.qt.io/official_releases/qt/5.12/5.12.0/single/qt-everywhere-src-5.12.0.tar.xz"

	],

	"license" : "LICENSE.LGPLv21",

	"dependencies" : [ "LibPNG", "LibTIFF", "LibJPEG-Turbo", "FreeType" ],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",

	},

	"variables" : {

		# Make sure we pick up the python headers from {buildDir},
		# rather than any system level headers. We refer to this
		# variable in "commands" below.
		"pythonIncludeDir" : "{buildDir}/include/python2.7",

	},

	"commands" : [

		"./configure"
			" -prefix {buildDir}"
			" -plugindir {buildDir}/qt/plugins"
			" -release"
			" -opensource -confirm-license"
			" -no-rpath"
			" -no-dbus"
			" -skip qtconnectivity"
			" -skip qtwebengine"
			" -skip qt3d"
			" -skip qtdeclarative"
			" -no-libudev"
			" -no-icu"
			" -qt-pcre"
			" -nomake examples"
			" -nomake tests"
			" {extraArgs}"
			" -I {buildDir}/include -I {buildDir}/include/freetype2"
			" -L {buildDir}/lib",

		"make -j {jobs} && make install",

	],

	"manifest" : [

		"bin/moc",
		"bin/qmake",
		"bin/rcc",
		"bin/uic",

		"include/Qt*",

		"lib/libQt*",
		"lib/Qt*.framework",

		"mkspecs",
		"qt",
		"lib/cmake",

	],

	"platform:osx" : {

		"variables" : {

			"extraArgs" : "-no-freetype",

		},

	},

	"platform:linux" : {

		"variables" : {

			"extraArgs" : "-qt-xcb",

		},

	},

}

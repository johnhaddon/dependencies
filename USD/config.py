{

	"downloads" : [

		"https://github.com/PixarAnimationStudios/USD/archive/v18.09.tar.gz"

	],

	"license" : "LICENSE.txt",

	"dependencies" : [ "Boost", "Python", "OpenImageIO", "TBB", "Alembic" ],

	"commands" : [

		"cmake"
			" -D CMAKE_INSTALL_PREFIX={buildDir}"
			" -D CMAKE_PREFIX_PATH={buildDir}"
			" -D Boost_NO_SYSTEM_PATHS=TRUE"
			" -D Boost_NO_BOOST_CMAKE=TRUE"
			" -D PXR_BUILD_IMAGING=FALSE"
			" -D PXR_BUILD_TESTS=FALSE"
			# Needed to prevent CMake picking up system python libraries on Mac.
			" -D CMAKE_FRAMEWORK_PATH={buildDir}/lib/Python.framework/Versions/2.7/lib"
			" ."
		,

		"make VERBOSE=1 -j {jobs}",
		"make install",

		"mv {buildDir}/lib/python/pxr {buildDir}/python",

	],

	"manifest" : [

		"bin/usd*",
		"bin/sdfdump",

		"include/pxr",

		"lib/libtrace{sharedLibrarySuffix}",
		"lib/libarch{sharedLibrarySuffix}",
		"lib/libtf{sharedLibrarySuffix}",
		"lib/libjs{sharedLibrarySuffix}",
		"lib/libwork{sharedLibrarySuffix}",
		"lib/libplug{sharedLibrarySuffix}",
		"lib/libkind{sharedLibrarySuffix}",
		"lib/libgf{sharedLibrarySuffix}",
		"lib/libvt{sharedLibrarySuffix}",
		"lib/libar{sharedLibrarySuffix}",
		"lib/libsdf{sharedLibrarySuffix}",
		"lib/libpcp{sharedLibrarySuffix}",
		"lib/libusd*{sharedLibrarySuffix}",
		"lib/usd",

		"python/pxr",

		"share/usd",

	],

}

{

	"downloads" : [

		"https://support.hdfgroup.org/ftp/HDF5/current18/src/hdf5-1.8.20.tar.gz"

	],

	"license" : "COPYING",

	"commands" : [

		"./configure --prefix={buildDir} --enable-threadsafe --disable-hl --with-pthread=/usr/include",

		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"lib/libhdf5*{sharedLibrarySuffix}*",

	],

}

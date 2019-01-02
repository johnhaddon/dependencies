{

	"downloads" : [

		"https://download.savannah.gnu.org/releases/freetype/freetype-2.9.1.tar.gz",

	],

	"license" : "docs/FTL.TXT",

	"environment" : {

		"LDFLAGS" : "-L{buildDir}/lib",

	},

	"commands" : [

		"./configure --prefix={buildDir} --with-harfbuzz=no",
		"make -j {jobs}",
		"make install",

	],

	"manifest" : [

		"include/freetype2",
		"lib/libfreetype*{sharedLibrarySuffix}*",

	],

}

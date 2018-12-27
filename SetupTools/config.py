# We don't need setuptools ourselves, but PySide needs it as part of its
# install process. PySide actually tries to download it itself if it can't
# find it, but the ez_setup script it uses to do that is totally broken.
{

	"downloads" : [

		"https://files.pythonhosted.org/packages/37/1b/b25507861991beeade31473868463dad0e58b1978c209de27384ae541b0b/setuptools-40.6.3.zip"

	],

	"license" : "LICENSE",

	"dependencies" : [ "Python" ],

	"environment" : {

		"LD_LIBRARY_PATH" : "{buildDir}/lib",
		"PATH" : "{buildDir}/bin",

	},

	"commands" : [

		"python bootstrap.py",
		"python setup.py install",

	],

}

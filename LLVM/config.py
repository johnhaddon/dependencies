{

	"downloads" : [

		"https://github.com/llvm/llvm-project/releases/download/llvmorg-7.1.0/llvm-7.1.0.src.tar.xz",
		"https://github.com/llvm/llvm-project/releases/download/llvmorg-7.1.0/cfe-7.1.0.src.tar.xz"

	],

	"license" : "LICENSE.TXT",

	"commands" : [

		"mv ../cfe* tools/clang",
		"mkdir build",
		"cd build &&"
			" cmake"
			" -DCMAKE_INSTALL_PREFIX={buildDir}"
			" -DCMAKE_BUILD_TYPE=Release"
			" -DLLVM_ENABLE_RTTI=ON"
			" ..",
		"cd build && make install -j {jobs}"

	],

}

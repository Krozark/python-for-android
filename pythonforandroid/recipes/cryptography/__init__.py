from pythonforandroid.recipe import RustCompiledComponentsRecipe
from os.path import join


class CryptographyRecipe(RustCompiledComponentsRecipe):

    name = 'cryptography'
    version = '46.0.3'
    url = 'https://github.com/pyca/cryptography/archive/refs/tags/{version}.tar.gz'
    depends = ['openssl', 'cffi']
    hostpython_prerequisites = ['maturin']

    def get_recipe_env(self, arch, **kwargs):
        env = super().get_recipe_env(arch, **kwargs)
        openssl_build_dir = self.get_recipe('openssl', self.ctx).get_build_dir(arch.arch)
        build_target = self.RUST_ARCH_CODES[arch.arch].upper().replace("-", "_")
        openssl_include = "{}_OPENSSL_INCLUDE_DIR".format(build_target)
        openssl_libs = "{}_OPENSSL_LIB_DIR".format(build_target)
        env[openssl_include] = join(openssl_build_dir, 'include')
        env[openssl_libs] = join(openssl_build_dir)
        env["ANDROID_API_LEVEL"] = str(self.ctx.ndk_api)
        # maturin invokes the Android Python to run cryptography-cffi's build
        # script, which needs cffi to be importable.  cffi for the target arch
        # lives in get_python_install_dir, not the host site-packages that
        # PYTHONPATH is already set to.
        target_site = self.ctx.get_python_install_dir(arch.arch)
        env["PYTHONPATH"] = target_site + ":" + env.get("PYTHONPATH", "")
        return env


recipe = CryptographyRecipe()
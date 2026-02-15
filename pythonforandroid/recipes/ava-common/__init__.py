from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    version = 'master'
    url = 'https://github.com/Krozark/Ava-common/archive/refs/heads/{version}.tar.gz'
    depends = ['setuptools']


recipe = AvaCommonRecipe()

from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    name = 'ava-common'
    version = '1.4.1'
    url = 'https://github.com/Krozark/Ava-common/archive/{version}.tar.gz'
    depends = ['setuptools']


recipe = AvaCommonRecipe()

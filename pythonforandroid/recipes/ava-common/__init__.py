from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    version = '1.3.0'
    url = 'git+https://github.com/Krozark/Ava-common'
    depends = ['setuptools']


recipe = AvaCommonRecipe()

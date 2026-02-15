from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    version = 'master'
    url = 'git+https://github.com/Krozark/Ava-common/'
    depends = ['setuptools']


recipe = AvaCommonRecipe()

from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    name = 'ava-common'
    # version = 'master'
    version = '1.4.3'
    url = 'git+https://github.com/Krozark/Ava-common/'
    depends = ['setuptools']


recipe = AvaCommonRecipe()

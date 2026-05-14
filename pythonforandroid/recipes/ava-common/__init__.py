from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    name = 'ava-common'
    version = '26.05.14'
    # version = 'master'
    url = 'git+https://github.com/Krozark/Ava-common/'
    depends = []


recipe = AvaCommonRecipe()

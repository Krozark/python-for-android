from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    name = 'ava-common'
    version = '1.4.4'
    # version = 'master'
    url = 'git+https://github.com/Krozark/Ava-common/'
    depends = []


recipe = AvaCommonRecipe()

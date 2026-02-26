from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    name = 'sound-player'
    version = '1.0.8'
    url = 'https://github.com/Krozark/sound-player/archive/{version}.tar.gz'
    depends = ['setuptools']


recipe = AvaCommonRecipe()

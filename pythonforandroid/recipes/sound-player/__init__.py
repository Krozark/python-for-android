from pythonforandroid.recipe import PyProjectRecipe


class SoundPlayerRecipe(PyProjectRecipe):
    name = 'sound-player'
    version = '1.1.0'
    url = 'https://github.com/Krozark/sound-player/archive/{version}.tar.gz'
    depends = ['setuptools']


recipe = SoundPlayerRecipe()

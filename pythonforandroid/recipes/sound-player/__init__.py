import os

from pythonforandroid.recipe import PyProjectRecipe


class SoundPlayerRecipe(PyProjectRecipe):
    name = 'sound-player'
    version = "master"
    url = 'git+https://github.com/Krozark/sound-player/'
    depends = ['setuptools']

    def download(self):
        os.environ['GIT_LFS_SKIP_SMUDGE'] = '1'
        super().download()


recipe = SoundPlayerRecipe()

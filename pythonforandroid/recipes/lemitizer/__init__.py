from pythonforandroid.recipe import PyProjectRecipe


class LemmatizerRecipe(PyProjectRecipe):
    name = 'lemmatizer'
    version = '0.2.1'
    url = 'https://github.com/Krozark/lemmatizer/archive/{version}.tar.gz'
    depends = ['setuptools']


recipe = LemmatizerRecipe()

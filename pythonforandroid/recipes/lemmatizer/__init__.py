from pythonforandroid.recipe import PyProjectRecipe


class LemmatizerRecipe(PyProjectRecipe):
    name = 'lemmatizer'
    version = '0.2.3'
    url = 'git+https://github.com/Krozark/lemmatizer/'
    depends = ['setuptools']


recipe = LemmatizerRecipe()

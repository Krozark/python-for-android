from pythonforandroid.recipe import PyProjectRecipe


class LemmatizerRecipe(PyProjectRecipe):
    name = 'lemmatizer'
    version = '0.2.1'
    url = 'git+https://github.com/Krozark/lemmatizer/'
    depends = ['setuptools']


recipe = LemmatizerRecipe()

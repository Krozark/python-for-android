from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    site_packages_name = 'ava-common'
    version = '1.0.0'
    url = 'git+https://github.com/Krozark/Ava-common'
    depends = ['jsonschema']

recipe = AvaCommonRecipe()

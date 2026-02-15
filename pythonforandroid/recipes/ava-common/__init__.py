from pythonforandroid.recipe import PyProjectRecipe


class AvaCommonRecipe(PyProjectRecipe):
    site_packages_name = 'ava-common'
    version = 'master'
    url = 'git+https://github.com/Krozark/Ava-common'
    depends = ['jsonschema']

recipe = AvaCommonRecipe()

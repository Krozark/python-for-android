from pythonforandroid.recipe import PyProjectRecipe


class JsonschemaRecipe(PyProjectRecipe):
    version = "4.17.3"
    url = "https://files.pythonhosted.org/packages/36/3d/ca032d5ac064dff543aa13c984737795ac81abc9fb130cd2fcff17cfabc7/jsonschema-4.17.3.tar.gz"

    depends = [
        "pyrsistent",
        "attrs",
    ]


recipe = JsonschemaRecipe()

from pythonforandroid.recipe import PythonRecipe


class BitstringRecipe(PythonRecipe):
    version = "4.4.0"
    url = "https://pypi.python.org/packages/source/b/bitstring/bitstring-{version}.tar.gz"
    depends = ["setuptools", "bitarray", "tibs"]
    call_hostpython_via_targetpython = False


recipe = BitstringRecipe()

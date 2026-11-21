from pythonforandroid.recipe import PythonRecipe


class kivyMDRecipe(PythonRecipe):
    version = "2.0.0"
    url = "https://github.com/Krozark/kivymd/archive/{version}.zip"

    depends = [
        "kivy",
        "pillow",
        "materialyoucolor",
        "materialshapes",
        "asyncgui",
        "asynckivy",
    ]
    site_packages_name = "kivyMD"
    patches = ["kv.patch"]
    call_hostpython_via_targetpython = False
    install_in_hostpython = True


recipe = kivyMDRecipe()

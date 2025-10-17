from pythonforandroid.recipe import PyProjectRecipe


class MeteofranceApiRecipe(PyProjectRecipe):
    version = "1.4.0"
    url = "https://files.pythonhosted.org/packages/87/15/1c8fe7e537042e9d83d5fc4707c2632483c95194418b7cf75fc261739674/meteofrance_api-1.4.0.tar.gz"
    name = "meteofrance-api"
    depends = [
        "urllib3",
        "charset-normalizer",
        "typing_extensions",
        "certifi",
        "pytz",
        "idna",
    ]


recipe = MeteofranceApiRecipe()

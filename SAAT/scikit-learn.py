from pythonforandroid.recipe import Recipe


class SciKitLearnRecipe(Recipe):
    version = '1.0.1'
    url = f'https://github.com/scikit-learn/scikit-learn/archive/refs/tags/{version}.tar.gz'


    depends = ["numpy", "scipy", "joblib", "threadpoolctl"]


recipe = SciKitLearnRecipe()

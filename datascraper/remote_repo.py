import requests

class RemoteRepo():
    """A class returning Json data either from a local repository
      (local json file) or from a remote repository.
    """

    def get_data(self, query):
        """ Returns:
                JsonObject: A Json representation of the data.
        """
        url = f"https://thecocktaildb.com/api/json/v1/1/search.php?f={query}"
        response = requests.get(url, timeout=30)
        return response.json()

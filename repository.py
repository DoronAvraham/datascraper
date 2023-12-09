import orjson
import requests

class Repository():
    """A class returning Json data either from a local repository
      (local json file) or from a remote repository.
    """
    def __init__(self, remote):
        self.remote = remote

    def get_data(self):
        """ Returns:
                JsonObject: A Json representation of the data.
        """
        if self.remote:
            return self.__get_remote()
        else:
            return self.__get_local()

    def __get_local(self):
        with open("cocktails.json", "r", encoding="utf-8") as file:
            cocktails_json = file.read()
        return orjson.loads(cocktails_json) # pylint: disable=maybe-no-member

    def __get_remote(self):
        query = "b"
        url = f"https://thecocktaildb.com/api/json/v1/1/search.php?f={query}"
        response = requests.get(url, timeout=30)
        return response.json()

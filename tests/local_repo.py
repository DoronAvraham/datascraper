import orjson

class LocalRepo():

    def get_data(self):
        with open("tests/cocktails.json", "r", encoding="utf-8") as file:
            cocktails_json = file.read()
        return orjson.loads(cocktails_json) # pylint: disable=maybe-no-member

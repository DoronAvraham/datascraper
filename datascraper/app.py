import string
from datascraper.cocktails_parser import CocktailsParser
from datascraper.database import CocktailsDB
from datascraper.remote_repo import RemoteRepo

class App:

    def run(self):
        repo = RemoteRepo()
        parser = CocktailsParser()
        db = CocktailsDB()
        db.create_table()

        #all_letters_and_numbers = ["a","_","b"] # For quick tests.
        all_letters_and_numbers = string.ascii_lowercase + string.digits
        for letter in all_letters_and_numbers:
            cocktails_json = repo.get_data(letter)
            print(cocktails_json)
            print("============")
            cocktails_list = parser.parse(cocktails_json)
            if cocktails_list:
                db.insert_cocktails(cocktails_list)

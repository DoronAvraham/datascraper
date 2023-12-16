import string
from datascraper.cocktails_parser import CocktailsParser
from datascraper.database import CocktailsDB
from datascraper.db_handlers import handler_postgresql
from datascraper.remote_repo import RemoteRepo

class App:

    def run(self):
        repo = RemoteRepo()
        parser = CocktailsParser()
        handler = handler_postgresql()
        db = CocktailsDB(handler)
        db.create_table()

        all_letters_and_numbers = string.ascii_lowercase + string.digits
        for letter in all_letters_and_numbers:
            cocktails_json = repo.get_data(letter)
            print(cocktails_json)
            print("============")
            cocktails_list = parser.parse(cocktails_json)
            if cocktails_list:
                db.insert_cocktails(cocktails_list)

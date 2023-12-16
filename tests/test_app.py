from datascraper.cocktails_parser import CocktailsParser
from datascraper.database import CocktailsDB
from datascraper.db_handlers import handler_postgresql
from tests.local_repo import LocalRepo

__DB_HOST = "localhost"
__DB_USER = "Test"
__DB_PASSWORD = "Test"

def test_data_deserialized_and_stored():

    repo = LocalRepo()
    json_data = repo.get_data()

    parser = CocktailsParser()
    cocktails_list = parser.parse(json_data)

    handler = handler_postgresql(user = __DB_USER, password = __DB_PASSWORD, host = __DB_HOST)
    db = CocktailsDB(handler)
    db.create_table()
    db.insert_cocktails(cocktails_list)

    assert db.tables_exist_and_filled

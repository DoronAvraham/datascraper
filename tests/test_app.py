from datascraper.cocktails_parser import CocktailsParser
from datascraper.database import CocktailsDB
from datascraper.db_handlers import handler_postgresql
from tests.local_repo import LocalRepo



def test_data_deserialized_and_stored():

    repo = LocalRepo()
    json_data = repo.get_data()

    parser = CocktailsParser()
    cocktails_list = parser.parse(json_data)

    db = CocktailsDB(handler_postgresql)
    db.create_table()
    db.insert_cocktails(cocktails_list)

    assert db.tables_exist_and_filled

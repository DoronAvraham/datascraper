from datascraper.cocktails_parser import CocktailsParser
from datascraper.database import CocktailsDB
from tests.local_repo import LocalRepo


def test_data_deserialized_and_stored():

    repo = LocalRepo()
    json_data = repo.get_data()

    parser = CocktailsParser()
    cocktails_list = parser.parse(json_data)

    db = CocktailsDB()
    db.create_table()
    db.insert_cocktails(cocktails_list)

    assert db.tables_exist_and_filled

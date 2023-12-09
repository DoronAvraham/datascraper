from cocktails_parser import CocktailsParser
from database import CocktailsDB
from repository import Repository


repo = Repository(remote = True)
cocktailsJson = repo.get_data()

parser = CocktailsParser()
cocktails = parser.parse(cocktailsJson)

db = CocktailsDB()
db.create_and_store(cocktails)

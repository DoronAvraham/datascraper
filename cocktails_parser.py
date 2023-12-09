from cocktail import Cocktail

class CocktailsParser: 
    DRINKS = "drinks"
    __DRINK_ID = "idDrink"
    __DRINK_NAME = "strDrink"
    __INGREDIENT = "strIngredient"
    __MEASURE = "strMeasure"
    __INSTRUCTIONS = "strInstructions"
    __THUMBNAIL = "strDrinkThumb"
    __IMAGE = "strImageSource"

    def parse(self, cocktails_json):
        """ Parse Json data and deserialize it into Cocktails list.
        
        Returns:
                list[Cocktails]: A list of cocktails.
        """
        cocktails = []
        cocktails_list = cocktails_json[self.DRINKS]
        for cocktail in cocktails_list:
            drink_id = cocktail[self.__DRINK_ID]
            name = cocktail[self.__DRINK_NAME]
            instructions = cocktail[self.__INSTRUCTIONS]
            thumbnail = cocktail[self.__THUMBNAIL]
            image = cocktail[self.__IMAGE]

            ingredients = []
            for x in range(1, 16):
                ingredient = cocktail[self.__INGREDIENT + str(x)]
                if ingredient is None:
                    break
                ingredients.append(ingredient)

            measures = []
            for x in range(1, 16):
                measure = cocktail[self.__MEASURE + str(x)]
                if measure is None:
                    break
                measures.append(measure)

            # Prevent indexoutofboundsexception when inserting to DB.
            while (len(ingredients) > len(measures)):
                measures.append("")

            cocktails.append(
                Cocktail(drink_id, name, ingredients, measures, instructions, thumbnail, image))

        return cocktails

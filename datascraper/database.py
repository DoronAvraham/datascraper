class CocktailsDB:

    __TABLE_COCKTAILS = "Cocktails"
    __TABLE_INGREDIENTS = "Ingredients"

    def __init__(self, handler):
        self.handler = handler


    def create_table(self):

        with self.handler as connection:
            cursor = connection.cursor()
            # Create Cocktails table
            cursor.execute('''
                CREATE TABLE Cocktails (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    instructions TEXT,
                    thumbnail TEXT,
                    image TEXT
                )
            ''')

            # Create Ingredients table
            cursor.execute('''
                CREATE TABLE Ingredients (
                    id SERIAL PRIMARY KEY,
                    cocktail_id INTEGER,
                    ingredient TEXT NOT NULL,
                    measure TEXT,
                    FOREIGN KEY (cocktail_id) REFERENCES Cocktails(id)
                )
            ''')

            connection.commit()

    def insert_cocktails(self, cocktails):
        with self.handler as connection:
            cursor = connection.cursor()

            for cocktail in cocktails:
                # Insert data into Cocktails table
                cursor.execute('''
                INSERT INTO Cocktails (id, name, instructions, thumbnail, image)
                VALUES (%s, %s, %s, %s, %s)
                ''', (cocktail.id, cocktail.name,
                    cocktail.instructions,
                    cocktail.thumbnail_url,
                    cocktail.image_url))

                for i, ingredient in enumerate(cocktail.ingredients):
                    cursor.execute('''
                        INSERT INTO Ingredients (cocktail_id, ingredient, measure)
                        VALUES (%s, %s, %s)
                    ''', (cocktail.id, ingredient, cocktail.measures[i]))

            connection.commit()


    def tables_exist_and_filled(self):
        with self.handler as connection:
            cursor = connection.cursor()

            cursor.execute(f"SELECT (SELECT COUNT(*) FROM {self.__TABLE_COCKTAILS}) > 0)")
            result = cursor.fetchone()
            table_filled = bool(result[0])
            if not table_filled:
                return False

            cursor.execute(f"SELECT (SELECT COUNT(*) FROM {self.__TABLE_INGREDIENTS}) > 0)")
            result = cursor.fetchone()
            table_filled = bool(result[0])

            return table_filled

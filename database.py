import sqlite3

class CocktailsDB:

    def create_and_store(self, cocktails):
        """ Create cocktails table and store all cocktails.

        Args:
        parameter (list[Cocktails]): A list of cocktails to be stored.
        
        Returns:
                list[Cocktails]: A list of cocktails.
        """
        connection = sqlite3.connect("my_cocktails_bar.db")
        cursor = connection.cursor()
        self.__create_table(cursor)
        connection.commit()
        self.__insert_cocktails(cursor, cocktails)
        connection.commit()
        connection.close()

    def __create_table(self, cursor):
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
                id INTEGER PRIMARY KEY,
                cocktail_id INTEGER,
                ingredient TEXT NOT NULL,
                measure TEXT,
                FOREIGN KEY (cocktail_id) REFERENCES Cocktails(id)
            )
        ''')

    def __insert_cocktails(self, cursor, cocktails):
        for cocktail in cocktails:
            # Insert data into Cocktails table
            cursor.execute('''
            INSERT INTO Cocktails (id, name, instructions, thumbnail, image)
            VALUES (?, ?, ?, ?, ?)
            ''', (cocktail.id, cocktail.name,
                  cocktail.instructions,
                  cocktail.thumbnail_url,
                  cocktail.image_url))

            for i, ingredient in enumerate(cocktail.ingredients):
                cursor.execute('''
                    INSERT INTO Ingredients (cocktail_id, ingredient, measure)
                    VALUES (?, ?, ?)
                ''', (cocktail.id, ingredient, cocktail.measures[i]))

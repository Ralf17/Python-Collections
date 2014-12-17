#!/usr/bin/env python

import apsw

connection = apsw.Connection("cookbook1.db3")
cursor = connection.cursor()

sql = 'CREATE TABLE Recipes(pkID INTEGER PRIMARY KEY, name TEXT, servings TEXT, source TEXT)'

cursor.execute(sql)

sql = 'CREATE TABLE Instructions(pkId INTEGER PRIMARY KEY, instructions TEXT, recipeID NUMERIC)'

cursor.execute(sql)

sql = 'CREATE TABLE Ingredients(pkID INTEGER PRIMARY KEY, ingredients TEXT, recipeID NUMERIC)'

cursor.execute(sql)

sql = 'INSERT INTO Recipes(name, servings, source) VALUES ("Spanish Rice", 4, "Greg Walters")'

cursor.execute(sql)

sql = 'SELECT last_insert_rowid()'

cursor.execute(sql)

for x in cursor.execute(sql):
	lastid = x[0]
	
sql = 'INSERT INTO Instructions(recipeID, instructions) VALUES(%s, "Brown hamburger. Stir in all other ingredients. Bring to a boil. Stir. Lower to simmer. Cover and cook for 20 minutes or until all liquid is absorbed.")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "1 cup parboiled Rice (uncooked)")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "1 pound Hamburger")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "2 cups Water")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "1 8 oz can Tomato Sauce")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "1 small Onion chopped")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "1 clove Garlic chopped")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "1 tablespoon Ground Cumin")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "1 teaspoon Ground Oregano")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "Salt and Pepper to taste")' % lastid

cursor.execute(sql)

sql = 'INSERT INTO Ingredients(recipeID, ingredients) VALUES(%s, "Salsa to taste")' % lastid

cursor.execute(sql)







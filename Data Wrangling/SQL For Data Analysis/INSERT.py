#
# Insert a newborn baby opossum into the animals table and verify that it's been added.
# To do this, fill in the rest of SELECT_QUERY and INSERT_QUERY.
# 
# SELECT_QUERY should find the names and birthdates of all opossums.
# 
# INSERT_QUERY should add a new opossum to the table, whose birthdate is today.
# (Or you can choose any other date you like.)
#
# The animals table has columns (name, species, birthdate) for each individual.
#

SELECT_QUERY = '''
SELECT name, birthdate
  FROM animals
 WHERE species = 'opossum';
'''

INSERT_QUERY = "INSERT INTO animals values('Baby','opossum','2017-03-29');"


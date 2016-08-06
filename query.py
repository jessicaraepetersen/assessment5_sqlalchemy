"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
Brand.query.get(8)
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter(Model.name == 'Corvette', Model.brand_name == 'Chevrolet').all()
# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()
# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()
# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()
# Get all brands that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded == 1903, Brand.discontinued == None).all()
# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.
Brand.query.filter( (Brand.discontinued != None) | (Brand.founded < 1950) ).all()
# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()
# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    models = Model.query.options(db.joinedload('brand')).all()
    for model in models:
        if model.year == year:
            print "Model: %s, Brand: %s, Headquarters: %s" % (model.name, 
                                                        model.brand_name, 
                                                        model.brand.headquarters)


def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands = Brand.query.options(db.joinedload('model')).all()

    for brand in brands:
        models = brand.model
        print "Brand: %s" % (brand.name)
        print "Models: "
        for model in models:
            print model.name
        print "\n"

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?

# The returned value of the query Brand.query.filter_by(name='Ford') is 
# <flask_sqlalchemy.BaseQuery object at 0x7fd53b16c3d0>, which is a query object
# at the location "0x7fd53b16c3d0" in memory. Because of the nature of the query
# this object loads only Brand instances with the name Ford.

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

# An association table is the table between two tables that APPEAR to have a
# many-to-many relationship with each other. The association table operates as a 
# special kind of middle table that contains a number of foreign keys, each in a 
# many-to-one relationship from the association table to the individual data 
# tables. In this way, an association table REALLY manages two one-to-many
# relationships. Thus, association tables have no meaningful or unique fields 
# themselves; they are entirely comprised of foreign keys.


# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    '''This function takes in any string as a parameter and returns a list of 
    objects that are brands whose name contains or is equal to the input string.'''

    string = '%' + mystr + '%'
    return Brand.query.filter(Brand.name.like(string)).all() 



def get_models_between(start_year, end_year):
    '''This function takes in a start year and end year (two integers), and 
    returns a list of objects that are models with years that fall between the 
    start year (inclusive) and end year (exclusive).'''

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()
















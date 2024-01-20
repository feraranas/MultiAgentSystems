from owlready import *

onto = get_ontology("http://test.org/onto.owl")

class Drug(Thing):
     ontology = onto

class ActivePrinciple(Thing):
     ontology = onto

# This class will define a property in the ontology. 
# What it does in link instances of the `Drug` class
# to instances of the `ActivePrinciple` class.
class has_for_active_principle(Property):
     """ In Python, when we see something like domain = [Drug] within a class definition, 
     it typically means that the variable `domain` is assigned a list containing the class 
     `Drug` as its single element.
     """
     ontology = onto
     domain = [Drug]
     range = [ActivePrinciple]

acetaminophen = ActivePrinciple("acetaminophen")

# Here we create an instance of the `Drug` class
# named `my_acetaminophen_drug` and associate it 
# with the `acetaminophen` instance through the
# `has_for_active_principle` property.
my_acetaminophen_drug = Drug(has_for_active_principle = [acetaminophen])
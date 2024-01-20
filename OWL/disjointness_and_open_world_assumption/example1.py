from owlready import *

onto = get_ontology("http://test.org/onto.owl")

class Drug(Thing):
     ontology = onto

class ActivePrinciple(Thing):
     ontology = onto

AllDisjoint(Drug, ActivePrinciple)
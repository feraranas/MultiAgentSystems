from owlready import *

onto = get_ontology("http://test.org/onto.owl")

class Drug(Thing):
     ontology = onto

class ActivePrinciple(Thing):
     ontology = onto

class has_for_active_principle(Property):
     ontology = onto
     domain = [Drug]
     range = [ActivePrinciple]

acetaminophen = ActivePrinciple("acetaminophen")

my_acetaminophen_drug = Drug(has_for_active_principle = [acetaminophen])

my_acetaminophen_drug.is_a.append(restriction(has_for_active_principle, ONLY, one_of(acetaminophen)))
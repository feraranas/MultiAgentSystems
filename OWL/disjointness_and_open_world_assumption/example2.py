from owlready import *

onto = get_ontology("http://test.org/onto.owl")

class ActivePrinciple(Thing):
     ontology = onto

acetaminophen = ActivePrinciple("acetaminophen")
aspirin       = ActivePrinciple("aspirin")

AllDistinct(acetaminophen, aspirin)
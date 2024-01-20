# Classes and Individuals (Instances)

## Creating a Class

A new Class can be created in an ontology by inheriting the owlready2.Thing class

The **ontology class attribute** can be used to associate your class to the given ontology. If not specified, this attribute is inherited from the parent class (in the example below, the parent class is Thing, which is defined in the `owl` ontology).

```python
from owlready2 import *

onto = get_ontology("http://test.org/onto.owl")

class Drug(Thing):
     namespace = onto
     # ontology = onto
```

The **namespace Class attribute** is used to build the full IRI of the Class, and can be an ontology or a namespace (see Namespaces). 

The `with` statement can also be used to provide the ontology (or namespace):

```python
onto = get_ontology("http://test.org/onto.owl")

with onto:
     class Drug(Thing):
         pass
```

The .iri attribute of the Class can be used to obtain the full IRI of the class.

```python
print(Drug.iri) # Output: http://test.org/onto.owl#Drug
```
.name and .iri attributes are writable and can be modified (this allows to change the IRI of an entity, which is sometimes called “refactoring”).

## Creating and managing subclasses

Subclasses can be created by inheriting an ontology class. Multiple inheritance is supported.

```python
class DrugAssociation(Drug): # A drug associating several active principles
     pass
```

Owlready2 provides the `.is_a` attribute for getting the list of *superclasses* (__bases__ can be used, but with some limits described in Class constructs, restrictions and logical operators). It can also be modified for adding or removing superclasses.

```python
print(DrugAssociation.is_a) # Output: [onto.Drug]
```

The .subclasses() method returns the list of direct subclasses of a class.

```python
print(Drug.subclasses()) # Output: [onto.DrugAssociation]
```

The .descendants() and .ancestors() Class methods return a set of the descendant and ancestor Classes (including self, but excluding non-entity classes such as restrictions).
```python
DrugAssociation.ancestors()
# Output {onto.DrugAssociation, owl.Thing, onto.Drug}
```

## Creating classes dynamically

The `types` Python module can be used to create classes and subclasses dynamically:

```python
import types

with my_ontology:
     NewClass = types.new_class("NewClassName", (SuperClass,))
```

## Creating equivalent classes

The `.equivalent_to`  Class attribute is a list of equivalent classes. It behaves like `.is_a` (programmatically).

To obtain all equivalent classes, including indirect ones (due to transitivity), use .INDIRECT_equivalent_to.

## Creating Individuals

Individuals are instances in ontologies. They are created as any other Python instances. The first parameter is the name (or identifier) of the Individual; it corresponds to the .name attribute in Owlready2. If not given, the name if automatically generated from the Class name and a number.

```python
my_drug = Drug("my_drug")
print(my_drug.name) # output: my_drug

print(my_drug.iri) # output: http://test.org/onto.owl#my_drug

unamed_drug = Drug()
print(unamed_drug.name) # output: drug_1
```

Additional keyword parameters can be given when creating an Individual, and they will be associated to the corresponding Properties.

```python
my_drug = Drug("my_drug2", namespace = onto, has_for_active_principle = [],...)
```

The Instances are immediately available in the ontology:

```python
print(onto.drug_1) # output: onto.drug_1
```

The `.instances()` class method can be used to iterate through all Instances of a Class (including its subclasses). It returns a generator.

```python
for i in Drug.instances(): print(i)
```

Multiple calls with the individual name and namespace will returns the same individual (without creating a duplicate), and update the individual if property values are given.

```python
assert Drug("my_drug3") is Drug("my_drug3")
```

Finally, Individuals also have the `.equivalent_to` attribute (which correspond to the “same as” relation).

## Querying Individual relations

For a given Individual, the values of a property can be obtained with the usual “object.property” dot notation. See Properties for more details.

```python
print(onto.my_drug.has_for_active_principle)
```

Property name can be prefixed with “INDIRECT_” to obtain all indirect relations (i.e. those asserted at the class level with restriction, implied by transistive properties, subproperties, equivalences, etc):

```python
print(onto.my_drug.INDIRECT_has_for_active_principle)
```

# Introspecting Individuals

The list of properties that exist for a given individual can be obtained by the .get_properties() method. It returns a generator that yields the properties (without dupplicates).

```python
onto.drug_1.get_properties()
```

The following example shows how to list the properties of a given individual, and the associated values:

```python
for prop in onto.drug_1.get_properties():
     for value in prop[onto.drug_1]:
         print(".%s == %s" % (prop.python_name, value))
```

Notice the “Property[individual]” syntax. It allows to get the values as a list, even for functional properties (contrary to getattr(individual, Property.python_name).

Inverse properties can be obtained by the .get_inverse_properties() method. It returns a generator that yields (subject, property) tuples.

```python
onto.drug_1.get_inverse_properties()
```
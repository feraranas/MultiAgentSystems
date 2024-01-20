# Disjointness and open world assumption

By default, OWL considers the world as `open`, i.e. everything that is not stated in the ontology is not `false` but `possible` (this is known as **open world assumption**). Therefore, things and facts that are `false` or `impossible` must be clearly stated as so in the ontology.

## Disjoint Classes

Two or more Classes are disjoint if there is no Instance belonging to all these Classes (remember that, contrary to Python instances, an OWL Instance can have several Classes).

A **Classes disjointness** is created with the AllDisjoint global function, which takes two or more Classes as parameters. [In this example](./example1.py), we have two Classes, Drug and ActivePrinciple, and we assert that they are disjoint (yes, we need to specify that explicitely – sometimes ontologies seem a little dumb!).

```python
from owlready import *

onto = get_ontology("http://test.org/onto.owl")

class Drug(Thing):
     ontology = onto

class ActivePrinciple(Thing):
     ontology = onto

AllDisjoint(Drug, ActivePrinciple)
```

## Disjoint Properties

OWL also introduces Disjoint Properties. Disjoint Properties can also be created using the AllDisjoint() function.

## Distinct Instances

Two Instances are distinct if they are different. In OWL, two Instances might be considered as being actually the same single Individual, unless they are distinct. Distinctness is to Instances what Disjointness is to Classes.

[This example](./example2.py) creates two active principles and asserts that they are distinct (yes, we also need to state explicitely that acetaminophen and aspirin are not the same!)

```python
acetaminophen = ActivePrinciple("acetaminophen")
aspirin       = ActivePrinciple("aspirin")

AllDistinct(acetaminophen, aspirin)
```

> In Owlready, AllDistinct is actually the same function as AllDisjoint – the exact meaning depends on the parameters (AllDisjoint if you provide Classes, AllDistinct if you provide Instances, and disjoint Properties if you provide Properties).

## Closing Instances

The open world assumption also implies that the properties of a given Instance are not limited to the ones that are explicitely stated. [For example](./example3.py), if you create a Drug Instance with a single Active Principle, it does not mean that it has only a single Active Principle.

```python
class has_for_active_principle(Property):
     ontology = onto
     domain   = [Drug]
     range    = [ActivePrinciple]

my_acetaminophen_drug = Drug(has_for_active_principle = [acetaminophen])
```

In the example above, `my_acetaminophen_drug` has an acetaminophen Active Principle **(this fact is true)** and it may have other Active Principle(s) **(this fact is possible)**.

If you want `my_acetaminophen_drug` to be a Drug with acetaminophen and no other Active Principle, you have to state it explicitely using a **restriction** (see Restrictions) like [this example](./example4.py).

```python
my_acetaminophen_drug.is_a.append(restriction(has_for_active_principle, ONLY, one_of(acetaminophen)))
```

Notice that we used one_of() to ‘turn’ the acetaminophen Instance into a Class that we can use in the restriction.

You’ll quickly find that the open world assumption often leads to tedious and long lists of AllDistincts and Restrictions. Hopefully, Owlready provides the .closed_world() method for automatically ‘closing’ an instance. .closed_world() will automatically add ONLY restriction as needed; it accepts an optional parameter: a list of the Properties to ‘close’ (defaults to all Properties whose domain is compatible with the Instance).

```python
my_acetaminophen_drug.closed_world()
```

If you want to close the whole world, this can be done as following:
```python
onto.add(AllDistinct(*onto.instances))
for instance in onto.instances:
     instance.closed_world()
```

References
[docs](https://pythonhosted.org/Owlready/disjoint.html)
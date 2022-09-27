## Pydantic Cidoc-CRM Implementation
[![License](https://img.shields.io/github/license/jonasengelmann/pydantic-cidoc-crm)](LICENSE)

A Python implementation of [Cidoc-CRM 7.1.1](https://doi.org/10.26225/FDZH-X261) using [pydantic](https://pydantic-docs.helpmanual.io/) and [rdflib](https://rdflib.readthedocs.io/).

Data modelling in conformity with Cidoc-CRM poses some challenges. Cidoc-CRM has a complex inheritance structure, from which specific range and domain restrictions are derived. Complying with these restrictions can be difficult at times. This package is an attempt to facilitate working with Cidoc-CRM in Python, as well as mitigate some of its challenges. By means of rigours type checking, domain and range are ensured to be correct at all times, as well as typos prevented that would hinder interoperability. 


To conform to Python's syntax and standards, a few name changes had to be made:
1. Underscores and dashes in class names are omitted (E24_Physical_Human-Made_Thing -> E24PhysicalHumanMadeThing)
2. All properties start with a lower p (P1_is_identified_by -> p1_is_identified_by)
3. Dashes in property names are replaced by underscores (P4_has_time-span -> p4_has_time_span)

However, when an object is serialized, all names are converted back.

### Limitations

Cardinality and XSD types are not defined in the RDFS files. Since this model is automatically generated from theses files, they are not implemented here either. For now, every property accepts an instance or a list of instances of the required domain class or one of its subclasses.

## Installation

```console
$ pip3 install pydantic_cidoc_crm
```

## Usage

```python
from pydantic_cidoc_crm import E53Place, E41Appellation
x = E53Place(
    iri="http:/localhost/a_place",
    p1_is_identified_by=E41Appellation(
        iri="http:/localhost/a_place/appellation/1",
        p190_has_symbolic_content="Berlin"
    )
)
x.serialize()
```

```console
<http:/localhost/a_place/appellation> <http://www.cidoc-crm.org/cidoc-crm/P190_has_symbolic_content> "Berlin" .
<http:/localhost/a_place/appellation> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E41_Appellation> .
<http:/localhost/a_place> <http://www.cidoc-crm.org/cidoc-crm/P1_is_identified_by> <http:/localhost/a_place/appellation> .
<http:/localhost/a_place> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://www.cidoc-crm.org/cidoc-crm/E53_Place>
```

### Domain restriction:
```python
from pydantic_cidoc_crm import E53Place, E41Appellation
x = E53Place(
    iri="http:/localhost/a_place",
    p48_has_preferred_identifier=E41Appellation(
        iri="http:/localhost/a_place/identifier/1",
        p190_has_symbolic_content="123"
    )
)
```
Will throw a validation error:
```console
pydantic.error_wrappers.ValidationError: 1 validation error for E53Place
p48_has_preferred_identifier
  Domain must be E42Identifier or a subclass of it. (type=value_error)
```


### Range restriction and safeguarding against typos:

```python
from pydantic_cidoc_crm import E53Place, E41Appellation
x = E53Place(
    iri="http:/localhost/a_place",
    p1_is_identefied_by=E41Appellation(
        iri="http:/localhost/a_place/appellation/1",
        p190_has_symbolic_content="Berlin"
    )
)
```
Will throw a validation error (notice the typo):
```console
pydantic.error_wrappers.ValidationError: 1 validation error for E53Place
p1_is_identefied_by
  extra fields not permitted (type=value_error.extra)
```


### Subclassing

Often there is the need to subclass from a Cidoc-CRM class. Here is an example showing how a subclass can be implemented.

```python
from typing import Optional
from pydantic_cidoc_crm import E22HumanMadeObject, E39Actor

class MyOwnClass(E22HumanMadeObject):
    my_own_property: Optional[E39Actor] = None

    def __init__(self, **data):
        super().__init__(**data)
        self._mapping["MyOwnClass"] = "http://www.localhost/ontology/MyOwnClass"
        self._mapping["my_own_property"] = "http://www.localhost/ontology/my_own_property"
```


## License

This project is licensed under MIT license - see the [LICENSE](LICENSE) file for more information.

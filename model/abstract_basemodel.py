import abc
import datetime
from typing import Any, Union

from pydantic import BaseModel, Field
from rdflib import Literal, URIRef
from rdflib.namespace import RDF, XSD


class NotInMapping(BaseException):
    pass


class InvalidType(BaseException):
    pass


class AbstractBaseModel(BaseModel, abc.ABC):
    iri: str = Field(exclude=True, allow_mutation=False)

    class Config:
        validate_all = True
        validate_assignment = True
        extra = "forbid"
        arbitrary_types_allowed = True

    @classmethod
    def __get_validators__(cls):
        def validator(v: Any):
            if isinstance(v, cls):
                return v
            raise ValueError(f"Domain must be {cls.__name__} or a subclass of it.")

        yield validator

    @staticmethod
    def _convert_to_rdf_literal(
        value: Union[URIRef, str, int, float, datetime.date, datetime.datetime]
    ) -> Literal:
        if isinstance(value, URIRef):
            return value
        elif isinstance(value, str):
            return Literal(value)
        elif isinstance(value, int):
            return Literal(value, datatype=XSD.int)
        elif isinstance(value, float):
            return Literal(value, datetime=XSD.decimal)
        elif isinstance(value, datetime.date):
            return Literal(value.isoformat(), datatype=XSD.date)
        elif isinstance(value, datetime.datetime):
            return Literal(value.isoformat(), datatype=XSD.dateTime)
        raise InvalidType(value)

    def to_triples(self, recursive=True) -> list:
        triples = [
            (URIRef(self.iri), RDF.type, URIRef(self._mapping[self.__class__.__name__]))
        ]
        for key in self.dict(
            exclude_unset=True, exclude_none=True, exclude_defaults=True
        ).keys():
            values = getattr(self, key)

            if not isinstance(values, list):
                values = [values]

            for value in values:
                if isinstance(value, AbstractBaseModel):
                    if recursive:
                        triples.extend(value.to_triples())
                    value = URIRef(value.iri)
                else:
                    value = self._convert_to_rdf_literal(value)
                try:
                    predicate = URIRef(self._mapping[key])
                except KeyError:
                    raise NotInMapping(key)

                triples.append((URIRef(self.iri), predicate, value))

        return triples

    def serialize(self) -> str:
        serialized_triples = set()

        for triple in self.to_triples():
            serialized_triples.add(
                f"{triple[0].n3()} {triple[1].n3()} {triple[2].n3()}"
            )
        return " .\n".join(sorted(serialized_triples))

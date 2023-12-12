# Auto generated from definedterm_profile.yaml by pythongen.py version: 0.0.1
# Generation date: 2023-12-12T21:15:54
# Schema: DefinedTerm_profile
#
# id: https://w3id.org/stroemphi/DefinedTerm_profile
# description: A LinkML schema to define a profile for the DefinedTerm class from Schema.org.
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
DCT = CurieNamespace('dct', 'http://purl.org/dc/terms/')
DEFINEDTERM_PROFILE = CurieNamespace('definedterm_profile', 'https://w3id.org/stroemphi/DefinedTerm_profile/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = DEFINEDTERM_PROFILE


# Types

# Class references
class ThingId(URIorCURIE):
    pass


class IntangibleId(ThingId):
    pass


class CreativeWorkId(ThingId):
    pass


class DefinedTermId(IntangibleId):
    pass


class DefinedTermSetId(CreativeWorkId):
    pass


@dataclass
class Thing(YAMLRoot):
    """
    The most generic type of item.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "Thing"
    class_model_uri: ClassVar[URIRef] = DEFINEDTERM_PROFILE.Thing

    id: Union[str, ThingId] = None
    alternateName: Optional[Union[str, List[str]]] = empty_list()
    description: Optional[str] = None
    name: Optional[str] = None
    sameAs: Optional[str] = None
    url: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThingId):
            self.id = ThingId(self.id)

        if not isinstance(self.alternateName, list):
            self.alternateName = [self.alternateName] if self.alternateName is not None else []
        self.alternateName = [v if isinstance(v, str) else str(v) for v in self.alternateName]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.sameAs is not None and not isinstance(self.sameAs, str):
            self.sameAs = str(self.sameAs)

        if self.url is not None and not isinstance(self.url, URIorCURIE):
            self.url = URIorCURIE(self.url)

        super().__post_init__(**kwargs)


@dataclass
class Intangible(Thing):
    """
    A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured
    values, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Intangible"]
    class_class_curie: ClassVar[str] = "schema:Intangible"
    class_name: ClassVar[str] = "Intangible"
    class_model_uri: ClassVar[URIRef] = DEFINEDTERM_PROFILE.Intangible

    id: Union[str, IntangibleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, IntangibleId):
            self.id = IntangibleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class CreativeWork(Thing):
    """
    The most generic kind of creative work, including books, movies, photographs, software programs, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["CreativeWork"]
    class_class_curie: ClassVar[str] = "schema:CreativeWork"
    class_name: ClassVar[str] = "CreativeWork"
    class_model_uri: ClassVar[URIRef] = DEFINEDTERM_PROFILE.CreativeWork

    id: Union[str, CreativeWorkId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CreativeWorkId):
            self.id = CreativeWorkId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DefinedTerm(Intangible):
    """
    A word, name, acronym, phrase, etc. with a formal definition. Often used in the context of category or subject
    classification, glossaries or dictionaries, product or creative work types, etc. Use the name property for the
    term being defined, use termCode if the term has an alpha-numeric code allocated, use description to provide the
    definition of the term.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DefinedTerm"]
    class_class_curie: ClassVar[str] = "schema:DefinedTerm"
    class_name: ClassVar[str] = "DefinedTerm"
    class_model_uri: ClassVar[URIRef] = DEFINEDTERM_PROFILE.DefinedTerm

    id: Union[str, DefinedTermId] = None
    inDefinedTermSet: Union[str, URIorCURIE] = None
    termCode: str = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DefinedTermId):
            self.id = DefinedTermId(self.id)

        if self._is_empty(self.inDefinedTermSet):
            self.MissingRequiredField("inDefinedTermSet")
        if not isinstance(self.inDefinedTermSet, URIorCURIE):
            self.inDefinedTermSet = URIorCURIE(self.inDefinedTermSet)

        if self._is_empty(self.termCode):
            self.MissingRequiredField("termCode")
        if not isinstance(self.termCode, str):
            self.termCode = str(self.termCode)

        super().__post_init__(**kwargs)


@dataclass
class DefinedTermSet(CreativeWork):
    """
    A set of defined terms for example a set of categories or a classification scheme, a glossary, dictionary or
    enumeration.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["DefinedTermSet"]
    class_class_curie: ClassVar[str] = "schema:DefinedTermSet"
    class_name: ClassVar[str] = "DefinedTermSet"
    class_model_uri: ClassVar[URIRef] = DEFINEDTERM_PROFILE.DefinedTermSet

    id: Union[str, DefinedTermSetId] = None
    hasDefinedTerm: Optional[Union[str, DefinedTermId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DefinedTermSetId):
            self.id = DefinedTermSetId(self.id)

        if self.hasDefinedTerm is not None and not isinstance(self.hasDefinedTerm, DefinedTermId):
            self.hasDefinedTerm = DefinedTermId(self.hasDefinedTerm)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=DEFINEDTERM_PROFILE.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=DEFINEDTERM_PROFILE.name, domain=None, range=Optional[str])

slots.alternateName = Slot(uri=SCHEMA.alternateName, name="alternateName", curie=SCHEMA.curie('alternateName'),
                   model_uri=DEFINEDTERM_PROFILE.alternateName, domain=None, range=Optional[Union[str, List[str]]])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=DEFINEDTERM_PROFILE.description, domain=None, range=Optional[str])

slots.sameAs = Slot(uri=SCHEMA.sameAs, name="sameAs", curie=SCHEMA.curie('sameAs'),
                   model_uri=DEFINEDTERM_PROFILE.sameAs, domain=None, range=Optional[str])

slots.url = Slot(uri=SCHEMA.url, name="url", curie=SCHEMA.curie('url'),
                   model_uri=DEFINEDTERM_PROFILE.url, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.definedTerm__inDefinedTermSet = Slot(uri=SCHEMA.inDefinedTermSet, name="definedTerm__inDefinedTermSet", curie=SCHEMA.curie('inDefinedTermSet'),
                   model_uri=DEFINEDTERM_PROFILE.definedTerm__inDefinedTermSet, domain=None, range=Union[str, URIorCURIE])

slots.definedTerm__termCode = Slot(uri=SCHEMA.termCode, name="definedTerm__termCode", curie=SCHEMA.curie('termCode'),
                   model_uri=DEFINEDTERM_PROFILE.definedTerm__termCode, domain=None, range=str)

slots.definedTermSet__hasDefinedTerm = Slot(uri=SCHEMA.hasDefinedTerm, name="definedTermSet__hasDefinedTerm", curie=SCHEMA.curie('hasDefinedTerm'),
                   model_uri=DEFINEDTERM_PROFILE.definedTermSet__hasDefinedTerm, domain=None, range=Optional[Union[str, DefinedTermId]])
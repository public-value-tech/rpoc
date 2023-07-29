# Auto generated from rpoc.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-07-29T20:25:40
# Schema: rpoc
#
# id: https://pub.tech/schema/rpoc/
# description: Information about people, their roles together with orgainsational context based on
#              [schema.org](http://schema.org) and [Team Topologies](https://teamtopologies.com/).
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
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
from linkml_runtime.linkml_model.types import Boolean, Date, Float, String, Uri
from linkml_runtime.utils.metamodelcore import Bool, URI, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
GSSO = CurieNamespace('GSSO', 'http://purl.obolibrary.org/obo/GSSO_')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
RPOC = CurieNamespace('rpoc', 'https://pub.tech/schema/rpoc/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = RPOC


# Types

# Class references
class NamedThingId(extended_str):
    pass


class PersonId(NamedThingId):
    pass


class ContextId(NamedThingId):
    pass


class RoleRoleName(extended_str):
    pass


class OrganizationId(NamedThingId):
    pass


class PlaceId(extended_str):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RPOC.NamedThing
    class_class_curie: ClassVar[str] = "rpoc:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = RPOC.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[Union[dict, "Image"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.image is not None and not isinstance(self.image, Image):
            self.image = Image(**as_dict(self.image))

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    A person (alive, dead, undead, or fictional).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Person
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = RPOC.Person

    id: Union[str, PersonId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[str] = None
    gender: Optional[Union[str, "GenderType"]] = None
    current_address: Optional[Union[dict, "Address"]] = None
    position: Optional[str] = None
    nick: Optional[str] = None
    avatar: Optional[Union[dict, "Image"]] = None
    has_employment_history: Optional[Union[Union[dict, "EmploymentEvent"], List[Union[dict, "EmploymentEvent"]]]] = empty_list()
    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, str):
            self.birth_date = str(self.birth_date)

        if self.gender is not None and not isinstance(self.gender, GenderType):
            self.gender = GenderType(self.gender)

        if self.current_address is not None and not isinstance(self.current_address, Address):
            self.current_address = Address(**as_dict(self.current_address))

        if self.position is not None and not isinstance(self.position, str):
            self.position = str(self.position)

        if self.nick is not None and not isinstance(self.nick, str):
            self.nick = str(self.nick)

        if self.avatar is not None and not isinstance(self.avatar, Image):
            self.avatar = Image(**as_dict(self.avatar))

        if not isinstance(self.has_employment_history, list):
            self.has_employment_history = [self.has_employment_history] if self.has_employment_history is not None else []
        self.has_employment_history = [v if isinstance(v, EmploymentEvent) else EmploymentEvent(**as_dict(v)) for v in self.has_employment_history]

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class HasAliases(YAMLRoot):
    """
    A mixin applied to any class that can have aliases/alternateNames
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RPOC.HasAliases
    class_class_curie: ClassVar[str] = "rpoc:HasAliases"
    class_name: ClassVar[str] = "HasAliases"
    class_model_uri: ClassVar[URIRef] = RPOC.HasAliases

    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class Context(NamedThing):
    """
    A team, group, project, or other entity that has a context for a person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Project
    class_class_curie: ClassVar[str] = "schema:Project"
    class_name: ClassVar[str] = "Context"
    class_model_uri: ClassVar[URIRef] = RPOC.Context

    id: Union[str, ContextId] = None
    primary_email: Optional[str] = None
    mission_statement: Optional[str] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    parent: Optional[Union[str, ContextId]] = None
    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ContextId):
            self.id = ContextId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.mission_statement is not None and not isinstance(self.mission_statement, str):
            self.mission_statement = str(self.mission_statement)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.parent is not None and not isinstance(self.parent, ContextId):
            self.parent = ContextId(self.parent)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class Role(YAMLRoot):
    """
    A set of responsibilities, skills and tasks that a person has in a context
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Role
    class_class_curie: ClassVar[str] = "schema:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = RPOC.Role

    role_name: Union[str, RoleRoleName] = None
    role_type: Optional[Union[str, "RoleType"]] = None
    description: Optional[str] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.role_name):
            self.MissingRequiredField("role_name")
        if not isinstance(self.role_name, RoleRoleName):
            self.role_name = RoleRoleName(self.role_name)

        if self.role_type is not None and not isinstance(self.role_type, RoleType):
            self.role_type = RoleType(self.role_type)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class Membership(YAMLRoot):
    """
    A person's roles in a context
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RPOC.Membership
    class_class_curie: ClassVar[str] = "rpoc:Membership"
    class_name: ClassVar[str] = "Membership"
    class_model_uri: ClassVar[URIRef] = RPOC.Membership

    person: Optional[Union[str, PersonId]] = None
    role: Optional[Union[str, RoleRoleName]] = None
    context: Optional[Union[str, ContextId]] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.person is not None and not isinstance(self.person, PersonId):
            self.person = PersonId(self.person)

        if self.role is not None and not isinstance(self.role, RoleRoleName):
            self.role = RoleRoleName(self.role)

        if self.context is not None and not isinstance(self.context, ContextId):
            self.context = ContextId(self.context)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Organization(NamedThing):
    """
    An organization such as a company or university
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Organization
    class_class_curie: ClassVar[str] = "schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = RPOC.Organization

    id: Union[str, OrganizationId] = None
    mission_statement: Optional[str] = None
    founding_date: Optional[str] = None
    founding_location: Optional[Union[str, PlaceId]] = None
    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if self.mission_statement is not None and not isinstance(self.mission_statement, str):
            self.mission_statement = str(self.mission_statement)

        if self.founding_date is not None and not isinstance(self.founding_date, str):
            self.founding_date = str(self.founding_date)

        if self.founding_location is not None and not isinstance(self.founding_location, PlaceId):
            self.founding_location = PlaceId(self.founding_location)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class Place(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RPOC.Place
    class_class_curie: ClassVar[str] = "rpoc:Place"
    class_name: ClassVar[str] = "Place"
    class_model_uri: ClassVar[URIRef] = RPOC.Place

    id: Union[str, PlaceId] = None
    name: Optional[str] = None
    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PlaceId):
            self.id = PlaceId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v) for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class Address(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.PostalAddress
    class_class_curie: ClassVar[str] = "schema:PostalAddress"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = RPOC.Address

    street: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.street is not None and not isinstance(self.street, str):
            self.street = str(self.street)

        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.postal_code is not None and not isinstance(self.postal_code, str):
            self.postal_code = str(self.postal_code)

        super().__post_init__(**kwargs)


@dataclass
class Event(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RPOC.Event
    class_class_curie: ClassVar[str] = "rpoc:Event"
    class_name: ClassVar[str] = "Event"
    class_model_uri: ClassVar[URIRef] = RPOC.Event

    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    duration: Optional[float] = None
    is_current: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.duration is not None and not isinstance(self.duration, float):
            self.duration = float(self.duration)

        if self.is_current is not None and not isinstance(self.is_current, Bool):
            self.is_current = Bool(self.is_current)

        super().__post_init__(**kwargs)


@dataclass
class Interaction(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RPOC.Interaction
    class_class_curie: ClassVar[str] = "rpoc:Interaction"
    class_name: ClassVar[str] = "Interaction"
    class_model_uri: ClassVar[URIRef] = RPOC.Interaction

    type: Optional[str] = None
    status: Optional[str] = None
    start_date: Optional[Union[str, XSDDate]] = None
    end_date: Optional[Union[str, XSDDate]] = None
    related_to: Optional[str] = None
    obsoleted_by: Optional[Union[str, ContextId]] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.start_date is not None and not isinstance(self.start_date, XSDDate):
            self.start_date = XSDDate(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, XSDDate):
            self.end_date = XSDDate(self.end_date)

        if self.related_to is not None and not isinstance(self.related_to, str):
            self.related_to = str(self.related_to)

        if self.obsoleted_by is not None and not isinstance(self.obsoleted_by, ContextId):
            self.obsoleted_by = ContextId(self.obsoleted_by)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class EmploymentEvent(Event):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RPOC.EmploymentEvent
    class_class_curie: ClassVar[str] = "rpoc:EmploymentEvent"
    class_name: ClassVar[str] = "EmploymentEvent"
    class_model_uri: ClassVar[URIRef] = RPOC.EmploymentEvent

    employed_at: Optional[Union[str, OrganizationId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.employed_at is not None and not isinstance(self.employed_at, OrganizationId):
            self.employed_at = OrganizationId(self.employed_at)

        super().__post_init__(**kwargs)


@dataclass
class WithLocation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RPOC.WithLocation
    class_class_curie: ClassVar[str] = "rpoc:WithLocation"
    class_name: ClassVar[str] = "WithLocation"
    class_model_uri: ClassVar[URIRef] = RPOC.WithLocation

    in_location: Optional[Union[str, PlaceId]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.in_location is not None and not isinstance(self.in_location, PlaceId):
            self.in_location = PlaceId(self.in_location)

        super().__post_init__(**kwargs)


@dataclass
class Image(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = RPOC.Image
    class_class_curie: ClassVar[str] = "rpoc:Image"
    class_name: ClassVar[str] = "Image"
    class_model_uri: ClassVar[URIRef] = RPOC.Image

    url: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.url is not None and not isinstance(self.url, URI):
            self.url = URI(self.url)

        super().__post_init__(**kwargs)


# Enumerations
class ContextType(EnumDefinitionImpl):

    team = PermissibleValue(text="team",
                               description="A team is a group of people working together on a project")
    group = PermissibleValue(text="group",
                                 description="A group is a collection of people with a common interest")
    project = PermissibleValue(text="project",
                                     description="A project is a temporary endeavor with a defined goal")
    organization = PermissibleValue(text="organization",
                                               description="An organization is a group of people with a common purpose")

    _defn = EnumDefinition(
        name="ContextType",
    )

class RoleType(EnumDefinitionImpl):

    permanent = PermissibleValue(text="permanent",
                                         description="A member who is permanent part of a team or group")
    enabling = PermissibleValue(text="enabling",
                                       description="A enabling role is a person who helps a team or group without being a permanent member")
    temporary = PermissibleValue(text="temporary",
                                         description="A short lived role that is not permanent")

    _defn = EnumDefinition(
        name="RoleType",
    )

class InteractionType(EnumDefinitionImpl):

    collaboration = PermissibleValue(text="collaboration",
                                                 description="A collaboration interaction is a relationship between two contexts which work together on a project")
    facilitating = PermissibleValue(text="facilitating",
                                               description="A facilitating interaction is a relationship between two contexts which help each other")
    xaas = PermissibleValue(text="xaas",
                               description="A XaaS interaction is a relationship between two contexts where one provides a service to the other")

    _defn = EnumDefinition(
        name="InteractionType",
    )

class GenderType(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="GenderType",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "nonbinary man",
                PermissibleValue(text="nonbinary man",
                                 meaning=GSSO["009254"]) )
        setattr(cls, "nonbinary woman",
                PermissibleValue(text="nonbinary woman",
                                 meaning=GSSO["009253"]) )
        setattr(cls, "transgender woman",
                PermissibleValue(text="transgender woman",
                                 meaning=GSSO["000384"]) )
        setattr(cls, "transgender man",
                PermissibleValue(text="transgender man",
                                 meaning=GSSO["000372"]) )
        setattr(cls, "cisgender man",
                PermissibleValue(text="cisgender man",
                                 meaning=GSSO["000371"]) )
        setattr(cls, "cisgender woman",
                PermissibleValue(text="cisgender woman",
                                 meaning=GSSO["000385"]) )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=RPOC.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=RPOC.name, domain=None, range=Optional[str])

slots.nick = Slot(uri=SCHEMA.alternateName, name="nick", curie=SCHEMA.curie('alternateName'),
                   model_uri=RPOC.nick, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=RPOC.description, domain=None, range=Optional[str])

slots.image = Slot(uri=SCHEMA.image, name="image", curie=SCHEMA.curie('image'),
                   model_uri=RPOC.image, domain=None, range=Optional[Union[dict, Image]])

slots.avatar = Slot(uri=RPOC.avatar, name="avatar", curie=RPOC.curie('avatar'),
                   model_uri=RPOC.avatar, domain=None, range=Optional[Union[dict, Image]])

slots.parent = Slot(uri=RPOC.parent, name="parent", curie=RPOC.curie('parent'),
                   model_uri=RPOC.parent, domain=None, range=Optional[Union[str, ContextId]])

slots.gender = Slot(uri=SCHEMA.gender, name="gender", curie=SCHEMA.curie('gender'),
                   model_uri=RPOC.gender, domain=None, range=Optional[Union[str, "GenderType"]])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=RPOC.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=RPOC.birth_date, domain=None, range=Optional[str])

slots.employed_at = Slot(uri=RPOC.employed_at, name="employed_at", curie=RPOC.curie('employed_at'),
                   model_uri=RPOC.employed_at, domain=None, range=Optional[Union[str, OrganizationId]])

slots.company = Slot(uri=RPOC.company, name="company", curie=RPOC.curie('company'),
                   model_uri=RPOC.company, domain=None, range=Optional[Union[str, OrganizationId]])

slots.position = Slot(uri=RPOC.position, name="position", curie=RPOC.curie('position'),
                   model_uri=RPOC.position, domain=None, range=Optional[str])

slots.is_current = Slot(uri=RPOC.is_current, name="is_current", curie=RPOC.curie('is_current'),
                   model_uri=RPOC.is_current, domain=None, range=Optional[Union[bool, Bool]])

slots.has_employment_history = Slot(uri=RPOC.has_employment_history, name="has_employment_history", curie=RPOC.curie('has_employment_history'),
                   model_uri=RPOC.has_employment_history, domain=None, range=Optional[Union[Union[dict, EmploymentEvent], List[Union[dict, EmploymentEvent]]]])

slots.in_location = Slot(uri=RPOC.in_location, name="in_location", curie=RPOC.curie('in_location'),
                   model_uri=RPOC.in_location, domain=None, range=Optional[Union[str, PlaceId]])

slots.current_address = Slot(uri=RPOC.current_address, name="current_address", curie=RPOC.curie('current_address'),
                   model_uri=RPOC.current_address, domain=None, range=Optional[Union[dict, Address]])

slots.related_to = Slot(uri=RPOC.related_to, name="related_to", curie=RPOC.curie('related_to'),
                   model_uri=RPOC.related_to, domain=None, range=Optional[str])

slots.obsoleted_by = Slot(uri=RPOC.obsoleted_by, name="obsoleted_by", curie=RPOC.curie('obsoleted_by'),
                   model_uri=RPOC.obsoleted_by, domain=None, range=Optional[Union[str, ContextId]])

slots.type = Slot(uri=RPOC.type, name="type", curie=RPOC.curie('type'),
                   model_uri=RPOC.type, domain=None, range=Optional[str])

slots.street = Slot(uri=RPOC.street, name="street", curie=RPOC.curie('street'),
                   model_uri=RPOC.street, domain=None, range=Optional[str])

slots.city = Slot(uri=RPOC.city, name="city", curie=RPOC.curie('city'),
                   model_uri=RPOC.city, domain=None, range=Optional[str])

slots.website = Slot(uri=RPOC.website, name="website", curie=RPOC.curie('website'),
                   model_uri=RPOC.website, domain=None, range=Optional[Union[str, URI]])

slots.url = Slot(uri=SCHEMA.contentUrl, name="url", curie=SCHEMA.curie('contentUrl'),
                   model_uri=RPOC.url, domain=None, range=Optional[Union[str, URI]])

slots.mission_statement = Slot(uri=RPOC.mission_statement, name="mission_statement", curie=RPOC.curie('mission_statement'),
                   model_uri=RPOC.mission_statement, domain=None, range=Optional[str])

slots.founding_date = Slot(uri=RPOC.founding_date, name="founding_date", curie=RPOC.curie('founding_date'),
                   model_uri=RPOC.founding_date, domain=None, range=Optional[str])

slots.founding_location = Slot(uri=RPOC.founding_location, name="founding_location", curie=RPOC.curie('founding_location'),
                   model_uri=RPOC.founding_location, domain=None, range=Optional[Union[str, PlaceId]])

slots.postal_code = Slot(uri=RPOC.postal_code, name="postal_code", curie=RPOC.curie('postal_code'),
                   model_uri=RPOC.postal_code, domain=None, range=Optional[str])

slots.start_date = Slot(uri=PROV.startedAtTime, name="start_date", curie=PROV.curie('startedAtTime'),
                   model_uri=RPOC.start_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.duration = Slot(uri=RPOC.duration, name="duration", curie=RPOC.curie('duration'),
                   model_uri=RPOC.duration, domain=None, range=Optional[float])

slots.end_date = Slot(uri=PROV.endedAtTime, name="end_date", curie=PROV.curie('endedAtTime'),
                   model_uri=RPOC.end_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.role_name = Slot(uri=SCHEMA.roleName, name="role_name", curie=SCHEMA.curie('roleName'),
                   model_uri=RPOC.role_name, domain=None, range=URIRef)

slots.role_type = Slot(uri=RPOC.role_type, name="role_type", curie=RPOC.curie('role_type'),
                   model_uri=RPOC.role_type, domain=None, range=Optional[Union[str, "RoleType"]])

slots.status = Slot(uri=SCHEMA.status, name="status", curie=SCHEMA.curie('status'),
                   model_uri=RPOC.status, domain=None, range=Optional[str])

slots.person = Slot(uri=RPOC.person, name="person", curie=RPOC.curie('person'),
                   model_uri=RPOC.person, domain=None, range=Optional[Union[str, PersonId]])

slots.role = Slot(uri=RPOC.role, name="role", curie=RPOC.curie('role'),
                   model_uri=RPOC.role, domain=None, range=Optional[Union[str, RoleRoleName]])

slots.context = Slot(uri=RPOC.context, name="context", curie=RPOC.curie('context'),
                   model_uri=RPOC.context, domain=None, range=Optional[Union[str, ContextId]])

slots.persons = Slot(uri=RPOC.persons, name="persons", curie=RPOC.curie('persons'),
                   model_uri=RPOC.persons, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.roles = Slot(uri=RPOC.roles, name="roles", curie=RPOC.curie('roles'),
                   model_uri=RPOC.roles, domain=None, range=Optional[Union[Dict[Union[str, RoleRoleName], Union[dict, Role]], List[Union[dict, Role]]]])

slots.contexts = Slot(uri=RPOC.contexts, name="contexts", curie=RPOC.curie('contexts'),
                   model_uri=RPOC.contexts, domain=None, range=Optional[Union[Dict[Union[str, ContextId], Union[dict, Context]], List[Union[dict, Context]]]])

slots.memberships = Slot(uri=RPOC.memberships, name="memberships", curie=RPOC.curie('memberships'),
                   model_uri=RPOC.memberships, domain=None, range=Optional[Union[Union[dict, Membership], List[Union[dict, Membership]]]])

slots.organizations = Slot(uri=RPOC.organizations, name="organizations", curie=RPOC.curie('organizations'),
                   model_uri=RPOC.organizations, domain=None, range=Optional[Union[Dict[Union[str, OrganizationId], Union[dict, Organization]], List[Union[dict, Organization]]]])

slots.hasAliases__aliases = Slot(uri=RPOC.aliases, name="hasAliases__aliases", curie=RPOC.curie('aliases'),
                   model_uri=RPOC.hasAliases__aliases, domain=None, range=Optional[Union[str, List[str]]])

slots.Person_primary_email = Slot(uri=SCHEMA.email, name="Person_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=RPOC.Person_primary_email, domain=Person, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))

slots.Context_primary_email = Slot(uri=SCHEMA.email, name="Context_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=RPOC.Context_primary_email, domain=Context, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))
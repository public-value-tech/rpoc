
# rpoc


**metamodel version:** 1.7.0

**version:** None


Information about people, their roles together with orgainsational context based on [schema.org](http://schema.org) and [Team Topologies](https://teamtopologies.com/).


### Classes

 * [Address](Address.md)
 * [Container](Container.md)
 * [Event](Event.md)
     * [EmploymentEvent](EmploymentEvent.md)
 * [Interaction](Interaction.md)
 * [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity
     * [Concept](Concept.md)
     * [Context](Context.md) - A team, group, project, or other entity that has a context for a person
     * [Organization](Organization.md) - An organization such as a company or university
     * [Person](Person.md) - A person (alive, dead, undead, or fictional).
 * [Place](Place.md)
 * [Role](Role.md) - A set of responsibilities, skills and tasks that a person has in a context

### Mixins

 * [HasAliases](HasAliases.md) - A mixin applied to any class that can have aliases/alternateNames
 * [WithLocation](WithLocation.md)

### Slots

 * [birth_date](birth_date.md)
 * [city](city.md)
 * [contexts](contexts.md)
 * [current_address](current_address.md) - The address at which a person currently lives
 * [description](description.md)
 * [duration](duration.md)
 * [employed_at](employed_at.md)
 * [end_date](end_date.md)
 * [founding_date](founding_date.md)
 * [founding_location](founding_location.md)
 * [gender](gender.md)
 * [➞aliases](hasAliases__aliases.md)
 * [has_employment_history](has_employment_history.md)
 * [id](id.md)
 * [image](image.md)
 * [in_location](in_location.md)
 * [is_current](is_current.md)
 * [mission_statement](mission_statement.md)
 * [name](name.md)
 * [obsoleted_by](obsoleted_by.md)
 * [organizations](organizations.md)
 * [parent](parent.md)
 * [persons](persons.md)
 * [postal_code](postal_code.md)
 * [primary_email](primary_email.md)
     * [Context➞primary_email](Context_primary_email.md)
     * [Person➞primary_email](Person_primary_email.md)
 * [related_to](related_to.md)
 * [role_name](role_name.md)
 * [role_type](role_type.md)
 * [roles](roles.md)
 * [start_date](start_date.md)
 * [status](status.md)
 * [street](street.md)
 * [type](type.md)

### Enums

 * [ContextType](ContextType.md)
 * [GenderType](GenderType.md)
 * [InteractionType](InteractionType.md)
 * [RoleType](RoleType.md)

### Subsets

 * [BasicSubset](BasicSubset.md) - A subset of the schema that handles basic information

### Types


#### Built in

 * **Bool**
 * **Curie**
 * **Decimal**
 * **ElementIdentifier**
 * **NCName**
 * **NodeIdentifier**
 * **URI**
 * **URIorCURIE**
 * **XSDDate**
 * **XSDDateTime**
 * **XSDTime**
 * **float**
 * **int**
 * **str**

#### Defined

 * [Boolean](types/Boolean.md)  (**Bool**)  - A binary (true or false) value
 * [Curie](types/Curie.md)  (**Curie**)  - a compact URI
 * [Date](types/Date.md)  (**XSDDate**)  - a date (year, month and day) in an idealized calendar
 * [DateOrDatetime](types/DateOrDatetime.md)  (**str**)  - Either a date or a datetime
 * [Datetime](types/Datetime.md)  (**XSDDateTime**)  - The combination of a date and time
 * [Decimal](types/Decimal.md)  (**Decimal**)  - A real number with arbitrary precision that conforms to the xsd:decimal specification
 * [Double](types/Double.md)  (**float**)  - A real number that conforms to the xsd:double specification
 * [Float](types/Float.md)  (**float**)  - A real number that conforms to the xsd:float specification
 * [Integer](types/Integer.md)  (**int**)  - An integer
 * [Ncname](types/Ncname.md)  (**NCName**)  - Prefix part of CURIE
 * [Nodeidentifier](types/Nodeidentifier.md)  (**NodeIdentifier**)  - A URI, CURIE or BNODE that represents a node in a model.
 * [Objectidentifier](types/Objectidentifier.md)  (**ElementIdentifier**)  - A URI or CURIE that represents an object in the model.
 * [String](types/String.md)  (**str**)  - A character string
 * [Time](types/Time.md)  (**XSDTime**)  - A time object represents a (local) time of day, independent of any particular day
 * [Uri](types/Uri.md)  (**URI**)  - a complete URI
 * [Uriorcurie](types/Uriorcurie.md)  (**URIorCURIE**)  - a URI or a CURIE

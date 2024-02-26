
# Class: Person


A person (alive, dead, undead, or fictional).

URI: [rpoc:Person](https://pub.tech/schema/rpoc/Person)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EmploymentEvent]<has_employment_history%200..*-++[Person&#124;primary_email:string%20%3F;nick:string%20%3F;position:string%20%3F;birth_date:string%20%3F;gender:string%20%3F;aliases:string%20*;id(i):string;name(i):string%20%3F;description(i):string%20%3F],[Image]<avatar%200..1-++[Person],[Membership]-%20person%200..1>[Person],[Person]uses%20-.->[HasAliases],[NamedThing]^-[Person],[NamedThing],[Membership],[Image],[HasAliases],[EmploymentEvent])](https://yuml.me/diagram/nofunky;dir:TB/class/[EmploymentEvent]<has_employment_history%200..*-++[Person&#124;primary_email:string%20%3F;nick:string%20%3F;position:string%20%3F;birth_date:string%20%3F;gender:string%20%3F;aliases:string%20*;id(i):string;name(i):string%20%3F;description(i):string%20%3F],[Image]<avatar%200..1-++[Person],[Membership]-%20person%200..1>[Person],[Person]uses%20-.->[HasAliases],[NamedThing]^-[Person],[NamedThing],[Membership],[Image],[HasAliases],[EmploymentEvent])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Uses Mixin

 *  mixin: [HasAliases](HasAliases.md) - A mixin applied to any class that can have aliases/alternateNames

## Referenced by Class

 *  **None** *[person](person.md)*  <sub>0..1</sub>  **[Person](Person.md)**
 *  **None** *[persons](persons.md)*  <sub>0..\*</sub>  **[Person](Person.md)**

## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [Person➞primary_email](Person_primary_email.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [nick](nick.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [position](position.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [birth_date](birth_date.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [gender](gender.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [avatar](avatar.md)  <sub>0..1</sub>
     * Range: [Image](Image.md)
 * [has_employment_history](has_employment_history.md)  <sub>0..\*</sub>
     * Range: [EmploymentEvent](EmploymentEvent.md)

### Inherited from NamedThing:

 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [image](image.md)  <sub>0..1</sub>
     * Range: [Image](Image.md)

### Mixed in from HasAliases:

 * [➞aliases](hasAliases__aliases.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Person |
| **In Subsets:** | | basic_subset |


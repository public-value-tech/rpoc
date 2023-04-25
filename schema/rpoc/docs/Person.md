
# Class: Person


A person (alive, dead, undead, or fictional).

URI: [rpoc:Person](https://pub.tech/schema/rpoc/Person)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[EmploymentEvent]<has_employment_history%200..*-++[Person&#124;primary_email:string%20%3F;birth_date:string%20%3F;gender:GenderType%20%3F;aliases:string%20*;id(i):string;name(i):string%20%3F;description(i):string%20%3F;image(i):string%20%3F],[Address]<current_address%200..1-++[Person],[Container]++-%20persons%200..*>[Person],[Person]uses%20-.->[HasAliases],[NamedThing]^-[Person],[NamedThing],[HasAliases],[EmploymentEvent],[Container],[Address])](https://yuml.me/diagram/nofunky;dir:TB/class/[EmploymentEvent]<has_employment_history%200..*-++[Person&#124;primary_email:string%20%3F;birth_date:string%20%3F;gender:GenderType%20%3F;aliases:string%20*;id(i):string;name(i):string%20%3F;description(i):string%20%3F;image(i):string%20%3F],[Address]<current_address%200..1-++[Person],[Container]++-%20persons%200..*>[Person],[Person]uses%20-.->[HasAliases],[NamedThing]^-[Person],[NamedThing],[HasAliases],[EmploymentEvent],[Container],[Address])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Uses Mixin

 *  mixin: [HasAliases](HasAliases.md) - A mixin applied to any class that can have aliases/alternateNames

## Referenced by Class

 *  **None** *[persons](persons.md)*  <sub>0..\*</sub>  **[Person](Person.md)**

## Attributes


### Own

 * [Person➞primary_email](Person_primary_email.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [birth_date](birth_date.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [gender](gender.md)  <sub>0..1</sub>
     * Range: [GenderType](GenderType.md)
 * [current_address](current_address.md)  <sub>0..1</sub>
     * Description: The address at which a person currently lives
     * Range: [Address](Address.md)
 * [has_employment_history](has_employment_history.md)  <sub>0..\*</sub>
     * Range: [EmploymentEvent](EmploymentEvent.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [image](image.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

### Mixed in from HasAliases:

 * [➞aliases](hasAliases__aliases.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Person |
| **In Subsets:** | | basic_subset |



# Class: Organization


An organization such as a company or university

URI: [rpoc:Organization](https://pub.tech/schema/rpoc/Organization)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Place],[Place]<founding_location%200..1-%20[Organization&#124;mission_statement:string%20%3F;founding_date:string%20%3F;aliases:string%20*;id(i):string;name(i):string%20%3F;description(i):string%20%3F],[EmploymentEvent]-%20employed_at%200..1>[Organization],[Organization]uses%20-.->[HasAliases],[NamedThing]^-[Organization],[NamedThing],[Image],[HasAliases],[EmploymentEvent])](https://yuml.me/diagram/nofunky;dir:TB/class/[Place],[Place]<founding_location%200..1-%20[Organization&#124;mission_statement:string%20%3F;founding_date:string%20%3F;aliases:string%20*;id(i):string;name(i):string%20%3F;description(i):string%20%3F],[EmploymentEvent]-%20employed_at%200..1>[Organization],[Organization]uses%20-.->[HasAliases],[NamedThing]^-[Organization],[NamedThing],[Image],[HasAliases],[EmploymentEvent])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Uses Mixin

 *  mixin: [HasAliases](HasAliases.md) - A mixin applied to any class that can have aliases/alternateNames

## Referenced by Class

 *  **None** *[company](company.md)*  <sub>0..1</sub>  **[Organization](Organization.md)**
 *  **None** *[employed_at](employed_at.md)*  <sub>0..1</sub>  **[Organization](Organization.md)**
 *  **None** *[organizations](organizations.md)*  <sub>0..\*</sub>  **[Organization](Organization.md)**

## Attributes


### Own

 * [mission_statement](mission_statement.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [founding_date](founding_date.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [founding_location](founding_location.md)  <sub>0..1</sub>
     * Range: [Place](Place.md)

### Inherited from NamedThing:

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
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
| **Mappings:** | | schema:Organization |


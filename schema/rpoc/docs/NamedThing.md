
# Class: NamedThing


A generic grouping for any identifiable entity

URI: [rpoc:NamedThing](https://pub.tech/schema/rpoc/NamedThing)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Person],[Organization],[Image]<image%200..1-++[NamedThing&#124;id:string;name:string%20%3F;description:string%20%3F],[NamedThing]^-[Person],[NamedThing]^-[Organization],[NamedThing]^-[Context],[Image],[Context])](https://yuml.me/diagram/nofunky;dir:TB/class/[Person],[Organization],[Image]<image%200..1-++[NamedThing&#124;id:string;name:string%20%3F;description:string%20%3F],[NamedThing]^-[Person],[NamedThing]^-[Organization],[NamedThing]^-[Context],[Image],[Context])

## Children

 * [Context](Context.md) - A team, group, project, or other entity that has a context for a person
 * [Organization](Organization.md) - An organization such as a company or university
 * [Person](Person.md) - A person (alive, dead, undead, or fictional).

## Referenced by Class


## Attributes


### Own

 * [id](id.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [name](name.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [image](image.md)  <sub>0..1</sub>
     * Range: [Image](Image.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Close Mappings:** | | schema:Thing |


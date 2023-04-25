
# Class: Context


A team, group, project, or other entity that has a context for a person

URI: [rpoc:Context](https://pub.tech/schema/rpoc/Context)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[HasAliases],[Context]<parent%200..1-%20[Context&#124;primary_email:string%20%3F;mission_statement:string%20%3F;start_date:date%20%3F;end_date:date%20%3F;aliases:string%20*;id(i):string;name(i):string%20%3F;description(i):string%20%3F;image(i):string%20%3F],[Membership]-%20context%200..1>[Context],[Container]++-%20contexts%200..*>[Context],[Interaction]-%20obsoleted_by%200..1>[Context],[Context]uses%20-.->[HasAliases],[NamedThing]^-[Context],[Membership],[Interaction],[Container])](https://yuml.me/diagram/nofunky;dir:TB/class/[NamedThing],[HasAliases],[Context]<parent%200..1-%20[Context&#124;primary_email:string%20%3F;mission_statement:string%20%3F;start_date:date%20%3F;end_date:date%20%3F;aliases:string%20*;id(i):string;name(i):string%20%3F;description(i):string%20%3F;image(i):string%20%3F],[Membership]-%20context%200..1>[Context],[Container]++-%20contexts%200..*>[Context],[Interaction]-%20obsoleted_by%200..1>[Context],[Context]uses%20-.->[HasAliases],[NamedThing]^-[Context],[Membership],[Interaction],[Container])

## Parents

 *  is_a: [NamedThing](NamedThing.md) - A generic grouping for any identifiable entity

## Uses Mixin

 *  mixin: [HasAliases](HasAliases.md) - A mixin applied to any class that can have aliases/alternateNames

## Referenced by Class

 *  **None** *[context](context.md)*  <sub>0..1</sub>  **[Context](Context.md)**
 *  **None** *[contexts](contexts.md)*  <sub>0..\*</sub>  **[Context](Context.md)**
 *  **None** *[obsoleted_by](obsoleted_by.md)*  <sub>0..1</sub>  **[Context](Context.md)**
 *  **None** *[parent](parent.md)*  <sub>0..1</sub>  **[Context](Context.md)**

## Attributes


### Own

 * [Context➞primary_email](Context_primary_email.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [mission_statement](mission_statement.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [start_date](start_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [end_date](end_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [parent](parent.md)  <sub>0..1</sub>
     * Range: [Context](Context.md)

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
| **Mappings:** | | schema:Project |
| **In Subsets:** | | basic_subset |


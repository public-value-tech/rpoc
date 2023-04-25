
# Class: Role


A set of responsibilities, skills and tasks that a person has in a context

URI: [rpoc:Role](https://pub.tech/schema/rpoc/Role)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Membership]-%20role%200..1>[Role&#124;role_name:string;role_type:RoleType%20%3F;description:string%20%3F;start_date:date%20%3F;end_date:date%20%3F;aliases:string%20*],[Container]++-%20roles%200..*>[Role],[Role]uses%20-.->[HasAliases],[Membership],[HasAliases],[Container])](https://yuml.me/diagram/nofunky;dir:TB/class/[Membership]-%20role%200..1>[Role&#124;role_name:string;role_type:RoleType%20%3F;description:string%20%3F;start_date:date%20%3F;end_date:date%20%3F;aliases:string%20*],[Container]++-%20roles%200..*>[Role],[Role]uses%20-.->[HasAliases],[Membership],[HasAliases],[Container])

## Uses Mixin

 *  mixin: [HasAliases](HasAliases.md) - A mixin applied to any class that can have aliases/alternateNames

## Referenced by Class

 *  **None** *[role](role.md)*  <sub>0..1</sub>  **[Role](Role.md)**
 *  **None** *[roles](roles.md)*  <sub>0..\*</sub>  **[Role](Role.md)**

## Attributes


### Own

 * [role_name](role_name.md)  <sub>1..1</sub>
     * Range: [String](types/String.md)
 * [role_type](role_type.md)  <sub>0..1</sub>
     * Range: [RoleType](RoleType.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)
 * [start_date](start_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [end_date](end_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)

### Mixed in from HasAliases:

 * [➞aliases](hasAliases__aliases.md)  <sub>0..\*</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | schema:Role |
| **In Subsets:** | | basic_subset |



# Class: Membership


A person's roles in a context

URI: [rpoc:Membership](https://pub.tech/schema/rpoc/Membership)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Role],[Person],[Context]<context%200..1-%20[Membership&#124;start_date:date%20%3F;end_date:date%20%3F;description:string%20%3F],[Role]<role%200..1-%20[Membership],[Person]<person%200..1-%20[Membership],[Context])](https://yuml.me/diagram/nofunky;dir:TB/class/[Role],[Person],[Context]<context%200..1-%20[Membership&#124;start_date:date%20%3F;end_date:date%20%3F;description:string%20%3F],[Role]<role%200..1-%20[Membership],[Person]<person%200..1-%20[Membership],[Context])

## Referenced by Class

 *  **None** *[memberships](memberships.md)*  <sub>0..\*</sub>  **[Membership](Membership.md)**

## Attributes


### Own

 * [person](person.md)  <sub>0..1</sub>
     * Range: [Person](Person.md)
 * [role](role.md)  <sub>0..1</sub>
     * Range: [Role](Role.md)
 * [context](context.md)  <sub>0..1</sub>
     * Range: [Context](Context.md)
 * [start_date](start_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [end_date](end_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [description](description.md)  <sub>0..1</sub>
     * Range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | rpoc:Membership |
| **In Subsets:** | | basic_subset |


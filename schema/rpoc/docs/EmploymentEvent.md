
# Class: EmploymentEvent




URI: [rpoc:EmploymentEvent](https://pub.tech/schema/rpoc/EmploymentEvent)


[![img](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization],[Event],[Organization]<employed_at%200..1-%20[EmploymentEvent&#124;start_date(i):date%20%3F;end_date(i):date%20%3F;duration(i):float%20%3F;is_current(i):boolean%20%3F],[Person]++-%20has_employment_history%200..*>[EmploymentEvent],[Event]^-[EmploymentEvent],[Person])](https://yuml.me/diagram/nofunky;dir:TB/class/[Organization],[Event],[Organization]<employed_at%200..1-%20[EmploymentEvent&#124;start_date(i):date%20%3F;end_date(i):date%20%3F;duration(i):float%20%3F;is_current(i):boolean%20%3F],[Person]++-%20has_employment_history%200..*>[EmploymentEvent],[Event]^-[EmploymentEvent],[Person])

## Parents

 *  is_a: [Event](Event.md)

## Referenced by Class

 *  **None** *[has_employment_history](has_employment_history.md)*  <sub>0..\*</sub>  **[EmploymentEvent](EmploymentEvent.md)**

## Attributes


### Own

 * [employed_at](employed_at.md)  <sub>0..1</sub>
     * Range: [Organization](Organization.md)

### Inherited from Event:

 * [start_date](start_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [end_date](end_date.md)  <sub>0..1</sub>
     * Range: [Date](types/Date.md)
 * [duration](duration.md)  <sub>0..1</sub>
     * Range: [Float](types/Float.md)
 * [is_current](is_current.md)  <sub>0..1</sub>
     * Range: [Boolean](types/Boolean.md)

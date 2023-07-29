export type NamedThingId = string
export type PersonId = string
export type ContextId = string
export type RoleRoleName = string
export type OrganizationId = string
export type PlaceId = string
/**
 * A generic grouping for any identifiable entity
 */
export interface NamedThing  {
    id?: string,
    name?: string,
    description?: string,
    image?: Image,
}
/**
 * A person (alive, dead, undead, or fictional).
 */
export interface Person  extends NamedThing, HasAliases  {
    primary_email?: string,
    birth_date?: string,
    gender?: string,
    /**
     * The address at which a person currently lives
     */current_address?: Address,
    position?: string,
    nick?: string,
    avatar?: Image,
    has_employment_history?: EmploymentEvent[],
    aliases?: string,
    id?: string,
    name?: string,
    description?: string,
    image?: Image,
}
/**
 * A mixin applied to any class that can have aliases/alternateNames
 */
export interface HasAliases  {
    aliases?: string,
}
/**
 * A team, group, project, or other entity that has a context for a person
 */
export interface Context  extends NamedThing, HasAliases  {
    primary_email?: string,
    mission_statement?: string,
    start_date?: date,
    end_date?: date,
    parent?: ContextId,
    aliases?: string,
    id?: string,
    name?: string,
    description?: string,
    image?: Image,
}
/**
 * A set of responsibilities, skills and tasks that a person has in a context
 */
export interface Role  extends HasAliases  {
    role_name?: string,
    role_type?: string,
    description?: string,
    start_date?: date,
    end_date?: date,
    aliases?: string,
}
/**
 * A person's roles in a context
 */
export interface Membership  {
    person?: PersonId,
    role?: RoleRoleName,
    context?: ContextId,
    start_date?: date,
    end_date?: date,
    description?: string,
}
/**
 * An organization such as a company or university
 */
export interface Organization  extends NamedThing, HasAliases  {
    mission_statement?: string,
    founding_date?: string,
    founding_location?: PlaceId,
    aliases?: string,
    id?: string,
    name?: string,
    description?: string,
    image?: Image,
}

export interface Place  extends HasAliases  {
    id?: string,
    name?: string,
    aliases?: string,
}

export interface Address  {
    street?: string,
    city?: string,
    postal_code?: string,
}

export interface Event  {
    start_date?: date,
    end_date?: date,
    duration?: number,
    is_current?: boolean,
}

export interface Interaction  {
    type?: string,
    status?: string,
    start_date?: date,
    end_date?: date,
    related_to?: string,
    obsoleted_by?: ContextId,
    description?: string,
}

export interface EmploymentEvent  extends Event  {
    employed_at?: OrganizationId,
    start_date?: date,
    end_date?: date,
    duration?: number,
    is_current?: boolean,
}

export interface WithLocation  {
    in_location?: PlaceId,
}

export interface Image  {
    url?: string,
}


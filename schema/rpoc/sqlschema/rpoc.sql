

CREATE TABLE "Address" (
	street TEXT, 
	city TEXT, 
	postal_code TEXT, 
	PRIMARY KEY (street, city, postal_code)
);

CREATE TABLE "Concept" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Container" (
	persons TEXT, 
	roles TEXT, 
	contexts TEXT, 
	organizations TEXT, 
	PRIMARY KEY (persons, roles, contexts, organizations)
);

CREATE TABLE "Context" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	primary_email TEXT, 
	mission_statement TEXT, 
	start_date DATE, 
	end_date DATE, 
	parent TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(parent) REFERENCES "Context" (id)
);

CREATE TABLE "Event" (
	start_date DATE, 
	end_date DATE, 
	duration FLOAT, 
	is_current BOOLEAN, 
	PRIMARY KEY (start_date, end_date, duration, is_current)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	primary_email TEXT, 
	birth_date TEXT, 
	gender VARCHAR(17), 
	current_address TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Place" (
	id TEXT NOT NULL, 
	name TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Role" (
	id TEXT NOT NULL, 
	role_name TEXT, 
	role_type VARCHAR(9), 
	description TEXT, 
	start_date DATE, 
	end_date DATE, 
	PRIMARY KEY (id)
);

CREATE TABLE "Interaction" (
	type TEXT, 
	status TEXT, 
	start_date DATE, 
	end_date DATE, 
	related_to TEXT, 
	obsoleted_by TEXT, 
	PRIMARY KEY (type, status, start_date, end_date, related_to, obsoleted_by), 
	FOREIGN KEY(obsoleted_by) REFERENCES "Context" (id)
);

CREATE TABLE "Organization" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	image TEXT, 
	mission_statement TEXT, 
	founding_date TEXT, 
	founding_location TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(founding_location) REFERENCES "Place" (id)
);

CREATE TABLE "Context_aliases" (
	backref_id TEXT, 
	aliases TEXT, 
	PRIMARY KEY (backref_id, aliases), 
	FOREIGN KEY(backref_id) REFERENCES "Context" (id)
);

CREATE TABLE "Person_aliases" (
	backref_id TEXT, 
	aliases TEXT, 
	PRIMARY KEY (backref_id, aliases), 
	FOREIGN KEY(backref_id) REFERENCES "Person" (id)
);

CREATE TABLE "Place_aliases" (
	backref_id TEXT, 
	aliases TEXT, 
	PRIMARY KEY (backref_id, aliases), 
	FOREIGN KEY(backref_id) REFERENCES "Place" (id)
);

CREATE TABLE "Role_aliases" (
	backref_id TEXT, 
	aliases TEXT, 
	PRIMARY KEY (backref_id, aliases), 
	FOREIGN KEY(backref_id) REFERENCES "Role" (id)
);

CREATE TABLE "EmploymentEvent" (
	start_date DATE, 
	end_date DATE, 
	duration FLOAT, 
	is_current BOOLEAN, 
	employed_at TEXT, 
	"Person_id" TEXT, 
	PRIMARY KEY (start_date, end_date, duration, is_current, employed_at, "Person_id"), 
	FOREIGN KEY(employed_at) REFERENCES "Organization" (id), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);

CREATE TABLE "Organization_aliases" (
	backref_id TEXT, 
	aliases TEXT, 
	PRIMARY KEY (backref_id, aliases), 
	FOREIGN KEY(backref_id) REFERENCES "Organization" (id)
);

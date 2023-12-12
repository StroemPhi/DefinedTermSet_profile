

CREATE TABLE "CreativeWork" (
	id TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DefinedTerm" (
	id TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	"inDefinedTermSet" TEXT NOT NULL, 
	"termCode" TEXT NOT NULL, 
	PRIMARY KEY (id)
);

CREATE TABLE "Intangible" (
	id TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Thing" (
	id TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DefinedTermSet" (
	id TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	"hasDefinedTerm" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("hasDefinedTerm") REFERENCES "DefinedTerm" (id)
);

CREATE TABLE "CreativeWork_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "CreativeWork" (id)
);

CREATE TABLE "DefinedTerm_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "DefinedTerm" (id)
);

CREATE TABLE "Intangible_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "Intangible" (id)
);

CREATE TABLE "Thing_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "Thing" (id)
);

CREATE TABLE "DefinedTermSet_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "DefinedTermSet" (id)
);

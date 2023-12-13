

CREATE TABLE "CreativeWork" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "DefinedTermSet" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	name TEXT NOT NULL, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "Intangible" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "Thing" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "DefinedTerm" (
	identifier TEXT NOT NULL, 
	description TEXT, 
	name TEXT, 
	url TEXT, 
	"inDefinedTermSet" TEXT NOT NULL, 
	"termCode" TEXT NOT NULL, 
	"sameAs" TEXT, 
	"DefinedTermSet_identifier" TEXT, 
	PRIMARY KEY (identifier), 
	FOREIGN KEY("inDefinedTermSet") REFERENCES "DefinedTermSet" (identifier), 
	FOREIGN KEY("DefinedTermSet_identifier") REFERENCES "DefinedTermSet" (identifier)
);

CREATE TABLE "CreativeWork_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "CreativeWork" (identifier)
);

CREATE TABLE "DefinedTermSet_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "DefinedTermSet" (identifier)
);

CREATE TABLE "Intangible_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "Intangible" (identifier)
);

CREATE TABLE "Thing_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "Thing" (identifier)
);

CREATE TABLE "DefinedTerm_alternateName" (
	backref_id TEXT, 
	"alternateName" TEXT, 
	PRIMARY KEY (backref_id, "alternateName"), 
	FOREIGN KEY(backref_id) REFERENCES "DefinedTerm" (identifier)
);

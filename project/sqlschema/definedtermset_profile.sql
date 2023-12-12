

CREATE TABLE "CreativeWork" (
	id TEXT NOT NULL, 
	"alternateName" TEXT, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DefinedTerm" (
	id TEXT NOT NULL, 
	"alternateName" TEXT, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	"inDefinedTermSet" TEXT NOT NULL, 
	"termCode" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("inDefinedTermSet") REFERENCES "DefinedTermSet" (id)
);

CREATE TABLE "DefinedTermSet" (
	id TEXT NOT NULL, 
	"alternateName" TEXT, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	"hasDefinedTerm" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("hasDefinedTerm") REFERENCES "DefinedTerm" (id)
);

CREATE TABLE "Intangible" (
	id TEXT NOT NULL, 
	"alternateName" TEXT, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Thing" (
	id TEXT NOT NULL, 
	"alternateName" TEXT, 
	description TEXT, 
	name TEXT, 
	"sameAs" TEXT, 
	url TEXT, 
	PRIMARY KEY (id)
);

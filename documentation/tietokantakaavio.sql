CREATE TABLE "tyontekijat" (
  "id" int PRIMARY KEY,
  "nimi" text UNIQUE,
  "salasana" text
);

CREATE TABLE "projektit" (
  "id" int PRIMARY KEY,
  "nimi" text UNIQUE,
  "projektipaallikko_id" int
);

CREATE TABLE "tyoajatt" (
  "projektit_id" int,
  "kayttajat_id" int,
  "aika" int
);


ALTER TABLE "projektit" ADD FOREIGN KEY ("projektipaallikko_id") REFERENCES "tyontekijat" ("id");

ALTER TABLE "tyoaikakirjaukset" ADD FOREIGN KEY ("kayttajat_id") REFERENCES "tyontekijat" ("id");

ALTER TABLE "tyoaikakirjaukset" ADD FOREIGN KEY ("projektit_id") REFERENCES "projektit" ("id");

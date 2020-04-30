# Käyttäjätarinat

#### 1. Minä käyttäjänä haluan kirjauta palveluun ja se onnistuu yläreunassa olevalla kirjaudu linkillä.

SQL:

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account 

WHERE account.username = ? AND account.password = ?
 LIMIT ? OFFSET ?



#### 2. Minä käyttäjänä haluan kirjauta palvelusta ulos ja se onnistuu yläreunassa olevalla linkillä.

SQL:

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account 



#### 3. Voin rekisteröityä sovellukseen yläkulman sign up painikkeesta.

SQL:

INSERT INTO account (date_created, date_modified, name, username, password) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)



#### 4. Kaikkien sovellukseen lisättyjen projektien tarkastelu onnistuu minulta kirjautumatta tai kirjautuneena.

SQL:

SELECT projektit.id AS projektit_id, projektit.nimi AS projektit_nimi, projektit.valmis AS projektit_valmis, projektit.projektipaallikko AS projektit_projektipaallikko 
FROM projektit

SELECT projekti_id, SUM(tyoaika) FROM tyoajat GROUP BY projekti_id



#### 5. Kaikkien sovellukseen lisättyjen työaikojen tarkastelu onnistuu minulta kirjautumatta tai kirjautuneena.

SQL:

SELECT tyoajat.id AS tyoajat_id, tyoajat.account_id AS tyoajat_account_id, tyoajat.tyoaika AS tyoajat_tyoaika, tyoajat.projekti_id AS tyoajat_projekti_id, tyoajat.date_created AS tyoajat_date_created 

SELECT account_id, SUM(tyoaika) FROM tyoajat GROUP BY account_id



#### 6. Kirjautuneen voin lisätä itselleni työaikaa tunteina (desimaali, vähintään 1h).

SQL:

INSERT INTO tyoajat (account_id, tyoaika, projekti_id, date_created) VALUES (?, ?, ?, CURRENT_TIMESTAMP)



#### 7. Kirjautuneena voin lisätä sovellukseen projekteja, joiden projektipäälliköksi asetun automaattisesti.

SQL:

INSERT INTO projektit (nimi, valmis, projektipaallikko) VALUES (?, ?, ?)



#### 8. Voin asettaa projektit valmiiksi kun olen kirjautuneena sovellukseen.

SQL:

UPDATE projektit SET valmis=? WHERE projektit.id = ?



#### 9. Voin poistaa projektin kun olen kirjautuneena

SQL:

DELETE FROM projektit WHERE projektit.id = ?



#### 10. Yläreunassa olevalla linkkivalikolla voin liikkua eri ominaisuuksien välillä helposti.



#### 11. Voin poistaa työaikoja kirjautuneena.

SQL:

DELETE FROM tyoajat WHERE tyoajat.id = ?



#### 12. Voin tarkastella etusivulta kuinka monella henkilöllä on vähintään yksi työaikamerkintä.

SQL:

SELECT account.id AS account_id, account.date_created AS account_date_created, account.date_modified AS account_date_modified, account.name AS account_name, account.username AS account_username, account.password AS account_password 
FROM account 
WHERE account.id = ?

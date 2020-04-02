# Harjoitustyö - projektien työaikaseuranta

Tässä harjoitustyössä luodaan työaikaseuranta, johon voidaan kirjautua henkilönä.
Henkilölle voidaan lisätä projekteja missä hän on osallisena joka päällikkönä tai 
rivimiehenä. Henkilö voi lisätä itselleen työaikaa ja katsella omaa mennyttä työmääräänsä. Mikäli hän on jonkin projektin päällikkö hänellä on myös 
mahdollisuus nähdä siitä kaikki.

# Työ tällä hetkellä
Tällä hetkellä sovelluksessa voidaan tarkastella lisättyjä työaikoja sekä lisättyjä projekteja. Sovellukseen myös pystytään kirjautumaan sisään ja sieltä pystytään kirjautua ulos. Mikäli sisään 
on kirjauduttu voidaan projekteja lisätä ja työaikoja lisätä. Projektit voidaan myös merkitä valmiiksi.Yhteenveto kysely antaa näkyviin kaikki työntekjät joilla on vähintään yksi työaika tietokannassa.
## Ongelmia työssä
Yritin lisätä projekteille mahdollisuutta poistaa koko projekti. Tässä en kuitenkaan onnistunut koska engine antaa ROLLBACK tulokset. Hieman tätä tutkin ja päättelin, että voiko tämä johtua siitä, että
projektipäällikkö on liitetty suoraan projektiin kirjautumisen perusteella. Pitäisikö siis pitää tällä jonkin laista liitostaulua?

## Linkki sovellukseen Herokussa
[Heroku](https://tsoha-tyoaikaseuranta.herokuapp.com/)

Testitunnus:

käyttäjä:sauli

salasana:niinisto

### Käyttäjätarinat
[käyttäjätarinat](https://github.com/karhuherra/nytsaisitoimia/blob/master/documentation/userstory)

### linkki tietokantakaavioon
[tietokantakaavio](https://github.com/karhuherra/nytsaisitoimia/blob/master/documentation/85aa0012.png)


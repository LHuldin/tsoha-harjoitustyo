# Retro peli ja laite kirjasto
- Käyttäjä voi rekisteröityä ja kirjautua sovellukseen
- Kirjauduttuaan käyttäjä voi lisätä kirjastoon laitteita (tietokoneet ja pelikonsolit) tai sovelluksia ja pelejä.
- käyttäjä voi määritelllä lisäämänsä tuotteet joko yksityisiksi tai julkisiksi.
- käyttäjä voi myös poistaa lisäämiään tuotteita.
- Julkiseksi määritellyt tuotteet näkyvät oman sivun lisäksi kaikkien käyttäjien yhteisellä sivulla
- Yhteisellä sivulla käyttäjillä on mahdollista jättää myös kommentteja

## Ohjelman testaus
- Ohjelman VANHA VERSIO löytyy osoitteesta (https://tsoha-harjoitustyo.fly.dev)
- Koska ohjelman päivittäminen fly.io palveluun ei tällä hetkellä onnistu voi sitä testata seuraavilla ohjeilla:
- Kloonaa tämä repositorio koneellesi.
- Siirry repositorion juurihakemistoon ja luo sinne .env tiedosto.
- Lisää .env tiedostoon seuraavat rivit:
    ```
    DATABASE_URL=<tietokannan-paikallinen-osoite>
    SECRET_KEY=<salainen-avain>
    ```
- Aktivoi virtuaaliympäristö ja asenna tarvittavat riipuvuudet seuraavilla komennoilla:
    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r ./requirements.txt
    ```
- Tietokanta määritellään postgres tietokantaan seuraavalla komennolla:
    ```
    $ psql < schema.sql
    ```
- Nyt olet valmis käynnistämään ohjelman komennolla:
    ```
    $ flask run
    ```

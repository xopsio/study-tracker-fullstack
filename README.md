# Study Tracker – Fullstack

Study Tracker on fullstack-harjoitusprojekti, jonka avulla harjoitellaan ohjelmistokehitystä, versionhallintaa, testausta ja frontend–backend-rakennetta.

Projekti on vielä kehitysvaiheessa. Tavoitteena on rakentaa sovellus, jossa opiskeluun liittyviä tietoja voidaan käsitellä ja seurata.

## Teknologiat

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- FastAPI
- Pydantic v2

### Tietokanta
- SQLite

### Testaus
- pytest
- FastAPI TestClient

### Työkalut
- Git
- GitHub
- dokumentaatio
- koodikatselmointi

## Projektin rakenne

- `frontend/` – käyttöliittymän tiedostot
- `backend/` – FastAPI-sovellus ja tietomallit
- `db/` – tietokantaan liittyvät tiedostot
- `tests/` – automaattiset testit
- `docs/` – projektin tarkempi dokumentaatio
- `scripts/` – kehitystä ja testausta tukevat skriptit

## Kehityskäytännöt

Projektissa pyritään tekemään muutokset pieninä ja hallittuina kokonaisuuksina.

Muutokset testataan ennen niiden yhdistämistä päähaaraan, ja Git-historiaa käytetään projektin kehityksen seuraamiseen.

## Haaroitusmalli

Projektissa käytetään kahta pääasiallista haaraa:

- `main` sisältää vakaan version projektista.
- `develop` toimii kehityshaarana.

Uudet muutokset tehdään `develop`-haarassa. Valmiit ja tarkistetut muutokset yhdistetään `main`-haaraan pull requestin kautta.

Tarvittaessa yksittäisiä ominaisuuksia voidaan kehittää omissa feature-haaroissa, jotka yhdistetään ensin `develop`-haaraan.

## Tekoälytyökalut

Projektissa voidaan käyttää tekoälypohjaisia työkaluja oppimisen, ongelmien analysoinnin ja koodikatselmoinnin tukena. Kehityspäätökset ja muutosten hyväksyminen tehdään kuitenkin projektin kehittäjän toimesta.

Tarkemmat työkalukohtaiset ohjeet löytyvät `docs/`-hakemistosta.

## Dokumentaatio

Projektin tarkempi dokumentaatio löytyy `docs/`-hakemistosta.

Keskeisiä projektitiedostoja ovat myös:

- `AGENTS.md` – agenttien ja työkalujen toimintarajat
- `best_practices.md` – projektin kehityskäytännöt

## Versionhallinta

Projektissa käytetään Git-versionhallintaa ja GitHubia.

Kehitystyö tehdään haaroissa ja muutokset yhdistetään päähaaraan pull requestien kautta.

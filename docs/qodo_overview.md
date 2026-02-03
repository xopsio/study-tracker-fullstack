# Qodo.ai usage and documentation


Tämä projekti on **opiskeluun ja osaamisen näyttämiseen tarkoitettu fullstack-harjoitusprojekti**.
Projektin tavoitteena on oppia ohjelmistokehitystä hallitusti, ymmärtäen ja ammattimaisesti
– ei vain tuottamalla koodia.

Projektissa yhdistyvät:
- frontend (HTML, CSS, JavaScript)
- backend (Python, FastAPI)
- tietokannat
- testaus
- versionhallinta
- open source -tyylinen työskentely

---

## Qodo.ai tässä projektissa

Qodo.ai:tä käytetään **oppimisen tukena**, ei automaattisena koodinkorjaajana.

Qodon käyttö on tässä projektissa **tarkasti ohjattua ja dokumentoitua**.
Tavoitteena on varmistaa, että:
- jokainen korjaus ymmärretään
- muutokset ovat pieniä ja hallittuja
- oppiminen menee nopeuden edelle

---

## Qodoa koskevat dokumentit

Projektissa on useita tiedostoja, jotka yhdessä määrittelevät,
miten Qodoa (ja muita tekoälyagentteja) saa käyttää.

### AGENTS.md
**Sijainti:** projektin juuressa

Määrittelee:
- miten tekoälyagentit saavat toimia
- että diagnoosi tehdään ennen koodia
- että muutokset pidetään pieninä
- mitkä komennot käytetään varmentamiseen

Tämä on **korkeimman tason ohjetiedosto** agenteille.

---

### best_practices.md
**Sijainti:** projektin juuressa

Määrittelee projektin pakolliset käytännöt:
- oppimismallin (selitys ennen korjausta)
- kieli- ja tyylistandardit
- frontend- ja backend-käytännöt
- testausvaatimukset
- pydantic v2 -säännöt

Tätä tiedostoa noudatetaan aina, myös Qodon ehdotuksia arvioitaessa.

---

### docs/qodo_workflow.md

Määrittelee **pakollisen työnkulun Qodon käyttöön**:

1. **Diagnoosi ilman koodia**
   - mikä on juurisyy
   - mihin tiedostoon kosketaan
   - miten korjaus varmennetaan

2. **Minimaalinen korjaus**
   - yksi tiedosto
   - pieni diff
   - ei refaktorointia ilman pyyntöä

Tämä toimii checklistinä joka kerta, kun Qodoa käytetään.

---

### docs/qodo_prompts.md

Sisältää **valmiit kehotteet (promptit)** Qodon käyttöön.

Niillä varmistetaan, että Qodo:
- selittää ennen korjaamista
- ei tee arvailuja
- tarkistaa versiot ja ympäristön
- suosii testattavuutta

Promptit kopioidaan suoraan Qodon käyttöliittymään.

---

### docs/learning-log.md

**Oppimisloki**, johon kirjataan Qodon käyttö.

Yksi rivi per tapaus, muodossa:

päivämäärä – ongelma – juurisyy – korjaus – varmennus


Lokiin kirjoitetaan **vain**, kun Qodoa on käytetty ei-triviaaliin ongelmaan.
Tarkoitus on estää samojen virheiden toistuminen ja lukita opittu tieto.

---

### docs/commit-notes.md

Sisältää muistiinpanot Qodoon liittyvistä commit-käytännöistä.
Auttaa ymmärtämään, miksi tietyt dokumentaatio-commitit on tehty.

---

## Projektin perusperiaatteet

- oppiminen ennen automaatiota
- ymmärrys ennen nopeutta
- pienet muutokset ovat parempia kuin suuret
- testaus ja varmennus ovat pakollisia
- tekoäly on työkalu, ei ajattelun korvike

---

## Lopuksi

Tämä projekti on rakennettu siten, että se:
- soveltuu opiskeluun
- kelpaa TET-harjoitteluun
- vastaa open source -projektien työskentelytapaa
- tukee osaamisen näyttämistä

Jos korjaus tehdään ilman ymmärrystä,
työnkulku on epäonnistunut.

Tavoite on oppia tekemään asiat oikein.

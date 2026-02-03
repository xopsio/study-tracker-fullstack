## workflow (must follow)

> this workflow must be followed every time qodo is used.  
> suomennos: tätä työnkulkua on noudatettava joka kerta, kun qodoa käytetään.

### step 1: diagnose only (no code)

**prompt**
diagnose the issue only.
explain the root cause in 1–3 sentences,
tell me exactly where to change,
and how to verify.
do not provide any code yet.

**before continuing, confirm**
- i understand the root cause
- i know exactly which file will be changed
- i know how the fix will be verified

**suomennos**
vaihe 1: diagnosoi vain (ei koodia)

kehote:
diagnosoi ongelma vain.
selitä juurisyy 1–3 lauseella,
kerro täsmälleen mihin muutos tehdään,
ja miten korjaus varmennetaan.
älä anna vielä koodia.

ennen jatkamista varmista:
- ymmärrän juurisyyn
- tiedän tarkalleen mitä tiedostoa muutetaan
- tiedän miten korjaus varmennetaan

---

### step 2: minimal fix (single file)

**prompt**
now provide the minimal fix.
change only this file: <file_path>.
keep the diff as small as possible.
do not refactor unrelated code.
include a short verification step.

**rules**
- one file only
- small diff
- no new dependencies

---

**suomennos**
vaihe 2: minimaalinen korjaus (yksi tiedosto)

kehote:
anna nyt minimaalinen korjaus.
muuta vain tätä tiedostoa: <tiedostopolku>.
pidä muutos mahdollisimman pienenä.
älä refaktoroi tai koske muuhun koodiin.
lisää lyhyt varmennusohje.

säännöt:
- vain yksi tiedosto
- pieni muutos
- ei uusia riippuvuuksia

## project standards

- source code language: english only
- comments: lowercase only
- strings: english + lowercase only

- pydantic v2:
  use ConfigDict(from_attributes=True)
  do not use orm_mode

- backend tests:
  pytest + fastapi TestClient

- tests must not perform real network calls

**suomennos**
projektin standardit

- lähdekoodin kieli: vain englanti
- kommentit: vain pienet kirjaimet
- merkkijonot: englanti ja pienet kirjaimet

- pydantic v2:
  käytä ConfigDict(from_attributes=True)
  älä käytä orm_modea

- backend-testit:
  pytest + fastapi TestClient

- testit eivät saa tehdä oikeita verkkokutsuja

## verification (always)

before committing or accepting a fix, verify:

- backend starts without errors
- at least one relevant endpoint works
- tests pass (if tests exist or were modified)

**suomennos**
varmennus (aina)

ennen committia tai korjauksen hyväksymistä varmista:

- backend käynnistyy ilman virheitä
- vähintään yksi oleellinen endpoint toimii
- testit menevät läpi (jos testejä on tai niitä on muutettu)

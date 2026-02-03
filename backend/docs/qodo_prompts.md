# qodo prompts (learning-first)

this file defines the exact prompts i use with qodo to ensure it teaches,
not just fixes code. always follow the two-step workflow:
1) diagnose only
2) minimal fix

---

## 1. diagnose only (no code)

**english**
diagnose the issue only.
explain the root cause in 1–3 sentences,
tell me exactly where the change should be made,
and how to verify the fix.
do not provide any code yet.

**suomi**
diagnosoi ongelma vain.
selitä juurisyy 1–3 lauseella,
kerro tarkasti mihin muutos tehdään,
ja miten korjaus varmennetaan.
älä anna vielä koodia.

---

## 2. minimal fix for a single file

**english**
now provide the minimal fix.
change only this file: <file_path>.
keep the diff as small as possible.
do not refactor or touch unrelated code.
include a short verification step.

**suomi**
anna nyt minimaalinen korjaus.
muuta vain tätä tiedostoa: <tiedostopolku>.
pidä muutos mahdollisimman pienenä.
älä refaktoroi tai koske muuhun koodiin.
lisää lyhyt varmennusohje.

---

## 3. explain before fixing (learning enforcement)

**english**
before proposing any fix,
explain why the current code behaves incorrectly
and what concept or rule is being violated.

**suomi**
ennen kuin ehdotat korjausta,
selitä miksi nykyinen koodi toimii väärin
ja mitä käsitettä tai sääntöä se rikkoo.

---

## 4. multiple options, choose one

**english**
if there are multiple valid solutions,
list two options briefly
and recommend one with a clear reason.

**suomi**
jos mahdollisia ratkaisuja on useita,
listaa kaksi vaihtoehtoa lyhyesti
ja suosittele yhtä selkeällä perustelulla.

---

## 5. version and environment check

**english**
verify assumptions about versions and environment
(e.g. pydantic v2, fastapi, python version)
before suggesting a fix.

**suomi**
tarkista oletukset versioista ja ympäristöstä
(esim. pydantic v2, fastapi, python-versio)
ennen kuin ehdotat korjausta.

---

## 6. test-focused help

**english**
focus on making the code testable.
prefer fixes that improve clarity and testability
over clever or compact solutions.

**suomi**
keskity tekemään koodista testattavaa.
suosi ratkaisuja, jotka parantavat selkeyttä ja testattavuutta
älykkäiden tai tiiviiden ratkaisujen sijaan.

---

## 7. stop and ask if unclear

**english**
if the intent of the code is unclear,
ask one clarifying question instead of guessing.

**suomi**
jos koodin tarkoitus on epäselvä,
kysy yksi tarkentava kysymys arvaamisen sijaan.

---

## default rule

**english**
learning and understanding are more important than speed.
do not optimize for fewer lines of code.

**suomi**
oppiminen ja ymmärrys ovat tärkeämpiä kuin nopeus.
älä optimoi koodirivien määrää.

## project constraints (must respect)

**english**
follow repository standards strictly:
english only in source code,
lowercase comments,
lowercase strings,
pydantic v2 conventions,
small focused diffs.

**suomi**
noudata projektin standardeja tarkasti:
vain englanti lähdekoodissa,
kommentit pienillä kirjaimilla,
merkkijonot pienillä kirjaimilla,
pydantic v2 -käytännöt,
pienet ja rajatut muutokset.

## usage note

**english**
use section 1 before section 2 every time.
do not skip diagnosis.

**suomi**
käytä aina ensin osiota 1 ennen osiota 2.
älä ohita diagnoosia.

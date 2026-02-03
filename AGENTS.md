# agents

this file defines how ai agents must operate in this repository.
it prioritizes learning, safety, and small verifiable changes.

---

## goal

help me learn by diagnosing issues and proposing small, verifiable fixes.

**suomennos**
tavoite: auta minua oppimaan diagnosoimalla ongelmia ja ehdottamalla pieniä, varmennettavia korjauksia.

---

## workflow rules (must follow)

- first: diagnose (root cause + where to change + how to verify).
- then: propose the minimal patch.
- keep diffs small and focused.
- change only the files requested or clearly related to the issue.
- do not refactor unless explicitly requested.

**suomennos**
työnkulun säännöt (pakolliset):
- ensin: diagnoosi (juurisyy + mihin muutos tehdään + miten varmennetaan).
- sitten: minimaalinen korjaus.
- pidä muutokset pieninä ja rajattuina.
- muuta vain pyydettyjä tai selvästi asiaan liittyviä tiedostoja.
- älä refaktoroi ilman erillistä pyyntöä.

---

## project constraints (strict)

- source code language: english only
- comments: lowercase only
- strings: english + lowercase only
- pydantic v2 is used in this repository
- follow best_practices.md

**suomennos**
projektin rajoitteet (tiukat):
- lähdekoodin kieli: vain englanti
- kommentit: vain pienet kirjaimet
- merkkijonot: englanti ja pienet kirjaimet
- pydantic v2 on käytössä tässä repossa
- noudata best_practices.md:tä

---

## verification commands

- backend run (windows powershell): scripts/run_backend.ps1
- tests (windows powershell): scripts/run_tests.ps1

**suomennos**
varmennuskomennot:
- backendin käynnistys (windows powershell): scripts/run_backend.ps1
- testit (windows powershell): scripts/run_tests.ps1

---

## conventions

- prefer feature branches: feature/<name> or chore/<name>
- commit messages: type: short summary (e.g., "chore: normalize frontend strings")
- update documentation when behavior changes:
  - docs/api.md
  - docs/testing.md

**suomennos**
käytännöt:
- suosi feature-branchia: feature/<nimi> tai chore/<nimi>
- commit-viestit: tyyppi: lyhyt yhteenveto (esim. "chore: normalize frontend strings")
- päivitä dokumentaatio, kun käytös muuttuu:
  - docs/api.md
  - docs/testing.md

---

## authority

- if this file conflicts with other guidance, this file takes precedence.

**suomennos**
määräysvalta:
- jos tämä tiedosto on ristiriidassa muiden ohjeiden kanssa, tätä noudatetaan.




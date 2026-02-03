# agents

## goal
help me learn by diagnosing issues and proposing small, verifiable fixes.

**suomennos**
tavoite: auta minua oppimaan diagnosoimalla ongelmia ja ehdottamalla pieniä, varmennettavia korjauksia.

## workflow rules
- first: diagnose (cause + where to change + how to verify).
- then: propose the minimal patch.
- keep diffs small and focused.
- change only the files requested or clearly related to the issue.

**suomennos**
työnkulun säännöt:
- ensin: diagnoosi (syy + mihin muutos tehdään + miten varmennetaan).
- sitten: minimaalinen korjaus.
- pidä muutokset pieninä ja rajattuina.
- muuta vain pyydettyjä tiedostoja tai selvästi niihin liittyviä.

## project constraints
- source code language: english only
- comments: lowercase only
- strings: english + lowercase only
- pydantic v2 is used in this repository

**suomennos**
projektin rajoitteet:
- lähdekoodin kieli: vain englanti
- kommentit: vain pienet kirjaimet
- merkkijonot: englanti ja pienet kirjaimet
- pydantic v2 on käytössä tässä repossa

## verification commands
- backend run (windows powershell): scripts/run_backend.ps1
- tests (windows powershell): scripts/run_tests.ps1

**suomennos**
varmennuskomennot:
- backendin käynnistys (windows powershell): scripts/run_backend.ps1
- testit (windows powershell): scripts/run_tests.ps1

## conventions
- prefer feature branches: feature/<name> or chore/<name>
- commit messages: type: short summary (e.g., "chore: normalize frontend strings")
- update docs when behavior changes (docs/api.md, docs/testing.md)

**suomennos**
käytännöt:
- suosi feature-branchia: feature/<nimi> tai chore/<nimi>
- commit-viestit: tyyppi: lyhyt yhteenveto (esim. "chore: normalize frontend strings")
- päivitä dokumentit kun käytös muuttuu (docs/api.md, docs/testing.md)



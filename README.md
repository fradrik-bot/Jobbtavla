# Daniels jobbtavla

Samlar lediga jobb runt Bonäshamn/Järpen/Åre från Platsbanken, JobTech Links,
LinkedIn och SkiStar, matchar dem mot Daniels profil och visar dem på en karta.
Hämtningen körs automatiskt varje morgon av GitHub Actions.

## Uppsättning (en gång)
1. Skapa konto på github.com och ett nytt **publikt** repo, t.ex. `jobbtavla`.
2. *Add file → Upload files*: dra in alla filer från zip-filen och tryck *Commit changes*.
   Mappen `.github` följer inte alltid med vid uppladdning. Saknas den: *Add file → Create new file*,
   skriv namnet `.github/workflows/update.yml` och klistra in innehållet från filen.
3. *Settings → Actions → General → Workflow permissions*: välj **Read and write permissions** och spara.
4. *Settings → Pages*: Source **Deploy from a branch**, branch **main**, mapp **/ (root)**, spara.
5. *Actions → Uppdatera jobb → Run workflow*. Vänta tills den blir grön (ca 5 minuter).
6. Adressen blir https://DITT-ANVÄNDARNAMN.github.io/jobbtavla/ – skicka den till Daniel.

Sidan innehåller inga kontaktuppgifter. Telefon och e-post i det personliga brevet
fyller Daniel i själv, och de sparas bara i hans webbläsare.

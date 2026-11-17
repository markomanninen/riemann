---
title: "Kuinka tarkasti alkuluvut voi ennustaa? Riemannin hypoteesi ja tekoälyn askel kohti sitä"
subtitle: "Selittävä lähdeteksti. Pohjana World Science Festivalin video ”AI Closes In on the Riemann Hypothesis” (Brian Greene haastattelee Alex Kontorovichia), kohdat 0:00–19:00"
---

# 1. Punainen lanka yhdellä kappaleella

Koko tarina vastaa yhteen kysymykseen: **kuinka tarkasti voimme ennustaa, montako alkulukua on annettuun rajaan asti?** Gauss löysi noin vuonna 1795 hyvän arvion. Riemann näytti vuonna 1859, että arvion *virhe* määräytyy yhden funktion, zeta-funktion, nollakohtien sijainnista. Mitä lähempänä nollakohdat ovat pystysuoraa σ = ½, sitä pienempi virhe. Riemannin hypoteesi väittää, että ne kaikki ovat täsmälleen tällä suoralla, jolloin virhe on pienin mahdollinen. Sitä ei ole todistettu. Syksyllä 2026 tekoäly todisti heikomman väitteen, ”kvasi-Riemannin hypoteesin”: nollakohdat ovat ainakin kaistan 1/8–7/8 sisällä. Tästä seuraa ensimmäistä kertaa virheraja, joka on selvästi pienempi kuin aiemmin osattiin todistaa. Hypoteesi itse on yhä auki.

Esitys etenee neljässä osassa:

1. **Mistä puhutaan:** alkulukujen jakaumasta ja siitä, kuinka hyvin sitä voi ennustaa.
2. **Miksi puhutaan nyt:** tekoäly otti syyskuussa ja lokakuussa 2026 askeleen, jota alan asiantuntija ei odottanut näkevänsä elinaikanaan.
3. **Mitä puhutaan:** ketju Gaussista Riemanniin, nollakohdista virheeseen ja lopulta siihen, mitä tekoäly todisti.
4. **Mihin päädyttiin:** mitä nyt tiedetään, mitä ei, ja miksi tuloksella on merkitystä.

# 2. Mistä puhutaan: alkulukujen arvoitus

Alkuluku on yhtä suurempi kokonaisluku, jota ei voi kirjoittaa kahden pienemmän kokonaisluvun tulona: 2, 3, 5, 7, 11, 13 ja niin edelleen. Alkulukuja on äärettömän monta, ja jokainen kokonaisluku on yksikäsitteisesti alkulukujen tulo. Alkuluvut ovat siis lukujen ”rakennuspalikat”.

Pienistä luvuista alkuluvut löytyvät helposti, mutta luvut kasvaessa se vaikeutuu. **Mikään käytännöllinen kaava ei anna seuraavaa alkulukua.** Yksittäiset alkuluvut näyttävät tulevan sattumanvaraisesti: välillä kaksi on peräkkäin (11 ja 13), välillä tulee pitkä tauko.

Siksi matemaatikot esittävät toisenlaisen kysymyksen: **montako alkulukua on keskimäärin jonkin luvun x lähellä?** Tai yhtä hyvin: jos olet alkuluvun p kohdalla, kuinka kaukana on keskimäärin seuraava alkuluku q? Tähän kysymykseen on hyvä vastaus, ja koko Riemannin hypoteesin tarina kertoo siitä, *kuinka hyvä* tuo vastaus on.

# 3. Miksi puhutaan juuri nyt

Videon alussa Kontorovich sanoo, että jos häneltä olisi kysytty 29. syyskuuta 2026, hän olisi lyönyt vetoa, ettei näe tätä tulosta elinaikanaan. Seuraavana päivänä, 30. syyskuuta, päivätty OpenAI:n mallin tuottama 199-sivuinen todistus väitti, että kaikki zeta-funktion ei-triviaalit nollakohdat ovat kaistassa 1/8 ≤ σ ≤ 7/8, ja todistus oli tarkistettu tietokoneella Lean-ohjelmalla. Noin viikkoa myöhemmin valmistui 49-sivuinen versio, jonka mukaan nollakohdat ovat kaistassa 1/12 ≤ σ ≤ 11/12. Sitä ei ole vielä tarkistettu Leanilla. OpenAI julkisti tulokset 6. lokakuuta 2026.

Haastattelija Brian Greene korostaa: tekoäly *ei* ole ratkaissut Riemannin hypoteesia. Se kavensi aluetta, jossa zeta-funktion nollakohdat voivat olla, ja jo tämä osittainen askel hämmästytti matemaatikot. Kontorovichin mukaan ”tekoäly voi ratkaista suuria matemaattisia ongelmia” -hetki voi tapahtua vain kerran, ja nyt se on tapahtunut.

Jotta ymmärtää, miksi tämä on iso asia, pitää ymmärtää ketju alkuluvuista nollakohtiin. Se ketju on tämän esityksen sisältö.

# 4. Mitä puhutaan: ketju kuudessa askeleessa

## Askel 1 – Gauss: alkulukujen tiheys on 1 / ln x

Kontorovich kertoo, että nuori Gauss laski noin vuonna 1795 ikävystyneenä alkulukutaulukoita kolmeen miljoonaan asti ja samalla logaritmitaulukoita. Hän jakoi luvut tuhannen luvun lohkoihin ja laski alkuluvut kustakin lohkosta. Ensimmäisessä lohkossa (1–1000) alkulukuja on 168, kolmen miljoonan kohdalla enää noin 65–70 tuhatta lukua kohden.

Gauss huomasi, että alkulukujen osuus harvenee tietyllä tahdilla: **lähellä lukua x noin joka (ln x):s luku on alkuluku.** Tässä ln on luonnollinen logaritmi, ja se kasvaa hyvin hitaasti: ln 1000 ≈ 6,9, ln 1 000 000 ≈ 13,8 ja ln 10¹² ≈ 27,6. Sama asia toisin sanottuna: kahden peräkkäisen alkuluvun keskimääräinen väli lähellä x:ää on noin ln x.

Tästä Gauss sai arvion alkulukujen kokonaismäärälle. Merkitään π(x) = alkulukujen määrä x:ään asti. (Kirjain π on tässä pelkkä nimi, eikä sillä ole tekemistä luvun 3,14 kanssa.) Jos tiheys pisteessä t on 1 / ln t, kokonaismäärä saadaan laskemalla tiheydet yhteen eli integroimalla:

> **Gaussin arvio:** π(x) ≈ Li(x) = ∫₂ˣ dt / ln t.

Arvaus tunnetaan Gaussin konjektuurina. Se on hämmästyttävän hyvä, mutta herättää heti seuraavan kysymyksen, joka on koko tarinan ydin: **kuinka suuri virhe π(x) − Li(x) voi olla?**

## Askel 2 – Riemann 1859: zeta-funktio on silta alkulukuihin

Bernhard Riemann oli Gaussin oppilas ja peri tämän professuurin Göttingenissä. Vuonna 1859 hän kirjoitti ainoan lukuteoreettisen artikkelinsa. Siinä hän otti käyttöön funktion, joka tunnettiin jo aiemmin reaalimuuttujan funktiona:

> ζ(s) = 1 + 1/2ˢ + 1/3ˢ + 1/4ˢ + …

Miksi tämä liittyy alkulukuihin? Euler oli osoittanut jo 1700-luvulla, että saman summan voi kirjoittaa **tulona, jossa on yksi tekijä jokaista alkulukua kohti**. Tämä seuraa siitä, että jokainen luku on yksikäsitteisesti alkulukujen tulo. Zeta-funktio on siis alkulukujen ”sormenjälki”: kaikki tieto alkuluvuista on koodattu siihen.

Riemannin uusi idea oli laajentaa zeta **kompleksiluvuille** s = σ + i·t. Kompleksiluvun voi ajatella tason pisteenä: vaakasuunta σ on reaaliosa ja pystysuunta t imaginaariosa. Kontorovich kuvaa tätä videolla 1800-luvun huipentumaksi: täysin diskreetti kysymys alkuluvuista muutettiin jatkuvaksi kysymykseksi, ja vieläpä luvuilla, joissa on ”olemattoman” negatiivisen luvun neliöjuuri.

Kompleksitasossa zetalla on muutama tärkeä piirre:

- **Napa kohdassa s = 1:** siellä zeta kasvaa äärettömäksi, koska summa 1 + 1/2 + 1/3 + … kasvaa rajatta.
- **Triviaalit nollakohdat** kohdissa −2, −4, −6, …: ne tunnetaan täysin, eivätkä ne ole kiinnostavia.
- **Ei-triviaalit nollakohdat:** pisteet, joissa ζ(s) = 0. Ne ovat kaikki **kriittisessä kaistassa** 0 < σ < 1.

## Askel 3 – Miksi nollakohdat ratkaisevat virheen

Tämä on tarinan tärkein ja vähiten ilmeinen lenkki. Riemann löysi **eksplisiittisen kaavan**: alkulukujen laskurin voi kirjoittaa muodossa

> (alkulukujen määrä) = (Gaussin sileä keskiarvo) − (summa aaltoja, yksi jokaista nollakohtaa kohti).

Jokainen nollakohta ρ = σ + i·t tuottaa aallon, joka värähtelee sitä tiheämmin, mitä suurempi t on. **Aallon korkeus kasvaa kuin x^σ.** Nollakohdan *vaakasijainti* σ määrää siis suoraan, kuinka suuren poikkeaman se aiheuttaa alkulukujen määrään:

- Jos jokin nolla olisi suoralla σ = 1, sen aalto olisi yhtä suuri kuin itse keskiarvo, eikä Gaussin arvio pitäisi edes suhteellisesti.
- Jos kaikki nollat ovat suoralla σ = ½, kaikki aallot ovat korkeintaan noin √x:n kokoisia. Tämä on pienin mahdollinen virhe.
- Yleisesti: jos kaikkien nollien σ ≤ θ, virhe on enintään noin x^θ (logaritmisia kertoimia lukuun ottamatta).

Vertauskuva: alkulukujen porrasfunktio on kuin ääni, ja nollakohdat ovat sen sävelet. Kun riittävän monta säveltä lasketaan yhteen, sileästä keskiarvosta muotoutuvat portaat täsmälleen alkulukujen kohdille. Siksi nollakohtien sijainnin tunteminen on sama asia kuin alkulukujen heilunnan tunteminen.

## Askel 4 – Missä nollakohdat ovat: suora ½ ja symmetria

Zetalla on symmetria: arvot kohdissa s ja 1 − s ovat sidoksissa toisiinsa. Geometrisesti tämä on peilaus pystysuoran σ = ½ yli. Lisäksi kuvan ylä- ja alapuoli ovat toistensa peilikuvia. Siksi jos suoran ½ ulkopuolella olisi yksi nollakohta, siellä olisi aina neljä nollakohtaa, jotka ovat toistensa peilikuvia.

Kontorovich kertoo, että Riemann ei maininnut sitä artikkelissaan, mutta hänen muistiinpanoistaan löytyi myöhemmin ensimmäisten nollakohtien laskuja. Ne olivat täsmälleen suoralla ½. Ensimmäinen on korkeudella t ≈ 14,1347, seuraavat korkeuksilla 21,0220, 25,0109 ja 30,4249.

> **Riemannin hypoteesi:** kaikki zeta-funktion ei-triviaalit nollakohdat ovat suoralla σ = ½.

Riemann sanoi, että jos hypoteesi pätee, siitä seuraa paitsi alkulukulause myös paras mahdollinen virhearvio. Tietokoneilla on tarkistettu yli 12 biljoonaa nollakohtaa, ja kaikki ovat suoralla. Äärettömän moneen nollakohtaan tarvitaan kuitenkin todistus. Hypoteesi on yksi Clay-instituutin seitsemästä Millennium-ongelmasta, ja sen ratkaisijalle on luvattu miljoonan dollarin palkinto.

## Askel 5 – Biljoonaesimerkki: mitä ”virhe √x” tarkoittaa käytännössä

Kontorovich havainnollistaa hypoteesin merkitystä esimerkillä. Montako alkulukua on biljoonaan (10¹²) asti? Ne voisi laskea yksitellen, mutta se veisi Gaussilta ikuisuuden. Sen sijaan Gaussin integraalin voi laskea nopeasti:

| | Arvo |
|---|---|
| Todellinen määrä π(10¹²) | 37 607 **912 018** |
| Gaussin arvio Li(10¹²) | 37 607 **950 281** |
| Ero | 38 263 |

Kuusi ensimmäistä numeroa täsmää. Kontorovichin sanoin, jos kaikki nollakohdat ovat suoralla ½, noin **ensimmäinen puolikas numeroista on täsmälleen oikein ja jälkimmäinen puolikas heiluu**, koska suoralla ½ on nollakohtia. ”Puolikas” tulee suoraan neliöjuuresta: √x:ssä on noin puolet x:n numeroista. Videolla Kontorovich arvioi lennosta määrän olevan noin 100 miljardia, mutta oikea luku on noin 37,6 miljardia.

Sama ilmiö toistuu kaikilla kymmenen potensseilla 10²⁴:ään asti: Gaussin arvio osuu suunnilleen puoleen numeroista.

## Askel 6 – Mitä on todistettu: 1896 ja 2026

Riemann ei osannut todistaa hypoteesiaan. Hän ei osannut todistaa edes heikompaa väitettä, ettei suoralla σ = 1 ole nollakohtia, joten hän ei todistanut alkulukulausetta. Hän rakensi menetelmän, jolla sen voisi todistaa.

**1896:** Jacques Hadamard ja Charles de la Vallée Poussin todistivat samana vuonna toisistaan riippumatta, ettei zetalla ole nollakohtia suoralla σ = 1. Riemannin menetelmällä tästä seurasi **alkulukulause**: π(x) / Li(x) → 1. Gaussin arvaus oli nyt todistettu. Virhe on kuitenkin taattu vain hieman pienemmäksi kuin x itse, joten arvio pitää suhteellisesti mutta ei kerro, montako numeroa on oikein. Vaikka tulosta on parannettu yli sadan vuoden ajan, nykyinenkään ehdoton virheraja ei ole muotoa x^θ millään θ < 1.

**2026, kvasi-Riemannin hypoteesi:** jos kaikki nollakohdat ovat kaistassa 1/8 ≤ σ ≤ 7/8, virhe on enintään noin x^(7/8). Tämä on ensimmäinen virheraja, joka säästää kiinteän potenssin x:stä. Matemaatikko Maksym Radziwiłł on sanonut, että valtaosa Riemannin hypoteesin seurauksista seuraa jo kvasi-RH:sta.

# 5. Tekoälyn tulos tarkemmin, varaukset mukaan lukien

- **Kaksi versiota:** 30.9.2026 päivätty 199-sivuinen todistus (kaista 1/8–7/8), joka on tarkistettu Leanilla, ja noin viikkoa myöhemmin valmistunut 49-sivuinen versio (kaista 1/12–11/12), jota ei ole vielä tarkistettu Leanilla. Matemaatikot keskittyvät lähinnä lyhyempään versioon, koska se on helpompi lukea ja käyttää samankaltaisia tekniikoita.
- **Menetelmä:** todistus käyttää niin sanottuja metaplektisiä muotoja, ja keskeinen ainesosa on Alexander Dunnin ja Maksym Radziwiłłin vuonna 2021 todistama kaava. Henryk Iwaniec oli vuonna 2002 lähellä samaa funktioperhettä.
- **Reaktiot:** Jared Duker Lichtman on kutsunut tulosta ylivoimaisesti merkittävimmäksi tekoälyn matemaattiseksi saavutukseksi tähän mennessä. Radziwiłł pitää papereita huonosti kirjoitettuina. Peter Sarnak ei kutsu tulosta teoreemaksi ennen kuin ihmiset ovat tarkistaneet kaikki yksityiskohdat. Muiden matemaatikkojen 7–13-sivuiset tiivistykset kiertävät yksityisesti.
- **Mitä se ei ole:** se ei ole Riemannin hypoteesin todistus. Will Sawin epäilee, että uudet menetelmät eivät vie rajaa 7/8 puolikkaaseen asti.

# 6. Tausta videolta: miten tekoäly oppi todistamaan

Kontorovich kuvaa kehitystä vaiheittain. Kolme vuotta sitten tekoäly alkoi ratkoa kansainvälisen matematiikkaolympialaisen (IMO) tehtäviä. Kesällä 2024 DeepMindin Lean-pohjainen AlphaProof jäi yhden pisteen päähän kullasta. Kesällä 2025 useampi järjestelmä ylsi kultamitalitasolle, osa formaalisti ja osa pelkällä luonnollisella kielellä.

Hän erottaa kaksi lähestymistapaa:

- **Kielimallit** ennustavat seuraavan sanan todennäköisyyksien perusteella. Matematiikka ei kuitenkaan ole jazzia, jossa ”väärä nuotti” voi olla hyvä: jokaisen päättelyaskeleen on oltava oikein. Nykyiset mallit pilkkovat todistuksen pieniin askeliin, ja toiset mallit arvioivat jokaisen askeleen. Ihmisen on silti tarkistettava lopputulos.
- **Formaalit järjestelmät, kuten Lean,** pilkkovat todistuksen pienimpiin päättelyaskeliin, joista jokaisen ohjelma tarkistaa koneellisesti. Jos Lean hyväksyy todistuksen, ihmistä ei tarvita tarkistamaan sitä.

Kontorovich ja Terence Tao vetivät ”Prime Number Theorem+” -projektia, jossa alkulukulause ja sen vaatima kompleksianalyysi kirjoitettiin Leaniin. Tämä on syy, miksi Kontorovich tuntee sekä alkulukulauseen että formaalin tarkistuksen läheltä.

# 7. Yhteenveto: mihin päädyttiin

1. **Kysymys:** kuinka tarkasti alkulukujen määrän voi ennustaa? Gaussin arvio Li(x) on erinomainen. Koko kysymys on sen virheessä.
2. **Mekanismi:** virhe koostuu aalloista, yksi jokaista zeta-funktion nollakohtaa kohti, ja nollakohdan vaakasijainti σ määrää aallon koon x^σ.
3. **Rajaukset ja seuraukset:**

| Missä nollakohdat ovat | Mitä se kertoo alkuluvuista | Tila |
|---|---|---|
| Kaistassa 0 ≤ σ ≤ 1 | Ei vielä mitään tarkkaa | Riemann 1859 |
| Ei yhtään suoralla σ = 1 | Gaussin arvio pitää suhteellisesti (alkulukulause) | Todistettu 1896 |
| Kaistassa 1/8 ≤ σ ≤ 7/8 | Virhe enintään noin x^(7/8) | Tekoäly 2026, Lean-tarkistettu. Ihmisten tarkistus kesken |
| Kaistassa 1/12 ≤ σ ≤ 11/12 | Virhe enintään noin x^(11/12) | Tekoäly 2026, matemaatikkojen tarkastelussa |
| Kaikki suoralla σ = ½ | Virhe noin √x, eli puolet numeroista on oikein | **Riemannin hypoteesi – avoin** |

4. **Merkitys:** tekoäly kavensi ensimmäistä kertaa nollakohtien aluetta kiinteällä leveydellä, mikä antaa alkuluvuille aiempaa paljon tiukemman virherajan. Kontorovich ei odottanut näkevänsä tätä elinaikanaan.
5. **Mikä on yhä auki:** itse Riemannin hypoteesi, viimeinen askel kaistasta yhdeksi suoraksi. Sekä matemaatikkojen että Leanin tarkistukset ovat osittain kesken. Lisäksi matematiikkayhteisö pohtii, mitä tämä merkitsee alalle ja nuorten matemaatikkojen koulutukselle.

# 8. Sanasto

- **Alkuluku:** yhtä suurempi kokonaisluku, joka on jaollinen vain ykkösellä ja itsellään.
- **ln x:** luonnollinen logaritmi. Se kasvaa hyvin hitaasti (ln 10¹² ≈ 27,6).
- **π(x):** alkulukujen määrä x:ään asti.
- **Li(x):** Gaussin arvio, integraali ∫ dt / ln t.
- **Alkulukulause:** π(x) / Li(x) → 1. Todistettiin 1896.
- **Kompleksiluku s = σ + i·t:** tason piste, jossa σ on vaaka- ja t pystykoordinaatti.
- **ζ(s), zeta-funktio:** 1 + 1/2ˢ + 1/3ˢ + …, laajennettuna kaikille kompleksiluvuille.
- **Nollakohta:** piste, jossa ζ(s) = 0.
- **Kriittinen kaista ja suora:** alue 0 < σ < 1 ja sen keskilinja σ = ½.
- **Kvasi-Riemannin hypoteesi:** heikompi versio, jonka mukaan nollakohdat ovat jossain kiinteässä kaistassa a ≤ σ ≤ 1 − a, missä a > 0.
- **Lean:** ohjelma, joka tarkistaa matemaattisen todistuksen koneellisesti askel askeleelta.

# 9. Kuvat ja mitä ne näyttävät

![**Kuva 1. Gaussin havainto.** Vasen: alkulukujen määrä jokaisessa tuhannen luvun lohkossa kolmeen miljoonaan asti (harmaat pisteet) ja käyrä 1000 / ln x. Yksittäiset lohkot heittelevät, mutta keskiarvo seuraa käyrää. Oikea: peräkkäisten alkulukujen keskimääräinen väli kasvaa kuin ln x.](01_gauss_havainto.png)

![**Kuva 2. Gaussin arvio ja alkulukulause.** Vasen: alkulukujen todellinen määrä π(x) porrasfunktiona, Gaussin arvio Li(x) ja karkeampi x / ln x. Oikea: suhde π(x) / Li(x) lähestyy ykköstä.](02_alkulukulause.png)

![**Kuva 3. Zeta-funktion kompleksitaso.** Napa kohdassa s = 1, triviaalit nollakohdat negatiivisilla parillisilla luvuilla, kriittinen kaista 0 < σ < 1 ja ensimmäiset ei-triviaalit nollakohdat suoralla σ = ½.](03_kriittinen_kaista.png)

![**Kuva 4. Symmetria.** Kuviteltu nollakohta suoran ½ ulkopuolella toisi mukanaan kolme peilikuvaansa. Riemannin hypoteesin mukaan tällaisia ei ole.](04_symmetria.png)

![**Kuva 5. Miten nollakohdat löydetään.** Hardyn Z-funktio on suoralla ½ reaalinen, ja jokainen sen nollan ylitys on nollakohta.](05_hardyn_Z.png)

![**Kuva 6. Biljoonaesimerkki.** π(10¹²) ja Li(10¹²) täsmäävät kuudessa ensimmäisessä numerossa, ja loput heiluvat.](06_biljoona_numerot.png)

![**Kuva 7. Virheen raja.** Todellinen virhe π(x) − Li(x) ja raja √x · ln x / 8π, jonka sisällä virhe pysyy, jos Riemannin hypoteesi pätee.](07_virhetermi.png)

![**Kuva 8. Kaistan kaventuminen.** 1859: koko kaista. 1896: reunat suljettu pois. 2026: kaistat 1/8–7/8 ja 1/12–11/12. Riemannin hypoteesi: yksi suora.](08_kaistan_kaventuminen.png)

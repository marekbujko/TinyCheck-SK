# TinyCheck

![Architecture](/assets/network-home.png)

### Popis

TinyCheck umožňuje jednoducho zachytiť sieťovú komunikáciu zo smartfónu alebo akéhokoľvek zariadenia, ktoré možete pripojiť k prístupovému bodu Wi-Fi a rýchlo ju analyzovať. Pomocou heuristiky alebo špecifických indikátorov kompromitácie (IoC) tak môžete skontrolovať, či zo smartfónu odchádza podozrivá alebo škodlivá komunikácia.

Myšlienka TinyCheck vznikla na stretnutí o stalkerware s [francúzskym útulkom pre ženy](https://www.centre-hubertine-auclert.fr). Počas tohto stretnutia hovorili o tom, ako ľahko zistiť [stalkerware](https://stopstalkerware.org/) bez inštalácie veľmi technických aplikácií alebo forenznej analýzy smartfónu obete. Pôvodným konceptom bolo vyvinúť malé kioskové zariadenie založené na Raspberry Pi, ktoré môžu používať ľudia bez technických znalostí na testovanie svojich smartfónov proti škodlivej komunikácii stalkerského softvéru alebo akéhokoľvek spyware.

Samozrejme, TinyCheck sa dá použiť aj na odhalenie akejkoľvek škodlivej komunikácie od počítačovej kriminality až po štátom sponzorované útoky. Umožňuje koncovému používateľovi použiť vlastné rozšírené indikátory kompromitácie prostredníctvom backendu s cieľom odhaliť "duchov" na sieti.

<p align="center"><strong>Ak potrebujete viac informácií o tom, ako ho nainštalovať, používať a o jeho funkciách, neváhajte sa pozrieť na <a href="https://github.com/KasperskyLab/TinyCheck/wiki">TinyCheck Wiki (anglicky)</a>.</strong></p>

<p align="center">Ak máte akékoľvek otázky týkajúce sa projektu, chcete prispieť alebo len poslať svoj názor, <br />neváhajte nás kontaktovať na adrese tinycheck[@]kaspersky[.]com.</p>

### Možnosti použitia

TinyCheck môžu jednotlivci a subjekty používať viacerými spôsobmi:

- Cez sieť - TinyCheck je nainštalovaný v sieti a je prístupný z pracovnej stanice prostredníctvom prehliadača.
- V režime kiosku - TinyCheck možete použiť ako kiosk, aby si návštevníci mohli otestovať vlastné zariadenia.
- Úplne samostatne - pomocou powerbanky, dvoch rozhraní Wi-Fi alebo 4G dongle a malej dotykovej obrazovky [ako na videu](https://twitter.com/felixaime/status/1331535790392946689).

### Inštalácia

Tu nájdete niekoľko krokov na [Wiki inštalačnej stránke - anglicky](https://github.com/KasperskyLab/TinyCheck/wiki/TinyCheck-installation).

### Zoznámte sa s frontendom

Frontend - ktorý je prístupný z `http://tinycheck.local` je druh tunela, ktorý pomáha používateľovi v celom procese zachytávania a reportingu siete. Umožňuje používateľovi nastaviť pripojenie Wi-Fi k existujúcej sieti Wi-Fi, vytvoriť efemérnu sieť Wi-Fi, zachytiť komunikáciu a zobraziť používateľovi správu... za menej ako jednu minútu, 5 kliknutí a bez akýchkoľvek technických znalostí.

![Frontend](/assets/frontend.png)

### Zoznámte sa s backendom

Po inštalácii sa môžete pripojiť k backendu TinyCheck vyhľadaním adresy URL `https://tinycheck.local` a prijatím certifikátu SSL s vlastným podpisom.

![Backend](/assets/backend.png)

Backend umožňuje upravovať konfiguráciu TinyCheck, pridávať rozšírené IOC a prvky na bielych zoznamoch s cieľom zabrániť falošným poplachom. Niekoľko IOC je už k dispozícii, napríklad niekoľko pravidiel suricata, FreeDNS, Name servers, CIDR, o ktorých je známe, že hostia škodlivé servery a podobne.

### Špeciálne poďakovanie

**Felix Aime**, za jeho nápad a nadšenie pri vývoji a testovaní tohto projektu. Felix je hlavným prispievateľom a my si jeho prácu na projekte TinyCheck veľmi vážime.

**Ľudia, ktorí poskytli niektoré IOC**
- [Cian Heasley](https://twitter.com/nscrutables) pre jeho Android stalkerware IOC repozitár, k dispozícii tu: https://github.com/diskurse/android-stalkerware
- [Echap](https://github.com/AssoEchap) pre ich úžasný stalkerware IOC repozitár, k dispozícii tu: https://github.com/AssoEchap/stalkerware-indicators
- [Emilien](https://twitter.com/__Emilien__) pre jeho pravidlá Stratum, ktoré sú k dispozícii tu: https://github.com/kwouffe/cryptonote-hunt
- [Costin Raiu](https://twitter.com/craiu) pre jeho domény geo-tracker, ktoré sú k dispozícii tu: https://github.com/craiu/mobiletrackers/blob/master/list.txt

**Revízia kódu**
- Dan Demeter [@_xdanx](https://twitter.com/_xdanx)
- Maxime Granier
- Florian Pires [@Florian_Pires](https://twitter.com/Florian_Pires)
- Ivan Kwiatkowski [@JusticeRage](https://twitter.com/JusticeRage)

**Iné**
- GReAT (skvelí) kolegovia.
- Tatyana, Kristina, Christina a Arnaud z Kaspersky (podpora IOC)
- Zeek a Suricata úžasní správcovia.
- Ľudia z virtual-keyboard.js.org a loading.io.
- Yan Zhu za jeho úžasnú Spectre CSS knižnicu (https://picturepan2.github.io/spectre/)
- Marek Bujko (slovenská lokalizácia).

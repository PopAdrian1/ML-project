# ML-project

🍎 Documentația Proiectului: Predicția Producției de Mere prin Machine Learning

1. Obiectivul Proiectului

Proiectul dezvoltă un model de Machine Learning capabil să estimeze producția medie de mere (kg/pom) la nivelul fiecărui județ din 
România de la an la an.

Modelul combina trei categorii de factori pentru a prezice/estima productia reala a fiecarui copac:
- Factori genetici : tipul de portaltoi, care ne spune atat inaltimea copacului, productia maxima a acestuia, cat si densitatea unei livezi formata din fiecare tip
- Factori climatici: clima (precipitatii, temperatura, etc.) si umiditate
- Factori geografici si de sol: fiecare dataset este structurat sa acopere toate judetele din Romania; pentru datele de sol avem nevoie de ph, nutrienti si tipul/textura solulului

Valoare practică: estimarea timpurie a recoltei permite alocarea eficientă a resurselor (irigare, fertilizare) și identificarea județelor cu potențial mare.

3. Dataset-uri

Toate sursele de date sunt integrate intr-un singur dataset mare organizat pe judete si ani.

2.1 Dataset copaci fructiferi (link: http://statistici.insse.ro:8077/tempo-online/#/pages/tables/insse-table)

AGR114A - Nr. total pomi in fiecare an si judet
AGR115A - Producție totală (tone)
AGR116A - Producție medie (kg/pom)

Parametrii:
- An
- Judet
- nr. copaci de o anumita specie pe judet
- productie totala pe judet
- productia in kg/pom

2.2 Date climatice

Surse: https://power.larc.nasa.gov/data-access-viewer/

Avem nevoie de datele climatice anuale la nivel de judet.

Parametrii:
- Temperatură minimă (Aprilie)°C : Risc de îngheț la înflorire — principalul factor de compromitere totală a recoltei
- Temperatură medie (Iulie–August)°C : Acumulare de zahăr, colorare și calibrul fructului
- Precipitații (Iunie–August)mm : Dimensiunea fructului; excesul favorizează boli
- Chill Hours (Oct–Feb, sub 7°C) ore : Supravietuirea copacului pe timp de iarna
- Growing Degree Days (Mart–Sept)GDD (bază 10°C) : Indicatorul termic global al sezonului de vegetație

2.3 Characteristici sol 

Surse: ESDAC (LUCAS Soil) sau SoilGrids (ISRIC).

Parametrii:
- pH sol 5.5–7.5. Merele preferă 6.0–7.0; 
- Textură dominantă : Lut, Luto-argilos, Nisipos-lutos (Retinerea apei si aerisirea radacinii)
- Conținut materie organică (Fertilitatea)

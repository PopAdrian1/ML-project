# ML-project

🍎 Predicția Producției de Mere prin Machine Learning

1. Obiectivul Proiectului

Proiectul dezvoltă un model de Machine Learning capabil să estimeze producția de mere (kg/pom) la nivelul fiecărui județ din România de la an la an.


2. Dataset-uri

Toate sursele de date sunt integrate intr-un singur dataset mare organizat pe judete si ani.

Fiecare Dataset se desfasoara pe o perioada de 24 de ani in intervalul 2000-2004. 

Pentru datasetul de clima si sol extras datele prin intermediul unor API si ulterior au fost grupate in functie de judet si ani.

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

Adaugam si tipul de rootstock (pitic, semipitic, viguros, etc.) care este calculat in functie de numarul de copaci de pe judet si productia per copac. Totusi aceasta coloana va fi folosita drept categorie pentru a impiedica modelul sa triseze (ex: rootstock pitic - rezulta automat productie mica). 

2.2 Date climatice

Sursa = "https://power.larc.nasa.gov/api/temporal/daily/point"

Parametrii:
    - temperatura medie anuala si pe sezoane
    - zilele de inghet pe sezoane
    - temperatura medie iarna
    - precipitateiile pe sezoane si anual 
    - umiditatea solului pe sezoane 
    - numarul maxim de zile consecutive de seceta pe an 


Datele de clima sunt extrase lunar si apoi agregate pe ani si sezoane. 

Agregarea pe sezoane ajuta la anaaliza climei in etapele de dezvoltare a copacului. 

Ex: zilele de inghet primavara pot afecat procesul de inflorire a marului, ceea ce ulterior afecteaza productia acestuia. 

2.3 Characteristici sol 

Sursa: "https://rest.isric.org/soilgrids/v2.0/properties/query"

Parametrii:
        - ph-ul solului
        - tipul solului (clay, sand, silt)
        - nitrogen (cantitatea de nutrienti necesari pentru plante)
        - SOC (cantitatea de carbon - faciliteaza absorbtia de apa)
        - CEC (capacitatea de schimb cationic - cat de bine retine solul nutrientii)


Datele de sol extrase pe judete sunt folosite ca factori statici deoarece datele de sol nu se schimba semnificativ de la an la an. 

Umiditatea solului este preluata in datasetul de clima. 


3. Valoare practică

 Estimarea timpurie a recoltei permite alocarea eficientă a resurselor (irigare, fertilizare) și identificarea județelor cu potențial mare.


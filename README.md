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

4. Metodologia de Antrenare
 - Split Temporal: S-a utilizat o metodă de împărțire a datelor bazată pe timp (primii 70% ani pentru antrenament, ultimii 30% pentru test) pentru a simula o predictie reală pe anii viitori.-  - Cross-Validation: S-a aplicat TimeSeriesSplit (5 fold-uri) pentru a asigura stabilitatea modelului.
 - Evaluare: Performanța a fost măsurată prin $R^2$ (coeficient de determinare), MAE (eroarea absolută medie), Bias și Varianță.
 
 
 5. Analiza Modelelor și Rezultate
 - S-au comparat mai mulți algoritmi de regresie, cu următoarele concluzii:
 - Modele Liniare (Ridge/Lasso): Performanță mai scazuta scăzută, indicând o relație non-liniară între climă și producție cu un bias destul de ridicat .
 - Random Forest: Rezultate bune pe antrenament, dar tendință ridicată de overfitting.
 - Extra Trees (Câștigător): Cel mai bun echilibru între acuratețe și generalizare . 

Daca ramanem pe ideea de predictie a productie per copac intampinam un acuracy foarte mic <30 %.

O posibila problema ar fi faptul ca productia/copac este influentata de alti factori externi care nu sunt prezenti in dataset (bloi, furtuni, etc). 

Totodata datele din dataset pot fi eronate avand in vedere ca nu a fost un dataset concret si complet ci am combinat eu date preluate din dataseturi oficiale cu date de la API-uri externe. 

Rezultate: 
Linear Regression      | 0.2202   |   0.1571   |  0.0631    |   0.78   |   6.41
Ridge                  | 0.2102   |   0.1187   |  0.0915    |   0.79   |   6.48
Lasso                  | 0.0177   |   -0.0867   |  0.1045    |   0.98   |   6.77
Decision Tree          | 0.2582   |   0.2774   |  -0.0192    |   0.74   |   6.06
Random Forest          | 0.6665   |   0.2281   |  0.4385    |   0.33   |   6.03
Extra Trees            | 0.7156   |   0.3189   |  0.3968    |   0.28   |   5.80
AdaBoost               | 0.3392   |   0.2361   |  0.1032    |   0.66   |   6.18
XGBoost                | 0.7507   |   0.2357   |  0.5149    |   0.25   |   5.93

Am modificat targetul pentru a prezice Productia totala in tone pe fiecare judet. Astfel am observat o crestere a acuratetii.

Rezultate:

Linear Regression      | 0.7001   |   0.6445   |  0.0557    |   0.30   |   5355.78
Ridge                  | 0.6934   |   0.6312   |  0.0622    |   0.31   |   5181.70
Lasso                  | 0.6978   |   0.6373   |  0.0605    |   0.30   |   5305.01
Decision Tree          | 0.7493   |   0.6342   |  0.1151    |   0.25   |   4672.39
Random Forest          | 0.9095   |   0.7287   |  0.1808    |   0.09   |   3981.67
Extra Trees            | 0.9167   |   0.8108   |  0.1059    |   0.08   |   3411.19
AdaBoost               | 0.7877   |   0.6763   |  0.1113    |   0.21   |   4546.73
XGBoost                | 0.9302   |   0.6830   |  0.2473    |   0.07   |   4266.83
 
Am pastrat exemplele si cu productia per copac.

Proiectul nu este complet deoarece Modelele negesita tunning pentru a evita sau a scadea sansa de overfiting. 

Folderul "Proiect Nou" contine un proiect de rezerva care se alineaza pe aceeasi idee doar ca am pornit de la un target diferit.

Am luat datasetul de pe Kaglle. Am adaugat datele de clima. Am incercaat sa prezic randamentul productiei de mere pe diferite Zone/Tari. 

Folosind acest dataset si respectiv target a generat rezultate semnificativ mai bune ceea ce m-a facut sa cred ca datasetul precedent a fost eronat.

Sursa date copaci: https://www.kaggle.com/code/loicdfsdf/crop-statistics-fao-all-countries/input

Sursa date Clima: "https://power.larc.nasa.gov/api/temporal/daily/point"


Rezultate:

Linear Regression      | 0.2600   |   0.2235   |  0.0365    |   0.74   |   85316.30
Ridge                  | 0.2551   |   0.2228   |  0.0322    |   0.74   |   85623.36
Lasso                  | 0.2600   |   0.2235   |  0.0365    |   0.74   |   85316.63
Decision Tree          | 0.1874   |   0.1618   |  0.0256    |   0.81   |   87652.99
Random Forest          | 0.9186   |   0.7348   |  0.1838    |   0.08   |   47635.38
Extra Trees            | 0.9560   |   0.8534   |  0.1026    |   0.04   |   34213.33
AdaBoost               | 0.3373   |   0.3133   |  0.0240    |   0.66   |   88215.45
XGBoost                | 0.8798   |   0.6947   |  0.1851    |   0.12   |   51964.97

Ca si la proiectul precedent "Extra Trees" pare cel mai bun model, cu cea mai buna acuratete. 
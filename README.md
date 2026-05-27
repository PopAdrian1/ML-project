# ML-project

# 🍎 Predicția Randamentului Producției de Mere prin Machine Learning

Proiectul dezvoltă un model de Machine Learning capabil să estimeze randamentul producției de mere (Yield, exprimat în hg/ha) la nivelul fiecărei țări, pe baza datelor istorice de producție și a datelor climatice.

Modelul este antrenat pe un dataset integrat care acoperă zeci de țări din toate continentele, pe o perioadă de 15 ani (2005–2019).


1. Dataset-uri

Toate sursele de date sunt integrate intr-un singur dataset mare organizat pe judete si ani.

1.1 Date de Producție — FAO / Kaggle

Sursa: https://www.kaggle.com/code/loicdfsdf/crop-statistics-fao-all-countries/input

Datele de producție au o acoperire globală pentru perioada 1961–2023. În cadrul proiectului, datele au fost filtrate doar pentru specia **Mere (Malus domestica)** și au fost extrase trei variabile principale:

- `Area harvested` — suprafața recoltată (ha)
- `Production` — producția totală (tone)
- `Yield` — randamentul producției (hg/ha) — **variabila țintă**

S-a aplicat o transformare pentru a trece de la formatul pe elemente la formatul desfășurat pe țară și an. După filtrare și curățare, datele sunt salvate în `Dataset Mere Final.csv`.

1.2 Date Climatice — NASA POWER API

Sursa: `https://power.larc.nasa.gov/api/temporal/daily/point`

Datele climatice sunt extrase zilnic per coordonate geografice și agregate anual și pe sezoane. Acoperă toate țările din dataset pentru perioada 2005–2019.

Variabile extrase:

| Variabilă | Sezon | Relevanță Agronomică |

| Temp_Medie_An | Anual | Condițiile termice generale |
| Precip_Tot_An | Anual | Disponibilul total de apă |
| Zile_Inghet_An | Anual | Riscul global de îngheț |
| Temp_Max_primavara | Primăvară | Stres termic la înflorire |
| Precip_primavara | Primăvară | Apă disponibilă la înflorire |
| Inghet_primavara | Primăvară | Distrugerea florilor |
| Umid_Sol_primavara | Primăvară | Umiditate sol la înflorire |
| Temp_Max_vara | Vară | Stres termic la creșterea fructelor |
| Precip_vara | Vară | Irigare naturală a fructelor |
| Inghet_vara | Vară | Deteriorare fructe (rar) |
| Umid_Sol_vara | Vară | Disponibil hidric la maturare |

Agregarea pe sezoane ajută la analiza climei în etapele de dezvoltare a mărului. De exemplu, zilele de îngheț primăvara pot afecta procesul de înflorire, ceea ce ulterior afectează producția.
 

2. Preprocesarea Datelor

- Filtrare exclusivă pe specia "Meri"
- Eliminarea anilor anteriori lui 2005 (date climatice incomplete)
- Eliminarea coloanelor redundante: `Area Code`, `Item Code`, `Element Code`, `Year Code`, `Flag`
- Tratarea valorilor lipsă prin interpolare acolo unde este posibil; rândurile care nu pot fi interpolate sunt eliminate
- Verificare finală: zero valori null în datasetul de antrenament
- Coloanele cu procent ridicat de zerouri (ex: `Inghet_vara`) sunt păstrate — reflectă o realitate agronomică, nu o eroare de date


3. Metoda de Antrenare

- Split Temporal: primii 70% ani pentru antrenament, ultimii 30% pentru test — respectă ordinea temporală și previne data leakage
- Cross-Validation: TimeSeriesSplit cu 5 fold-uri — fiecare fold de validare este cronologic după cel de antrenament
- Optimizare Hiperparametri: RandomizedSearchCV cu `n_iter=100` — testează 100 de combinații aleatorii, mai eficient decât GridSearch exhaustiv
- Variabila țintă: `Yield` (hg/ha)
- Featuri: 11 variabile climatice + encoding binar al țării
- Excluse din antrenament: `Area harvested`, `Production`, `Year`

Am incercat sa aplic si logartim pe target însă nu am observat o creștere în acuratețe sau avantaje majore. Am creat o noua coloana in memorie ca sa am sa rulez si varianta cu logaritmn oricand fara sa afectez targetul original. 

4. Modele Evaluate și Rezultate

Au fost evaluați 8 algoritmi și am observat că modelel de regresie liniare nu functionează bine si asta e normal deoarece am observat din diagramele de corelatie si distributie faptul că nu exista relatii liniare bine dezvoltate între randament si factorii climatici. 

| Model | R² Train | R² Test | Varianță | Bias | MAE Test (hg/ha) |

| Linear Regression | 0.2600 | 0.2235 | 0.0365 | 0.74 | 85,316 |
| Ridge | 0.2551 | 0.2228 | 0.0322 | 0.74 | 85,624 |
| Lasso | 0.2600 | 0.2235 | 0.0365 | 0.74 | 85,317 |
| Decision Tree | 0.1874 | 0.1618 | 0.0256 | 0.81 | 87,653 |
| AdaBoost | 0.2558 | 0.2410 | 0.0148 | 0.74 | 94,664 |
| Random Forest | 0.8367 | 0.6752 | 0.1615 | 0.16 | 53,964 |
| XGBoost | 0.8798 | 0.6947 | 0.1851 | 0.12 | 51,965 |
| **Extra Trees** | **0.8905** | **0.7928** | **0.0977** | **0.11** | **43,178** |

Model Câștigător — Extra Trees

Extra Trees obține cel mai bun echilibru între acuratețe și generalizare: **R² Test = 0.7928**, MAE = 43,178 hg/ha și cel mai mic bias dintre modelele de tip ansamblu.

Față de Random Forest, Extra Trees introduce o randomizare suplimentară — pragurile de split sunt alese complet aleatoriu, ceea ce reduce overfitting-ul și îmbunătățește generalizarea pe date.



5. Importanța Variabilelor (Feature Importance)

| Rang | Variabilă | Importanță |

| 1 | Area (țară) | 0.43 |
| 2 | Temp_Medie_An | 0.09 |
| 3 | Zile_Inghet_An | 0.07 |
| 4 | Temp_Max_vara | 0.07 |
| 5 | Umid_Sol_primavara | 0.06 |
| 6 | Inghet_primavara | 0.05 |
| 7 | Umid_Sol_vara | 0.05 |
| 8 | Precip_vara | 0.05 |
| 9 | Precip_Tot_An | 0.04 |
| 10 | Inghet_vara | 0.04 |
| 11 | Temp_Max_primavara | 0.04 |
| 12 | Precip_primavara | 0.03 |

Deși ideea de bază era să prezic randamentul în funcție de datele de producție anterioare și factorii climatici am observat faptul că Țara influențează foarte mult rezultatul în timp ce factori climatici nu au o importanță ridicată. În teorie da, în fieacre țară, randamentul producție ține și de alti factori: economie, sol, tehnologie și astfel am putea aproxima în funcție de țară și să applicăm și factori climatici pentru a avea o acuratețe mult mai mare.


6. Predicție Țări Europene

Am făcut un test practic pentru a prezice randamentul tărilor din Europa. Având în vedere că nu am date doar până în 2019 și am folosit ca date climatice de intrare media de pe anii precedenți, nu știu cât de corect ar fi să zic că prezic randamentul pe anul 2026.

Ca rezultate am observat că locul 1 este ocupat de Elveția cu un randament foarte mare (500465 hg/ha, aprox 50.05 tone/ha). România se situează pe locul 25 și Polonia pe locul 20.

Modelul tinde să subestimeze ușor randamentele foarte mari (diferență de 4–6 tone/ha pentru țările din vestul Europei). Pentru țări cu randamente medii precum România și Polonia, predicțiile sunt mai precise (sub 2 tone/ha diferență față de valorile reale).


7. Posibile Îmbunătățiri

- Adăugarea unor variabile agronomice (soiuri, tip de sol, suprafață irigată, fertilizanți, economie, tehnologie) pentru a reduce dependența de variabila țară
- Mai multe date istorice — datasetul actual (~1700 înregistrări) este relativ mic pentru modele de tip ansamblu
- Testarea **LightGBM** și **CatBoost** — variante optimizate de gradient boosting care gestionează bine variabilele categoriale


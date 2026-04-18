

PARAMETRI_COPACI = {
    "Numar_Pomi" : "Numarul de meri dintr-un judet",
    "Kg_pe_Pom"  : "Productia de fructe per copac",
    "Tone_Totale"  : "Productia totala de fructe"
}


PARAMETRI_SOL = {
    "phh2o": "Aciditatea solului (optim 6-7 pentru meri)",
    "clay": "Procentul de argila (reține apa)",
    "sand": "Procentul de nisip (drenaj rapid)",
    "silt": "Procentul de lut (fertilitate)",
    "soc": "Carbon organic (sănătatea solului)",
    "nitrogen": "Azot total (creștere vegetativă)",
    "cec": "Capacitatea de stocare a nutrienților"
}


PARAMETRI_CLIMA = {

    "Primavara": {
        "temp_medie": "Temperatura medie (influențează viteza de înmugurire)",
        "temp_min_abs": "Cea mai scăzută temperatură (risc de îngheț la floare)",
        "precipitatii_total": "Cantitatea de apă (importantă pentru pornirea în vegetație)",
        "zile_inghet": "Număr de zile cu temp < 0 grade după 1 Martie",
        "umiditate_sol": "Umiditatea la nivelul rădăcinilor (disponibilitatea apei)"
    },

    "Vara": {
        "temp_medie_vara": "Temperatura medie vara",
        "precipitatii_vara": "Precipitații totale vara",
        "umid_sol_rad_vara": "Umiditate sol rădăcină vara",
        "zile_inghet_vara": "Număr zile îngheț vara"
    },

    "Anual": {
        "temp_medie_an": "Temperatura medie anuală",
        "precipitatii_an": "Precipitații totale anuale",
        "cdd10_an": "Suma termică totală (CDD > 10°C)",
    },

    "Toamna": {
    "precipitatii_toamna": "Precipitații toamna (an precedent)",
    "temp_medie_toamna": "Temperatura medie toamna (an precedent)",
    "umid_sol_rad_toamna": "Umiditate sol rădăcină toamna (an precedent)",
    "zile_inghet_toamna": "Număr zile îngheț toamna (an precedent)",
    },

    "Iarna":{
    "temp_min_iarna": "Temperatura minimă iarna",
    "zile_inghet_iarna": "Număr zile îngheț iarna"
    }
}

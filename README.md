# Bysykkelprognose for Bergen

Maskinlæringsprosjekt i DAT158 ved HVL, hausten 2026.

Prosjektet spår kor mange bysykkelturar det blir per time i heile Bergen, ut frå klokkeslett, dato og vêr.

- **App:** https://2026-dat158-bysykkel.streamlit.app
- **Rapport:** [rapport.pdf](rapport.pdf)

Appen kan bruke litt tid på å starte om ingen har brukt han på ei stund.

## Filer

| Fil | Innhald |
|------------------------------------|------------------------------------|
| `01_datarydding.ipynb` | Les, ryddar og slår saman tur- og vêrdata. Lagar `data/timetabell.csv`. |
| `02_modell.ipynb` | Features, tidsdeling, modellar og test. Lagrar `modell.joblib`. |
| `features.py` | Lagar features. Blir brukt både i trening og i appen. |
| `app.py` | Streamlit-appen. |
| `modell.joblib` | Den ferdig trena modellen. |
| `data/` | Rydda data. |
| `figurar/`, `resultat/` | Figurar og resultattabellar. |

## Køyre sjølv

1.  Installer pakkane:

pip install -r requirements.txt

2.  Last ned rådata (ikkje med i repoet på grunn av storleiken):
    - **Turdata:** alle månadsfilene (CSV) frå https://bergenbysykkel.no/apne-data til `data/rådata/bysykkel/`
    - **Vêrdata:** frå https://seklima.met.no, stasjon Bergen - Florida (SN50540), timeverdiar for lufttemperatur, nedbør (1 t), middelvind og høgaste vindkast frå juni 2018. Lagre som CSV i `data/rådata/ver/`.
3.  Køyr `01_datarydding.ipynb` og så `02_modell.ipynb`.
4.  Start appen:

streamlit run app.py

Steg 2 og 3 kan du hoppe over om du berre vil køyre appen.

## Data og lisensar

- Bergen Bysykkel, opne data. NLOD 2.0.
- MET Norge / seklima. CC BY 4.0.
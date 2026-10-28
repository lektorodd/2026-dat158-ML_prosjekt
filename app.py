import datetime as dt

import joblib
import numpy as np
import pandas as pd
import streamlit as st

from features import lag_features

st.set_page_config(page_title="Bysykkelprognose for Bergen")


# Streamlit køyrer heile fila på nytt ved kvart klikk.
# cache_resource gjer at modellen berre blir lasta éin gong.
@st.cache_resource
def last_modell():
    return joblib.load("modell.joblib")

modell = last_modell()

st.title("Bysykkelprognose for Bergen")
st.write("Vel dato og vêr, så viser appen kor mange bysykkelturar modellen "
         "ventar i heile Bergen kvar time frå kl. 05 til 23.")

# Input frå brukaren
dato = st.sidebar.date_input("Dato", value=dt.date(2025, 6, 11))
temp = st.sidebar.slider("Temperatur (°C)", -10, 30, 12)
nedbor = st.sidebar.slider("Nedbør (mm per time)", 0.0, 6.0, 0.0, step=0.5)
st.sidebar.caption("Same vêr heile dagen. Over om lag 6 mm har modellen nesten ingen data.")

# Éi rad per time frå kl. 05 til 23, same kolonnar som under treninga
timar = pd.date_range(pd.Timestamp(dato) + pd.Timedelta(hours=5), periods=19, freq="h")
dogn = pd.DataFrame({"tid_lokal": timar, "temp": temp, "nedbor": nedbor})

spaadd = np.clip(modell.predict(lag_features(dogn)), 0, None)
torr = np.clip(modell.predict(lag_features(dogn.assign(nedbor=0.0))), 0, None)

# Nøkkeltal
kol1, kol2 = st.columns(2)
kol1.metric("Venta turar i løpet av dagen", f"{spaadd.sum():.0f}",
            f"{spaadd.sum() - torr.sum():+.0f} mot opphald")
kol2.metric("Travlaste time", f"kl. {timar[spaadd.argmax()].hour:02d}")
kol2.caption(f"om lag {spaadd.max():.0f} turar")

# Kurve over dagen
kurve = pd.DataFrame({"Valt vêr": spaadd, "Opphald": torr},
                     index=[t.hour for t in timar])
st.line_chart(kurve, x_label="Time på dagen", y_label="Venta turar per time",
              color=["#1f77b4", "#ff7f0e"])

st.caption("Modell: gradient boosting trena på 2024. Feil på teståret 2025: "
           "MAE 16 turar per time. Data: Bergen Bysykkel (NLOD 2.0) og MET Norge/seklima (CC BY 4.0).")
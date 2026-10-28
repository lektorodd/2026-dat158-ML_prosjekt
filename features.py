import holidays
import pandas as pd

def lag_features(tabell):
    """Tek ein tabell med tid_lokal, temp og nedbor. Gir X til modellen."""
    tid = tabell["tid_lokal"]
    # include_sundays=False: elles tel pakken alle søndagar som heilagdag
    heilagdagar = holidays.Norway(include_sundays=False)
    return pd.DataFrame({
        "time": tid.dt.hour,
        "vekedag": tid.dt.dayofweek,      # 0 = måndag, 6 = søndag
        "maned": tid.dt.month,
        "heilagdag": tid.dt.date.map(lambda d: d in heilagdagar).astype(int),
        "temp": tabell["temp"],
        "nedbor": tabell["nedbor"],
    }, index=tabell.index)

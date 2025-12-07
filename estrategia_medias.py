import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Descargar datos
data = yf.download("AAPL", start="2023-01-01")

# Medias móviles
data["SMA20"] = data["Close"].rolling(20).mean()
data["SMA50"] = data["Close"].rolling(50).mean()

# Señales
data["Señal"] = 0
data.loc[data["SMA20"] > data["SMA50"], "Señal"] = 1
data.loc[data["SMA20"] < data["SMA50"], "Señal"] = -1

# Backtesting
data["Retorno"] = data["Close"].pct_change()
data["Estrategia"] = data["Señal"].shift(1) * data["Retorno"]

capital = 100000
data["Capital"] = capital * (1 + data["Estrategia"]).cumprod()

print(data[["Close", "Capital"]].tail())

# Gráfico
plt.plot(data["Close"])
plt.plot(data["SMA20"])
plt.plot(data["SMA50"])
plt.show()

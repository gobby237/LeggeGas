import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parametri (adatta se necessario)
dead_volume = 1.2      # volume morto V₀ in cm³ (o impostalo a 0 se già incluso)
R = 83136            # costante dei gas in L·atm/(mol·K)
# Se tuoi dati sono in altre unità, convertili prima

# 1) Leggi il file dati: colonne t_index, P (atm), VC (L), T (°C)
#    Qui non hai una colonna tempo: usiamo l'indice e moltiplichiamo per 0.1 s
df = pd.read_csv('tenuta_finale.txt', sep=r'\s+', names=['P','VC','T'])

# 2) Definisco l'array dei tempi (in secondi)
n_points = len(df)
t = np.arange(n_points) * 0.1  # 0, 0.1, 0.2, ..., (n_points-1)*0.1

# 3) Calcolo moli n = P*(VC+V0)/(R*(T+273.15))
#    Attenzione: se VC è in cm³, converti in L: df['VC']/=1000
df['n'] = df['P'] * (df['VC'] + dead_volume) / (R * (df['T'] + 273.15))

# 4) Grafico n vs t
plt.figure()
plt.plot(t, df['n'], marker='o', linestyle='-')
plt.xlabel('Tempo (s)')
plt.ylabel('Moli di aria, n (mol)')
plt.title('Andamento delle moli in funzione del tempo')
plt.grid(True)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from tkinter import Tk, filedialog
from matplotlib.lines import Line2D


etichette_leggenda = ["0°", "15°", "25°", "35°", "45°", "55°"]


Tk().withdraw()
file_paths = filedialog.askopenfilenames(title="Seleziona file .txt", filetypes=[("Text files", "*.txt")])

if not file_paths:
    print("Nessun file selezionato.")
    exit()

plt.figure(figsize=(10, 6))
colors = plt.cm.tab10.colors

for i, file_path in enumerate(file_paths):
    try:
        data = np.loadtxt(file_path)
        x = data[:, 0]  # 1/p [m²/Kg]
        y = data[:, 1]  # Volume [cm²]

        slope, intercept, *_ = linregress(x, y)
        y_fit = slope * x + intercept
        residui = y - y_fit  # Calcolo dei residui

        colore = colors[i % len(colors)]
        legenda = etichette_leggenda[i] if i < len(etichette_leggenda) else f"Serie {i+1}"

        plt.plot(x, residui, 'o', markersize=1, label=f"{legenda}", color=colore)

    except Exception as e:
        print(f"Errore nel file {file_path}: {e}")

# Impostazioni grafiche
plt.rcParams.update({
    'font.size': 14,
    'axes.titlesize': 18,
    'axes.labelsize': 16,
    'xtick.labelsize': 14,
    'ytick.labelsize': 14,
    'legend.fontsize': 12
})

legend_elements = [
    Line2D([0], [0], 
           marker='o', 
           color='w',
           label=etichetta,
           markerfacecolor=colore,
           markersize=12)  # Dimensione assoluta in punti
    for etichetta, colore in zip(etichette_leggenda, colors)
]

plt.axhline(0, color='gray', linestyle='--', linewidth=1)  # Linea guida y=0
plt.xlabel("1/p [m²/kg]", fontsize=18)
plt.ylabel("Residuo [cm³]", fontsize=18)
plt.title("Residui dilatazione, $y_i - (a + bx_i)$", fontsize=20)
plt.legend(handles=legend_elements, fontsize=12, loc='best')
plt.tick_params(axis='both', which='major', labelsize=10)
plt.legend(loc='lower left')  # Posizioni disponibili:
plt.grid(True)
plt.tight_layout()
plt.show()

# Sostituisci le tue attuali impostazioni grafiche con:
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

# Crea figura e assi separatamente
fig, ax = plt.subplots(figsize=(10, 6))
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

        ax.plot(x, residui, 'o', markersize=2, label=f"{legenda}", color=colore)

    except Exception as e:
        print(f"Errore nel file {file_path}: {e}")

# Crea elementi per la legenda personalizzata
legend_elements = [
    Line2D([0], [0],
           marker='o',
           color='w',
           label=etichetta,
           markerfacecolor=colore,
           markersize=16)  # Aumenta la dimensione del pallino
    for etichetta, colore in zip(etichette_leggenda, colors)
]

# Impostazioni grafiche
plt.rcParams.update({
    'font.size': 18,
    'axes.titlesize': 18,
    'axes.labelsize': 16,
    'xtick.labelsize': 18,
    'ytick.labelsize': 18,
    'legend.fontsize': 14
})

ax.tick_params(axis='both', which='major', labelsize=16)


# Riduci la larghezza dell'area plottabile per fare spazio alla legenda
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])  # lascia 25% a destra per la legenda

# Linea guida
ax.axhline(0, color='gray', linestyle='--', linewidth=1)

# Etichette e titolo
ax.set_xlabel("1/p [m²/kg]", fontsize=18)
ax.set_ylabel("Residuo [cm³]", fontsize=18)
ax.set_title("Residui compressione, $y_i - (a + bx_i)$", fontsize=22)

# Legenda esterna a destra
ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5), frameon=True)

# Griglia e layout finale
ax.grid(True)
plt.show()

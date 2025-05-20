import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk, filedialog
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D

# Etichette temperature
etichette_leggenda = ["0°", "15°", "25°", "35°", "45°", "55°"]

# Funzione per schiarire o scurire un colore
def adjust_color_brightness(color, factor=1.2):
    c = mcolors.to_rgb(color)
    c = np.array(c) * factor
    c = np.clip(c, 0, 1)
    return tuple(c)

Tk().withdraw()
file_paths = filedialog.askopenfilenames(
    title="Seleziona 12 file .txt in coppie: compressione e dilatazione per ogni temperatura",
    filetypes=[("Text files", "*.txt")]
)

if not file_paths:
    print("Nessun file selezionato.")
    exit()

if len(file_paths) != 12:
    print("Errore: devi selezionare esattamente 12 file (6 coppie compressione/dilatazione).")
    exit()

plt.figure(figsize=(12, 7))
base_colors = plt.cm.tab10.colors[:6]
legend_elements = []

for i in range(6):
    idx_comp = 2 * i
    idx_dilat = 2 * i + 1

    # Dati compressione
    try:
        data_comp = np.loadtxt(file_paths[idx_comp])
        x_comp = data_comp[:, 0]
        y_comp = data_comp[:, 1]
    except Exception as e:
        print(f"Errore nel file {file_paths[idx_comp]}: {e}")
        continue

    # Dati dilatazione
    try:
        data_dilat = np.loadtxt(file_paths[idx_dilat])
        x_dilat = data_dilat[:, 0]
        y_dilat = data_dilat[:, 1]
    except Exception as e:
        print(f"Errore nel file {file_paths[idx_dilat]}: {e}")
        continue

    colore_base = base_colors[i]
    colore_comp = colore_base
    colore_dilat = adjust_color_brightness(colore_base, factor=1.4)

    # Plot con marker piccoli nel grafico
    plt.plot(x_comp, y_comp, 'o', markersize=1.5, color=colore_comp)
    plt.plot(x_dilat, y_dilat, 's', markersize=1.5, color=colore_dilat)

    # Elementi della legenda con marker grandi
    legend_elements.append(Line2D([0], [0], marker='o', color='w', label=f"{etichette_leggenda[i]} compressione",
                                  markerfacecolor=colore_comp, markersize=8))
    legend_elements.append(Line2D([0], [0], marker='s', color='w', label=f"{etichette_leggenda[i]} dilatazione",
                                  markerfacecolor=colore_dilat, markersize=8))

plt.xlabel("1/p [cm²/Kg]", fontsize=18)
plt.ylabel("Volume [cm³]", fontsize=18)
plt.title("Dati grezzi dilatazione e compressione a confronto", fontsize=22)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend(handles=legend_elements, ncol=2, fontsize=14)
plt.grid(True)
plt.tight_layout()
plt.show()

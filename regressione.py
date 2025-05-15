import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
from tkinter import Tk, filedialog
from matplotlib.lines import Line2D

# Etichette leggenda fisse
etichette_leggenda = ["0°", "15°", "25°", "35°", "45°", "55°"]

# Seleziona file
Tk().withdraw()
file_paths = filedialog.askopenfilenames(title="Seleziona file .txt", filetypes=[("Text files", "*.txt")])

if not file_paths:
    print("Nessun file selezionato.")
    exit()

# --- PRIMA FINESTRA: GRAFICO ---
fig1, ax1 = plt.subplots(figsize=(10, 6))
colors = plt.cm.tab10.colors

x_min, x_max = 0.25, 0.95
y_min, y_max = 6, 22.68
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(y_min, y_max)

legend_elements = []
fit_results = []

for i, file_path in enumerate(file_paths):
    try:
        data = np.loadtxt(file_path)
        x = data[:, 0]
        y = data[:, 1]

        # Fit lineare
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        y_fit = slope * x + intercept
        residuals = y - y_fit
        sigma_post = np.sqrt(np.sum(residuals**2) / (len(x) - 2))

        # Errore su b e a con σ_post
        delta_x = np.sum((x - np.mean(x))**2)
        err_b = sigma_post / np.sqrt(delta_x)
        err_a = sigma_post * np.sqrt(np.sum(x**2) / (len(x) * delta_x))

        x_fit_line = np.linspace(x_min, x_max, 100)
        y_fit_line = slope * x_fit_line + intercept

        colore = colors[i % len(colors)]
        legenda = etichette_leggenda[i] if i < len(etichette_leggenda) else f"Serie {i+1}"

        ax1.plot(x, y, 'o', markersize=0.5, color=colore, alpha=0.4)
        ax1.plot(x_fit_line, y_fit_line, '-', color="black", linewidth=0.5)

        legend_elements.append(Line2D([0], [0], marker='o', color='w',
                                      label=legenda,
                                      markerfacecolor=colore,
                                      markersize=5))

        fit_results.append((legenda, intercept, slope, err_a, err_b, sigma_post))

    except Exception as e:
        print(f"Errore nel file {file_path}: {e}")

# Legenda retta nera
legend_elements.append(Line2D([0], [0], color='black', lw=1, label='Retta interpolante'))
ax1.set_xlabel("1/p [cm^2/Kg]")
ax1.set_ylabel("Volume [cm^3]")
ax1.set_title("Regressione in fase di compressione")
ax1.legend(handles=legend_elements, title="Legenda")
ax1.grid(True)

# --- SECONDA FINESTRA: TABELLA ---
# --- SECONDA FINESTRA: TABELLA ---
fig2, ax2 = plt.subplots(figsize=(8, 2 + 0.4 * len(fit_results)))
ax2.axis('off')

if fit_results:
    col_labels = ["Temperatura", "a", "b", "err(a)", "err(b)", "σ_post"]
    table_data = [
        [temp, f"{a:.4f}", f"{b:.4f}", f"{err_a:.4f}", f"{err_b:.4f}", f"{sigma:.4f}"]
        for temp, a, b, err_a, err_b, sigma in fit_results
    ]

    table = ax2.table(cellText=table_data,
                      colLabels=col_labels,
                      loc='center',
                      cellLoc='center',
                      colLoc='center',
                      bbox=[0, 0, 1, 0.9])  # lascia spazio sopra per il titolo

    table.auto_set_font_size(False)
    table.set_fontsize(10)

    # Aumenta spaziatura verticale delle celle
    for key, cell in table.get_celld().items():
        cell.set_height(0.08)

    ax2.set_title("Dilatazione", fontsize=14, pad=20)

plt.tight_layout()
plt.show()


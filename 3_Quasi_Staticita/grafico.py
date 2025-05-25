import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from tkinter import Tk, filedialog

def carica_dati():
    Tk().withdraw()
    file_path = filedialog.askopenfilename(title="Seleziona un file dati",
                                           filetypes=[("File di testo", "*.txt")])
    if not file_path:
        raise ValueError("Nessun file selezionato.")
    
    # Usa pandas con delim_whitespace=True per separatori multipli spazi/tab
    df = pd.read_csv(file_path, delim_whitespace=True, header=None, comment='#')
    
    if df.shape[1] < 3:
        raise ValueError("Il file deve avere almeno 3 colonne: x, y, errore su y.")
    
    return df.iloc[:, 0].values, df.iloc[:, 1].values, df.iloc[:, 2].values

def plot_dati(x, y, yerr):
    plt.figure(figsize=(10, 6))
    plt.errorbar(x, y, yerr=yerr, fmt='o', markersize=5, capsize=4, color='blue')
    
    plt.xlabel("T [K]", fontsize=18)
    plt.ylabel("Moli", fontsize=18)
    plt.title("Moli in funzione della temperatura", fontsize=22)

    # Format scientifico solo sull’asse Y
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda val, _: f"{val:.2e}"))

    # Limiti y con margine del 20%
    ymin = min(y - yerr)
    ymax = max(y + yerr)
    delta = ymax - ymin
    plt.ylim(ymin - 0.5*delta, ymax + 0.5*delta)

    # Linea tratteggiata a y = 1.1e-3
    plt.axhline(1.1e-3, linestyle='--', color='black', linewidth=1)

    plt.grid(True)
    plt.tick_params(axis='both', labelsize=16)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        x, y, yerr = carica_dati()
        plot_dati(x, y, yerr)
    except Exception as e:
        print(f"Errore: {e}")

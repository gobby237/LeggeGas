import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from tkinter import Tk, filedialog

def carica_dati():
    Tk().withdraw()
    file_path = filedialog.askopenfilename(title="Seleziona un file dati",
                                           filetypes=[("File di testo", "*.txt")])
    if not file_path:
        raise ValueError("Nessun file selezionato.")
    
    dati = np.loadtxt(file_path)
    if dati.shape[1] < 3:
        raise ValueError("Il file deve avere almeno 3 colonne: x, y, errore su y.")
    
    return dati[:, 0], dati[:, 1], dati[:, 2]

def plot_dati(x, y, yerr):
    plt.figure(figsize=(10, 6))
    plt.errorbar(x, y, yerr=yerr, fmt='o', markersize=5, capsize=4, label="Dati")
    
    plt.xlabel("T (K)", fontsize=18)
    plt.ylabel("Moli", fontsize=18)
    plt.title("Moli in funzione della temperatura", fontsize=22)
    
    # 👉 Notazione scientifica con 2 cifre significative sull'asse y
    plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda val, _: f"{val:.2e}"))

    plt.grid(True)
    plt.legend()
    plt.tick_params(axis='both', labelsize=16)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        x, y, yerr = carica_dati()
        plot_dati(x, y, yerr)
    except Exception as e:
        print(f"Errore: {e}")

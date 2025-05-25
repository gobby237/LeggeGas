import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt

def carica_dati(file_path):
    """
    Legge un file di testo con due colonne numeriche
    e restituisce due array: x e y.
    """
    data = np.loadtxt(file_path)
    return data[:, 0], data[:, 1]

def regressione_lineare(x, y):
    """
    Esegue regressione lineare y = a x + b con minimo quadrati
    e restituisce (a, b).
    """
    a, b = np.polyfit(x, y, deg=1)
    return a, b

def calcola_residui(x, y, a, b):
    """
    Calcola i residui y - (a x + b).
    """
    y_pred = a * x + b
    return y - y_pred

def seleziona_file():
    """
    Apre una finestra di dialogo per selezionare fino a 6 file .txt.
    """
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title="Seleziona fino a 6 file .txt per la regressione",
        filetypes=[("Text files", "*.txt")]
    )
    return list(file_paths)

def main():
    file_paths = seleziona_file()
    if not file_paths:
        print("Nessun file selezionato. Il programma terminerà.")
        return
    if len(file_paths) > 6:
        print("Hai selezionato più di 6 file. Verranno usati solo i primi 6.")
        file_paths = file_paths[:6]

    plt.figure(figsize=(10, 6))
    plt.title("Residui delle regressioni lineari")
    plt.xlabel("Indice del punto dati")
    plt.ylabel("Residuo")

    for file_path in file_paths:
        x, y = carica_dati(file_path)
        a, b = regressione_lineare(x, y)
        residui = calcola_residui(x, y, a, b)
        plt.plot(residui, marker='o', linestyle='-', label=file_path.split("/")[-1])

    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

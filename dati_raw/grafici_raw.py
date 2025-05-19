import matplotlib.pyplot as plt
import numpy as np
from tkinter import Tk, filedialog

def select_files():
    root = Tk()
    root.withdraw()
    
    temperatures = ['0°', '15°', '25°', '35°', '45°', '55°']
    files = []
    
    for temp in temperatures:
        print(f"Seleziona il file per {temp}")
        file_path = filedialog.askopenfilename(
            title=f"Seleziona file dati per {temp}",
            filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
        )
        if not file_path:
            raise ValueError("Selezione file annullata")
        files.append(file_path)
    
    return files

def plot_data(files):
    plt.figure(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 1, len(files)))
    
    for i, file_path in enumerate(files):
        data = np.loadtxt(file_path)
        x = data[:, 0]  # Prima colonna = Volume [cm³]
        y = data[:, 1]  # Seconda colonna = 1/p [cm²/Kg]
        
        plt.plot(x, y, 
                 marker='o',
                 linestyle='-',
                 color=colors[i],
                 markersize = 0.5,
                 label=f'{5*i}°' if i == 0 else f'{15 + 10*(i-1)}°')  # Genera le label corrette
    
    plt.xlabel('1/p [cm²/Kg]', fontsize=18)
    plt.ylabel('Volume [cm³]', fontsize=18)
    plt.title('Fase di dilatazione', fontsize=20)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='Temperatura', title_fontsize=16, fontsize=10)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    try:
        selected_files = select_files()
        plot_data(selected_files)
    except Exception as e:
        print(f"Errore: {str(e)}")
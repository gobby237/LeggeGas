#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    double x1, x2;       // le due stime
    double sigma1, sigma2;  // i rispettivi errori

    cout << "Inserisci x1 e il suo errore sigma1: ";
    cin >> x1 >> sigma1;

    cout << "Inserisci x2 e il suo errore sigma2: ";
    cin >> x2 >> sigma2;

    if (sigma1 <= 0 || sigma2 <= 0) {
        cerr << "Gli errori devono essere positivi." << endl;
        return 1;
    }

    // Calcolo dei pesi
    double w1 = 1.0 / (sigma1 * sigma1);
    double w2 = 1.0 / (sigma2 * sigma2);

    // Media pesata
    double mu = (x1 * w1 + x2 * w2) / (w1 + w2);

    // Errore sulla media pesata
    double sigma_mu = sqrt(1.0 / (w1 + w2));

    // Output con 6 cifre decimali
    cout << fixed << setprecision(6);
    cout << "\nMedia pesata: " << mu << " ± " << sigma_mu << endl;

    return 0;
}

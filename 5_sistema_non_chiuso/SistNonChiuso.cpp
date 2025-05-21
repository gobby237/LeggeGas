#include <iostream>
#include <math.h>
#include <vector>
#include <fstream>
using namespace std; 
int main ()
{
    // prendo il file in tenuta finale con p,v t. Mi servono le prime due 

    string nome = ""; 

    cout << "Inserire nome file: "; 
    cin >> nome; 

    double val1, val2, val3; 

    vector<double> n,t,p,v; 

    ifstream fin (nome); 
    ofstream out ("MoliTempo.txt", std::ios::app); 
    ofstream dout ("RettaIdeale.txt", std::ios::app);

    while (fin >> val1 >> val2 >> val3)
    {
        p.push_back(val1); 
        v.push_back(val2); 
        t.push_back(val3); 
    }

    // abbiamo gli array pieni 

    double b = 0; 
    cout << "Inserire coeff angolare regressione 55C: "; 
    cin >> b; 

    for (int i = 0; i < t.size(); i ++ )
    {
        n.push_back((p.at(i)*9.81*(b + v.at(i)))/(831.4*(t.at(i) + 273.15)));
        // out << 0.1*(i+1) << "   " << (p.at(i)*9.81*(b + v.at(i)))/(831.4*(t.at(i) + 273.15)) << "\n"; 
    }

    for (int i = 0; i < t.size(); i ++ )
    {
        // dout << 0.1*(i+1) << "   " << (p.at(0)*9.81*(b + v.at(i)))/(831.4*(t.at(i) + 273.15)) << "\n"; 
    }


    // facciamo la media 

    double media, somma; 

    somma = 0; 
    for (auto c: n)
    {
        somma += c;  
    }

    media = somma/n.size();

    // e poi calcoliamo l'errore 

    cout << "La media degli ni vale " << media << endl; 

    cout << "La differenza tra l'ultimo ed il primo vale: " << n.back() - n.front() << endl; 

    cout << "L'errore relativo sul sistema non chiuso vale (*1000): " << 1000*(n.back() - n.front())/(sqrt(3)*2*media) << endl; 







    return 0;
}
#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>
#include <string>
using namespace std; 
int main ()
{

    string nome = ""; 

    cout << "Inserire il nome del file: "; 
    cin >> nome; 

    ifstream fin (nome + ".txt"); 
    ofstream out (nome + "_analisi.txt"); 

    vector<double> t, v, p; 

    double val, jol, fr; 

    while (fin >> val >> jol >> fr)
    {
        p.push_back(val); 
        v.push_back(jol); 
        t.push_back(fr); 
    }

    // abbiamo tutti i valori 


    for (int i = 0; i < p.size(); i ++ )
    {
        out << 1/p.at(i) << "   " << v.at(i) << "  " << t.at(i) << "\n"; 
    }




    return 0; 
}

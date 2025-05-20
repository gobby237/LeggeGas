#include <fstream>
#include <iostream>
#include <vector>
using namespace std; 
int main ()
{
    // voglio calcolare la pressione ideale se le moli fossero rimaste uguali 

    vector<double> p,v,t;
    
    ifstream fin ("tenuta_finale.txt"); 
    ofstream out ("test.txt", std::ios::app); 

    double val1, val2, val3, b;

    cout << "Inserire il coeff angolare della regressione a 55C: "; 
    cin >> b; 

    while (fin >> val1 >> val2 >> val3)
    {
        p.push_back(val1); 
        v.push_back(val2); 
        t.push_back(val3+273.15); 
    }

    double n0 = 0; 

    // calcoliamo le moli ideali (quelle iniziali)
    n0 = (p.front()*9.81*(v.front() + b))/(831.4*t.front()); 

    cout << n0 << endl; 

    // stampiamo in un file le pressioni che avremmo dovuto misurare se le moli fossero risultate costanti 

    for (int i = 0; i < t.size(); i ++ )
    {
        out << (n0*831.4*t.at(i))/((v.at(i) +b)*9.81) << "\n"; 
    }




    return 0;
}
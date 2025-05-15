#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
using namespace std; 
int main ()
{

    string nome = ""; 

    cout << "inserire nome file:"; 
    cin >> nome; 


    ifstream fin(nome); 
    ofstream out("n_compressione.txt", std::ios::app);

    vector<double> t,b,n; // temperatura 
    
    double val, g; 
    
    while (fin >> val >> g)
    {
        b.push_back(val); 
        t.push_back(g); 
    }

    for(int i = 0; i < t.size(); i ++ )
    {
        n.push_back(b.at(i)/((t.at(i)+273.15)*pow(8.3136,4)));
    }

    for (auto c: n)
    {
        out << c << "\n"; 
    }
    




    return 0; 
}
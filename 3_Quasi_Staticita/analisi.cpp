#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>
#include <cstdlib> // per abs()
using namespace std; 
int main ()
{

    
    /*
    
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
        n.push_back((b.at(i)*981)/((t.at(i)+273.15)*(83136)));
    }

    for (auto c: n)
    {
        out << c << "\n"; 
    }

    */
    
    

    /*
    
    fstream fin1 ("n_compressione.txt"); 
    fstream fin2 ("n_dilatazione.txt"); 
    fstream fin3 ("Errori_relativi.txt"); 
    ofstream out ("grafico.txt", std::ios::app); 

    double val1, val2;

    vector<double> n_comp, n_dil,t , errel, sigma;
    
    while(fin1>>val1)
    {
        n_comp.push_back(val1); 
    }
    while(fin2>>val2)
    {
        n_dil.push_back(val2); 
    }
    while(fin3>>val1>>val2)
    {
        t.push_back(val1); 
        errel.push_back(val2); 
    }

    // sputo fuori moli medie tra compressione temperatura, moli medie ed incertezza (moltiplico il rel per la media)
    double media = 0; 

    for(int i = 0; i < 6; i ++ )
    {
        media = (n_comp.at(i) + n_dil.at(i))/2;
        out << t.at(i) << "    " << media << "    " << errel.at(i)*media << "\n"; 
    }

    */

    
    

    /*

    ofstream out ("Errori_relativi.txt", std::ios::app); 

    ifstream fin1 ("n_dilatazione.txt"); 
    ifstream fin2 ("n_compressione.txt"); 

    double val1, val2; 
    vector<double> n_dil, n_comp; 

    while (fin1>>val1)
        n_dil.push_back(val1); 

    while (fin2>>val2)
        n_comp.push_back(val2); 

    
    vector<double> media; 

    for (int i = 0; i < n_comp.size(); i ++ )
    {
        media.push_back((n_comp.at(i) + n_dil.at(i))/2);
    }

    // ho tutte le medie

    for (int i = 0; i < n_comp.size(); i ++ )
    {
        out << abs(n_comp.at(i) - n_dil.at(i))/(2*sqrt(3)*media.at(i)) << "\n"; 
    }
    
    */

    ifstream fin ("analisi_dati.txt"); 
    ofstream out ("grafico.txt", std::ios::app);

    // temp / errt / b / err b / moli

    double val1, val2, val3, val4, val5;
    vector<double> t, errt, b, errb, errn, n;

    while (fin>>val1>>val2>>val3>>val4>>val5)
    {
        t.push_back(val1); 
        errt.push_back(val2); 
        b.push_back(val3); 
        errb.push_back(val4);
        n.push_back(val5); 
    }

    // nel file out: t / moli / err moli 
    
    for(int i = 0; i < 6; i ++ )
    {
        errn.push_back(n.at(i)*sqrt(pow((errb.at(i)/b.at(i)),2) + pow((errt.at(i)/t.at(i)),2)));
    }

    for (int i = 0; i < 6; i ++ )
    {
        out << t.at(i) << "     " << n.at(i) << "     " << errn.at(i) << "\n"; 
    }




    return 0; 
}
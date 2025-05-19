#include <iostream> 
#include <vector> 
#include <cmath>
#include <fstream>
using namespace std; 
int main ()
{

    string nome; 
    vector<double> t; 

    cout << "Inserire nome file: ";
    cin >> nome; 
    ifstream fin (nome); 
    ofstream out ("risultati.txt", std::ios::app);

    double val,g,b; 

    while (fin>>g>>b>>val)
    {
        t.push_back(val + 273.15);
    }

    double somma = 0; 
    double media = 0;
    double stdev = 0; 
    double scarti = 0; 

    for (auto c: t)
    {
        somma += c; 
    }

    media = (double) somma / t.size(); 

    for (auto c: t)
    {
        scarti += pow((c - media),2);  
    }

    stdev = sqrt(scarti/(t.size()-1));

    cout << "RISULTATI" << endl; 
    cout << "Stdev: " << stdev << endl; 
    cout << "Media: " << media << endl; 
    cout << "Errore rel: " << stdev/media << endl;  

    string temp; 
    cout << "Inserire temp: "; 
    cin >> temp; 

    out << temp << "    " << stdev/media << "   " << stdev*1000/media << "   " << 0.3/(sqrt(3)*media) << "\n"; 


    return 0; 
}
// PrimerIntento.cpp : Este archivo contiene la funci�n "main". La ejecuci�n del programa comienza y termina ah�.
//

#include <iostream>
#include <string>
using namespace std;

class Persona
{
private: 
    float altura;
    float peso;
    string nombre;
public:
    Persona()
    {
        altura = 0;
        peso = 0;
        nombre = "";
    }
    Persona(float a, float p, string n)
    {
        altura = a;
        peso = p;
        nombre = n;
    }
    //set y get
    void setAltura(float a)
    {
        altura = a;
    }
    float getAltura()
    {
        return altura;
    }
    void setPeso(float p)
    {
        peso = p;
    }
    float getPeso()
    {
        return peso;
    }
    void setNombre(string n)
    {
        nombre = n;
    }
    string getNombre()
    {
        return nombre;
    }
};

int main()
{

    Persona IMC;

    float Height;
    float Weight;
    string Name;
    string SuPeso;


    cout << "Ingrese su nombre." << endl;
    cin >> Name;
    IMC.setNombre(Name);

    cout << "Ingrese su altura." << endl;
    cin >> Height;
    IMC.setAltura(Height);

    cout << "Ingrese su peso." << endl;
    cin >> Weight;
    IMC.setPeso(Weight);

  

    //cout << "Hello World!";
    return 0;
}

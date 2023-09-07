#include <iostream>
#include <string>
#include "TAD.h"
#include <sstream>
#include <vector>
#include "news.cpp"

using namespace std;

void addNews(Nodo *nodo, const string data) // Agrega una noticia y la ordena por prioridad
{
    nodo->addNodo(new Nodo(data));
}

// Insertar noticia en una posicion

void insertNews(Nodo *nodo, const string data, int pos)
{
    if(pos >= nodo->countNodos())
    {
        nodo->addNodo(new Nodo(data));
        return;
    }

    pos--;

    // Crear puntero auxiliar
    Nodo *aux = nodo;
    
    // Crear el nodo original
    nodo->addNodo(new Nodo(data));

    // llevar el puntero al nuevo nodo

    while (nodo->getNext() != NULL)
    {
        nodo = nodo->getNext();
    }

    // Llevar el puntero auxiliar a la posicion

    for (int i = 0; i < pos; i++)
    {
        aux = aux->getNext();
    }

    if(pos == 0)
    {    
        nodo->getPrev()->setNext(nodo->getNext());
        nodo->setPrev(aux->getPrev());
        aux->setPrev(nodo);
        nodo->setNext(aux);
    }
    else
    {
        nodo->getPrev()->setNext(nodo->getNext());
        nodo->setNext(aux);
        nodo->setPrev(aux->getPrev());
        aux->getPrev()->setNext(nodo);
        aux->setPrev(nodo);
    }
}

void changePriority(Nodo *nodo, int pos, int Y)
{

    Y = pos - Y;

    pos--;

    // LLevar el puntero a la posicion
    for(int i = 0; i < pos; i++)
    {
        nodo = nodo->getNext();
    }

    // Guardar el dato
    string copy = nodo->getData();

    // Eliminar el nodo
    nodo->getPrev()->setNext(nodo->getNext());
    nodo->getNext()->setPrev(nodo->getPrev());

    nodo = nodo->getPrev();

    // Llevar el puntero al inicio

    while (nodo->getPrev() != NULL)
    {
        nodo = nodo->getPrev();
    }

    insertNews(nodo, copy, Y);

}

void apiNews(Nodo *nodo)
{
    Newsapi newsapi;

    vector<News *> allrecords = newsapi.getRecords();

    for (int i = 0; i < allrecords.size(); i++)
    {
        addNews(nodo, allrecords.at(i)->getTitle());
    }
}

void showAll(Nodo *nodo)
{

    cout << "TODAS LAS NOTICIAS: " << endl << endl;

    // Llevar el puntero al inicio

    while (nodo->getPrev() != NULL)
    {
        nodo = nodo->getPrev();
    }

    int i = 1;

    do
    {
        cout << "RELEVANCIA: " << i << endl;

        cout << nodo->getData() << endl;
        nodo = nodo->getNext();

        cout << endl;
        i++;
    }
    while (nodo != NULL);
}

// Mostrar top 5

void showTop5(Nodo *nodo)
{
    // Llevar el puntero al inicio

    cout << "LAS 5 NOTICIAS MAS RELEVANTES: " << endl << endl;

    while (nodo->getPrev() != NULL)
    {
        nodo = nodo->getPrev();
    }

    for (int i = 0; i < 5; i++)
    {
        cout << "RELEVANCIA: " << i + 1 << endl;
        cout << nodo->getData() << endl;
        nodo = nodo->getNext();
        cout << endl;
    }
}

// Borrar noticias que contengan una palabra

void deleteNews(Nodo *nodo)
{
    // entrada de datos por consola

    string input;

    cout << "INGRESE LAS PALABRAS A ELIMINAR SEPARADAS POR COMA SIN ESPACIOS: ";

    getline(cin, input);
    
    vector<string> array; // Declara un vector para almacenar los elementos

    // Crea un objeto istringstream para dividir el string
    istringstream ss(input);
    string token;

    // Divide el string en elementos y los almacena en el vector
    while (getline(ss, token, ',')) {
        // Convierte el token a entero y lo agrega al vector
        array.push_back((token));
    }

    // Recorrer titulares

    while (nodo->getNext() != NULL)
    {
        // Recorrer palabras

        for(int j = 0; j < array.size(); j++)
        {
            // Buscar palabra en titular

            string texto = nodo->getData();
            string palabraABuscar = array[j];

            size_t posicion = texto.find(palabraABuscar);

            if (posicion != string::npos) {
                nodo->getPrev()->setNext(nodo->getNext());
                nodo->getNext()->setPrev(nodo->getPrev());
            }
        }

        nodo = nodo->getNext();
    }
}

// Mostrar noticias que contengan una palabra

void searchWords(Nodo *nodo)
{
    // entrada de datos por consola

    string input;

    cout << "INGRESE LAS PALABRAS A BUSCAR SEPARADAS POR COMA SIN ESPACIOS: ";

    getline(cin, input);
    
    vector<string> array; // Declara un vector para almacenar los elementos

    // Crea un objeto istringstream para dividir el string
    istringstream ss(input);
    string token;

    // Divide el string en elementos y los almacena en el vector
    while (getline(ss, token, ',')) {
        // Convierte el token a entero y lo agrega al vector
        array.push_back((token));
    }

    // Recorrer titulares

    int rel = 1; // Relevancia

    while (nodo->getNext() != NULL)
    {
        // Recorrer palabras

        for(int j = 0; j < array.size(); j++)
        {
            // Buscar palabra en titular

            string texto = nodo->getData();
            string palabraABuscar = array[j];

            size_t posicion = texto.find(palabraABuscar);

            if (posicion != string::npos) {
                cout << "RELEVANCIA: " << rel << endl;
                cout << texto << endl;
                rel++;
            }
        }

        nodo = nodo->getNext();
    }
}
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include "news.h"
#include "json.hpp"

using namespace std;

int main()
{   
    // Agregar noticias sin relevancia especifica

    cout << "NOTICIAS SIN RELEVANCIA ESPECIFICA" << endl << endl;

    Nodo *nodo = new Nodo("nuevas vacunas contra virus de la gripe esperanza para un invierno saludable");
    addNews(nodo, "descubrimiento cientifico el agua en marte abre nuevas preguntas");
    addNews(nodo, "tecnologia 5g llega a mas ciudades mayor velocidad en internet movil");
    addNews(nodo, "reciclaje de plasticos un paso crucial para un futuro sostenible");
    addNews(nodo, "astronomos observan un nuevo planeta potencialmente habitable");
    addNews(nodo, "avance medico terapia genica ofrece esperanza a pacientes con enfermedades raras");

    showAll(nodo);

    // Agregar noticias con relevancia especifica

    cout << endl << "NOTICIAS CON RELEVANCIA ESPECIFICA" << endl << endl;

    insertNews(nodo, "crisis climatica advertencia de expertos sobre aumento de niveles del mar", 2);
    insertNews(nodo, "tecnologia 5g llega a mas ciudades mayor velocidad en internet movil", 1);
    insertNews(nodo, "reciclaje de plasticos un paso crucial para un futuro sostenible", 9);

    showAll(nodo);

    // Cambiar prioridad de una noticia

    cout << endl << "CAMBIAR PRIORIDAD DE UNA NOTICIA" << endl << endl;

    changePriority(nodo, 5, +4);

    showAll(nodo);

    // Mostrar top 5

    cout << "TOP 5" << endl << endl;

    showTop5(nodo);

    // Buscar palabras en las noticias

    cout << endl << "BUSCAR PALABRAS EN LAS NOTICIAS" << endl << endl;

    searchWords(nodo);

    // Eliminar noticias por palabra clave

    cout << endl << "ELIMINAR NOTICIAS POR PALABRA CLAVE" << endl << endl;

    deleteNews(nodo);

    showAll(nodo);    

}


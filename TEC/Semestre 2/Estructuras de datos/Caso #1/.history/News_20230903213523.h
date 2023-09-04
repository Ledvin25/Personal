#include <iostream>
#include "TAD.h"

void addNews(Nodo )
{
   
}

void ShowAll(Nodo &nodo)
{
   while (nodo.getNext() != NULL)
   {
      cout << nodo.getData() << endl;
      nodo = nodo.getNext();
   }
}

showTop5(Nodo &nodo)
{
   int i = 0;
   while (nodo.getNext() != NULL && i < 5)
   {
      cout << nodo.getData() << endl;
      nodo = nodo.getNext();
      i++;
   }
}






/*
changePriority(int pos, int Y); // Cambia la prioridad de la noticia
   // moveToPosition(new_pos);

checkPriority(); // Verifica que las noticias esten ordenadas por prioridad
   // moveToPosition(new_pos);

addNews(string key_words); // Agrega una noticia y la ordena por prioridad
   // addData(data);
   // checkPriority(Y);

deleteNews(string key_words); // Elimina una noticia
   // deleteData(data);

showTop5(); // Muestra las 5 noticias con mayor prioridad
   // displayData(pos);

showAll(); // Muestra todas las noticias con un bucle que finaliza cuando se llega al final de la lista
   // displayData(pos);

searchWord(string key_words); // Busca una o varias noticias que contengan las palabras escodigas
   // displayData(pos);

deleteWords(string key_words); // Elimina noticias que contengan una o varias palabras escodigas
   // deleteNews(key_words);

*/
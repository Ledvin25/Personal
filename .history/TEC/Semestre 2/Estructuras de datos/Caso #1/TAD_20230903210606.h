#include <iostream>
#include <string>
using namespace std;

Class Nodo
{
    private:
        array data;
        Nodo *next;
        Nodo *prev;
    public:
        
        // Constructor

        Nodo(string data)
        {
            this->data = data;
            this->next = NULL;
            this->prev = NULL;
        }

        // Agregar nodo

        void addNodo(Nodo *nodo)
        {
            if(this->next == NULL)
            {
                this->next = nodo;
                nodo->prev = this;
            }
            else
            {
                this->next->addNodo(nodo);
            }
        }

        // Eliminar nodo

        void deleteNodo(int pos)
        {
            if(this->next != NULL)
            {
                if(pos == 0)
                {
                    this->prev->next = this->next;
                    this->next->prev = this->prev;
                }
                else
                {
                    this->next->deleteNodo(pos-1);
                }
            }
        }
        
        // Mostrar nodo

        void displayNodo(int pos)
        {
            if(this->next != NULL)
            {
                if(pos == 0)
                {
                    cout << this->data << endl;
                }
                else
                {
                    this->next->displayNodo(pos-1);
                }
            }
        }

        // Mover al siguiente nodo

        void getNext()
        {
            if(this->next != NULL)
            {
                this->next->displayNodo(pos-1);
            }
        }

        // Mover al nodo anterior

        void getPrev()
        {
            if(this->prev != NULL)
            {
                this->prev->displayNodo(pos-1);
            }
        }

        // Buscar nodo

        void searchNodo(int pos)
        {
            if(this->next != NULL)
            {
                if(pos == 0)
                {
                    return this->data;
                }
                else
                {
                    this->next->searchNodo(pos-1);
                }
            }
        }
};
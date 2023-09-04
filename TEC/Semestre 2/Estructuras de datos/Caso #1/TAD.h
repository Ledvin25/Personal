#include <iostream>
#include <string>

using namespace std;

class Nodo
{
    private:
        string data;
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
        
    // Obtener dato

        string getData()
        {
                return this->data;
        }

    // Obtener siguiente

        Nodo *getNext()
        {
            return this->next;
        }

    // Obtener anterior

        Nodo *getPrev()
        {
            return this->prev;
        }

    // Fijar siguiente

        void setNext(Nodo *next)
        {
            this->next = next;
        }
    
    // Fijar anterior

        void setPrev(Nodo *prev)
        {
            this->prev = prev;
        }

    // Contar nodos

        int countNodos()
        {
            if(this->next == NULL)
            {
                return 1;
            }
            else
            {
                return 1 + this->next->countNodos();
            }
        }
};   


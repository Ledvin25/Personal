Class Nodo
{
    private:
        string data;
        Nodo *next;
        Nodo *prev;
    public:
        
        // Constructor

        Nodo(info data)
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

};


/*addData(info data, int pos); // Agrega un dato en la posicion pos

deleteData(int pos); // Elimina un dato en la posicion pos

displayData(int pos); // Muestra un dato en la posicion pos

getNext(); // Mueve el puntero a la siguiente posicion

getPrev(); // Mueve el puntero a la posicion anterior

moveToPosition(int new_pos, info data); // Se mueve la noticia a la posicion new_pos*/
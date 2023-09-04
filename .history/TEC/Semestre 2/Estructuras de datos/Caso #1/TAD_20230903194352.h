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

        // Insertar info

        void setData(info data)
        {
            this->data = data;
        }

};


/*addData(info data, int pos); // Agrega un dato en la posicion pos

deleteData(int pos); // Elimina un dato en la posicion pos

displayData(int pos); // Muestra un dato en la posicion pos

getNext(); // Mueve el puntero a la siguiente posicion

getPrev(); // Mueve el puntero a la posicion anterior

moveToPosition(int new_pos, info data); // Se mueve la noticia a la posicion new_pos*/
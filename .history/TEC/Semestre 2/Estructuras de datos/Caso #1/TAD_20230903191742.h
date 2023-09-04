Class Nodo
{
    private:
        info data;
        Nodo *next;
        Nodo *prev;
    public:
        Nodo(info data);
        Nodo(info data, Nodo *next, Nodo *prev);
        info getData();
        void setData(info data);
        Nodo *getNext();
        void setNext(Nodo *next);
        Nodo *getPrev();
        void setPrev(Nodo *prev);

};


/*addData(info data, int pos); // Agrega un dato en la posicion pos

deleteData(int pos); // Elimina un dato en la posicion pos

displayData(int pos); // Muestra un dato en la posicion pos

getNext(); // Mueve el puntero a la siguiente posicion

getPrev(); // Mueve el puntero a la posicion anterior

moveToPosition(int new_pos, info data); // Se mueve la noticia a la posicion new_pos*/
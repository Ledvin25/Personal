class News{
    private:
        string title;
        string description;
        string date;
        int priority;
        News *next;
    
    public:
        News();
        
        News(string title, string description, string date, int priority);
        void setTitle(string title);
        void setDescription(string description);
        void setDate(string date);
        void setPriority(int priority);
        void setNext(News *next);
        string getTitle();
        string getDescription();
        string getDate();
        int getPriority();
        News *getNext();
};


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
#ifndef BTREE_H
#define BTREE_H

#include <iostream>
#include <vector>
#include "bTreeNode.h"

class BTree {
private:

    const int maxKeys = 3; // Maximo numero de claves por nodo
    BTreeNode* root; // Puntero a la raiz del arbol

    //--------------------------- Metodos auxiliares ---------------------------//

    // Inserta una clave en un nodo que no esta lleno
    void insertNonFull(BTreeNode* node, const std::string& keywords, int id, int page, const std::string& paragraph) 
    {
        int lastKey = node->keys.size() - 1; // Indice de la ultima clave

        // Si el nodo es una hoja
        if (node->isLeaf) 
        {
            Clave newKey("");
            node->keys.push_back(newKey); // Insertar clave vacia

            // Desplazar claves para insertar la nueva clave
            while (lastKey >= 0 && keywords < node->keys[lastKey].word) 
            {
                node->keys[lastKey + 1] = node->keys[lastKey];
                lastKey--;
            }
            
            // Crear clave final
            Clave finalKey(keywords);
            finalKey.paragraphs.push_back(Paragraph(id, page, paragraph));
            node->keys[lastKey + 1] = finalKey;
        } 
        else
        {
            // Buscar hijo donde insertar la clave
            while (lastKey >= 0 && keywords < node->keys[lastKey].word) 
            {
                lastKey--;
            }
            lastKey++;

            // Si el hijo esta lleno, hacer split
            if (node->children[lastKey]->keys.size() == maxKeys) {
                splitChild(node, lastKey, node->children[lastKey]);
                if (keywords > node->keys[lastKey].word) {
                    lastKey++;
                }
            }

            // Si la clave ya existe, insertar el parrafo en la clave
            if (keywords == node->keys[lastKey].word) 
            {
                node->keys[lastKey].paragraphs.push_back(Paragraph(id, page, paragraph));
            } 
            else 
            {
                // Insertar clave en el hijo
                insertNonFull(node->children[lastKey], keywords, id, page, paragraph);
            }
        }
    }

    // Splitchild de toda la vida
    void splitChild(BTreeNode* parent, int index, BTreeNode* child) 
    {
        
        BTreeNode* newNode = new BTreeNode(child->isLeaf);

        // Insertar nueva clave en el padre
        parent->keys.insert(parent->keys.begin() + index, child->keys[maxKeys / 2]);

        // Insertar nuevo hijo en el padre
        parent->children.insert(parent->children.begin() + index + 1, newNode);

        // Copiar claves y punteros al nuevo nodo
        newNode->keys.assign(child->keys.begin() + maxKeys / 2 + 1, child->keys.end());
        child->keys.resize(maxKeys / 2); // Redimensionar vector de claves

        // Si el nodo no es una hoja, copiar punteros a los hijos
        if (!child->isLeaf) 
        {
            newNode->children.assign(child->children.begin() + maxKeys / 2 + 1, child->children.end());
            child->children.resize(maxKeys / 2 + 1);
        }
    }

    // Busca una palabra en el arbol
    std::vector<Paragraph> findKeyword(BTreeNode* node, const std::string& keyword) 
    {
        // Busqueda binaria aprovechando que las claves estan ordenadas alfabeticamente
        int left = 0;
        int right = node->keys.size() - 1;

        // Buscar clave
        while (left <= right) 
        {
            int mid = left + (right - left) / 2;
            if (node->keys[mid].word == keyword) 
            {
                return node->keys[mid].paragraphs;
            } 
            else if (node->keys[mid].word < keyword) 
            {
                left = mid + 1;
            } 
            else 
            {
                right = mid - 1;
            }
        }

        // Si no es hoja, buscar en el hijo correspondiente
        if (!node->isLeaf) 
        {
            int childIndex = left;
            if (left > 0 && node->keys[left - 1].word < keyword) 
            {
                childIndex = left - 1;
            }
            return findKeyword(node->children[childIndex], keyword);
        }

        return std::vector<Paragraph>();
    }

    // Imprime el arbol
    void printNode(BTreeNode* node) 
    {
        if (node != nullptr) 
        {
            for (int i = 0; i < node->keys.size(); i++) {
                std::cout << node->keys[i].paragraphs[0].paragraph << " ";
                
            }
            std::cout << std::endl;

            if (!node->isLeaf) 
            {
                for (int i = 0; i < node->children.size(); i++) {
                    printNode(node->children[i]);
                }
            }
        }
    }

public:

    // Constructor
    BTree() : root(nullptr) {}

    void insert(const std::string& keywords, int id, int page, const std::string& paragraph) 
    {
        // Si el arbol esta vacio, crear nodo raiz
        if (root == nullptr) {
            root = new BTreeNode(true);
            Clave newKey(keywords);
            newKey.paragraphs.push_back(Paragraph(id, page, paragraph));
            root->keys.push_back(newKey);
        } 
        else // Si no, insertar clave en el arbol
        {
            if (root->keys.size() == maxKeys) // Si la raiz esta llena, hacer split
            {
                BTreeNode* newRoot = new BTreeNode(false);
                newRoot->children.push_back(root);
                splitChild(newRoot, 0, root);
                root = newRoot;
            }
            if (keywords == root->keys[0].word) // Si la clave ya existe, insertar el parrafo en la clave
            {
                root->keys[0].paragraphs.push_back(Paragraph(id, page, paragraph));
            } 
            else // Si no, insertar clave en el arbol
            {
                insertNonFull(root, keywords, id, page, paragraph);
            }
        }
    }

    std::vector<Paragraph> searchKeyword(const std::string& keyword) 
    {
        return findKeyword(root, keyword);
    }

    void print() 
    {
        printNode(root);
    }

};

#endif // BTREE_H
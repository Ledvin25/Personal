#include <iostream>
#include <vector>
#include "BTree.h"

int main() {
    BTree btree;
    btree.insert("apple", 1, 1, "applasdasde");
    btree.insert("apple", 2, 2, "applebanana");
    btree.insert("banana", 2, 2, "banasdasdana");
    btree.insert("cherry", 3, 3, "cherrysdasd");
    btree.insert("date", 4, 4, "datesdasd");
    btree.insert("elderberry", 5, 5, "elderberry");
    btree.insert("fig", 6, 6, "figsdasd");
    btree.insert("grape", 7, 7, "grapesdasd");
    btree.insert("honeydew", 8, 8, "honeydewsdasd");
    btree.insert("aa", 9, 9, "aasdasd");

    //btree.print();

    std::vector<Paragraph> paragraphs = btree.searchKeyword("apple");

    for (auto paragraph : paragraphs) {
        std::cout << paragraph.id << " " << paragraph.page << " " << paragraph.paragraph << std::endl;
    }

    return 0;
}

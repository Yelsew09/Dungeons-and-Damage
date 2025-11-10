#include <iostream>
#include <vector>

#ifndef _CLASSES_MAIN
#define _CLASSES_MAIN

class Player{
    public:
    int stats[10];
    int items[5];
    std::string passive;
    std::string activated;
    Player(int[10], int[5], std::string, std::string);
    void damage(int);
    void heal(int);
    void next_turn();
};

class Knight: public Player{
    public:
};

#endif
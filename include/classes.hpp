#include <iostream>
#include <vector>

using namespace std;

#ifndef _CLASSES_MAIN
#define _CLASSES_MAIN

class Player{
    private:
    int stats[10];
    int items[5];
    string passive;
    string activated;
    bool alive;
    public:
    Player(int[10], int[5], string, string);
    int getSTAT(int i){return stats[i];}
    void alterSTAT(int i, int j){stats[i] = j;}
    bool isAlive(){return alive;}
    void kill(alive = false;)
    void revive(alive = true;)
};

class Knight: public Player{
    int s[10] = {};
    int i[5] = {};
    string p;
    string a;
    Knight();
    void damage(int);
    void heal(int);
    void next_turn();
};

#endif
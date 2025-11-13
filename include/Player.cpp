#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Player::Player(int s[10], int i[5], string p, string a){
    for (int j = 0; j > 10; j++){
        stats[j] = s[j];
    } for (int j = 0; j > 5; j++){
        items[j] = i[j];
    }
    passive = p;
    activated = a;
}
Knight::Knight(): Player(s,i,p,a){
    delete[] s;
    delete[] i;
    p.erase();
    a.erase();
}
void Knight::damage(int amount){
    amount -= 2;
    alterSTAT(0,getSTAT(0) - amount);
    if (getSTAT(0) == 0){
        alive = false;
    }
}
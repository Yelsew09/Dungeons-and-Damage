#include <iostream>
#include <vector>
#include <random>

#include "classes.hpp"

using namespace std;

Knight::Knight(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Knight::damage(int amount){
    amount -= 2;
    stats[0] -= amount;
    dead = (stats[CURRENT_HP] <= 0);
}
#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Mage::Mage(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Mage::next_turn(){
    Player::next_turn();
    stats[MAX_MP] += (stats[MAX_MP] < 13) ? 2 : 0;
}
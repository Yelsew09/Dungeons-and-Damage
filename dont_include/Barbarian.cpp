#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;
Barbarian::Barbarian(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Barbarian::heal(int amount){Player::heal(amount * 2);}
void Barbarian::next_turn(){
    heal(2);
    Player::next_turn();
}
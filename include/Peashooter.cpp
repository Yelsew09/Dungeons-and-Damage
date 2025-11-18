#include <iostream>
#include <vector>
#include <random>

#include "classes.hpp"

using namespace std;

Peashooter::Peashooter(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Peashooter::next_turn(){
    Player::next_turn();
    effects.dmgBON += (stats[CURRENT_MP] == stats[MAX_MP]) ? 2 : 0;
}
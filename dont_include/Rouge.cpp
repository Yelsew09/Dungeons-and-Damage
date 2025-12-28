#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Rouge::Rouge(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Rouge::next_turn(){
    Player::next_turn();
    stats[SPEED] += (stats[SPEED] < 9) ? 1 : 0;
}
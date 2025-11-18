#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Bard::Bard(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Bard::next_turn(){
    Player::next_turn();
    // I need the command system to have this work
}
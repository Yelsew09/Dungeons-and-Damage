#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Narrator::Narrator(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Narrator::damage(int amount){Player::damage(0);}
void Narrator::heal(int amount){stats[CURRENT_HP] = stats[MAX_HP];}
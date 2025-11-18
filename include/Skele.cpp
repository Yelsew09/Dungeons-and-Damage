#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Skele::Skele(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Skele::damage(int amount){Player::damage((amount >= 15) ? 0 : amount);}
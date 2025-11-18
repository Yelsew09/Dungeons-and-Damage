#include <iostream>
#include <vector>
#include <random>

#include "classes.hpp"

using namespace std;

Peashooter::Peashooter(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Peashooter::next_turn(){
    if (effects.adtr > 0){
        effects.adtr--;
        effects.adv = (effects.adtr == 0) ? 0 : effects.adv;
    }
    stats[CURRENT_MP] += stats[MP_REFRESH];
    stats[CURRENT_MP] = (stats[CURRENT_MP] > stats[MAX_MP]) ? stats[MAX_MP] : stats[CURRENT_MP];
    effects.dmgBON += (stats[CURRENT_MP] == stats[MAX_MP]) ? 2 : 0;
}
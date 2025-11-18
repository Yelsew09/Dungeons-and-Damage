#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Rouge::Rouge(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Rouge::damage(int amount){
    stats[CURRENT_HP] -= amount;
    dead = (stats[CURRENT_HP] <= 0);
}
void Rouge::heal(int amount){
    stats[CURRENT_HP] += amount;
    stats[CURRENT_HP] = (stats[CURRENT_HP] > stats[MAX_HP]) ? stats[MAX_HP] : stats[CURRENT_HP];
}
void Rouge::next_turn(){
    if (effects.adtr > 0){
        effects.adtr--;
        effects.adv = (effects.adtr == 0) ? 0 : effects.adv;
    }
    stats[SPEED] += (stats[SPEED] < 9) ? 1 : 0;
    stats[CURRENT_MP] += stats[MP_REFRESH];
    stats[CURRENT_MP] = (stats[CURRENT_MP] > stats[MAX_MP]) ? stats[MAX_MP] : stats[CURRENT_MP];
}
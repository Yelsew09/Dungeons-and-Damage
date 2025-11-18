#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Peashooter::Peashooter(int s[10], int i[5], string p, string a): Player(s, i, p, a){}
void Peashooter::damage(int amount){
    stats[CURRENT_HP] -= amount;
    dead = (stats[CURRENT_HP] <= 0);
}
void Peashooter::heal(int amount){
    stats[CURRENT_HP] += amount;
    stats[CURRENT_HP] = (stats[CURRENT_HP] > stats[MAX_HP]) ? stats[MAX_HP] : stats[CURRENT_HP];
}
void Peashooter::next_turn(){
    if (effects.adtr > 0){
        effects.adtr--;
        effects.adv = (effects.adtr == 0) ? 0 : effects.adv;
    }
    stats[CURRENT_MP] += stats[MP_REFRESH];
    stats[CURRENT_MP] = (stats[CURRENT_MP] > stats[MAX_MP]) ? stats[MAX_MP] : stats[CURRENT_MP];
    effects.dmgBON += (stats[CURRENT_MP] == stats[MAX_MP]) ? 2 : 0;
}
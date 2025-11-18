#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Knight::Knight(int s[10], short i[5], string p, string a): Player(s, i, p, a){}
void Knight::damage(int amount){
    amount -= 2;
    stats[0] -= amount;
    dead = (stats[CURRENT_HP] <= 0);
}
void Knight::heal(int amount){
    stats[0] += amount;
    stats[0] = (stats[CURRENT_HP] > stats[MAX_HP]) ? stats[MAX_HP] : stats[CURRENT_HP];
}
void Knight::next_turn(){
    if (effects.adtr > 0){
        effects.adtr--;
        effects.adv = (effects.adtr == 0) ? 0 : effects.adv;
    }
    stats[CURRENT_MP] += stats[MP_REFRESH];
    stats[CURRENT_MP] = (stats[CURRENT_MP] > stats[MAX_MP]) ? stats[MAX_MP] : stats[CURRENT_MP];
}
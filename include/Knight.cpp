#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Knight::Knight(int s[10], int i[5], string p, string a): Player(s, i, p, a){}
void Knight::damage(int amount){
    amount -= 2;
    stats[0] -= amount;
    dead = (getHP() <= 0);
}
void Knight::heal(int amount){
    stats[0] += amount;
    stats[0] = (getHP() > stats[1]) ? stats[1] : stats[0];
}
void Knight::next_turn(){
    if (effects.adtr > 0){
        effects.adtr--;
        effects.adv = (effects.adtr == 0) ? 0 : effects.adv;
    }
    stats[5] += stats[7];
    stats[5] = (stats[5] > stats[6]) ? stats[6] : stats[5];
}
#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Player::Player(int s[10], int i[5], string p, string a){
    for (int j = 0; j < 10; j++){stats[j] = s[j];}
    for (int j = 0; j < 5; j++){items[j] = i[j];}
    passive = p;
    activated = a;
}

void Player::damage(int amount){
    stats[CURRENT_HP] -= amount;
    dead = stats[CURRENT_HP] <= 0;
}

void Player::heal(int amount){
    stats[CURRENT_HP] += amount;
    stats[CURRENT_HP] = (stats[CURRENT_HP] > stats[MAX_HP]) ? stats[MAX_HP] : stats[CURRENT_HP];
}

void Player::next_turn(){
    if (effects.adtr > 0){
        effects.adtr--;
        effects.adv = (effects.adtr == 0) ? 0 : effects.adv;
    }
    stats[CURRENT_MP] += stats[MP_REFRESH];
    stats[CURRENT_MP] = (stats[CURRENT_MP] > stats[MAX_MP]) ? stats[MAX_MP] : stats[CURRENT_MP];
}
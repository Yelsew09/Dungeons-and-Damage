#include <iostream>
#include <vector>
#include <random>

#include "classes.hpp"

using namespace std;

Player::Player(array<int32_t, 10> s, array<int16_t, 5> i, vector<string> o, vector<string> l, string p, string a): stats(s), items(i), options(o), spells(l), passive(p), activated(a){}
void Player::damage(int32_t amount){
    stats[CURRENT_HP] -= amount;
    dead = (stats[CURRENT_HP] <= 0);
}
void Player::heal(int32_t amount){
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
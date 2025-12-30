#include <iostream>
#include <vector>
#include <random>

#include "classes.hpp"

using namespace std;

// Oh boy I love this new thing that I already forgot the name of
Player::Player(array<int32_t, 10> s, array<int16_t, 5> i, vector<string> o, vector<string> l, string p, string a): stats(s), items(i), options(o), spells(l), passive(p), activated(a){}

// Subtract health from the player and change dead to match being over 0HP
void Player::damage(int32_t amount){
    stats[CURRENT_HP] -= amount;
    dead = (stats[CURRENT_HP] <= 0);
}

// Add health to the player and don't let it go over its max HP
void Player::heal(int32_t amount){
    stats[CURRENT_HP] += amount;
    stats[CURRENT_HP] = (stats[CURRENT_HP] > stats[MAX_HP]) ? stats[MAX_HP] : stats[CURRENT_HP];
}

// Advance to the next turn
void Player::next_turn(){
    if (effects.adtr > 0){
        effects.adtr--;
        effects.adv = (effects.adtr == 0) ? 0 : effects.adv;
    }
    stats[CURRENT_MP] += stats[MP_REFRESH];
    stats[CURRENT_MP] = (stats[CURRENT_MP] > stats[MAX_MP]) ? stats[MAX_MP] : stats[CURRENT_MP];
}

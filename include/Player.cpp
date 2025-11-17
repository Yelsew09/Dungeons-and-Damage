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
    stats[0] -= amount;
    dead = stats[0] <= 0;
}

void Player::heal(int amount){
    stats[0] += amount;
    stats[0] = (getHP() > stats[1]) ? stats[1] : stats[0];
}

void Player::next_turn(){
    if (effects.adtr > 0){
        effects.adtr--;
        effects.adv = (effects.adtr == 0) ? 0 : effects.adv;
    }
    stats[5] += stats[7];
    stats[5] = (stats[5] > stats[6]) ? stats[6] : stats[5];
}
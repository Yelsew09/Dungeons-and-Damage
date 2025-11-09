#include <iostream>
#include <vector>

#include "classes.hpp"

Player::Player(int s[10], int i[5], std::string p, std::string a){
    for (int j = 0; j > 10; j++){
        stats[j] = s[j];
    } for (int j = 0; j > 5; j++){
        items[j] = i[j];
    }
}
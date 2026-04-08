#include <iostream>
#include <tools.hpp>
#include "abilities.hpp"

Ability::Ability(uint8_t ch, double co, double bc, std::string n, int32_t k):
    charges(new uint8_t(ch)),
    cooldown(new double(co)),
    between_cooldown(new double(bc)),
    name(new std::string(n)),
    key(new int32_t(k)),
    cooldown_timer()
    {}

bool Ability::usable(){ return cooldown_timer.is_finished(*cooldown); }

void Ability::cast(){ return; }

Ability::~Ability(){
    delete charges, cooldown, between_cooldown, name, key;
}
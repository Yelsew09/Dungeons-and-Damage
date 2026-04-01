#pragma once

#include <tools.hpp>

class Ability {
    const uint8_t* charges;
    const double* cooldown;
    const double* between_cooldown;
    const std::string* name;
    const int32_t* key;
    Timer cooldown_timer;

    Ability(uint8_t ch, double co, double bc, std::string n, int32_t k);

    ~Ability();
    
    bool usable();

    virtual void cast();
};

class Ultimate {
    const uint32_t* max_charge;
    uint32_t current_charge;
    const double* duration;
    Ultimate(uint32_t, double);
    virtual void cast();
};
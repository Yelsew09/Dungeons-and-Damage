#include <iostream>
#include <chrono>
#include <tools.hpp>
#include "abilities.hpp"

Ultimate::Ultimate(uint32_t mc, double du):
    max_charge(new uint32_t(mc)),
    duration(new double(du))
    {}

void Ultimate::cast(){
    return;
}
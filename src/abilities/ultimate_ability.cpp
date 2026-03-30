#include <iostream>
#include <chrono>
#include "inclusions.hpp"
#include "abilities.hpp"

Ultimate::Ultimate(uint32_t mc, double du):
    max_charge(new uint32_t(mc)),
    duration(new double(du))
    {}
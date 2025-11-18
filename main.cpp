#include <iostream>
#include <vector>
#include <random>

#include "include/classes.hpp"

using namespace std;

std::random_device rd;
std::mt19937 gen(rd());

int main(){
    confirm("If you are new to this game, please consult the guide");
    return 0;
}
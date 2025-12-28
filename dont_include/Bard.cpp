#include <iostream>
#include <vector>

#include "classes.hpp"

using namespace std;

Bard::Bard(int s[10], short i[5], vector<string> o, vector<string> l, string p, string a):
Player(s, i, o, l, p, a){}
void Bard::next_turn(){
    Player::next_turn();
    confirm("As a bard, you can select multiple different sets of stats to fit your playstyle.");
    while (true){
        vector<string> usable_list = {
            "Offensive",
            "Defensive",
            "Utility",
            "Magical",
            "All-Rounded"
        };
        string option = roll_list(usable_list, "What set would you like to use?");
    }
}
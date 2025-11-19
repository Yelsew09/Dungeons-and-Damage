#include <iostream>
#include <vector>
#include <random>

#include "include/classes.hpp"

using namespace std;

std::random_device rd;
std::mt19937 gen(rd());

int main(){
    vector<string> current_options;
    string selected_option;
    confirm("If you are new to this game, please consult the guide");
    roll("Welcome to Dungeons and Damage!");
    wait(.5);
    roll("Not to be confused with Dungeons and Dragons.");
    wait(.5);
    roll("Although this game does feel like it.");
    wait(.5);
    roll("After some time, the not awaited c++ version of the game is released, and this is it.");
    wait(.5);
    current_options = {
        "Game Start",
        "Guide",
        "Options",
        "Quit"
    };
    selected_option = roll_list(current_options, "");
    if (selected_option == "Game Start"){
        // Start the game
    } else if (selected_option == "Guide"){
        // Initiate the guide
    } else if (selected_option == "Options"){
        // Display options menu
    } else if (selected_option == "Quit"){
        return 0;
    } else {
        roll("Please select a valid option\n");
        wait(.5);
    }
    return 0;
}
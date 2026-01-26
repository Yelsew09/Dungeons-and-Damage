#include <iostream>
#include <vector>
#include <random>
#include <array>

#include "include/classes.hpp"

using namespace std;

random_device rd;
mt19937 gen(rd());
bool debug = false;
vector<string> options;
string selected_option;

int main(){
    bool game_correct;
    roll("Welcome to Dungeons and Damage.\n"); wait(500);
    roll("Not to be confused with Dungeons and Dragons.\n"); wait(500);
    roll("Although they do feel very similar.\n"); wait(500);
    game_correct = true;
    while (game_correct){
        options = {
            "Game Start\n",
            "Options\n",
            "Guide\n",
            "Quit\n"
        };
        selected_option = roll_list(options, "Please select and option: ", (bool*)true);
        if (selected_option == "Options\n"){
            roll("Option menu coming soon\n"); wait();
        } else if (selected_option == "Guide\n"){
            roll("Guide coming soon\n"); wait();
        } else if (selected_option == "Quit\n"){
            game_correct = false;
        } else if (selected_option == "Game Start\n"){
            // Start the game. I'm going to bed now
        }
    }
    return 0;
}
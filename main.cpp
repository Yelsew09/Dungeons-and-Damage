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
uint32_t players;
string option;

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
            bool player_correct = true;
            while (player_correct){
                players = ask("How many players are there? (2 or 4)");
                if (players != 2 && players != 4){ roll("Please select 2 or 4"); wait(500); }
                else { player_correct = false; }
            }
            
        }
    }
    return 0;
}
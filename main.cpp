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

vector<Player> turn_order;

Player create_player(string type){
    if (type == "Knight") return Player(KNIGHT_STATS, KNIGHT_ITEMS, KNIGHT_OPTIONS, KNIGHT_SPELLS, KNIGHT_PASSIVE, KNIGHT_ACTIVATED);
    else if (type == "Peashooter") return Player(PEASHOOTER_STATS, PEASHOOTER_ITEMS, PEASHOOTER_OPTIONS, PEASHOOTER_SPELLS, PEASHOOTER_PASSIVE, PEASHOOTER_ACTIVATED);
    else if (type == "Rouge") return Player(ROUGE_STATS, ROUGE_ITEMS, ROUGE_OPTIONS, ROUGE_SPELLS, ROUGE_PASSIVE, ROUGE_ACTIVATED);
    else if (type == "Mage") return Player(MAGE_STATS, MAGE_ITEMS, MAGE_OPTIONS, MAGE_SPELLS, MAGE_PASSIVE, MAGE_ACTIVATED);
    else if (type == "Skele") return Player(SKELE_STATS, SKELE_ITEMS, SKELE_OPTIONS, SKELE_SPELLS, SKELE_PASSIVE, SKELE_ACTIVATED);
    else if (type == "Bard") return Player(BARD_STATS, BARD_ITEMS, BARD_OPTIONS, BARD_SPELLS, BARD_PASSIVE, BARD_ACTIVATED);
    else if (type == "Barbarian") return Player(BARBARIAN_STATS, BARBARIAN_ITEMS, BARBARIAN_OPTIONS, BARBARIAN_SPELLS, BARBARIAN_PASSIVE, BARBARIAN_ACTIVATED);
    return Player();
}

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
                players = ask("How many players are there? (this is here for future updates. The only accepted option is 2 atm)");
                if (players != 2){ roll("Please select 2"); wait(500); }
                else { player_correct = false; }
            }
            for (uint8_t i = 1; i <= players; i++){
                bool random_correct = true;
                options = {
                    "Knight\n",
                    "Peashooter\n",
                    "Rouge\n",
                    "Mage\n",
                    "Skele\n",
                    "Bard\n",
                    "Barbarian\n",
                    "Custom\n",
                    "Random\n"
                };
                while (random_correct){
                    option = roll_list(options, "Player " + to_string(i) + ", please select a character", false, true, (bool*)false);
                    if (option == "Knight\n"){
                        turn_order.push_back(Player(KNIGHT_STATS, KNIGHT_ITEMS, KNIGHT_OPTIONS, KNIGHT_SPELLS, KNIGHT_PASSIVE, KNIGHT_ACTIVATED));
                    }
                }
            }
        }
    }
    return 0;
}
#include <iostream>
#include <vector>
#include <random>
#include <array>
#include <unordered_map>

using namespace std;

#ifndef _CLASSES_MAIN
#define _CLASSES_MAIN

struct Effects{
    int32_t adv;
    int32_t adtr;
    int32_t dmgBON;
    int32_t ability_cooldown_current;
    int32_t ability_cooldown;
};

void clearOutput();
void roll(string text, uint32_t delay = 20, bool = true);
void wait(uint32_t time = 150);
void confirm(string, uint32_t = 500);
uint32_t ask(string = "What would you like to do? ", uint32_t = 500);
string roll_list(
    vector<string>, // options
    string = "What would you like to do? ", // asking
    bool = true, // clear
    bool = true, // contains_newlines
    bool* = nullptr, // withback
    uint32_t = 500, // r_delay
    uint32_t = 150  // l_delay
);
int64_t random_num(int64_t, int64_t, bool);
bool yes_or_no(string, uint32_t = 500);
void crash(string);

// Stat Macros
#define MAX_HP (int8_t) 0
#define ATTACK (int8_t) 1
#define ATTACK_BONUS (int8_t) 2
#define DEFENSE (int8_t) 3
#define MAX_MP (int8_t) 4
#define MP_REFRESH (int8_t) 5
#define ITEM_USES (int8_t) 6
#define SPEED (int8_t) 7

// Item Macros
#define SPOON (int8_t) 0
#define KNIVE (int8_t) 1
#define POTION (int8_t) 2
#define FENCE (int8_t) 3
#define DEAGLE (int8_t) 4

#define KNIGHT_STATS (array<int32_t, 8>){35,7,5,16,5,3,2,3}
#define KNIGHT_ITEMS (array<int16_t, 5>){3,3,3,1,0}
#define KNIGHT_PASSIVE (string) "Endure"
#define KNIGHT_ACTIVATED (string) "Smite the Pathetic"
#define KNIGHT_OPTIONS (vector<string>){"Attack", "Cast", "Item", "Pass", "Forfiet"}
#define KNIGHT_SPELLS (vector<string>){""}
#define KNIGHT_DATA (unordered_map<string, int32_t>){ {"Ab1Cool", 3} }

#define PEASHOOTER_STATS (array<int32_t, 8>){26,9,4,14,7,3,3,5}
#define PEASHOOTER_ITEMS (array<int16_t, 5>){1,1,1,1,0}
#define PEASHOOTER_PASSIVE (string) "Charge"
#define PEASHOOTER_ACTIVATED (string) "Photosynthesis B*tch"
#define PEASHOOTER_OPTIONS (vector<string>){"Attack", "Cast", "Item", "Pass", "Forfeit"}
#define PEASHOOTER_SPELLS (vector<string>){""}
#define PEASHOOTER_DATA (unordered_map<string, int32_t>){ {"Ab1Cool", 5} }

#define ROUGE_STATS (array<int32_t, 8>){20,10,3,13,6,2,7,4}
#define ROUGE_ITEMS (array<int16_t, 5>){1,5,3,2,0}
#define ROUGE_PASSIVE (string) "Evade"
#define ROUGE_ACTIVATED (string) "Nuh uh"
#define ROUGE_OPTIONS (vector<string>){""}
#define ROUGE_SPELLS (vector<string>){""}
#define ROUGE_DATA (unordered_map<string, int32_t>){ {"Ab1Cool", 5} }

#define MAGE_STATS (array<int32_t, 8>){21,5,2,11,5,2,2,4}
#define MAGE_ITEMS (array<int16_t, 5>){2,2,3,1,0}
#define MAGE_PASSIVE (string) "Hone"
#define MAGE_ACTIVATED (string) "I don't care how big the room is"
#define MAGE_OPTIONS (vector<string>){""}
#define MAGE_SPELLS (vector<string>){""}

#define SKELE_STATS (array<int32_t, 8>){30,7,3,12,7,5,4,6}
#define SKELE_ITEMS (array<int16_t, 5>){3,4,0,0,0}
#define SKELE_PASSIVE (string) "Focus"
#define SKELE_ACTIVATED (string) "Dry Bones"
#define SKELE_OPTIONS (vector<string>){""}
#define SKELE_SPELLS (vector<string>){""}

#define BARD_STATS (array<int32_t, 8>){27,6,4,14,4,2,5,2}
#define BARD_ITEMS (array<int16_t, 5>){3,2,2,1,0}
#define BARD_PASSIVE (string) "Adapt"
#define BARD_ACTIVATED (string) "1d4 Psychic Damage"
#define BARD_OPTIONS (vector<string>){""}
#define BARD_SPELLS (vector<string>){""}
//
#define BARD_DEFAULT_STATS BARD_STATS
#define BARD_OFFENSIVE_STATS (array<int32_t, 8>){20,10,4,12,5,2,3,2}
#define BARD_DEFENSIVE_STATS (array<int32_t, 8>){30,3,4,17,4,2,3,2}
#define BARD_SUBSIDIARY_STATS (array<int32_t, 8>){25,4,4,14,2,1,8,2}
#define BARD_MAGICAL_STATS (array<int32_t, 8>){25,2,2,13,8,3,3,2}

#define BARBARIAN_STATS (array<int32_t, 8>){40,12,2,15,2,1,1,1}
#define BARBARIAN_ITEMS (array<int16_t, 5>){4,2,2,0,0}
#define BARBARIAN_PASSIVE (string) "Regenerate"
#define BARBARIAN_ACTIVATED (string) "Rage"
#define BARBARIAN_OPTIONS (vector<string>){""}
#define BARBARIAN_SPELLS (vector<string>){"Cast Iron"}

#define NARRATOR_STATS (array<int32_t, 8>){2^31-1,2^31-1,2^31-1,2^31-1,2^31-1,2^31-1,2^31-1,2^31-1}
#define NARRATOR_ITEMS (array<int16_t, 5>){32767,32767,32767,32767,32767}
#define NARRATOR_PASSIVE (string) "Godlike"
#define NARRATOR_ACTIVATED (string) "You must die"
#define NARRATOR_OPTIONS (vector<string>){""}
#define NARRATOR_SPELLS (vector<string>){""}

class Player{
    public:
    array<int32_t, 8> stats;
    array<int16_t, 5> items;
    vector<string> options;
    vector<string> spells;
    int32_t current_hp, current_mp;
    string passive;
    string activated;
    string classname;
    Effects effects;
    bool dead = false;
    Player(array<int32_t, 8>, array<int16_t, 5>, vector<string>, vector<string>, string, string);
    Player();
    void damage(int32_t, string);
    void heal(int32_t);
    void next_turn();
    void take_turn(Player&);
};

#endif
#include <iostream>
#include <vector>
#include <random>

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

void roll(string text, int32_t delay = 20, bool = true);
void wait(int32_t time = 500);
void confirm(string, int32_t = 500);
int32_t ask(string = "What would you like to do? ", int32_t = 500);
string roll_list(vector<string>, string = "What would you like to do? ", int32_t = 500, bool = true, int32_t = 150);
int64_t random_num(int64_t, int64_t, bool);
bool yes_or_no(string, int32_t = 500);
void crash(string);

#define CURRENT_HP (int8_t) 0
#define MAX_HP (int8_t) 1
#define ATTACK (int8_t) 2
#define ATTACK_BONUS (int8_t) 3
#define DEFENSE (int8_t) 4
#define CURRENT_MP (int8_t) 5
#define MAX_MP (int8_t) 6
#define MP_REFRESH (int8_t) 7
#define ITEM_USES (int8_t) 8
#define SPEED (int8_t) 9

#define KNIGHT_STATS (int32_t[10]){35,35,7,5,16,5,5,3,2,3}
#define KNIGHT_ITEMS (int16_t[5]) {3,3,3,1,0}
#define KNIGHT_PASSIVE (string) "Fortitude"
#define KNIGHT_ACTIVATED (string) ""
#define KNIGHT_EFFECTS (Effects){0,0,0,0,0}
#define KNIGHT_OPTIONS (vector<string>) {"Attack", "Magic", "Item", "Pass", "Run"}

#define PEASHOOTER_STATS (int32_t[10]) {26,26,9,4,14,7,7,3,3,5}
#define PEASHOOTER_ITEMS (int16_t[5]){1,1,1,1,0}
#define PEASHOOTER_PASSIVE (string) "Charge"
#define PEASHOOTER_ACTIVATED (string) ""
#define PEASHOOTER_EFFECTS (Effects){0,0,0,0,0}

#define MAGE_STATS (int32_t[10]){21,21,5,2,11,5,5,2,2,4};
#define MAGE_ITEMS (int16_t[5]){2,2,3,1,0};
#define MAGE_PASSIVE (string) "Zoning In";
#define MAGE_ACTIVATED (string) "";
#define MAGE_EFFECTS (Effects){0,0,0,0,0};

#define SKELE_STATS (int32_t[10]){30,30,7,3,12,7,7,5,4,6};
#define SKELE_ITEMS (int16_t[5]){3,4,0,0,0};
#define SKELE_PASSIVE (string) "Resilient";
#define SKELE_ACTIVATED (string) "";
#define SKELE_EFFECTS (Effects){0,0,0,0,0};

#define BARD_STATS (int32_t[10]){27,27,6,4,14,4,4,2,5,2};
#define BARD_ITEMS (int16_t[5]){3,2,2,1,0};
#define BARD_PASSIVE (string) "Jack of all Trades";
#define BARD_ACTIVATED (string) "";
#define BARD_EFFECTS (Effects){0,0,0,0,0};

#define BARBARIAN_STATS (int32_t[10]){40,40,12,2,15,2,2,1,1,1};
#define BARBARIAN_ITEMS (int16_t[5]){4,2,2,0,0};
#define BARBARIAN_PASSIVE (string) "Rage";
#define BARBARIAN_ACTIVATED (string) "";
#define BARBARIAN_EFFECTS (Effects){0,0,0,0,0};

#define NARRATOR_STATS (int32_t[10]){2147483647,2147483647,2147483647,2147483647,2147483647,2147483647,2147483647,2147483647,2147483647,2147483647};
#define NARRATOR_ITEMS (int16_t[5]){32767,32767,32767,32767,32767};
#define NARRATOR_PASSIVE (string) "Godlike";
#define NARRATOR_ACTIVATED (string) "You must die";
#define NARRATOR_EFFECTS (Effects){0,0,0,0,0};

class Player{
    public:
    array<int32_t, 10> stats;
    array<int16_t, 5> items;
    vector<string> options;
    vector<string> spells;
    string passive;
    string activated;
    Effects effects;
    bool dead = false;
    Player(array<int32_t, 10>, array<int16_t, 5>, vector<string>, vector<string>, string, string);
    void damage(int32_t);
    void heal(int32_t);
    void next_turn();
    void take_turn(Player&);
};

#endif
#include <iostream>
#include <vector>
#include <random>

using namespace std;

#ifndef _CLASSES_MAIN
#define _CLASSES_MAIN

struct Effects{
    int adv;
    int adtr;
    int dmgBON;
    int ability_cooldown_current;
    int ability_cooldown;
};

#define CURRENT_HP (int) 0
#define MAX_HP (int) 1
#define ATTACK (int) 2
#define ATTACK_BONUS (int) 3
#define DEFENSE (int) 4
#define CURRENT_MP (int) 5
#define MAX_MP (int) 6
#define MP_REFRESH (int) 7
#define ITEM_USES (int) 8
#define SPEED (int) 9

#define KNIGHT_STATS (int[10]){35,35,7,5,16,5,5,3,2,3}
#define KNIGHT_ITEMS (short[5]) {3,3,3,1,0}
#define KNIGHT_PASSIVE (string) "Fortitude"
#define KNIGHT_ACTIVATED (string) ""
#define KNIGHT_EFFECTS (Effects){0,0,0,0,0}
#define KNIGHT_OPTIONS (vector<string>) {"Attack", "Magic", "Item", "Pass", "Run"}


#define PEASHOOTER_STATS (int[10]) {26,26,9,4,14,7,7,3,3,5}
#define PEASHOOTER_ITEMS (short[5]){1,1,1,1,0}
#define PEASHOOTER_PASSIVE (string) "Charge"
#define PEASHOOTER_ACTIVATED (string) ""
#define PEASHOOTER_EFFECTS (Effects){0,0,0,0,0}

#define MAGE_STATS (int[10]){21,21,5,2,11,5,5,2,2,4};
#define MAGE_ITEMS (short[5]){2,2,3,1,0};
#define MAGE_PASSIVE (string) "Zoning In";
#define MAGE_ACTIVATED (string) "";
#define MAGE_EFFECTS (Effects){0,0,0,0,0};

#define SKELE_STATS (int[10]){30,30,7,3,12,7,7,5,4,6};
#define SKELE_ITEMS (short[5]){3,4,0,0,0};
#define SKELE_PASSIVE (string) "Resilient";
#define SKELE_ACTIVATED (string) "";
#define SKELE_EFFECTS (Effects){0,0,0,0,0};

#define BARD_STATS (int[10]){27,27,6,4,14,4,4,2,5,2};
#define BARD_ITEMS (short[5]){3,2,2,1,0};
#define BARD_PASSIVE (string) "Jack of all Trades";
#define BARD_ACTIVATED (string) "";
#define BARD_EFFECTS (Effects){0,0,0,0,0};

#define BARBARIAN_STATS (int[10]){40,40,12,2,15,2,2,1,1,1};
#define BARBARIAN_ITEMS (short[5]){4,2,2,0,0};
#define BARBARIAN_PASSIVE (string) "Rage";
#define BARBARIAN_ACTIVATED (string) "";
#define BARBARIAN_EFFECTS (Effects){0,0,0,0,0};

#define NARRATOR_STATS (int[10]){2147483647,2147483647,2147483647,2147483647,2147483647,2147483647,2147483647,2147483647,2147483647,2147483647};
#define NARRATOR_ITEMS (short[5]){32767,32767,32767,32767,32767};
#define NARRATOR_PASSIVE (string) "Godlike";
#define NARRATOR_ACTIVATED (string) "You must die";
#define NARRATOR_EFFECTS (Effects){0,0,0,0,0};

class Player{
    public:
    int stats[10];
    short items[5];
    vector<string> options;
    vector<string> spells;
    string passive;
    string activated;
    Effects effects;
    bool dead = false;
    Player(int[10], short[5], vector<string>, vector<string>, string, string);
    virtual void damage(int);
    virtual void heal(int);
    virtual void next_turn();
};

class Knight: public Player{
    public:
    Knight(int[10], short[5], vector<string>, vector<string>, string, string);
    void damage(int) override;
    using Player::heal;
    using Player::next_turn;
};

class Peashooter: public Player{
    public:
    Peashooter(int[10], short[5], vector<string>, vector<string>, string, string);
    using Player::damage;
    using Player::heal;
    void next_turn() override;
};

class Rouge: public Player{
    public:
    Rouge(int[10], short[5], vector<string>, vector<string>, string, string);
    using Player::damage;
    using Player::heal;
    void next_turn() override;
};

class Mage: public Player{
    public:
    Mage(int[10], short[5], vector<string>, vector<string>, string, string);
    using Player::damage;
    using Player::heal;
    void next_turn() override;
};

class Skele: public Player{
    public:
    Skele(int[10], short[5], vector<string>, vector<string>, string, string);
    void damage(int) override;
    using Player::heal;
    using Player::next_turn;
};

class Bard: public Player{
    public:
    Bard(int[10], short[5], vector<string>, vector<string>, string, string);
    using Player::damage;
    using Player::heal;
    void next_turn() override;
};

class Barbarian: public Player{
    public:
    Barbarian(int[10], short[5], vector<string>, vector<string>, string, string);
    using Player::damage;
    void heal(int) override;
    void next_turn() override;
};

class Narrator: public Player{
    public:
    Narrator(int[10], short[5], vector<string>, vector<string>, string, string);
    void damage(int) override;
    void heal(int) override;
    using Player::next_turn;
};

#endif
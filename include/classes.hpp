#include <iostream>
#include <vector>

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

#define KNIGHT_STATS (int[10]){35,35,7,5,16,5,5,3,2,3}
#define KNIGHT_ITEMS (int[5]){3,3,3,1,0}
#define KNIGHT_PASSIVE (string)"Fortitude"
#define KNIGHT_ACTIVATED (string)""
#define KNIGHT_EFFECTS (Effects){0,0,0,0,0}

#define PEASHOOTER_STATS (int[10]){26,26,9,4,14,7,7,3,3,5}
#define PEASHOOTER_ITEMS (int[5]){1,1,1,1,0}
#define PEASHOOTER_PASSIVE (string)"Charge"
#define PEASHOOTER_ACTIVATED (string)""

#define CURRENT_HP (int) 0
#define MAX_HP (int) 1
#define ATTACK (int) 2
#define ATTACK_BONUS (int) 3
#define DEFENCE (int) 4
#define CURRENT_MP (int) 5
#define MAX_MP (int) 6
#define MP_REFRESH (int) 7
#define ITEM_USES (int) 8
#define SPEED (int) 9

/* Index values for stats are as follows:
    *  0: Current HP
    *  1: Maximum HP
    *  2: Attack damage
    *  3: Attack roll bonus
    *  4: Defence
    *  5: Current MP
    *  6: Maximum MP
    *  7: MP refresh
    *  8: Item Uses
    *  9: Speed
    */

class Player{
    public:
    int stats[10];
    int items[5];
    string passive;
    string activated;
    bool dead;
    Effects effects;
    Player(int[10], int[5], string, string);
    virtual void damage(int);
    virtual void heal(int) ;
    virtual void next_turn();
};

class Knight: public Player{
    Knight(int[10], int[5], string, string);
    void damage(int) override;
    void heal(int) override;
    void next_turn() override;
};

class Peashooter: public Player{
    Peashooter(int[10], int[5], string, string);
    void damage(int) override;
    void heal(int) override;
    void next_turn() override;
};

class Rouge: public Player{
    Rouge(int[10], int[5], string, string);
    void damage(int) override;
    void heal(int) override;
    void next_turn() override;
};

class Mage: public Player{
    Mage(int[10], int[5], string, string);
    void damage(int) override;
    void heal(int) override;
    void next_turn() override;
};

class Skele: public Player{
    Skele(int[10], int[5], string, string);
    void damage(int) override;
    void heal(int) override;
    void next_turn() override;
};

class Bard: public Player{
    Bard(int[10], int[5], string, string);
    void damage(int) override;
    void heal(int) override;
    void next_turn() override;
};

class Barbarian: public Player{
    Barbarian(int[10], int[5], string, string);
    void damage(int) override;
    void heal(int) override;
    void next_turn() override;
};

class Narrator: public Player{
    Narrator(int[10], int[5], string, string);
    void damage(int) override;
    void heal(int) override;
    void next_turn() override;
};

#endif
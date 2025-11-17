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

#define KNIGHT_STATS {35,35,7,5,16,5,5,3,2,3};
#define KNIGHT_ITEMS {3,3,3,1,0};
#define KNIGHT_PASSIVE "Fortitude";
#define KNIGHT_ACTIVATED "";
#define KNIGHT_EFFECTS (Effects){0,0,0,0,0};

#define PEASHOOTER_STATS {26,26,9,4,14,7,7,3,3,5};
#define PEASHOOTER_ITEMS {1,1,1,1,0};
#define PEASHOOTER_PASSIVE "Charge";
#define PEASHOOTER_ACTIVATED "";


class Player{
    public:
    int stats[10];
    int items[5];
    string passive;
    string activated;
    bool dead;
    Effects effects;
    Player(int[10], int[5], string, string);
    int getHP(){return stats[0];}
    void setHP(int i){stats[0] = i;}
    int getMaxHP(){return stats[1];}
    void setMaxHP(int i){stats[1] = i;}
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
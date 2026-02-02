#include <iostream>
#include <vector>
#include <random>
#include <array>

#include "classes.hpp"

using namespace std;

// Oh boy I love this new thing that I already forgot the name of
Player::Player(array<int32_t, 8> s, array<int16_t, 5> i, vector<string> o, vector<string> l, string p, string a):
stats(s), items(i), options(o), spells(l), passive(p), activated(a),
current_hp(s[MAX_HP]), current_mp(s[MAX_MP])
{}

// Subtract health from the player and change dead to match being over 0HP
void Player::damage(int32_t amount){
    if (passive == KNIGHT_PASSIVE){
        if (amount < 0) amount--;
        else {
            amount -= 2;
            if (amount < 0) amount = 0;
        }
    }
    current_hp -= amount;
    dead = (current_hp <= 0);
}

// Add health to the player and don't let it go over its max HP
void Player::heal(int32_t amount){
    if (passive == BARBARIAN_PASSIVE) amount = ceil(amount * 1.5);
    current_hp += amount;
    if (current_hp > stats[MAX_HP]) current_hp = stats[MAX_HP];
}

// Advance to the next turn
void Player::next_turn(){
    string selected_option;
    if (passive == BARBARIAN_PASSIVE) heal(2);
    if (effects.adtr > 0){
        effects.adtr--;
        if (effects.adtr == 0) effects.adv = 0;
    }
    current_mp += stats[MP_REFRESH];
    if (current_mp > stats[MAX_MP]) current_mp = stats[MAX_MP];
    if (passive == BARD_PASSIVE){
        array<int32_t, 8> stat_block;
        while (true){
            options = {
                "Keep current stats\n",
                "Offensive\n",
                "Defensive\n",
                "Subsidiary\n",
                "Magical\n",
                "Well rounded (default)\n",
                "See current stats\n",
                "See stats of each\n"
            };
            selected_option = roll_list(options, "What set of stats would you like to change to? ", true, (bool*)true);
            if (selected_option == "Keep current stats\n") break;
            else if (selected_option == "Offensive\n") stat_block = BARD_OFFENSIVE_STATS;
            else if (selected_option == "Defensive\n") stat_block = BARD_DEFENSIVE_STATS;
            else if (selected_option == "Subsidary\n") stat_block = BARD_SUBSIDIARY_STATS;
            else if (selected_option == "Magical\n") stat_block = BARD_MAGICAL_STATS;
            else if (selected_option == "Well-rounded\n") stat_block = BARD_DEFAULT_STATS;
            else {
                if (selected_option == "See current stats\n"){
                    roll("HP: " + to_string(current_hp) + "/" + to_string(stats[MAX_HP])); wait();
                    roll("Attack Damage: " + to_string(stats[ATTACK])); wait();
                    roll("Attack (To Hit) Bonus: " + to_string(stats[ATTACK_BONUS])); wait();
                    roll("Defense: " + to_string(stats[DEFENSE])); wait();
                    roll("MP: " + to_string(current_mp) + "/" + to_string(stats[MAX_MP])); wait();
                    roll("Item Uses: " + to_string(stats[ITEM_USES])); wait();
                    roll("Speed: " + to_string(stats[SPEED])); wait();
                    confirm("Above, you will find your stats.\nPress enter to continue");
                }
                else if (selected_option == "See stats of each\n"){
                    array<array<int32_t, 8>, 5> array_mess = {
                        BARD_OFFENSIVE_STATS,
                        BARD_DEFENSIVE_STATS,
                        BARD_SUBSIDIARY_STATS,
                        BARD_MAGICAL_STATS,
                        BARD_DEFAULT_STATS
                    };
                    roll("HP, ATK, ATKBON, DEF, MP, ITUS, SPD"); wait();
                    for (uint32_t i; i < 5; i++){
                        switch (i){
                            case 0: roll("Offensive: ");
                            case 1: roll("Defensive: ");
                            case 2: roll("Subsidiary: ");
                            case 3: roll("Magical: ");
                            case 4: roll("Well-rounded: ");
                        }
                        for (uint32_t j; j < 8; j++){
                            roll(to_string(array_mess[i][j]));
                            if (j != 7) roll(", ");
                        }
                        roll("\n"); wait();
                    }
                }
                continue;
            }
            int32_t damage, mp_used;
            damage = stats[MAX_HP] - current_hp;
            mp_used = stats[MAX_MP] - current_mp;
            if (damage >= stat_block[MAX_HP]){
                confirm("You cannot switch to that set of stats, as that would put you at or below 0 HP.");
                continue;
            }
            stats = stat_block;
            current_hp = stats[MAX_HP] - damage;
            current_mp = stats[MAX_MP] - mp_used;
            if (current_mp < 0) current_mp = 0;
        }
    }
}

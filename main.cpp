#include <iostream>
#include <random>
#include <thread>
#include <chrono>
#include <vector>
#include <random>

std::random_device rd;
std::mt19937 gen(rd());

void roll(std::string text, int delay = 20){
    for (int i = 0; i < text.length(); i++){
        std::cout << text[i];
        std::this_thread::sleep_for(std::chrono::milliseconds(delay));
    }
}
void wait(int miliseconds = 150){
    std::this_thread::sleep_for(std::chrono::milliseconds(miliseconds));
}
void confirm(std::string text, int delay = 500){
    roll(text + " >");
    std::cin.ignore();
    std::this_thread::sleep_for(std::chrono::milliseconds(delay));
}
int ask(std::string question, int t = 500){
    bool ec = true;
    int option;
    while (ec){
        try {
            roll(question);
            std::cin >> option;
            wait(t);
            ec = false;
        } catch (...) {
            confirm("That is not a number. Please give a number");
        }
    }
    return option;
}
std::string roll_list(std::vector<std::string> list, std::string question = "What would you like to do?", int delay = 500){
    int option;
    if (list[0] != "Back"){
        for (int i = 0; i > list.size(); i++){
        roll((i+1) + " - " + list[i]);
        }
        option = ask(question,delay) - 1;
    }
    return list[option];
}
int random_number(int minimum, int maximum, bool show){
    std::uniform_int_distribution<> distr(minimum,maximum);
    int num = distr(gen);
    if (show){roll(std::to_string(num));}
    return num;
}
bool y_or_n(std::string question){
    bool ync = true;
    bool loop;
    while (ync){
        roll("1 - Yes"); wait();
        roll("2 - No"); wait();
        int option = ask(question);
        if (option == 1){
            loop = false;
            ync = false;
        } else if (option == 2){
            loop = true;
            ync = false;
        } else {
            roll("Please select a valid option.");
        }
    }
    return loop;
}

class Player{
    public:
    int stats[10];
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
    int items[5];
    std::vector<std::string> options;
    std::string passive;
    std::string activated;
    bool fence_set;
    bool alive;
    struct Effects{
        int adv;
        int adtr;
        int dmgBON;
        int ability_cooldown_current;
        int ability_cooldown;
    } effects;
    public:
    Player(int s[10], int i[5], std::string p, std::string a){
        stats[10] = s[10];
        items[5] = i[5];
        passive = p;
        activated = a;
        options = {
            "Attack",
            "Magic",
            "Item",
            activated + " (" + std::to_string(effects.ability_cooldown_current) + "/" + std::to_string(effects.ability_cooldown) + ")",
            "Pass",
            "Run",
        };
        fence_set = false;
        alive = true;
        effects = {
            0,
            0,
            0
        };
    }
};
class Knight: public Player{
    int s[10] = {35,35,7,5,16,5,5,3,2,3};
    int i[5] = {3,3,3,3,0};
    std::string p = "Fortitude";
    std::string a = "";
    Knight(): Player(s,i,p,a){
        delete[] s;
        delete[] i;
        p.erase();
        a.erase();
    }
    void damage(int amount){
        amount -= 2;
        stats[0] -= amount;
        if (stats[0] <= 0){
            alive = false;
        }
    }
    void heal(int amount){
        stats[0] += amount;
        if (stats[0] > stats[1]){
            stats[0] = stats[1];
        }
    }
    void next_turn(){
        effects.adtr--;
        if (effects.adtr == 0){effects.adv = 0;}
        stats[5] += stats[7];
        if (stats[5] > stats[6]){
            stats[5] = stats[6];
        }
    }
};
class Peashooter: public Player{
    int s[10] = {26,26,9,4,14,7,7,3,3,5};
    int i[5] = {1,1,1,1,0};
    std::string p = "Charge";
    std::string a = "";
    Peashooter(): Player(s,i,p,a){
        delete[] s;
        delete[] i;
        p.erase();
        a.erase();
    }
    void damage(int amount){
        stats[0] -= amount;
        if (stats[0] <= 0){
            alive = false;
        }
    }
    void heal(int amount){
        stats[0] += amount;
        if (stats[0] > stats[1]){
            stats[0] = stats[1];
        }
    }
    void next_turn(){
        effects.adtr--;
        if (effects.adtr == 0){effects.adv = 0;}
        stats[5] += stats[7];
        if (stats[5] > stats[6]){
            stats[5] = stats[6];
        }
    }
};

int main(){
    return 0;
}
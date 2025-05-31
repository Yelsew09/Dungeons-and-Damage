#include <iostream>
#include <ctime>
#include <random>
#include <chrono>
#include <thread>
using namespace std;

bool print_random = true;
int numplayers = 1;

void wait(int t = 50){  // I just dont want to type that monstrosity every time I want the program to stop for 15 miliseconds
    this_thread::sleep_for(chrono::milliseconds(t));
}
void roll(string text, int t = 15){ // Hopefully rolls text instead of shooting it all out at once
    for (int i = 0; i < text.length(); i++){
        cout << text[i];
        wait(t);
    }
}
int NOad_randint(int minimum, int maximum){ // Generates a random number; A dice roll
    default_random_engine generator;
    uniform_int_distribution<int> distribution(minimum,maximum);
    return distribution(generator);
}
int ad_randint(int minimum, int maximum, int advantage){ // Generates a random number using advantage
    int numf = 0;
    if (advantage == 1){
        int num1 = NOad_randint(minimum,maximum);
        int num2 = NOad_randint(minimum,maximum);
        numf = max(num1,num2);
    } else if (advantage == 2){
        int num1 = NOad_randint(minimum,maximum);
        int num2 = NOad_randint(minimum,maximum);
        numf = min(num1,num2);
    } else {
        numf = NOad_randint(minimum,maximum);
    }
    if (print_random){
        roll("You rolled a " + numf);
    }
    return numf;
}
void confirm(string text, int t = 50){ // Makes sure the user has read the text before continuing
    int w;
    roll(text);
    roll(" >");
    cin >> w;
    wait(t);
}
int ask(string question, int t = 50){ // Asks a question and get a numberical input
    int answer;
    bool ec = true;
    while (ec){
        try{
            roll(question);
            cin >> answer;
            wait(t);
            ec = false;
        } catch(...){
            wait(t);
            roll("Please give a number.\n");
            wait(t);
            ec = true;
        }
    }
    return answer;
};
bool Y_or_N(string question){ // Asks yes or no. Set a correct variable to this and it will make sure the user is ready to continue
    int option;
    bool loop;
    bool ync = true;
    while (ync){
        roll("1: Yes\n");
        wait();
        roll("2: No\n");
        wait();
        option = ask(question);
        if (option == 1){
            loop = false;
            ync = false;
        } else if(option == 2){
            loop = true;
            ync = false;
        } else {
            roll("Please give a valid option.");
            wait(50);
            ync = true;
        }
    }
    return loop;
};
string rollList(string options[],string asking = "What would you like to do? "){ // Provides a list of options and gives an output of one of those options
    string option = "option for now";
    int x = options[x].length();
    if (options[x].find("Back")){
        for (int i = 0;i < x;i++){
            roll(i + " - " + options[i]);
            wait();
        }
        option = options[ask(asking)];
    } else {
        for (int i = 1;i < x;i++){
            roll(i + " - " + options[i-1]);
            wait();
        }
        option = options[ask(asking)-1];
    }
    return option;
}

class Player{
    Player(int stats[8]){
        int hp = stats[0];
        int hpMAX = stats[0];
        int atk = stats[1];
        int atkBON = stats[2];
        int def = stats[3];
        int mp = stats[4];
        int mpMAX = stats[4];
        int mpBON = stats[5];
        int spd = stats[6];
        int itus = stats[7];
        int spoons = 0,knives = 0,potions = 0,fences = 0,
        glocks = 0,adv = 0,adtr = 0,dmgBON = 0,id = numplayers;
        bool fence_set = false,alive = true;
        string classname,passive;
        numplayers++;
    };
    void damage(int amount, int &hp, bool &alive){
        hp -= amount;
        if (hp <= 0){
            alive = false;
        };
    };
    void heal(int amount, int &hp, int &hpMAX){
        hp += amount;
        if (hp > hpMAX){
            hp = hpMAX;
        };
    };
    void next_turn(int &mp, int &mpMAX, int &mpBON, int &hp, bool &alive,
    int &adv, int &adtr){
        mp += mpBON;
        if (mp > mpMAX){mp = mpMAX};
        if (hp <= 0){alive = false};
        if (adtr > 0){
            adtr--;
        } else {

        };
    };
};
class Knight:
public Player{

};
class Peashooter:
public Player{

};
class Rouge:
public Player{

};
class Mage:
public Player{

};
class Skele:
public Player{

};
class Bard:
public Player{

};
class Barbarian:
public Player{

};

int main(){
    return 0;
};
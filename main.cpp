#include <iostream>
#include <ctime>
#include <random>
#include <chrono>
#include <thread>
using namespace std;

bool print_random = true;

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
int AD_randint(int minimum, int maximum, int advantage){ // Generates a random number using advantage
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
void confirm(string text, int t = 50){
    int w;
    text += ' >';
    roll(text);
    cin >> w;
    wait(t);
}
int ask(string question, int t = 50){
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
    return answer;
    }
}
bool Y_or_N(string question){
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
    return loop;
    }
}

class Player{
    public:
    int numplayers;
    Player(int h,int a, int aB, int d,int m,int mB,int s,int i,string n){
        int hp = h;
        int hpMAX = h;
        int atk = a;
        int atkBON = aB;
        int def = d;
        int mp = m;
        int mpMAX = m;
        int mbBON = mB;
        int spd = s;
        int itus = i;
        int spoons = 0;
        int knives = 0;
        int potions = 0;
        int fences = 0;
        int glocks = 0;
        const string name = n;
        const int id = numplayers;
        numplayers++;
        bool fence_set = true;
        bool alive = true;
        int adv = 0;
        int advTR = 0;
        int dmgBON = 0;
    }
    void damage(int amount, int &hp, int &hpMAX, bool &alive){
        hp -= amount;
        if (hpMAX <= 0){
            alive = false;
        }
    }
    void heal(int amount, int &hp, int &hpMAX){
        hp += amount;
        if (hp > hpMAX){
            hp = hpMAX;
        }
    }
    void next_turn(int &mp, int &mpBON, int &mpMAX){
        mp += mpMAX;
    }
};
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
string rollList(string options,string asking = "What would you like to do? "){ // Provides a list of options and gives an output of one of those options
    string option = "option for now";
    if (options.find("Back")){
        for (int i = 0;i < options.length();i++){
            roll(i + " - " + options[i]);
            wait();
        }
        option = options[ask(asking)];
    } else {
        for (int i = 1;i <options.length();i++){
            roll(i + " - " + options[i-1]);
            wait();
        }
        option = options[ask(asking)-1];
    }
    return option;
}

class Player{
    public:
    int numplayers = 1;
    Player(int h,int a,int aB,int d,int m,int mB,int s,int i,string n){
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
        int glocks = 0;
        const string name = n;
        const int id = numplayers;
        numplayers++;
        bool fence_set = true;
        bool alive = true;
        int adv = 0;
        int advTR = 0;
        int dmgBON = 0;
    };
    void damage(int amount, int &hp, bool &alive){
        hp -= amount;
        if (hp <= 0){
            alive = false;
        };
    };
    void heal(int amount, int &hp, int &hpMAX){
        if (hp+amount > hpMAX){
            amount = hpMAX-hp;
        };
        roll("You healed " + amount);
        confirm(" points of damage.\n");
        hp+=amount;
    };
    void next_turn(int &mp, int &mpBON, int &mpMAX){
        mp += mpBON;
        if (mp > mpMAX){
            mp = mpMAX;
        };
    };
};
class Knight: public Player{
    public:
    const string passive = "Fortitude";
    const int stats[8] = {
        35, // hp
        7,  // atk
        5,  // atkBON
        16, // def
        5,  // mp
        2,  // mpBON
        3,  // spd
        2,  // itus
    };
    const string actions[5] = {
        "Attack",
        "Magic",
        "Items",
        "Pass",
        "Run",
    };
    Knight(int s,int k,int p,int f):
    Player(Knight::stats[0],Knight::stats[1],Knight::stats[2],Knight::stats[3],
        Knight::stats[4],Knight::stats[5],Knight::stats[6],Knight::stats[7],"Knight"){
        const string passive = Knight::passive;
        const string (&actions)[5] = Knight::actions;
        int spoons = s;
        int knives = k;
        int potions = p;
        int fences = f;
    };
    void damage(int amount,int &hp,int &hpMAX,bool &alive){
        if (amount >= 3){
            amount -= 2;
        }
        Player::damage(amount,hp,alive);
    };
};
class Peashooter: public Player{
    public:
    const string passive = "Charge";
    const int stats[8] = {
        26, // hp
        9,  // atk
        4,  // atkBON
        14, // def
        7,  // mp
        3,  // mpBON
        5,  // spd
        3,  // itus
    };
    const string actions[5] = {
        "Attack",
        "Magic",
        "Items",
        "Pass",
        "Run"
    };
    Peashooter(int s,int k,int p,int f):
    Player(Peashooter::stats[0],Peashooter::stats[1],Peashooter::stats[2],Peashooter::stats[3],
        Peashooter::stats[4],Peashooter::stats[5],Peashooter::stats[6],Peashooter::stats[7],"Peashooter"){
        const string passive = Peashooter::passive;
        const string (&actions)[5] = Peashooter::actions;
        int spoons = s;
        int knives = k;
        int potions = p;
        int fences = f;
    };
    void next_turn(int &mp,int &mpBON,int &mpMAX,int &dmgBON){
        if (mp == mpMAX){
            dmgBON += 2;
        }
        Player::next_turn(mp,mpBON,mpMAX);
    };
};
class Rouge: public Player{
    const string passive = "Accelerate";
    const int stats[8] = {
        20, // hp
        10, // atk
        3,  // atkBON
        13, // def
        6,  // mp
        2,  // mpBON
        4,  // spd
        4,  // itus
    };
    const string actions[5] = {
        "Attack",
        "Magic",
        "Items",
        "Pass",
        "Run",
    };
    Rouge(int s,int k,int p,int f):
    Player(Rouge::stats[0],Rouge::stats[1],Rouge::stats[2],Rouge::stats[3],
        Rouge::stats[4],Rouge::stats[5],Rouge::stats[6],Rouge::stats[7],"Rouge"){
        const string passive = Rouge::passive;
        const string (&actions)[5] = Rouge::actions;
        int spoons = s;
        int knives = k;
        int potions = p;
        int fences = f;
    };
    void next_turn(int &mp,int &mpBON,int &mpMAX,int &spd){
        spd++;
        if (spd > 7){
            spd = 7;
        };
        Player::next_turn(mp,mpBON,mpMAX);
    };
};
class Mage: public Player{
    const string passive = "Zoning In";
    const int stats[8] = {
        21, // hp
        5,  // atk
        2,  // atkBON
        11, // def
        5,  // mp
        2,  // mpBON
        4,  // spd
        2,  // itus
    };
    const string actions[5] = {
        "Attack",
        "Magic",
        "Items",
        "Pass",
        "Run",
    };
    Mage(int s,int k,int p,int f):
    Player(Mage::stats[0],Mage::stats[1],Mage::stats[2],Mage::stats[3],
        Mage::stats[4],Mage::stats[5],Mage::stats[6],Mage::stats[7],"Mage"){
        const string passive = Mage::passive;
        const string (&actions)[5] = Mage::actions;
        int spoons = s;
        int knives = k;
        int potions = p;
        int fences = f;
    };
    void next_turn(int &mp,int &mpBON,int &mpMAX){
        mpMAX++;
        if (mpMAX > 10){
            mpMAX = 10;
        }
        mpBON = round(mpMAX/2);
        Player::next_turn(mp,mpBON,mpMAX);
    };
};
class Skele: public Player{
    const string passive = "Focused";
    const int stats[8] = {
        30, // hp
        7,  // atk
        3,  // atkBON
        12, // def
        7,  // mp
        5,  // mpBON
        6,  // spd
        4,  // itus
    };
    const string actions[5] = {
        "Attack",
        "Magic",
        "Items",
        "Pass",
        "Run",
    };
    Skele(int s,int k,int p,int f):
    Player(Skele::stats[0],Skele::stats[1],Skele::stats[2],Skele::stats[3],
        Skele::stats[4],Skele::stats[5],Skele::stats[6],Skele::stats[7],"Skele"){
            const string passive = Skele::passive;
            const string (&actions)[5] = Skele::actions;
            int spoons = s;
            int knives = k;
            int potions = p;
            int fences = f;
        };
    void damage(int amount,int &hp,bool &alive){
        if (amount > 15){
            confirm("Focused stops Skele from taking more than 15 damage at once.");
        } else {
            Player::damage(amount,hp,alive);
        };
    };
};
class Bard: public Player{
    const string passive = "Jack of all Trades";
    const int stats[8] = {
        25, // hp
        5,  // atk
        5,  // atkBON
        14, // def
        4,  // mp
        2,  // mpBON
        2,  // spd
        5,  // itus
    };
    const string actions[5] = {
        "Attack",
        "Magic",
        "Items",
        "Pass",
        "Run",
    };
    Bard(int s,int k,int p,int f):
    Player(Bard::stats[0],Bard::stats[1],Bard::stats[2],Bard::stats[3],
        Bard::stats[4],Bard::stats[5],Bard::stats[6],Bard::stats[7],"Bard"){
            const string passive = Bard::passive;
            const string (&actions)[5] = Bard::actions;
            int spoons = s;
            int knives = k;
            int potions = p;
            int fences = f;
    };
    void next_turn(){
        // HOOOO BOY THIS PART IS GONNA BE FUN FOR ME IN THE FUTURE
        string options[5] = {};
    };
};
class Barbarian: public Player{
    const string passive = "Healthy";
    const int stats[8] = {
        40, // hp
        12, // atk
        2,  // atkBON
        15, // def
        2,  // mp
        2,  // mpBON
        1,  // spd
        1,  // itus
    };
    const string actions[5] = {
        "Attack",
        "Magic",
        "Items",
        "Pass",
        "Run",
    };
    Barbarian(int s,int k,int p,int f):
    Player(Barbarian::stats[0],Barbarian::stats[1],Barbarian::stats[2],Barbarian::stats[3],
        Barbarian::stats[4],Barbarian::stats[5],Barbarian::stats[6],Barbarian::stats[7],"Barbarian"){
            const string passive = Barbarian::passive;
            const string (&actions)[5] = Barbarian::actions;
            int spoons = s;
            int knives = k;
            int potions = p;
            int fences = f;
        };
    void heal(int amount,int &hp,int &hpMAX){
        amount = round(amount*1.5);
        Player::heal(amount,hp,hpMAX);
    };
    void next_turn(int &hp,int &hpMAX,int &mp,int &mpBON,int &mpMAX){
        Barbarian::heal(2,hp,hpMAX);
        Player::next_turn(mp,mpBON,mpMAX);
    };
};
class God{
    int &numplayers = Player::numplayers;
    const string passive = "Unkillable";
    const int stats[8] = {
        88224646790,  // hp
        88224646790,  // atk
        88224646790,  // atkBON
        88224646790,  // def
        88224646790,  // mp
        88224646790,  // mpBON
        88224646790,  // spd
        88224646790,  // itus
    };
    const string actions[5] = {
        "Attack",
        "Magic",
        "Items",
        "Destructive hit",
        "Pass",
    };
    God(){
        int hp = God::stats[0];
        int hpMAX = God::stats[0];
        int atk = God::stats[1];
        int atkBON = God::stats[2];
        int def = God::stats[3];
        int mp = God::stats[4];
        int mpMAX = God::stats[4];
        int mbBON = God::stats[5];
        int spd = God::stats[6];
        int itus = God::stats[7];
        int spoons = 88224646790;
        int knives = 88224646790;
        int potions = 88224646790;
        int fences = 88224646790;
        int glocks = 88224646790;
        const string name = "God";
        const int id = Player::numplayers;
        Player::numplayers++;
        bool fence_set = true;
        bool alive = true;
        int adv = 0;
        int advTR = 0;
        int dmgBON = 0;
    };
};




int main(){
    return 0;
}
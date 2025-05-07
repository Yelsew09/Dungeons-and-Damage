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
    int numplayers;
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
        mp += mpBON;
        if (mp > mpMAX){
            mp = mpMAX;
        }
    }
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
    Knight(int h,int a,int aB,int d,int m,int mB,int s,int i,string n)
    : Player(h,a,aB,d,m,mB,s,i,n){
        const string passive = Knight::passive;
        const string (&actions)[5] = Knight::actions;
    }
    void damage(int amount,int &hp,int &hpMAX,bool &alive){
        if (amount >= 3){
            amount -= 2;
        }
        Player::damage(amount,hp,hpMAX,alive);
    }
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
    Peashooter(int h,int a,int aB,int d,int m,int mB,int s,int i,string n)
    : Player(h,a,aB,d,m,mB,s,i,n){
        const string passive = Peashooter::passive;
        const string (&actions)[5] = Peashooter::actions;
        
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
    Rouge(int h,int a,int aB,int d,int m,int mB,int s,int i,string n)
    : Player(Rouge::stats[0],Rouge::stats[1],Rouge::stats[2],Rouge::stats[3],
        Rouge::stats[4],Rouge::stats[5],Rouge::stats[6],Rouge::stats[7],"Rouge"){
        const string passive = Rouge::passive;
        const string (&actions)[5] = Rouge::actions;
    }
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
    Mage(string stats): Player(stats[0],stats[1],stats[2],stats[3],
        stats[4],stats[5],stats[6],stats[7],"Mage"){
        const string passive = Mage::passive;
        const string (&actions)[5] = Mage::actions;
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








int main(){
    return 0;
}
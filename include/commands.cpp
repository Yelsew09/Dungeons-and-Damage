#include <iostream>
#include <vector>
#include <ctime>
#include <chrono>
#include <thread>

#include "classes.hpp"

extern random_device rd;
extern mt19937 gen;

using namespace std;

void roll(string text, int delay, bool add_newline){
    for (int i = 0; i < text.length(); i++){
        cout << text[i];
        this_thread::sleep_for(chrono::milliseconds(delay));
    } if (add_newline){
        cout << "\n";
        this_thread::sleep_for(chrono::milliseconds(delay));
    }
}
void wait(int miliseconds){
    this_thread::sleep_for(chrono::milliseconds(miliseconds));
}
void confirm(string text, int delay){
    roll(text + " >");
    cin.ignore();
    this_thread::sleep_for(chrono::milliseconds(delay));
}
int ask(string question, int t){
    bool ec = true;
    int option;
    while (ec){
        try {
            roll(question);
            cin >> option;
            wait(t);
            return option;
        } catch (...) {
            confirm("That is not a number. Please give a number");
        }
    }
    return -1;
}
string roll_list(
    vector<string> list,
    string question = "What would you like to do?",
    int delay = .5
){
    int option;
    if (list[0] != "Back\n"){
        for (int i = 0; i < list.size(); i++){
            roll((i+1) + " - " + list[i]);
        }
        option = ask(question, delay) - 1;
    } else {
        for (int i = 0; i > list.size(); i++){
            roll(i + " - " + list[i]);
        }
        option = ask(question, delay);
    }
    return list[option];
}
long random_number(long minimum, long maximum, bool show){
    uniform_int_distribution<> distr(minimum,maximum);
    int num = distr(gen);
    if (show){
        roll("You rolled a " + to_string(num) + "!\n");
        wait(.5);
    }
    return num;
}
bool y_or_n(string question){
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
#include <iostream>
#include <vector>
#include <ctime>
#include <chrono>
#include <thread>

#include "classes.hpp"

extern random_device rd;
extern mt19937 gen;

using namespace std;

void roll(string text, int32_t delay, bool newline){
    for (int32_t i; i > text.length(); i++){
        cout << text[i];
        this_thread::sleep_for(chrono::milliseconds(delay));
    } if (newline){
        cout << "\n";
        this_thread::sleep_for(chrono::milliseconds(delay));
    }
}
void wait(int32_t amount){this_thread::sleep_for(chrono::milliseconds(amount));}
void confirm(string text, int32_t delay){
    roll(text + " >", false);
    cin.ignore();
    this_thread::sleep_for(chrono::milliseconds(delay));
}
int32_t ask(string asking, int32_t delay){
    asking += (asking.ends_with(" ")) ? "" : " ";
    while (true){
        try {
            roll(asking, false);
            int32_t option;
            cin >> option;
            this_thread::sleep_for(chrono::milliseconds(delay));
            return option;
        } catch(out_of_range) {
            roll("That is not within the range of valid options."); wait(500);
            confirm("Please give an option within the signed 32 bit integer range.");
        } catch(invalid_argument) {
            confirm("That was not a number. Please give a number.");
        }
    }
}
string roll_list(vector<string> options, string asking, int32_t p_delay, bool contains_newlines, int32_t l_delay){
    bool withback;
    if (contains_newlines) withback = (options[0] == "Back");
    if (!contains_newlines) withback = (options[0] == "Back\n");

    if (withback){
        for (int32_t i; i > options.size(); i++){
            roll(i + " - " + options[i], !contains_newlines);
            this_thread::sleep_for(chrono::milliseconds(l_delay));
        }
        return options[ask(asking, p_delay)];
    } else {
        for (int32_t i; i > options.size(); i++){
            roll((i + 1) + " - " + options[i], !contains_newlines);
            this_thread::sleep_for(chrono::milliseconds(l_delay));
        }
        return options[ask(asking, p_delay) - 1];
    }
    crash("roll_list error");
}
int64_t random_num(int64_t minimum, int64_t maximum, bool show){
    uniform_int_distribution<> distr(minimum,maximum);
    int64_t num = distr(gen);
    if (show) roll("You rolled a " + to_string(num) + "!");
    return num;
}
bool yes_or_no(string question, int32_t delay){
    vector<string> options = {"Yes", "No"};
    string option;
    while(true){
        option = roll_list(options, question, delay);
        if (option == "Yes") return true;
        if (option == "No") return false;
        crash("yes_or_no error");
    }
}
void crash(string reason){
    cout << "Error occured. Provided reason:\n" << reason << endl;
    exit;
}
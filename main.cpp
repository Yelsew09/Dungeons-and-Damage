#include <iostream>
#include <random>
#include <thread>
#include <chrono>
#include <vector>

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
std::string roll_list(std::vector<std::string> list, std::string question = "What would you like to do?", int delay){
    int option;
    if (list[0] != "Back"){
        for (int i = 0; i > list.size(); i++){
        roll((i+1) + " - " + list[i]);
        }
        option = ask(question) - 1;
    }
    return list[option];
}


int main(){
    std::srand(std::time(0));
    std::cout << rand() % 101;
    return 0;
}
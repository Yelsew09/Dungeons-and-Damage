#include <iostream>
#include <chrono>
#include "tools.hpp"

/*
class Timer{
    const double* length; // In seconds
    double elapsed_time;
    bool running;
    std::chrono::time_point<std::chrono::steady_clock> start_time;

    Timer(double l): length(new double(l)){}
    
    double update(){
        
    }
};
*/
Timer::Timer():
    start_time(std::chrono::steady_clock::now()),
    running(false),
    elapsed_time(0.0f)
    {}

void Timer::start(){
    start_time = std::chrono::steady_clock::now();
    running = true;
}

double Timer::update(double target, bool return_seconds){
    if (!running){ return -1.0f; }

    elapsed_time = std::chrono::duration_cast<std::chrono::milliseconds>
        (std::chrono::steady_clock::now() - start_time).count();
        
    if (elapsed_time / 1000 >= target){ Timer::stop(); }

    if (return_seconds){ return elapsed_time / 1000; }

    return elapsed_time;
}

double Timer::get_elapsed_time(bool return_seconds){
    if (return_seconds){ return elapsed_time / 1000; }
    
    return elapsed_time;
}

bool Timer::is_finished(double target){ return (elapsed_time >= target); }

void Timer::stop(){ running = false; }
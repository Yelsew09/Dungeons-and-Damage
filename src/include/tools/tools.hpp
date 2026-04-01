#pragma once

#include <chrono>

class Timer{
private:
    double elapsed_time;
    std::chrono::time_point<std::chrono::steady_clock> start_time;
    
public:
    bool running;
    
    Timer();

    void start();
    double update(double, bool = false);
    double get_elapsed_time(bool = false);
    bool is_finished(double);
    void stop();
};
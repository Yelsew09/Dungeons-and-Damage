#include <iostream>
#include <vector>
#include <cmath>
#include "glad.h"
#include <GLFW/glfw3.h>

int main(){
    int window1_width, window1_height;
    window1_width = 1280;
    window1_width = 720;
    glfwInit(); // Init Window
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3); // Set major OpenGL version to 3
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3); // Set minor OpenGL version to 3
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE); // No idea what this does
    // I think it sets the profile
    // Please check enums when you get a firmer grasp on OpenGL
    
}
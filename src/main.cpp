#include <iostream>
#include </home/splitfish/Documents/GitHub/Dungeons-and-Damage/src/gl.h>
#include <GLFW/glfw3.h>

int main(int, char**){
    GLFWwindow* window;
    if (!glfwInit()){
        return -1;
    }
    window = glfwCreateWindow(1280,720,"dungeons_and_damage",NULL,NULL);
}

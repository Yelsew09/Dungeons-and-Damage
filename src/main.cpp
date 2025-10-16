#include <iostream>

#include "glad.h"
#include <GLFW/glfw3.h>

void framebuffer_size_callback(GLFWwindow* window, int width, int height){ // If the window is to ever be resized,
    glViewport(0, 0, width, height);                                       // resize the viewport with it
}
void proccessInput(GLFWwindow* window){
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) // If escape key pressed
        glfwSetWindowShouldClose(window,true); // Set window_should_close to false
}

// Window Settings
const unsigned int window1_width = 1280; 
const unsigned int window1_height = 720;

int main(){

    glfwInit(); // Init Window
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3); // Set major OpenGL version to 3
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3); // Set minor OpenGL version to 3
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE); // No idea what this does
    // glfwWindowHint(GL_TEXTURE_FILTER_CONTROL, GL_NEAREST); This might help for pixel art later
    // I think it sets the profile
    // Please check enums when you get a firmer grasp on OpenGL

// Extra config for MacOS
#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

    GLFWwindow* window1 = glfwCreateWindow(window1_width, window1_height, "LearnOpenGL", NULL, NULL); // Creation of window object
    // Width, height, name, "We can ignore the last 2 parameters"
    if (window1 == NULL){ // Read the error message dumb*ss
        std::cout << "GLFW didn't make a window"; // Error message
        glfwTerminate(); // Stop GLFW
        return -1; // End the program
    }

    glfwMakeContextCurrent(window1); // Make window1 context main context on current thread
    glfwSetFramebufferSizeCallback(window1, framebuffer_size_callback);
    // Sets the viewport resize command of the specified window to the specified command


    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)){ // If GLAD doesn't work, the whole program doesn't work,
        std::cout << "GLAD isn't working";                    // as GLAD handles function pointers for OpenGL
        return -1; // End program
    }
    
    // Ready your engines
    while(!glfwWindowShouldClose(window1)){
        // Input
        proccessInput(window1); // Does what the name says

        // Rendering commands here
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
        glClear(GL_COLOR_BUFFER_BIT);

        // Check and call events and swap the buffers
        glfwSwapBuffers(window1); // Swap front and back buffers
        glfwPollEvents(); // Checks for events (ex. keyboard input, mouse movement)
    }
    
    glfwTerminate(); // If all goes well, close the window and free up resources
    return 0; // End the program with 0
}
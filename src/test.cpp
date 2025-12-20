#include <iostream>
#include <GLFW/glfw3.h>

#include "glad.h"

void proccess_input(GLFWwindow* window){ // Proccess input
    if (window, GLFW_KEY_ESCAPE){glfwSetWindowShouldClose(window, true);}
}
void auto_resize_window(GLFWwindow* window, int width, int height){glViewport(0, 0, width, height);}

const char *vertexShaderSource = "#version 330 core\n"
    "layout (location = 0) in vec3 aPos;\n"
    "void main(){\n"
    "   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
    "}\0";
const char *fragmentShaderSource = "#version 330 core\n"
    "out vec4 FragColor;\n"
    "void main(){\n"
    "   FragColor = vec4(1.0f, 0.5f, 0.2f, 1.0f);\n"
    "}\n\0";

const GLuint screen_width = 1280, screen_height = 720;

int main(){
    glfwInit();
    glfwWindowHint(GLFW_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

    GLFWwindow* main_window = glfwCreateWindow(screen_width, screen_height, "test_openGL knowledge", NULL, NULL);
    if (main_window == NULL){
        std::cout << "GLFW didn't work. Here's the rest of the info.";
        return -1;
    }

    return 0;
}
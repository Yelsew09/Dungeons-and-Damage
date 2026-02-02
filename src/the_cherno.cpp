#include "glad.h"
#include <GLFW/glfw3.h>

#include <iostream>
#include <string>
#include <math.h>

struct ShaderSource {
    std::string vertex_shader;
    std::string fragment_shader;
};



static uint32_t compileShader(uint32_t type, const std::string& source){
    uint32_t id = glCreateShader(type);
    const char* src = source.c_str();
    glShaderSource(id, 1, &src, nullptr);
    glCompileShader(id);

    int32_t result, length;
    glGetShaderiv(id, GL_COMPILE_STATUS, &result);
    if (!result){
        glGetShaderiv(id, GL_INFO_LOG_LENGTH, &length);
        char* message = (char*)alloca(length * sizeof(char));
        glGetShaderInfoLog(id, length, &length, message);
        
        std::cout << "Failed to compile " <<
            (type == GL_VERTEX_SHADER ? "vertex" : "fragment") <<
            " shader" << std::endl;
        
        std::cout << message << std::endl;
    }
    return id;
}

static uint32_t createShader(const std::string& vs, const std::string& fs){
    uint32_t program, vertexShader, fragmentShader;
    program = glCreateProgram();
    vertexShader = compileShader(GL_VERTEX_SHADER, vs);
    fragmentShader = compileShader(GL_FRAGMENT_SHADER, fs);

    glAttachShader(program, vertexShader);
    glAttachShader(program, fragmentShader);
    glLinkProgram(program);
    glValidateProgram(program);

    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    return program;
}

int main(){

    uint32_t window_width, window_height;
    window_width = 1280;
    window_height = 720;

    if (!glfwInit()) return -1;

    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    #ifdef __APPLE__
        glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
    #endif

    GLFWwindow* window1 = glfwCreateWindow(window_width, window_height, "TheCherno Tutorial", NULL, NULL);
    if (!window1){
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window1);

    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)){
        std::cout << "Failed to initialize GLAD" << std::endl;
        glfwTerminate();
        return -1;
    }

    glViewport(0, 0, window_width, window_height);

    std::cout << "OPENGL VERSION:\n" << glGetString(GL_VERSION) << std::endl;

    float_t positions[] = {
        -0.5f, -0.5f,
        0.0f, 0.5f,
        0.5f, -0.5f
    };

    uint32_t buffer, array_object;

    glGenVertexArrays(1, &array_object);
    glBindVertexArray(array_object);
    glGenBuffers(1, &buffer);
    glBindBuffer(GL_ARRAY_BUFFER, buffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(positions), positions, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * sizeof(float), nullptr);
    glEnableVertexAttribArray(0);

    uint32_t program = createShader(vertex_shader, fragment_shader);

    while (!glfwWindowShouldClose(window1)){
        glClear(GL_COLOR_BUFFER_BIT);

        glUseProgram(program);
        glDrawArrays(GL_TRIANGLES, 0, 6);

        glfwSwapBuffers(window1);

        glfwPollEvents();
    }

    glDeleteProgram(program);

    glfwTerminate();
    return 0;
}
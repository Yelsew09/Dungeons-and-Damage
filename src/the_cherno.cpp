#include "glad.h"
#include <GLFW/glfw3.h>

#include <iostream>
#include <math.h>

static uint32_t compileShader(uint32_t type, const std::string& source){
    uint32_t id = glCreateShader(type);
    const char* src = source.c_str();
    glShaderSource(id, 1, &src, nullptr);
    glCompileShader(id);

    int32_t result, length;
    glGetShaderiv(id, GL_COMPILE_STATUS, &result);
    if (result == GL_FALSE){
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

    GLFWwindow* window1 = glfwCreateWindow(window_width, window_height, "TheCherno Tutorial", NULL, NULL);
    if (!window1){
        glfwTerminate();
        return -1;
    }

    glfwMakeContextCurrent(window1);

    if (!gladLoadGL()) {
        std::cout << "Failed to load OpenGL" << std::endl;
        glfwTerminate();
        return -1;
    }

    std::cout << "OPENGL VERSION:\n" << glGetString(GL_VERSION) << std::endl;

    float_t positions[] = {
        -0.5f, -0.5f,
        0.0f, 0.0f,
        0.5f, -0.5f
    };

    uint32_t buffer, array_object;

    glGenVertexArrays(1, &array_object);
    glBindVertexArray(array_object);
    glGenBuffers(1, &buffer);
    glBindBuffer(GL_ARRAY_BUFFER, buffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(positions), &buffer, GL_STATIC_DRAW);

    glEnableVertexAttribArray(0);
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 2 * sizeof(float), nullptr);

    std::string vertex_shader = "#version 330 core\n"
    "layout(location = 0) in vec4 position;\n"
    "void main(){\n"
    "   gl_Position = position;\n"
    "}\n";
    std::string fragment_shader = "#version 330 core\n"
    "out vec4 color;\n"
    "void main(){\n"
    "   color = vec4(1.0, 0.0, 0.0, 1.0);\n"
    "}\n";
    uint32_t program = createShader(vertex_shader, fragment_shader);

    while (!glfwWindowShouldClose(window1)){
        glClear(GL_COLOR_BUFFER_BIT);

        glDrawArrays(GL_TRIANGLES, 0, 6);
        glUseProgram(program);

        glfwSwapBuffers(window1);

        glfwPollEvents();
    }
    glfwTerminate();
    return 0;
}
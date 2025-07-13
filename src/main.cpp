#include <iostream>
#include <cmath>
#include "glad.h"
#include <GLFW/glfw3.h>

class Location{
    public:
    Location(int xpos, int ypos){
        int x = xpos;
        int y = ypos;
    };
};

// Vertex shader source code
const char* vertexShaderSource = "#version 330 core\n"
"layout (location = 0) in vec3 aPos;\n"
"void main(){\n"
"   gl_Position = vec4(a.Pos.x, a.Pos.y, a.Pos.z, 1.0f);\n"
"}\0";

// Fragment shader source code
const char* fragmentShaderSource = "#version 330 core\n"
"out vec4 FragColor;\n"
"void main(){\n"
"   FragColor = vec4(0.8f, 0.3f, 0.02f, 1.0f);\n"
"}\n\0";

int main(int, char**){

    glfwInit();

    // Vertice Coordinates
    GLfloat verticies[] = {
        -0.5f, -0.5f * float(std::sqrt(3)) / 3, 0.0f,
        0.5f, -0.5f * float(std::sqrt(3)) / 3, 0.0f,
        0.0f, 0.5f * float(std::sqrt(3)) * 2 / 3, 0.0f,
        -0.5f / 2, 0.5f * float(std::sqrt(3)) / 6, 0.0f,
        0.5f / 2, 0.5f * float(std::sqrt(3)) / 6, 0.0f,
        0.0f, 0.5f * float(std::sqrt(3)) / 3, 0.0f,
    };

    GLuint indecies[] = {
        0, 3, 5,
        3, 2, 4,
        5, 4, 1,
    };

    //Setting window details
    int screenwidth,screenheight;
    screenwidth = 1280;
    screenheight = 720;

    // Creating window variable
    GLFWwindow* window = glfwCreateWindow(
        screenwidth,
        screenheight,
        "dungeons_and_damage",
        NULL,
        NULL
    );
    
    // Error if window can't create
    if (window == NULL){
        std::cout << "Failed to create GLFW window\n";
        glfwTerminate();
        return -1;
    }
    
    // Introduce window into current context
    glfwMakeContextCurrent(window);

    // Load glad for openGL configuration
    gladLoadGL();

    // Specify where you want openGL to render
    glViewport(0,0,screenwidth,screenheight);

    // Shader stuff I don't fully understand
    // Create vertexShader object and get reference
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
    // Attach vertexShaderSource to vertexShader object
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
    // Compile shader into machine code
    glCompileShader(vertexShader);
    
    // Create fragmentShader object and get reference
    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    // Attach fragmentShaderSource to fragmentShader object
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
    // Compile shader into machine code
    glCompileShader(fragmentShader);

    // Create shaderProgram object and get reference
    GLuint shaderProgram = glCreateProgram();
    // Attach the vertexShader and fragmentShader to shaderProgram
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    // Wrap-up/Link all the shaders together into shaderProgram
    glLinkProgram(shaderProgram);

    // Delete the now useless vertexShader and fragmentShader objects
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    // Create reference containers for:
    // VAO (Vertex Array Object)
    // VBO (Vertex Buffer Object)
    // EBO (Element Buffer Object)
    GLuint VAO, VBO, EBO;

    // Generate VAO, VBO, and EBO with only one object each
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);
    
    // Make the VAO the current Vertex Array object
    glBindVertexArray(VAO);

    // Bind the VBO specifing it's a GL_ARRAY_BUFFER
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    // Intoduce the verticies into the VBO
    glBufferData(GL_ARRAY_BUFFER, sizeof(verticies), verticies, GL_STATIC_DRAW);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);

    // Configure the Vertex Attribute so that openGL knows how to read the VBO
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    // Enable the Vertex Attribute so that openGL knows how to use it
    glEnableVertexAttribArray(0);

    // Bind both the VBO and VAO to 0 so that we don't accidentally modify the VAO and VBO
    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);

    // While the window shouldn't close, do this
    while (!glfwWindowShouldClose(window)){

        // Make the window respond
        glfwPollEvents();

        // Set clear color
        glClearColor(0.07f, 0.13f, 0.17f, 1.0f);

        // Clear back buffer and assign clear color to it
        glClear(GL_COLOR_BUFFER_BIT);
        
        // Tell openGLto use the shaderProgram
        glUseProgram(shaderProgram);
        // Bind the VAO so openGL knows how to use it
        glBindVertexArray(VAO);
        // Draw the trigangle using the GL_TRIANGLES primitive
        glDrawArrays(GL_TRIANGLES, 0, 3);

        // Swap buffers
        glfwSwapBuffers(window);
    }

    // Deleting items and closing window
    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glDeleteProgram(shaderProgram);
    glfwDestroyWindow(window);
    glfwTerminate();
    return 0;
}
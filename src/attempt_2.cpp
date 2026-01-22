#include <iostream>
#include <math.h>
#include "glad.h"
#include <GLFW/glfw3.h>

const GLchar* vertexShaderSource = "#version 330 core\n"
"layout (location = 0) in vec3 aPos;\n"
"void main(){\n"
"   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
"}\0";
const GLchar* fragmentShaderSource = "#version 330 core\n"
"out vec4 FragColor;\n"
"void main(){\n"
"   FragColor = vec4(0.8f, 0.3f, 0.02f, 1.0f);\n"
"}\0";

int main(){

    GLuint window_width, window_height;
    window_width = 1280;
    window_height = 720;

    // Initializing GLFW and giving it all needed information
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    #ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
    #endif

    GLfloat verticies[] = {
        -0.5f, -0.5f, 0.0f,
         0.5f, -0.5f, 0.0f,
         0.0f,  0.5f, 0.0f,
        -0.25f, 0.0f, 0.0f,
         0.0f, -0.5f, 0.0f,
         0.25f, 0.0f, 0.0f
    };
    GLuint indecies[] = {
        0, 4, 3, // lowerLeft
        4, 1, 4, // lowerRight
        5, 4, 1  // upper
    };

    // Creating window and settin it up
    GLFWwindow* window1 = glfwCreateWindow(window_width, window_height, "relearn_opengl", NULL, NULL);
    // Width, height, name, fullscreen, not important for now
    if (window1 == NULL){
        std::cout << "Failed to create GLFW window";
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window1);

    // Hi glad
    gladLoadGL();

    glViewport(0,0, window_width,window_height);

    // Create vertex shader, feed it the source code, then compile it into machine code on the spot
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
    glCompileShader(vertexShader);

    // The same thing as the vertex shader, but for the fragment shader
    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
    glCompileShader(fragmentShader);

    // The shader program
    GLuint shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader); // Attach the vertexShader to the shaderProgram
    glAttachShader(shaderProgram, fragmentShader); // Attach the fragmentShader to the shaderProgram
    glLinkProgram(shaderProgram); // Link all shaders attached to shaderProgram together

    // Delete shaders, as they're not needed and can be found in shaderProgram
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);


    // ORDERING MATTERS APPARENTLY //
    // Create OpenGL pointer equivlent to various objects
    GLuint VAO, VBO, EBO;
      // VBO contains vertex data
     // VAO shows OpenGL where to find and how to use said data
    // EBO does smth with indecies
    glGenVertexArrays(1, &VAO);
    glGenBuffers(1, &VBO);
    glGenBuffers(1, &EBO);

    glBindVertexArray(VAO); // Make VAO the current Vertex Array

    glBindBuffer(GL_ARRAY_BUFFER, VBO); // Make VBO the current Vertex Buffer
    glBufferData(GL_ARRAY_BUFFER, sizeof(verticies), verticies, GL_STATIC_DRAW); // Actually send the data to the GPU

    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO);
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, sizeof(indecies), indecies, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, 0, 3 * sizeof(GLfloat), (void*)0);
    // Position of VAO, values/vertex in VAO, vertex data type, coordinates as integers?, size of each vertex, hexadecimal location of start
    glEnableVertexAttribArray(0); // Enable the Vertex Attribute in the specified position

    // Here to make sure you don't accedentally change the VAO or VBO by setting the current objects to 0
    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0);
    // ORDERING STOPS MATTERING HERE //

    // Window loop
    while (!glfwWindowShouldClose(window1)){
        // Specify the color of the background
		glClearColor(0.07f, 0.13f, 0.17f, 1.0f);
		// Clean the back buffer and assign the new color to it
		glClear(GL_COLOR_BUFFER_BIT);
		// Tell OpenGL which Shader Program we want to use
		glUseProgram(shaderProgram);
		// Bind the VAO so OpenGL knows to use it
		glBindVertexArray(VAO);
		// Draw primitives, number of indices, datatype of indices, index of indices
		glDrawElements(GL_TRIANGLES, 9, GL_UNSIGNED_INT, 0);
		// Swap the back buffer with the front buffer
		glfwSwapBuffers(window1);
		// Take care of all GLFW events
		glfwPollEvents();
    }

    // Terminate program and delete stuff
    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glDeleteBuffers(1, &EBO);
    glDeleteProgram(shaderProgram);

    glfwDestroyWindow(window1);
    glfwTerminate();
    return 0;
}
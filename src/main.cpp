#include <iostream>

#include "glad.h"
#include <GLFW/glfw3.h>

bool can_render(float v[]){ // A bad attempt at a function that tells you if a shape should even be rendered based off vertex input
    for (int i; i < sizeof(v) / 4; i++){   // Iterate through all the verticies put into the function
        if (v[i] < 1.0f && v[i] > -1.0f){ // If any of them are on screen, return true to render the whole thing
            return true;
        }
        if (i % 3 == 0){i++;} // Skip every third vertex, being the z vertex
    }
    return false; // If there are no verticies on screen, return false to say don't render any of it
}

const GLchar* vertexShaderSource = "#version 330 core\n"
"layout (location = 0) in vec3 aPos;\n"
"void main(){\n"
"   gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0);\n"
"}\0";

const GLchar* fragmentShaderSource = "#version 330 core\n"
"out vec4 FragColor;\n"
"void main(){\n"
"   FragColor = vec4(0.8f, 0.3f, 0.02f, 1.0f);\n"
"}\n\0";

// Did stuff work
void did_shader_compile(GLuint& shader){
    GLint success;
    GLchar infoLog[512];
    glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
    if (!success){
        glGetShaderInfoLog(shader, 512, NULL, infoLog);
        std::cout << "ERROR::SHADER::COMPILATION_FAILED\n" << infoLog;
    }
}
void did_program_work(GLuint& program){
    GLint success;
    GLchar infoLog[512];
    glGetProgramiv(program, GL_LINK_STATUS, &success);
    if (!success){
        glGetProgramInfoLog(program, 512, NULL, infoLog);
        std::cout << "ERROR::SHADER::LINKAGE_FAILED\n" << infoLog;
    }
}

void framebuffer_size_callback(GLFWwindow* window, int width, int height){ // If the window is to ever be resized,
    glViewport(0, 0, width, height);                                      // resize the viewport with it
    // Bottom left corner of window in px, top right corner of window in px
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
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    /* Tell GLFW we are using the CORE profile
    This means we only have modern functions */

    GLfloat verticies[9] = {
        -0.5f, -0.5f, 0.0f,
        0.5f, -0.5f, 0.0f,
        0.5f, 0.5f, 0.0f
    };

// Extra config for MacOS
#ifdef __APPLE__
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
#endif

    GLFWwindow* window1 = glfwCreateWindow(window1_width, window1_height, "LearnOpenGL", NULL, NULL); // Creation of window object
    // Width, height, name, do we want it fullscreen, "...the last thing is not important"
    if (window1 == NULL){ // Read the error message dumb*ss
        std::cout << "GLFW didn't make a window"; // Error message
        glfwTerminate(); // Stop GLFW
        return -1; // End the program
    }

    glfwMakeContextCurrent(window1); // Tell glfw that we wand to use that window (make it the current context)
    glfwSetFramebufferSizeCallback(window1, framebuffer_size_callback);
    // Sets the viewport resize command of the specified window to the specified command

    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)){ // If GLAD doesn't work, the whole program doesn't work,
        std::cout << "GLAD isn't working";                   // as GLAD handles function pointers for OpenGL
        return -1; // End program
    }

    //////////////////////////// VERTEX SHADER SHENANAGIANS ////////////////////////////
    GLuint VBO; // Create space the Vertex Buffer Object (id for a buffer)
    glGenBuffers(1, &VBO); // Give the var VBO a value, serving as an ID
    glBindBuffer(GL_ARRAY_BUFFER, VBO); // Bind the id of VBO to the GL_ARRAY_BUFFER
    glBufferData(GL_ARRAY_BUFFER, sizeof(verticies), verticies, GL_STATIC_DRAW); // Actually send the buffer over to the GPU
               // Which buffer, size of the buffer, data being sent, type of buffer (see below)
              // GL_STATIC_DRAW - Data is set once and used once
             // GL_STREAM_DRAW  - Data is set once and used at most a few times
            // GL_DYNAMIC_DRAW  - Data is set many times and used many times
    
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER); // Create and assign the vertex shader
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL); // Attach vertexShader source code to vertexShader object
    // Shader object to be compiled, #of strings in source code, shader source code, IDK
    glCompileShader(vertexShader); // Compile the shader
    did_shader_compile(vertexShader);

    //////////////////////////// FRAGMENT SHADER SHENANAGAINS ////////////////////////////
    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER); // Create and assign the fragment shader
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL); // Set the fragmentShader source to be the fragmentShaderSource
    glCompileShader(fragmentShader); // Compile the shader
    did_shader_compile(fragmentShader);

    //////////////////////////// SHADER PROGRAMS ////////////////////////////
    GLuint shaderProgram = glCreateProgram(); // Create and assign the shaderProgram
    glAttachShader(shaderProgram, vertexShader);    // Attach vertex shader to program
    glAttachShader(shaderProgram, fragmentShader); // Attach fragment shader to program
    glLinkProgram(shaderProgram); // Link the vertexShader and fragmentShader

    // Ready your engines
    while(!glfwWindowShouldClose(window1)){
        // Input
        proccessInput(window1); // Does what the name says

        // Rendering commands here
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f); // Set clear color
        glClear(GL_COLOR_BUFFER_BIT); // Tell OpenGL to use the clear command (config with line above)
                                     // on the GL_COLOR_BUFFER_BIT

        glUseProgram(shaderProgram);

        // Check and call events and swap the buffers
        glfwSwapBuffers(window1); // Swap front and back buffers
        glfwPollEvents(); // Checks for events (ex. keyboard input, mouse movement)
        // If this isn't here, the window will constantly not being responding
    }
    glfwTerminate(); // If all goes well, close the window and free up resources
    return 0; // End the program with 0
}
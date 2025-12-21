#include <iostream>

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

void framebuffer_size_callback(GLFWwindow* window, GLint width, GLint height){ // If the window is to ever be resized,
    glViewport(0, 0, width, height);                                      // resize the viewport with it
    // Bottom left corner of window in px, top right corner of window in px
}
void proccessInput(GLFWwindow* window){
    if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) // If escape key pressed
        glfwSetWindowShouldClose(window,true); // Set window_should_close to false
}

// Window Settings
const GLuint window1_width = 1280;
const GLuint window1_height = 720;

int main(){

    glfwInit(); // Init Window
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3); // Set major OpenGL version to 3
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3); // Set minor OpenGL version to 3
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    /* Tell GLFW we are using the CORE profile
    This means we only have modern functions */

    GLfloat verticies[] = {
         0.5f,  0.5f, 0.0f,
         0.5f, -0.5f, 0.0f,
        -0.5f, -0.5f, 0.0f,
        -0.5f,  0.5f, 0.0f
    };
    GLuint indecies[] = {
        0, 1, 3,
        1, 2, 3
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
    GLuint VAO, VBO, EBO; // Create id the Vertex Buffer and Array Objects

    glGenVertexArrays(1, &VAO); // Give the VAO an id
    glBindVertexArray(VAO);
    glGenBuffers(1, &VBO); // Give the var VBO a value, serving as an ID
    glBindBuffer(GL_ARRAY_BUFFER, VBO); // Bind the id of VBO to the GL_ARRAY_BUFFER
    glBufferData(GL_ARRAY_BUFFER, sizeof(verticies), verticies, GL_STATIC_DRAW); // Actually send the buffer over to the GPU
               // Which buffer, size of the buffer, data being sent, type of buffer (see below)
              // GL_STREAM_DRAW  - Data is set once and used at most a few times
             // GL_STATIC_DRAW  - Data is set once and used many times
            // GL_DYNAMIC_DRAW  - Data is set many times and used many times
    
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 12, (void*)0); // Teach OpenGL how to read the VAO
    // Which vertex attribute we want to configure (the ID I'd assume), # of points, data type, only matters if coordnates are int, stride (distance between points in bytes), offset of start of relavent data
    glEnableVertexAttribArray(0); // Activate VAO with a location of 0

    glBindBuffer(GL_ARRAY_BUFFER, 0);
    glBindVertexArray(0);

    ///////////////////////////// VERTEX SHADER SHENANAGAINS /////////////////////////////
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

    
    glEnableVertexAttribArray(0);

    // Ready your engines
    while(!glfwWindowShouldClose(window1)){
        // Input
        proccessInput(window1); // Does what the name says

        // Rendering commands here
        glClearColor(0.2f, 0.3f, 0.3f, 1.0f); // Set clear color
        glClear(GL_COLOR_BUFFER_BIT); // Tell OpenGL to use the clear command (config with line above)
                                     // on the GL_COLOR_BUFFER_BIT

        glUseProgram(shaderProgram);
        glBindVertexArray(VAO);
        glDrawArrays(GL_TRIANGLES, 0, 3);

        // Check and call events and swap the buffers
        glfwSwapBuffers(window1); // Swap front and back buffers
        glfwPollEvents(); // Checks for events (ex. keyboard input, mouse movement)
        // If this isn't here, the window will constantly not being responding
    }

    glDeleteVertexArrays(1, &VAO);
    glDeleteBuffers(1, &VBO);
    glDeleteProgram(shaderProgram);

    glfwTerminate(); // If all goes well, close the window and free up resources
    return 0; // End the program with 0
}
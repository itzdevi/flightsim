#version 330 core

in vec3 Normal;
out vec4 FragColor;

uniform vec3 fragColor;

void main() {
    FragColor = vec4(fragColor, 1.0);
    //FragColor = vec4(Normal, 1.0);
}
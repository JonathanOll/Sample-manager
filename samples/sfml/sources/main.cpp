#include "main.hpp"
#include "SFML/Graphics.hpp"

sf::RenderWindow window;
sf::Clock timer;
int SCREEN_WIDTH = 1280, SCREEN_HEIGHT = 720;


void setup() {
    window.create(sf::VideoMode(SCREEN_WIDTH, SCREEN_HEIGHT), "Window");
}

void display() {
    window.clear(sf::Color::Black);



    window.display();
}

void update(float dt) {

    

}

void handleEvent(sf::Event event) {

    if (event.type == sf::Event::Closed || (event.type == sf::Event::KeyPressed && event.key.code == sf::Keyboard::Escape)) 
        window.close();

}

int main() {

    setup();

    while (window.isOpen()) {

        sf::Event event;
        while (window.pollEvent(event)) 
            handleEvent(event);
        
        update(timer.restart().asMicroseconds());
        display();

    }


    return EXIT_SUCCESS;

}
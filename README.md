# 🚀 Asteroid Game

A classic arcade-style asteroid shooter game built with Python and Pygame as part of my learning journey with [Boot.dev](https://boot.dev/) courses. This project represents one of my first experiences with Python game development, game loops, and modern Python package management with `uv`.

## Learning Journey

This project was created while following the Boot.dev curriculum and served as an introduction to:
- **Python Game Development**: First hands-on experience with Pygame
- **Game Loop Architecture**: Understanding frame-based game mechanics
- **Modern Python Tooling**: Discovering `uv` package manager and virtual environments
- **Object-Oriented Programming**: Implementing game entities as classes
- **Physics Simulation**: Basic collision detection and movement systems

## ✨ Features

- **Smooth Player Movement**: Navigate your triangular spaceship with responsive controls
- **Dynamic Asteroid Field**: Asteroids spawn continuously from screen edges with varying sizes
- **Asteroid Splitting**: Large asteroids break into smaller pieces when shot
- **Collision Detection**: Advanced circular collision system between player, asteroids, and shots
- **Shooting Mechanics**: Fire shots with cooldown system to prevent spam
- **60 FPS Gameplay**: Smooth, consistent frame rate for optimal gaming experience

## 🎮 Controls

- **Q/D**: Rotate left/right
- **Z/S**: Move forward/backward
- **SPACEBAR**: Shoot (with 0.3s cooldown)

## 🛠️ Technical Details

### Game Components

- **Player**: Triangular spaceship with rotation and movement capabilities
- **Asteroids**: Three size categories that split when destroyed
- **Shots**: Small projectiles fired by the player
- **Asteroid Field**: Manages continuous spawning of asteroids from screen edges

### Key Game Mechanics

- **Asteroid Spawning**: New asteroids appear every 0.8 seconds from random screen edges
- **Collision System**: Circle-based collision detection for all game objects
- **Physics**: Velocity-based movement with delta time for frame-independent motion
- **Game Over**: Collision with asteroids ends the game

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- `uv` package manager (recommended) or pip

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Chriiiiiss/asteroid-game.git
   cd asteroid-game
   ```

2. **Install dependencies using uv** (modern Python package manager):
   ```bash
   # Install uv if you haven't already
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Create virtual environment and install dependencies
   uv sync
   ```

   **Alternative with pip**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install pygame==2.6.1
   ```

3. **Run the game**:
   ```bash
   # Using uv
   uv run python main.py

   # Or with activated virtual environment
   python main.py
   ```

## 🏗️ Project Structure

```
asteroid-game/
├── main.py           # Game entry point and main loop
├── player.py         # Player class with movement and shooting
├── asteroid.py       # Asteroid class with splitting mechanics
├── shot.py          # Shot projectile class
├── asteroidfield.py # Asteroid spawning system
├── circleshape.py   # Base class for circular game objects
├── constants.py     # Game configuration and constants
├── pyproject.toml   # Project dependencies and metadata (uv format)
├── uv.lock          # Dependency lock file for reproducible builds
└── README.md        # This file
```

## ⚙️ Configuration

Game settings can be modified in `constants.py`:

- **Screen Size**: 1280x720 pixels
- **Player Speed**: 200 pixels/second
- **Player Turn Speed**: 300 degrees/second
- **Asteroid Spawn Rate**: Every 0.8 seconds
- **Shot Cooldown**: 0.3 seconds
- **Asteroid Sizes**: 3 different size categories

## 🎯 Game Objective

Survive as long as possible by:
1. Avoiding collisions with asteroids
2. Shooting asteroids to break them into smaller pieces
3. Clearing smaller asteroids completely to reduce screen clutter

## What I Learned

Through this Boot.dev project, I gained experience with:
- **Game Loop Fundamentals**: Understanding the update-draw cycle
- **Sprite Management**: Using Pygame's sprite groups for organization
- **Delta Time**: Frame-independent movement calculations
- **Collision Detection**: Implementing circle-based collision systems
- **Virtual Environments**: Managing Python dependencies with `uv` and `venv`
- **Object-Oriented Design**: Structuring game entities as classes

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Score system
- Power-ups
- Sound effects
- Multiple lives
- Increasing difficulty levels

## 📝 License

This project is open source and available under the [LICENSE](LICENSE) file.

---

*Built with Python and Pygame | Learning with [Boot.dev](https://boot.dev/)*

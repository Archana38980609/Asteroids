# Asteroids Game 🚀
![Demo](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWZqd2s3bmgyb2J0Y2N1c25yb2p0bHh2eWQyaWUxYzk2cDZ1aXAwZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/QWApsc7AuxLibwfimf/giphy.gif)

Play the classic Asteroids game built in Python! Control a spaceship, shoot at asteroids, and avoid getting hit. The bigger asteroids split into smaller pieces when you destroy them, making the game harder as you play. Navigate through space, destroy asteroids, and survive as long as possible!

## 🎮 Quick Start

```bash
git clone https://github.com/Archana38980609/Asteroids.git
cd Asteroids
python3 main.py
```

## 📋 Prerequisites

- Python 3.10+
- Pygame 2.6.1
- The [uv](https://github.com/astral-sh/uv) package manager (optional)
- Access to a Unix-like shell (e.g., zsh, bash)

## 🚀 Features

- Smooth ship controls with rotation 
- Screen wraparound — fly off one edge and appear on the other
- Dynamic asteroid spawning from screen edges
- Asteroid splitting — large asteroids break into smaller ones when shot
- Collision detection with game over on impact
- Object-oriented design demonstrating Python best practices

## 📦 Installation

### Option 1: Using uv (recommended)

```bash
git clone https://github.com/Archana38980609/Asteroids.git
cd Asteroids
uv venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
uv add pygame==2.6.1
```


### Option 2: Using pip
```bash
git clone https://github.com/Archana38980609/Asteroids.git
cd Asteroids
pip install pygame==2.6.1
```

Or install from requirements:
```bash
pip install -r requirements.txt
```


## 🎯 How to Run

### With uv:
```bash
uv run python main.py
```


### With standard Python:

- On Linux/macOS:
```bash
python3 main.py
```


- On Windows:
```bash
python main.py
```


## 🎮 Controls

| Key      | Action               |
| -------- | -------------------- |
| ← / →    | Rotate ship left/right|
| ↑ / ↓    | Thrust forward/backward|
| Spacebar | Fire bullets         |

**Objective:** Destroy asteroids while avoiding collisions. Large asteroids split into smaller ones when hit!

## 🏗️ Project Structure
```bash
Asteroids/
├── main.py              # Game initialization and main loop
├── constants.py         # Game configuration and constants
├── player.py           # Player ship class and controls
├── asteroid.py         # Asteroid class and behavior
├── asteroidfield.py    # Asteroid spawning system
├── shot.py             # Bullet/projectile logic
├── circleshape.py      # Base collision detection class
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore rules
└── README.md          # This file
```


## 🛠️ Dependencies

- `pygame==2.6.1` — Game development library for graphics and input

## 🎓 Learning Objectives

This project demonstrates:

- Multi-file Python projects and module organization
- Object-oriented programming with inheritance and polymorphism
- Game development concepts such as collision detection and sprite management
- Vector mathematics for movement and rotation

---

Enjoy the game! 🎮✨














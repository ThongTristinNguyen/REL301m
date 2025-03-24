# Optimizing Snake Game with Reinforcement Learning

## Course: REL301m - Reinforcement Learning

## Table of Contents

- [Introduction](#introduction)
- [Installing Python and Required Libraries](#installing-python-and-required-libraries)
- [Running the Program](#running-the-program)
- [Managing Training Data](#managing-training-data)
- [References](#references)

---

## Introduction

This project is part of the REL301m course, designed to help students understand Reinforcement Learning (RL) through the Snake game. The project implements three different RL algorithms:

- **Q-learning**
- **SARSA**
- **Deep Q-Network (DQN)**

The AI learns to play Snake by trial and error, receiving rewards based on its actions. When the snake moves toward food, it earns a reward. Through an exploration-exploitation process, the AI gradually learns to make optimal decisions.

The main objective of this project is to develop an AI Bot capable of learning how to play Snake from scratch without any predefined rules. The AI will explore, optimize its movement strategy, and make decisions based on accumulated experience.

---

## Installing Python and Required Libraries

This project requires **Python 3.7+** and the following dependencies:

```bash
pip install pygame
pip install tensorflow
pip install -r requirements.txt
```

For Windows 7 users, installing `Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017, and 2019` is necessary for TensorFlow to function properly.

---

## Running the Program

To run the game, navigate to the project directory and execute:

```bash
python main.py
```

By default, the game runs in manual player mode. To view available modes, use:

```bash
python main.py --help
```

To switch to AI mode, modify `main.py` and select the appropriate algorithm:

```python
# Select AI mode
algo = AI_Player()      # Human player mode
# algo = AI_RuleBased()  # Rule-based AI
# algo = AI_RLQ()        # Q-learning - Training mode
# algo = AI_RLQ(False)   # Q-learning - Testing mode (no exploration)
# algo = AI_SARSA()      # SARSA - Training mode
# algo = AI_SARSA(False) # SARSA - Testing mode (no exploration)
# algo = AI_DQN()        # DQN - Training mode
# algo = AI_DQN(False)   # DQN - Testing mode (no exploration)
```

---

## Managing Training Data

### Q-learning & SARSA

Training data (Q-table) is stored in a JSON file:

```
q-table.json
```

To use a pre-trained model, rename the file to:

```
q-table-learned.json
```

The JSON file contains state-action pairs, helping the AI decide the optimal move based on Q-values:

```json
"[<  v],[-1,+0,+0]": [
    -1.92,
    1.62,
    4.67
]
```

Where:

- `"<  v"` represents the food’s position relative to the snake (Southwest direction).
- `[-1,+0,+0]` indicates an obstacle to the left (-1), while no obstacles are present ahead or to the right (+0).
- The values `[-1.92, 1.62, 4.67]` correspond to turning left, moving forward, and turning right.
- The AI selects the action with the highest Q-value (turning right in this case).

### Deep Q-Network (DQN)

DQN uses a neural network to learn gameplay strategies, with training data stored as model weights:

```
weights.hdf5
```

To use a pre-trained model, rename the file:

```
weights-learned.hdf5
```

---

## References

This project is inspired by the original repository: [Snake AI](https://github.com/cfoh/snake-game).

Additional references:

- Chris Watkins - "Learning from Delayed Rewards" (1989): [http://www.cs.rhul.ac.uk/~chrisw/thesis.html](http://www.cs.rhul.ac.uk/~chrisw/thesis.html)
- [How to Teach an AI to Play Games – Deep Reinforcement Learning](https://towardsdatascience.com/how-to-teach-an-ai-to-play-games-deep-reinforcement-learning-28f9b920440a)


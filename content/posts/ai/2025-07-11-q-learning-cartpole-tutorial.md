---
ShowToc: true
categories: [ai]
date: 2025-07-11
description: Q-Learning is one of the foundational reinforcement learning algorithms.
  In this beginner-friendly guide, you'll learn how it works and how to apply it to
  the CartPole environment using OpenAI Gym and Python.
draft: false
image: /img/qlearning-cartpole-cover.jpg
keywords: Q-learning, reinforcement learning, CartPole, OpenAI Gym, Python, RL tutorial, beginner-friendly AI, epsilon greedy, tabular RL
tags: [ai, reinforcement-learning, q-learning, openai-gym, python, ai-agents, ml-tutorial, cartpole, beginner]
title: 'Q-Learning and CartPole: Your First Reinforcement Learning Agent'
---

# Q-Learning and CartPole: Your First Reinforcement Learning Agent

If you’ve dipped your toes into reinforcement learning, chances are you’ve encountered **Q-Learning** — a classic, foundational algorithm that’s simple to understand yet powerful enough to teach you how AI agents can learn from rewards.

In this post, you’ll learn:

* What Q-Learning is and how it works
* Why it’s great for beginners
* How to apply it to a real environment: **CartPole** from OpenAI Gym
* A complete, working Python example

Let’s get started!

## Table of Contents
---
## 1. What Is Q-Learning?

Q-Learning is a **model-free reinforcement learning algorithm**. That means the agent doesn’t need to know how the environment works — it learns purely from experience.

The core idea is to build a **Q-table**, which stores the expected reward (or “quality”) for taking an action in a given state.

### The Q-Learning Update Rule:

```text
Q(s, a) ← Q(s, a) + α * (r + γ * max(Q(s’, a’)) - Q(s, a))
```

Where:

* `s`: current state
* `a`: action taken
* `r`: immediate reward received
* `s’`: new state after the action
* `α`: learning rate
* `γ`: discount factor (importance of future rewards)

Over time, the Q-values converge toward optimal choices — letting the agent figure out which actions are best in each state.

---

## 2. Why Use Q-Learning?

| Feature                 | Benefit                           |
| ----------------------- | --------------------------------- |
| Simple & intuitive      | Easy to understand for beginners  |
| No model of environment | Doesn’t need transition functions |
| Table-based             | Transparent and easy to debug     |

### Limitations?

Q-Learning doesn’t scale well to continuous or high-dimensional state spaces. For those cases, we use **Deep Q-Networks (DQN)** — but Q-Learning remains the best place to start.

---

## 3. About the CartPole Environment

In CartPole, a pole is attached to a cart on a track. The agent’s goal is to move the cart left or right to **keep the pole balanced**.

### Why it’s great for RL practice:

* Fast feedback (short episodes)
* Easy to visualize
* Small state/action space

### State space (continuous):

| Variable      | Description              |
| ------------- | ------------------------ |
| Cart position | Cart’s location on track |
| Cart velocity | Speed of the cart        |
| Pole angle    | Tilt of the pole         |
| Pole velocity | Angular velocity of pole |

We’ll discretize these values to build a tabular Q-learning solution.

---

## 4. Building a Q-Learning Agent for CartPole

### Step 1: Discretize the State

CartPole’s state is continuous. To use Q-tables, we need to **map continuous values to discrete bins**.

```python
buckets = (1, 1, 6, 12)  # number of discrete bins for each variable
```

### Step 2: Setup Environment and Q-Table

```python
import gym
import numpy as np
import math

env = gym.make("CartPole-v1")

# Discretization setup
buckets = (1, 1, 6, 12)
q_table = np.zeros(buckets + (env.action_space.n,))
min_bounds = env.observation_space.low
max_bounds = env.observation_space.high
max_bounds[1] = 0.5
max_bounds[3] = math.radians(50)
min_bounds[1] = -0.5
min_bounds[3] = -math.radians(50)
```

### Step 3: Discretization Function

```python
def discretize(obs):
    ratios = [(obs[i] - min_bounds[i]) / (max_bounds[i] - min_bounds[i]) for i in range(len(obs))]
    new_obs = [int(round((buckets[i] - 1) * min(max(ratios[i]0), 1))) for i in range(len(obs))]
    return tuple(new_obs)
```

### Step 4: Training Loop

```python
alpha = 0.1
gamma = 0.99
epsilon = 1.0
epsilon_min = 0.01
epsilon_decay = 0.995
episodes = 1000

for ep in range(episodes):
    obs = discretize(env.reset())
    done = False
    total_reward = 0

    while not done:
        if np.random.random() < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[obs])

        next_obs_raw, reward, done, _, = env.step(action)
        next_obs = discretize(next_obs_raw)

        q_old = q_table[obs + (action,)]
        q_max = np.max(q_table[next_obs])
        q_table[obs + (action,)] = q_old + alpha * (reward + gamma * q_max - q_old)

        obs = next_obs
        total_reward += reward

    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    if (ep + 1) % 100 == 0:
        print(f"Episode {ep + 1}, Total Reward: {total_reward}")

env.close()
```

---

## 5. Output and Evaluation

After a few hundred episodes, the agent starts to get better at balancing the pole. You’ll notice:

* Rewards increase steadily
* Agent chooses better actions
* Episodes last longer

You can tune `buckets`, `alpha`, `gamma`, or `epsilon` to get even better performance.

---

## 6. What Comes After Q-Learning?

Q-Learning works well for small or discretized problems. But what about more complex environments?

Enter **DQN (Deep Q-Networks)** — which replace the Q-table with a neural network.

We’ll explore that in the next post.

---

## 7. Summary

| Concept        | Recap                                                |
| -------------- | ---------------------------------------------------- |
| Q-Learning     | Learns the value of state-action pairs using a table |
| CartPole       | Classic OpenAI Gym environment for learning RL       |
| Discretization | Converts continuous state to discrete bins           |
| Epsilon-greedy | Balances exploration and exploitation                |

Q-Learning gives you the essential building blocks for understanding how RL agents learn from rewards. It’s an ideal first step into the world of AI agents.
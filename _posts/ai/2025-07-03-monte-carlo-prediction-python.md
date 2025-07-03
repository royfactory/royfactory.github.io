---
categories: ai
cover: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
date: 2025-07-03
description: Learn Monte Carlo Prediction in Reinforcement Learning with Python. Complete
  tutorial covering MCP algorithm, Blackjack simulation, value estimation, and practical
  implementation using OpenAI Gym.
image: /img/blur-background-1680x1050-spectrum-electromagnetic-4k-901-1.jpg
keywords: monte carlo prediction, reinforcement learning, python, MCP, blackjack simulation,
  value estimation, OpenAI gym, RL tutorial, machine learning
layout: post
organiser: Royfactory
tags: ai reinforcement-learning mcp montecarlo python gym rl blackjacksimulation value-estimation
title: 'Monte Carlo Prediction: Reinforcement Learning with Python (MCP Tutorial)'
toc: true
---

# Monte Carlo Prediction: Reinforcement Learning with Python (MCP Tutorial)

In this tutorial, we’ll explore **Monte Carlo Prediction (MCP)** — a fundamental method in **Reinforcement Learning** used to estimate the value of states using experience.

We’ll apply MCP to the **Blackjack-v1** environment from the `gymnasium` library and walk through the core logic with clear Python code.

---

## 1. What is Monte Carlo Prediction?

Monte Carlo Prediction estimates the **value of a state** as the **average return** (total reward) received after visiting that state across multiple episodes.

Key ideas:
- Run **full episodes** from start to finish
- Track returns from each state
- Compute average return as value estimate

Mathematically, the state value is:

\[
V(s) = \mathbb{E}[G_t | S_t = s]
\]

Where:
- \( V(s) \) is the estimated value of state \( s \)
- \( G_t \) is the total return from time \( t \) onward

---

## 2. Setup

Install the `gymnasium` package and ensure Python 3.8+ is available.

```bash
pip install gymnasium
````

Then import the libraries:

```python
import gym
import numpy as np
from collections import defaultdict
```

---

## 3. Blackjack Environment

Initialize the Blackjack environment with the `sab=True` flag for usable state representation.

```python
env = gym.make('Blackjack-v1', sab=True)
```

---

## 4. Episode Generator and Policy

Define a simple policy:

* **Stick (0)** if player sum ≥ 20
* **Hit (1)** otherwise

```python
def simple_policy(state):
    return 0 if state[0] >= 20 else 1

def generate_episode(env, policy):
    episode = []
    state = env.reset()[0]
    while True:
        action = policy(state)
        next_state, reward, terminated, truncated, _ = env.step(action)
        episode.append((state, action, reward))
        state = next_state
        if terminated or truncated:
            break
    return episode
```

---

## 5. Monte Carlo Prediction Loop

Now we collect episodes and calculate state values using first-visit Monte Carlo prediction.

```python
returns_sum = defaultdict(float)
returns_count = defaultdict(int)
V = defaultdict(float)

num_episodes = 500000

for i in range(num_episodes):
    episode = generate_episode(env, simple_policy)
    visited_states = set()
    G = 0
    for t in reversed(range(len(episode))):
        state, _, reward = episode[t]
        G = reward + G
        if state not in visited_states:
            returns_sum[state] += G
            returns_count[state] += 1
            V[state] = returns_sum[state] / returns_count[state]
            visited_states.add(state)
```

---

## 6. Sample Output

Print a few estimated state values:

```python
for state in list(V.keys())[:10]:
    print(f"State: {state}, Estimated Value: {V[state]:.2f}")
```

Example output:

```
State: (13, 6, False), Estimated Value: -0.48
State: (20, 10, True), Estimated Value: 0.53
State: (18, 5, False), Estimated Value: 0.18
...
```

---

## 7. Summary

* Monte Carlo Prediction is **simple yet powerful** for estimating value functions.
* It works by **averaging returns from real episodes**, making it suitable when a model of the environment is not available.
* The approach requires **many episodes** to converge, but can be effective for small to mid-sized state spaces.

---

## Conclusion

We implemented Monte Carlo Prediction using the `Blackjack-v1` environment. This method provides a foundational tool in reinforcement learning and can be adapted to many tasks.

In future posts, we’ll compare this to **Temporal Difference Learning (TD)** and explore **policy evaluation and improvement** techniques.

---

## Recommended Titles

* "Monte Carlo Prediction in Python: A Beginner-Friendly RL Tutorial"
* "How to Estimate State Values with Monte Carlo (Blackjack Example)"
* "From Episodes to Value: Monte Carlo Prediction with Gym"
---
ShowToc: true
categories: [ai]
date: 2025-07-10
description: DQN (Deep Q-Network) is one of the most fundamental deep reinforcement
  learning algorithms. In this beginner-friendly tutorial, you'll learn what DQN is,
  why it matters, and how to use it to solve the classic CartPole environment using
  PyTorch and OpenAI Gym.
draft: false
image: /img/dqn-cartpole-cover.jpg
keywords: DQN, Deep Reinforcement Learning, CartPole, OpenAI Gym, PyTorch, Q-Learning,
  RL tutorial, AI agents, machine learning beginner
tags: [ai reinforcement-learning dqn gym pytorch q-learning deep-rl cartpole ml-tutorial]ai-agents
title: 'Mastering CartPole with DQN: Deep Reinforcement Learning for Beginners'
---

# Mastering CartPole with DQN: Deep Reinforcement Learning for Beginners

If you've played with reinforcement learning (RL) before, you've probably seen the classic CartPole balancing problem. And if you've tried solving it with traditional **Q-learning**, you might have run into some limitations.

That’s where **DQN** — Deep Q-Network — comes in.

In this guide, we’ll explain what DQN is, why it was a breakthrough in RL, and how to implement it step-by-step to solve the CartPole-v1 environment using **OpenAI Gym** and **PyTorch**. Whether you're new to RL or ready to level up from Q-tables, this tutorial is for you.

## Table of Contents
---
## 1. What is DQN?

Q-Learning works well for problems with small, discrete state spaces. But in the real world — or even a simple simulation like CartPole — the **state is continuous**, and creating a Q-table for every possible state is infeasible.

**DQN** solves this by using a **neural network to approximate the Q-function**. Instead of a table, the network learns to predict the expected reward for each action, given a state.

### DQN = Q-Learning + Deep Learning

| Component       | Purpose                          |
|----------------|----------------------------------|
| Neural Network | Predict Q-values for each action |
| Replay Buffer  | Store past experiences            |
| Target Network | Improve stability                 |
| ε-greedy Policy| Balance exploration vs. exploitation |

This combination enables DQN to scale to more complex environments — including Atari games, robotics, and beyond.

---

## 2. Recap: The CartPole Problem

In CartPole, your agent controls a cart with a pole attached to it. The goal? Keep the pole from falling over by moving the cart left or right.

### Environment Details:

- **State Space**: 4 floating point values (position, velocity, pole angle, angular velocity)
- **Action Space**: 0 (left), 1 (right)
- **Reward**: +1 for every time step the pole remains upright
- **Done**: When the pole falls beyond a threshold angle, or the cart moves too far from center

It’s a great starting point for reinforcement learning.

---

## 3. Why Q-Learning Isn’t Enough

Traditional Q-Learning relies on a Q-table that maps state-action pairs to expected rewards. That works for games like FrozenLake or GridWorld, but fails when:

- States are **continuous**
- The environment has **high dimensionality**
- We want to **generalize** across unseen states

DQN overcomes these by using a function approximator — a neural net — to estimate Q-values, enabling RL to move beyond toy problems.

---

## 4. DQN Components Explained

Let’s break down what you’ll need to build a working DQN agent.

### 1. Neural Network

The core of DQN is a network that takes in a state and outputs Q-values for all possible actions.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super().__init__()
        self.fc1 = nn.Linear(state_dim, 128)
        self.fc2 = nn.Linear(128, 128)
        self.out = nn.Linear(128, action_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.out(x)
````

---

Stores past experiences and samples them randomly to break temporal correlation.

```python
from collections import deque
import random

class ReplayBuffer:
    def __init__(self, capacity):
        self.buffer = deque(maxlen=capacity)

    def push(self, transition):
        self.buffer.append(transition)

    def sample(self, batch_size):
        return random.sample(self.buffer, batch_size)

    def __len__(self):
        return len(self.buffer)
```

---

The agent explores randomly at first, then gradually exploits what it has learned.

```python
def select_action(state, epsilon, policy_net):
    if random.random() < epsilon:
        return random.randint(0, 1)
    with torch.no_grad():
        return policy_net(state).argmax().item()
```

---

## 5. Training DQN on CartPole

### Step-by-Step Loop:

```python
import gym
import numpy as np
import torch.optim as optim

env = gym.make("CartPole-v1")
state_dim = env.observation_space.shape[0]
action_dim = env.action_space.n

policy_net = DQN(state_dim, action_dim)
target_net = DQN(state_dim, action_dim)
target_net.load_state_dict(policy_net.state_dict())

optimizer = optim.Adam(policy_net.parameters(), lr=1e-3)
replay_buffer = ReplayBuffer(10000)

batch_size = 64
gamma = 0.99
epsilon = 1.0

for episode in range(300):
    state = torch.FloatTensor(env.reset())
    total_reward = 0

    for t in range(500):
        action = select_action(state, epsilon, policy_net)
        next_state, reward, done, _ = env.step(action)
        next_state = torch.FloatTensor(next_state)

        replay_buffer.push((state, action, reward, next_state, done))
        state = next_state
        total_reward += reward

        if len(replay_buffer) >= batch_size:
            transitions = replay_buffer.sample(batch_size)
            s, a, r, ns, d = zip(*transitions)

            s = torch.stack(s)
            a = torch.LongTensor(a).unsqueeze(1)
            r = torch.FloatTensor(r).unsqueeze(1)
            ns = torch.stack(ns)
            d = torch.FloatTensor(d).unsqueeze(1)

            q_values = policy_net(s).gather(1, a)
            next_q = target_net(ns).max(1)[0].unsqueeze(1).detach()
            target = r + gamma * next_q * (1 - d)

            loss = F.mse_loss(q_values, target)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        if done:
            break

    epsilon = max(0.01, epsilon * 0.995)

    if episode % 10 == 0:
        target_net.load_state_dict(policy_net.state_dict())

    print(f"Episode {episode}, Total Reward: {total_reward}")
```

---

## 6. Observations and Performance

As training progresses:

* The total reward per episode increases
* The agent starts keeping the pole upright for longer durations
* Eventually, it consistently reaches the max score of 200

This is a solid indicator that the DQN is learning to solve the task effectively.

---

## 7. DQN Limitations and Next Steps

While DQN is powerful, it's not perfect:

* It can be **unstable** or **divergent** without tricks
* It struggles with **continuous action spaces**
* It treats all experiences equally in the replay buffer

### Enhancements (aka “Better DQN”):

* **Double DQN**: Reduces overestimation bias
* **Dueling DQN**: Separates state value and action advantage
* **Prioritized Experience Replay**: Focus on important transitions
* **Rainbow DQN**: Combines all of the above

We’ll explore these in future posts.

---

## 8. Conclusion

You’ve just implemented your first **Deep Q-Network** from scratch and trained it to solve CartPole. This is a big step toward mastering reinforcement learning with deep learning.

By understanding both the **code** and the **concepts**, you’re ready to explore more complex environments and powerful variants of DQN.
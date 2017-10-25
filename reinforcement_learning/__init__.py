import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    last_step = env.step(env.action_space.sample()) # take a random action
    if last_step[2]:
        env.reset()

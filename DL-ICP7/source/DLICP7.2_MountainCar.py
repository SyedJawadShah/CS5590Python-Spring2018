import gym
space = gym.make('MountainCar-v0')
for i in range(50):
    sample = space.reset()
    for t in range(100):
        space.render()
        print(sample)
        action = space.action_space.sample()
        sample, reward, done, info = space.step(action)
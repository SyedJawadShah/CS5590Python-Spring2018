import gym

game = gym.make('CartPole-v0')
for i in range(50):
    sample = game.reset()
    for t in range(100):
        game.render()
        print(sample)
        action = game.action_space.sample()
        sample, reward, done, info = game.step(action)
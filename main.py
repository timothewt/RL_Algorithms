import gymnasium as gym
import torch

from algorithms.A2C import A2C
from algorithms.DQN import DQN
from algorithms.REINFORCE import REINFORCE


if __name__ == "__main__":
	env = gym.make("CartPole-v1")

	# TODO : Ajouter actions continues
	# TODO : Paralléliser les environnements

	device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

	algo = A2C(config={
		"env": env,
		"device": device,
		"actor_hidden_layers_nb": 2,
		"actor_hidden_size": 64,
		"critic_hidden_layers_nb": 2,
		"critic_hidden_size": 64,
		"gamma": .99,
		"actor_lr": .001,
		"critic_lr": .0007,
		"log_freq": 20,
		"t_max": 10,
		"ent_coef": .001,
	})

	algo.train(max_steps=10_000, plot_training_stats=True)

	env.close()

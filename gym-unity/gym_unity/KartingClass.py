import gym

from baselines import ppo2
from baselines import logger

from gym_unity.envs import UnityEnv

def main():
    env = UnityEnv("./envs/classicRoad1", 1, use_visual=False, uint8_visual=False,)
    logger.configure('./logs') # Çhange to log in a different directory
    act = ppo2.learn(
        env,
        "cnn", # conv_only is also a good choice for GridWorld
        lr=2.5e-4,
        total_timesteps=1000000,
        buffer_size=50000,
        exploration_fraction=0.05,
        exploration_final_eps=0.1,
        print_freq=20,
        train_freq=5,
        learning_starts=20000,
        target_network_update_freq=50,
        gamma=0.99,
        prioritized_replay=False,
        checkpoint_freq=1000,
        checkpoint_path='./logs', # Change to save model in a different directory
        dueling=True
    )
    print("Saving model to unity_model.pkl")
    act.save("unity_model.pkl")

if __name__ == '__main__':
    main()

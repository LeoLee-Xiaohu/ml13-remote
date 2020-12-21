''' from gym_unity.envs import UnityToGymWrapper

unity_env = UnityEnvironment("3DBall")
env = UnityToGymWrapper(unity_env, 0, use_visual=True, uint8_visual=True)
'''

from gym_unity.envs import UnityToGymWrapper

env = UnityToGymWrapper('3DBall', 0, use_visual=False, uint8_visual=Ture)
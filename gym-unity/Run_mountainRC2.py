#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 12:17:25 2020

@author: Rui
"""
import matplotlib.pyplot as plt
import numpy as np
import sys

from gym_unity.envs import UnityEnv

'''%matplotlib inline'''

print("Python version:")
print(sys.version)

# check Python version
if (sys.version_info[0] < 3):
    raise Exception("ERROR: ML-Agents Toolkit (v0.3 onwards) requires Python 3")



env_name = "/Users/Rui/ml-agents/gym-unity/gym_unity/envs/mountainRoadC2.app"  # Name of the Unity environment binary to launch
env = UnityEnv(env_name, worker_id=0, use_visual=True)

# Examine environment parameters
print(str(env))
import numpy as np
import utils.paramUtil as paramUtil
from utils.plot_script import *

# Specify the file path
file_path = './gen_motion_00_L160_00_a.npy'
# Load the data from the .npy file
data = np.load(file_path) # shape (148, 22, 3)
t = 100
## Display the loaded data
print(data[t,:,:])

plot_3d_motion('test.mp4', paramUtil.t2m_kinematic_chain, data[0:1,:,:], title="Load animation data", fps=20)

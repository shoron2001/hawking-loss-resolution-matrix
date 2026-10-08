import matplotlib.pyplot as plt
import numpy as np

# Data from Section 7.1
steps = np.array(list(range(1, 10)))
v_drm = np.array([1, 3, 6, 1, 6, 3, 1, 9, 9])
# Generating a simulated Z-axis for spatial depth tracking
z_axis = np.linspace(10, 90, 9) 

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plotting the 3D string path
ax.plot3D(steps, v_drm, z_axis, color='#e74c3c', linewidth=3, marker='o', label='3D Data Channel')

# Customizing the 3D space
ax.set_title('3D Algorithmic Coordinate Reduction Suitability Lattice', fontsize=12, fontweight='bold')
ax.set_xlabel('Coordinate Steps (X)')
ax.set_ylabel('Modulo-9 Invariant (Y)')
ax.set_zlabel('Spatial Depth Spectrum (Z)')
ax.set_xticks(steps)
ax.set_yticks(range(1, 10))

ax.grid(True)
plt.show()

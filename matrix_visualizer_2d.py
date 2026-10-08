import matplotlib.pyplot as plt

# Data from Section 7.1
steps = list(range(1, 10))
v_drm = [1, 3, 6, 1, 6, 3, 1, 9, 9]

plt.figure(figsize=(8, 5))
plt.plot(steps, v_drm, marker='o', color='#1f77b4', linewidth=2.5, markersize=8, label='Invariant Wave Path')

# Graph customization
plt.title('2D Vector Trajectory Mapping (M9 Spectrum)', fontsize=12, fontweight='bold')
plt.xlabel('Coordinate Steps (X1 to X9)', fontsize=10)
plt.ylabel('Modulo-9 Invariant Output', fontsize=10)
plt.xticks(steps)
plt.yticks(range(1, 10))
plt.grid(True, linestyle='--', alpha=0.6)

# Annotating points
for i, val in enumerate(v_drm):
    plt.annotate(f'{val}', (steps[i], v_drm[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold')

plt.tight_layout()
plt.show()

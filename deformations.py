import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from scipy.special import sph_harm

# angular grid
theta = np.linspace(0, np.pi, 200)
phi = np.linspace(0, 2*np.pi, 200)
theta, phi = np.meshgrid(theta, phi)

# deformation parameters
l, m = 3, 0
beta = 0.3  # deformation strength
R0 = 1.0

# real spherical harmonic
Ylm = sph_harm(m, l, phi, theta)
Ylm_real = np.real(Ylm)

# surface radius
R = R0 * (1 + beta * Ylm_real)

# Cartesian coordinates
x = R * np.sin(theta) * np.cos(phi)
y = R * np.sin(theta) * np.sin(phi)
z = R * np.cos(theta)

# plot
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, facecolors=cm.coolwarm((Ylm_real-Ylm_real.min())/(Ylm_real.max()-Ylm_real.min())),
                rstride=2, cstride=2, linewidth=0, antialiased=False)
ax.set_box_aspect([1,1,1])
ax.axis("off")

plt.savefig(f"octupole_Y{l}{m}.pdf", bbox_inches='tight')
#plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

A = 1
B = 3
omega = 2*np.pi/10
N = 50
t = np.linspace(0,30,N)
#t
r = np.zeros((N,3))

r[:,0] = A*np.cos(omega*t)
r[:,1] = A*np.sin(omega*t)
r[:,2] = B*t

fig = plt.figure()

# Agrrgamos un plano 3D
ax1 = fig.add_subplot(111,projection='3d')

# Datos en array bi-dimensional


# plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
# Es necesario que los datos esten contenidos en un array bi-dimensional
ax1.scatter(r[:,0],r[:,1],r[:,2],s=100)

# Mostramos el gráfico
plt.show()


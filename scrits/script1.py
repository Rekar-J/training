import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    """
    Generate the Mandelbrot fractal set.
    """
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter):
    """
    Create the Mandelbrot set fractal image.
    """
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    fractal = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            c = x[i] + 1j * y[j]
            fractal[i, j] = mandelbrot(c, max_iter)

    return fractal

def plot_fractal(fractal, cmap="plasma"):
    """
    Plot the fractal image.
    """
    plt.figure(figsize=(10, 10))
    plt.imshow(fractal.T, extent=[xmin, xmax, ymin, ymax], cmap=cmap)
    plt.colorbar()
    plt.title("Mandelbrot Fractal")
    plt.xlabel("Real Part")
    plt.ylabel("Imaginary Part")
    plt.show()

# Parameters
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5  # Coordinate boundaries
width, height = 1000, 1000                     # Image dimensions
max_iter = 256                                 # Maximum iterations for the fractal

# Generate and plot the fractal
fractal = generate_fractal(xmin, xmax, ymin, ymax, width, height, max_iter)
plot_fractal(fractal)

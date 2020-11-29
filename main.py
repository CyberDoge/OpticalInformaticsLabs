import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate

a = 5
M = 4096
N = 512
b = N ** 2 / (4 * a * M)
gauss = lambda x: np.exp(-(x ** 2))
input_field = lambda x: np.exp(2j * np.pi * x) + np.exp(-5j * np.pi * x)

line = np.linspace(-a, a, N, endpoint=False)
plt.grid()
plt.title("Аmplitude and Phase gauss function")
plt.plot(line, np.absolute(gauss(line)))
plt.plot(line, np.angle(gauss(line)))
plt.show()


def fft(y, b, a):
    h = (b - a) / (N - 1)
    zeros = np.zeros(int((M - N) / 2))
    y = np.concatenate((zeros, y, zeros), axis=None)
    middle = int(len(y) / 2)
    y = np.concatenate((y[middle:], y[:middle]))
    Y = np.fft.fft(y, axis=-1) * h
    middle = int(len(Y) / 2)
    Y = np.concatenate((Y[middle:], Y[:middle]))
    Y = Y[int((M - N) / 2): int((M - N) / 2 + N)]
    return Y


line = np.linspace(-a, a, N, endpoint=False)
fft_y = fft(gauss(line), a, -a)
line = np.linspace(-b, b, N, endpoint=False)

plt.grid()
plt.title("Аmplitude and phase fft of gauss func")
plt.plot(line, np.absolute(fft_y))
plt.plot(line, np.angle(fft_y))
plt.show()


def custom_numeric_ft(a, b):
    step = 2 * b / (N - 1)
    Y = np.zeros(N, dtype=np.complex128)
    for i in range(len(Y)):
        u = -b + i * step
        Y[i] = integrate.quad(lambda x: np.exp(-(x ** 2) - 2 * np.pi * u * x * 1j), a, b)[0]
    return Y


line = np.linspace(-a, a, N, endpoint=False)
numeric_y = custom_numeric_ft(-a, a)

plt.grid()
plt.title("Аmplitude and Phase of custom numeric Fourier transmission")
plt.plot(line, np.absolute(numeric_y))
plt.grid()
plt.plot(line, np.angle(numeric_y))
plt.show()

plt.grid()
plt.title("Аmplitude of input field")
plt.plot(line, np.absolute(input_field(line)))
plt.grid()
plt.show()

plt.title("Phase of input field")
plt.plot(line, np.angle(input_field(line)))
plt.show()

line = np.linspace(-a, a, N, endpoint=False)
fft_y = fft(input_field(line), a, -a)
line = np.linspace(-b, b, N, endpoint=False)

plt.grid()
plt.title("Аmplitude and Phase fft of input field")
plt.plot(line, np.absolute(fft_y))
plt.plot(line, np.angle(fft_y))
plt.show()


def analytical_transformation(xi):
    return 7 * np.sin(10 * np.pi * xi) / (np.pi * (2 * xi ** 2 + 3 * xi - 5))

line = np.linspace(-a, a, N, endpoint=False)
plt.grid()
plt.title("Аmplitude and Phase of analytical solution of input field")
plt.plot(line, np.absolute(analytical_transformation(line)))
plt.plot(line, np.angle(analytical_transformation(line)))
plt.show()

gauss_2d = lambda x, y: np.exp(-x ** 2 - y ** 2)

line = np.linspace(-a, a, N, endpoint=False)
X, Y = np.meshgrid(line, line)
fig, arr = plt.subplots(1, 2, figsize=(15, 5))
amp = arr[0].imshow(np.absolute(gauss_2d(X, Y)), cmap='hot', interpolation='nearest')
phase = arr[1].imshow(np.angle(gauss_2d(X, Y)), cmap='hot', interpolation='nearest')
fig.colorbar(phase, ax=arr[1])
arr[0].set_title('Аmplitude Gauss 2d')
arr[1].set_title('Phase Gauss 2d')
plt.show()


def fft_2d(Z, a, b):
    for i in range(N):
        Z[:, i] = fft(Z[:, i], b, a)
    for i in range(N):
        Z[i, :] = fft(Z[i, :], b, a)
    return Z


line = np.linspace(-a, a, N, endpoint=False)
X, Y = np.meshgrid(line, line)
Z = gauss_2d(X, Y).astype(np.complex128)
fft_2d_z = fft_2d(Z, -a, a)
line = np.linspace(-b, b, N, endpoint=False)
X, Y = np.meshgrid(line, line)

fig, arr = plt.subplots(1, 2, figsize=(15, 5))
amp = arr[0].imshow(np.absolute(fft_2d_z), cmap='hot', interpolation='nearest')
arr[0].set_title('Аmplitude fft 3d gauss')
fig.colorbar(amp, ax=arr[0])
phase = arr[1].imshow(np.angle(fft_2d_z), cmap='hot', interpolation='nearest')
arr[1].set_title('Phase fft 3d gauss')
fig.colorbar(phase, ax=arr[1])
plt.show()

input_field_2d = lambda x, y: input_field(x) * input_field(y)

line = np.linspace(-a, a, N, endpoint=False)
fig, arr = plt.subplots(1, 2, figsize=(15, 5))
amp = arr[0].imshow(np.absolute(input_field_2d(X, Y)), cmap='hot', interpolation='nearest')
phase = arr[1].imshow(np.angle(input_field_2d(X, Y)), cmap='hot', interpolation='nearest')
fig.colorbar(phase, ax=arr[1])
arr[0].set_title('Аmplitude input field 3d')
arr[1].set_title('Phase input field 3d')
plt.show()


def analytical_transformation_2d(x, y):
    return analytical_transformation(x) * analytical_transformation(y)


line = np.linspace(-b, b, N, endpoint=False)
X, Y = np.meshgrid(line, line)
fig, arr = plt.subplots(1, 2, figsize=(15, 5))
amp = arr[0].imshow(np.absolute(analytical_transformation_2d(X, Y)), cmap='hot', interpolation='nearest')
phase = arr[1].imshow(np.angle(analytical_transformation_2d(X, Y)), cmap='hot', interpolation='nearest')
fig.colorbar(phase, ax=arr[1])
arr[0].set_title('Аmplitude analytical 3d')
arr[1].set_title('Phase analytical 3d')
plt.show()

line = np.linspace(-a, a, N, endpoint=False)
X, Y = np.meshgrid(line, line)
Z = input_field_2d(X, Y).astype(np.complex128)
fft_2d_z = fft_2d(Z, -a, a)
line = np.linspace(-b, b, N, endpoint=False)
X, Y = np.meshgrid(line, line)

fig, arr = plt.subplots(1, 2, figsize=(15, 5))
arr[0].set_title('Аmplitude input fft 3d')
fig.colorbar(arr[0].imshow(np.absolute(fft_2d_z), cmap='hot', interpolation='nearest'), ax=arr[0])
phase = arr[1].imshow(np.angle(fft_2d_z), cmap='hot', interpolation='nearest')
arr[1].set_title('Phase input fft 3d')
fig.colorbar(phase, ax=arr[1])
plt.show()

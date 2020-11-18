import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
a = 5
M = 4096
N = 512


gauss = lambda x: np.exp(-(x**2))
input_field = lambda x: x**2


line = np.linspace(-a, a, N, endpoint=False)
plt.grid()
plt.plot(line, np.absolute(gauss(line)))
plt.xlabel("x")
plt.ylabel("Аmplitude")
plt.show()

plt.grid()
plt.plot(line, np.angle(gauss(line)))
plt.xlabel("x")
plt.ylabel("Phase")
plt.show()

def fft(y, b, a, M, N):
    h = (b - a) / (N - 1)
    zeros = np.zeros(int((M - N) / 2))
    y = np.concatenate((zeros, y, zeros), axis=None)
    middle = int(len(y) / 2)
    y = np.concatenate((y[middle:], y[:middle]))
    Y = np.fft.fft(y, axis=-1) * h
    middle = int(len(Y) / 2)
    Y = np.concatenate((Y[middle:], Y[:middle]))
    Y = Y[int((M - N) / 2): int((M - N) / 2 + N)]
    interval = abs(N ** 2 / (4 * a * M))
    return Y, interval

line = np.linspace(-a, a, N, endpoint=False)
fft_y, interval = fft(gauss(line), a, -a, M, N)
line = np.linspace(-interval, interval, N, endpoint=False)

plt.grid()
plt.plot(line, np.absolute(fft_y))
plt.xlabel("x")
plt.ylabel("Аmplitude")
plt.show()
plt.grid()
plt.plot(line, np.angle(fft_y))
plt.xlabel("x")
plt.ylabel("Phase")

def fourier_transformation_numeric(a, b, M, N):
    interval = abs(N ** 2 / (4 * a * M))
    step = 2 * interval / (N - 1)
    Y = np.zeros(N, dtype=np.complex128)
    for i in range(len(Y)):
        u = -interval + i * step
        Y[i] = integrate.quad(lambda x: np.exp(-(x ** 2) -2 * np.pi * u * x * 1j), a, b)[0]
    return Y, interval

line = np.linspace(-a, a, N, endpoint=False)
numeric_y, interval = fourier_transformation_numeric(-a, a, M, N)
line = np.linspace(-interval, interval, N, endpoint=False)

plt.grid()
plt.plot(line, np.absolute(numeric_y))
plt.xlabel("x")
plt.ylabel("Аmplitude")

plt.grid()
plt.plot(line, np.angle(numeric_y))
plt.xlabel("x")
plt.ylabel("Phase")

line = np.linspace(-a, a, N, endpoint=False)
plt.grid()
plt.plot(line, np.absolute(input_field(line)))
plt.xlabel("x")
plt.ylabel("Аmplitude")
plt.show()

plt.grid()
plt.plot(line, np.angle(input_field(line)))
plt.xlabel("x")
plt.ylabel("Phase")
plt.show()

line = np.linspace(-a, a, N, endpoint=False)
fft_y, interval = fft(input_field(line), a, -a, M, N)
line = np.linspace(-interval, interval, N, endpoint=False)

plt.grid()
plt.plot(line, np.absolute(fft_y))
plt.xlabel("x")
plt.ylabel("Аmplitude")
plt.show()

plt.grid()
plt.plot(line, np.angle(fft_y))
plt.xlabel("x")
plt.ylabel("Phase")
plt.show()

def analytical_transformation(xi):
    return ((50 * np.pi**2 * xi ** 2 - 1) * np.sin(10 * np.pi * xi) + 10 * np.pi * xi * np.cos(10 * np.pi * xi))/ (2 * np.pi**3 * xi**3)

line = np.linspace(-a, a, N)
plt.grid()
plt.plot(line, np.absolute(analytical_transformation(line)))
plt.xlabel("x")
plt.ylabel("Аmplitude")
plt.show()

plt.grid()
plt.plot(line, np.angle(analytical_transformation(line)))
plt.xlabel("x")
plt.ylabel("Phase")
plt.show()

gauss_2d = lambda x, y: np.exp(-x ** 2 - y ** 2)

line = np.linspace(-a, a, N, endpoint=False)
X, Y = np.meshgrid(line, line)
fig, arr = plt.subplots(1, 2, figsize=(15,5))
amp = arr[0].imshow(np.absolute(gauss_2d(X, Y)), cmap='hot', interpolation='nearest')
phase = arr[1].imshow(np.angle(gauss_2d(X, Y)), cmap='hot', interpolation='nearest')
fig.colorbar(phase, ax=arr[1])
arr[0].set_title('Аmplitude')
arr[1].set_title('Phase')
plt.show()

def fft_2d(Z, a, b, N, M):
    for i in range(N):
        Z[:, i], area = fft(Z[:, i], b, a, M, N)
    for i in range(N):
        Z[i, :], area = fft(Z[i, :], b, a, M, N)
    return Z, area

line = np.linspace(-a, a, N, endpoint=False)
X, Y = np.meshgrid(line, line)
Z = gauss_2d(X, Y).astype(np.complex128)
fft_2d_z, area = fft_2d(Z, -a, a, N, M)
line = np.linspace(-area, area, N, endpoint=False)
X, Y = np.meshgrid(line, line)

fig, arr = plt.subplots(1, 2, figsize=(15,5))
amp = arr[0].imshow(np.absolute(fft_2d_z), cmap='hot', interpolation='nearest')
arr[0].set_title('Аmplitude')
fig.colorbar(amp, ax=arr[0])
phase = arr[1].imshow(np.angle(fft_2d_z), cmap='hot', interpolation='nearest')
arr[1].set_title('Phase')
fig.colorbar(phase, ax=arr[1])
plt.show()

input_field_2d = lambda x, y: input_field(x)*input_field(y)

line = np.linspace(-a, a, N, endpoint=False)
X, Y = np.meshgrid(line, line)
fig, arr = plt.subplots(1, 2, figsize=(15,5))
amp = arr[0].imshow(np.absolute(input_field_2d(X, Y)), cmap='hot', interpolation='nearest')
phase = arr[1].imshow(np.angle(input_field_2d(X, Y)), cmap='hot', interpolation='nearest')
fig.colorbar(phase, ax=arr[1])
arr[0].set_title('Аmplitude')
arr[1].set_title('Phase')
plt.show()

def analytical_transformation_2d(x, y):
    return analytical_transformation(x)*analytical_transformation(y)

line = np.linspace(-a, a, N, endpoint=False)
X, Y = np.meshgrid(line, line)
fig, arr = plt.subplots(1, 2, figsize=(15,5))
amp = arr[0].imshow(np.absolute(analytical_transformation_2d(X, Y)), cmap='hot', interpolation='nearest')
phase = arr[1].imshow(np.angle(analytical_transformation_2d(X, Y)), cmap='hot', interpolation='nearest')
fig.colorbar(phase, ax=arr[1])
arr[0].set_title('Аmplitude')
arr[1].set_title('Phase')
plt.show()

M = 256
N = 128
line = np.linspace(-a, a, N, endpoint=False)
X, Y = np.meshgrid(line, line)
Z = input_field_2d(X, Y).astype(np.complex128)
fft_2d_z, area = fft_2d(Z, -a, a, N, M)
line = np.linspace(-area, area, N, endpoint=False)
X, Y = np.meshgrid(line, line)

fig, arr = plt.subplots(1, 2, figsize=(15,5))
amp = arr[0].imshow(np.absolute(fft_2d_z), cmap='hot', interpolation='nearest')
arr[0].set_title('Аmplitude')
fig.colorbar(amp, ax=arr[0])
phase = arr[1].imshow(np.angle(fft_2d_z), cmap='hot', interpolation='nearest')
arr[1].set_title('Phase')
fig.colorbar(phase, ax=arr[1])
plt.show()

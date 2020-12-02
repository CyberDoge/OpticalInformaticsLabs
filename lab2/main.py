import matplotlib.pyplot as plt
import numpy as np

a = 10
N = 100000

line = np.linspace(-a, a, N, endpoint=False)
f = lambda x: np.sin(10*x)

ff = np.fft.fft(f(line), axis=-1)


plt.grid()
plt.title("Аmplitude and Phase of custom numeric Fourier transmission")
plt.plot(line, f(line))
plt.show()

plt.grid()
plt.title("Аmplitude and Phase gauss function")
plt.plot(line, np.absolute(ff))
plt.plot(line, np.angle(ff))
plt.show()

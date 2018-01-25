import matplotlib.pyplot as plt
belgium = [[0, 10860, 10860, 12470, 12470, 20780, 20780, 38080, 38080, 500000],
           [25, 25, 30, 30, 40, 40, 45, 45, 50, 50]]
germany = [[0, 7664, 7664, 52153, 52153,  250000, 250000, 500000],
           [0, 0, 15, 15, 42, 42, 45, 45]]
usa = [[0, 9525 * 0.8, 9525 * 0.8, 38700 * 0.8, 38700 * 0.8,  82500 * 0.8, 82500 * 0.8, 157500 * 0.8,
        157500 * 0.8,  200000 * 0.8, 200000 * 0.8, 500000 * 0.8, 500000 * 0.8, 500000],
       [10, 10, 12, 12, 22, 22, 24, 24, 32, 32, 35, 35, 37, 37]]
norway = [[0, 5465, 5465, 16900, 16900,  23790, 23790, 59805, 59805, 96205, 96205, 500000],
          [23, 23, 24.4, 24.4, 32.6, 32.6, 34.6, 34.5, 43.6, 43.6, 46.6, 46.6]]


plt.plot(belgium[0], belgium[1], linewidth=2.0, label='Belgium')
plt.plot(germany[0], germany[1], linewidth=2.0)
plt.plot(usa[0], usa[1], linewidth=2.0)
plt.plot(norway[0], norway[1], linewidth=2.0)

plt.axis([0, 500000, 0, 60])
plt.show()
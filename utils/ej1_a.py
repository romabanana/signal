import guandong as g
import matplotlib.pyplot as plt

t, y = g.gen_cuad(0, 1, 100, 10, 0)

#t, w= g.gen_sen(0, 1, 100, 2, 0)


plt.style.use("dark_background")
plt.plot(t, y)
#plt.plot(t, w)
plt.show()

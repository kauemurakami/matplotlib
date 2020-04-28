import matplotlib.pyplot as plt

x = [1,3,5,7]
y = [2,3,6, 10]

x2 =  [2,4,6,8]
y2 = [5,6,7,10]
plt.bar(x,y, color = 'red', label = 'Legen label 1')
plt.bar(x2,y2, color = 'blue', label = 'Legen label 2')
plt.legend()
plt.ylabel('altura media')
plt.xlabel('xlabel')
plt.title('titulo')
plt.show()

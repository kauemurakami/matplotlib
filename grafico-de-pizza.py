label = ['floresta', 'deserto']
dados = [40,60]

fig, ax = plt.subplots()
ax.pie(dados, labels= label, autopct='%1.f%%')
plt.show()

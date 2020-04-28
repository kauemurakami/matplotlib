import matplotlib.pyplot as plt

plt.plot([10,20,30,40],[1,10,7,8], label='Sala 1', color = 'red')
plt.plot([10,20,30,40],[3,12,7,10], label='Sala 1', color = 'red', linestyle = 'dashdot')
plt.plot([10,25,35,45], [1,15,9,12], label = 'Sala 2',  color = 'blue', linestyle = '--')
plt.ylabel('Alunos')
plt.xlabel('Notas')
plt.title('Relação aluno notas')
plt.legend()
plt.show()

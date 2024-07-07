aluno = dict()

aluno['nome'] = str(input("Informe o nome do aluno: "))
aluno['nota'] = float(input("Informe a nota do aluno: "))

print(f"O nome do aluno é {aluno['nome']}.")
print(f"A nota é {aluno['nota']}.")

if aluno['nota'] > 5:
   print("Aluno APROVADO.")
else:
   print("Aluno REPROVADO.")

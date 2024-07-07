# pessoas = {'nome': 'Rosane','idade': 52, 'sexo': 'feminino', 'cor': 'branca'}
# print(f"Meu nome é {pessoas["nome"]} , sou do sexo {pessoas["sexo"]}")


# print(f"As chaves sao {pessoas.keys()}")
# print(f"Os valores sao {pessoas.values()}")
# print(f"Os itenss sao {pessoas.items()}")

# # deleta um atributo
# print("deleta um atributo....")
# del pessoas['cor']

# print(f"As chaves sao {pessoas.keys()}")
# print(f"Os valores sao {pessoas.values()}")
# print(f"Os itenss sao {pessoas.items()}")


# ## atualiza o valor do nome
# print("altera um valor....")
# pessoas['nome'] = 'Joao'

# for k, v in pessoas.items():
#     print(f"{k} = {v}")


# ## adicionado nova chave
# print("dicionado nova chave....")
# pessoas['cidade'] = 'Rio'

# for k, v in pessoas.items():
#     print(f"{k} = {v}")


## LISTA de dicionario

brasil = []
estado1 = {'uf': 'Rio de janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'SAO PAULO', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0])
print(brasil[0]['sigla'])
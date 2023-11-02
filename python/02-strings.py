# String armazena uma sequência de caracteres
# Tudo o que tiver entre aspas é considerado uma string no Python
    # Podem ser duplas ou simples

# Para formatar o output, é possível usar o str.format
# Um par de colchetes são usados para substituir os argumentos na ordem que são passados
nome, idade = "Camile", 20
mensagem = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(mensagem)

# Indexes também podem ser especificados dentro dos colchetes, eles correspondem aos argumentos passados na função
    # O index começa no 0
x, y, z = 1,2,3
print('{0}, {1}, {2} e {0}'.format(x,y,z))

# É possivel nomear os argumentos
print('Hoje é um dia {adjetivo} e {clima}'.format(adjetivo = "agradável", clima = "ensolarado"))

# Pode ser usado com tuplas, dicionários, listas, etc
meu_dicionario = {'chave': 6, 'outra_chave': 7}
print("Minha outra chave é: {[outra_chave]}".format(meu_dicionario))

minha_lista = ['zero', 'um', 'dois']
print("o segundo elemento é {0[1]} e o terceiro é {0[2]} e minha primeira chave é {1[chave]}".format(minha_lista, meu_dicionario))


print('{:~^20}'.format('centered'))

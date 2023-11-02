# Variáveis são containers para armazenar valores de dados
# Para criar variáveis, é preciso especificar o nome e atrubuir um valor a ela: 
    # <variable name> = <valor>
    
# Não é necessário declarar uma variável antecipadamente ou o tipo de dado que ela irá receber
    # Atribuir um valor a variável é o suficiente para inicializá-la 
    # Quando o Python aloca a área necessária na memória, seu interpretador já escolhe o tipo adequado
x = "Python"   

# A função type() verifica o tipo de dado da variável
print(type(x))  # string

# As variáveis podem mudar de tipo depois de serem definidas
x = True    # bool
x = 2       # inr
    
# Não é possivel declarar variáveis com nomes de palavras reservadas do python
# Para verificar a lista de palavras reservadas:
import keyword
print(keyword.kwlist)

# Regras para declaração de variáveis:
    # Devem começar com uma letra ou _
    # O restante do nome da variável pode consistir em letras, numeros ou _
    # Espaços não são permitidos
    # São case sensitive, não diferenciam maiúsucla de minúscula

# Python usa o "=" para atribur valores para variáveis
    # O que estiver a esquerda do = é um nome para o objeto que está á direita
    
# É possível atribuir múltiplos valores para múltiplas variáveis
# A atribuição deve ser feita com a mesma quantidade de valores em ambos os lados
# Caso contrário, um erro será gerado
x, y, z = 1, 2, 3

# É possível extrair valores de uma lista e atribui-las em variáveis
frutas = ["Amora", "Morango", "Cereja"]
g, h, i = frutas

print(g) # Amoras
print(h) # Morangos
print(i) # Cerejas

# Se o número de variáveis ​​for menor que o número de valores, adicionar um * na última variável
# fará com que os valores restantes sejam atribuídos à variável como uma lista:
frutas = ["Amora", "Morango", "Cereja", "Melancia", "Pera"]
g, h, *i = frutas

print(g) # Amora
print(h) # Morango
print(i) # [Cereja, Melancia, Pera]

# Se o asterisco for adicionado a outra variável que não seja a último, 
# serão atribuidos valores à variável até que o número de valores restantes
# corresponda ao número de variáveis ​​restantes.
frutas = ["Amora", "Morango", "Cereja", "Melancia", "Pera"]
g, *h, i = frutas

print(g) # Amora
print(h) # ["Morango", "Cereja", "Melancia"]
print(i) # Pera

# É possivel atribuir um único valor para múltiplas variáveis
    # Atribuição em cascata
x = y = z = 5
print(x,y,z) # 5,5,5

# Há diferença quando se trata de modificar um objetos do tipo mutável (listas, dicionáiros, etc) 
# Abaixo, x e y estão referenciando o mesmo objeto
# Quando uma alteração é feita por meio da variável x, a mudança é refletida na variável y
x = y = [7,8,9]  
x[0] = 13
print(y)
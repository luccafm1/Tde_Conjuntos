# Luca Dias, Gabriel Vidal, Lucca Magalhães


# Para obter os pontos relativos a este trabalho, você deverá criar um programa, utilizando a linguagem Python, C, ou C++. Este programa, quando executado, irá apresentar os resultados de operações que serão realizadas entre dois conjuntos de dados.
# O programa que você desenvolverá irá receber como entrada do usuário vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de operações que estão descritas no arquivo, este número de operações será um inteiro; as linhas seguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código da operação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda e terceira linhas conterão os elementos dos conjuntos separados por virgulas. 
#A seguir está um exemplo entradas que podem existir em um teste para o programa que você irá desenvolver: 

# U
# 3, 5, 67, 7 
# 1, 2, 3, 4 
# I 
# 1, 2, 3, 4, 5 
# 4, 5 
# D 
# 1, A, C, 34 
# A, C, D, 23 
# C 
# 3, 4, 5, 5, A, B, R 
# 1, B, C, D, 1 

# Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e {𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U). A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados dos conjuntos identificados, e o resultado da operação. 
# No caso da união a linha de saída deverá conter a informação e a formatação mostrada a seguir: União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4} Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo de textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas e minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima. No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas e pontuadas conforme o exemplo de saída acima. 
# O uso de linhas extras na saída, ou erros de formatação, implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento. Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada contendo um número diferente de operações, operações com dados diferentes, e operações em ordem diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto no ambiente repl.it quanto no ambiente Github. Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com, no mínimo um arquivo de testes criado pelo próprio professor.

operadores = {'U': 'União', 'I': 'Interseção', 'C': 'Produto Cartesiano', 'D': 'Diferença'}

def operacao(string, file):
  listaA = set(next(file).strip().split(', '))
  listaB = set(next(file).strip().split(', '))

  if string in operadores:
    if string == 'U':
      resultado = listaA.union(listaB)
      resultado_formato = ', '.join(resultado)
    elif string == 'I':
      resultado = listaA.intersection(listaB)
      resultado_formato = ', '.join(resultado)
    elif string == 'D':
      resultado = listaA.difference(listaB)
      resultado_formato = ', '.join(resultado)
    elif string == 'C':
      resultado = [(x, y) for x in listaA for y in listaB]
      resultado_formato = ', '.join([f'({x}, {y})' for x, y in resultado])

    listaA_formato = ', '.join(listaA)
    listaB_formato = ', '.join(listaB)
    
    print(
      f"{operadores.get(string)}: conjunto 1: {{{listaA_formato}}}, conjunto 2: {{{listaB_formato}}}. Resultado: {{{resultado_formato}}}"
    )
    print()


#EXEMPLO 1: arquivo 1
with open("text.txt") as file:
  print('Arquivo 1')

  for line in file:

    if 'U' in line:
      operacao('U', file)
      
    elif 'I' in line:
      operacao('I', file)
      
    elif 'C' in line:
      operacao('C', file)
      
    elif 'D' in line:
      operacao('D', file)


#EXEMPLO 2: arquivo 2
with open("text2.txt") as file:
  print('Arquivo 2')

  for line in file:
    
    if 'U' in line:
      operacao('U', file)
      
    elif 'I' in line:
      operacao('I', file)
      
    elif 'C' in line:
      operacao('C', file)
      
    elif 'D' in line:
      operacao('D', file)


#EXEMPLO 3: arquivo 3
with open("text3.txt") as file:
  print('Arquivo 3')

  for line in file:
    
    if 'U' in line:
      operacao('U', file)
      
    elif 'I' in line:
      operacao('I', file)
      
    elif 'C' in line:
      operacao('C', file)
      
    elif 'D' in line:
      operacao('D', file)

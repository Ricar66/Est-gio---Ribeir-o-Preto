# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def pertence_fibonacci(num):

  a, b = 0, 1
  while b <= num:
    if b == num:
      return True
    a, b = b, a+b
  return False

# Solicita o número ao usuário
numero = int(input("Digite um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if pertence_fibonacci(numero):
  print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
  print(f"O número {numero} não pertence à sequência de Fibonacci.")  


#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
  
  def contar_as(texto):
      # Converte todo o texto para minúsculas para facilitar a contagem
    texto_minusculo = texto.lower()

      # Conta as ocorrências da letra 'a'
    contador = texto_minusculo.count('a')

    return contador

# Solicita ao usuário que digite uma string
texto = input("Digite um texto: ")

# Chama a função para contar as ocorrências da letra 'a' e imprime o resultado
quantidade_as = contar_as(texto)
print(f"A letra 'a' aparece {quantidade_as} vezes no texto.")

#3 Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

INDICE = 12
SOMA = 0
K = 1

while K < INDICE:
    K = K + 1; SOMA = SOMA + K; 

print(SOMA)
print("A soma dos números de 1 a 12 é: ", SOMA)

#4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, _9__
# b) 2, 4, 8, 16, 32, 64, _128__
# c) 0, 1, 4, 9, 16, 25, 36, __49__
# d) 4, 16, 36, 64, _100___
# e) 1, 1, 2, 3, 5, 8, __13__
# f) 2,10, 12, 16, 17, 18, 19, _20___

def proximo_elemento(sequencia):
  """
  Tenta descobrir o próximo elemento de uma sequência.

  Args:
    sequencia: Uma lista representando a sequência.

  Returns:
    O próximo elemento da sequência, caso seja possível determinar,
    ou None caso não haja uma regra clara.
  """

  # Sequências com regras claras
  if sequencia == sequencia[:len(sequencia)-1] + [sequencia[-1] + 2]:  
    return sequencia[-1] + 2
  elif all(x == 2**i for i, x in enumerate(sequencia)):  # Potências de 2
    return sequencia[-1] * 2
  elif all(x == i**2 for i, x in enumerate(sequencia)):  # Quadrados perfeitos
    return len(sequencia) ** 2
  elif all(x == (2*i)**2 for i, x in enumerate(sequencia, 1)):  # Quadrados de pares
    return (2 * (len(sequencia) + 1)) ** 2
  elif sequencia == [1, 1] + [x + y for x, y in zip(sequencia[2:], sequencia[1:])]:  # Fibonacci
    return sequencia[-1] + sequencia[-2]

  # Caso não haja uma regra clara, tenta continuar a sequência lógica
  return sequencia[-1] + 1

# Exemplos de uso
print(proximo_elemento([1, 3, 5, 7]))  # Saída: 9
print(proximo_elemento([2, 4, 8, 16, 32, 64]))  # Saída: 128
print(proximo_elemento([0, 1, 4, 9, 16, 25, 36]))  # Saída: 49
print(proximo_elemento([4, 16, 36, 64]))  # Saída: 100
print(proximo_elemento([1, 1, 2, 3, 5, 8]))  # Saída: 13
print(proximo_elemento([2, 10, 12, 16, 17, 18, 19]))

# 5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  
def descobrir_interruptores():
  """Descobre qual interruptor controla qual lâmpada em três salas.

  Retorna:
    Uma lista com três elementos, onde cada elemento representa o número do interruptor
    que controla a lâmpada naquela posição (1, 2 ou 3).
  """

  # Primeira ida: ligamos o interruptor 1 por alguns minutos, depois o interruptor 2
  # e observamos o estado da lâmpada em uma sala
  primeira_observacao = input("Estado da lâmpada na primeira ida (acesa, apagada e quente, ou apagada e fria): ")

  # Segunda ida: ligamos um dos interruptores restantes e observamos o estado da lâmpada em outra sala
  segunda_observacao = input("Estado da lâmpada na segunda ida (acesa ou apagada): ")

  # Lógica para determinar os interruptores
  if primeira_observacao == "acesa":
    # Interruptor 2 controla a primeira lâmpada
    if segunda_observacao == "acesa":
      # Interruptor que foi ligado na segunda ida controla a segunda lâmpada
      return [2, 1, 3] if primeira_observacao == "acesa" else [2, 3, 1]
    else:
      # Interruptor que foi ligado na segunda ida controla a terceira lâmpada
      return [2, 3, 1] if primeira_observacao == "acesa" else [2, 1, 3]
  elif primeira_observacao == "apagada e quente":
    # Interruptor 1 controla a primeira lâmpada
    if segunda_observacao == "acesa":
      # Interruptor que foi ligado na segunda ida controla a segunda lâmpada
      return [1, 3, 2]
    else:
      # Interruptor que foi ligado na segunda ida controla a terceira lâmpada
      return [1, 2, 3]
  else:
    # Interruptor 3 controla a primeira lâmpada
    if segunda_observacao == "acesa":
      # Interruptor que foi ligado na segunda ida controla a segunda lâmpada
      return [3, 2, 1]
    else:
      # Interruptor que foi ligado na segunda ida controla a terceira lâmpada
      return [3, 1, 2]

# Exemplo de uso
resultado = descobrir_interruptores()
print("A configuração dos interruptores é:", resultado)
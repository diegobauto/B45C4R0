from random  import choice
import interfaz

normal = ["HOLA", "OSO", "AMOR", "ADIOS"]
hard = ["DELICIOSO", "ROMANTICO", "TAMARINDO", "PROGRAMACION"]

def createWord():
  option = 0
  while option!=1 and option!=2:
    print("1. Fácil\n2. Dificíl")
    option = int(input("¿Qué dificultad desea?: "))
    if option == 1:
      word = choice(normal)
    elif option == 2:
      word = choice(hard)
  return word
  
def separate(word):
  final = []
  line = []
  for i in word:
    final.append(i)
    line.append("_")
  print(*final)
  print(*line)
  return final,line

def guessWord(final,line, letra):
  for i in range(10):
    char = letra.upper()
    if (char in final):
      for j in final:
        if j == char:
          #print(final.index(j))
          line[final.index(j)] = j
          final[final.index(j)] = "*"
    if final.count("*") == len(final):
      print("¡¡¡FELICIDADES HAS ADIVINADO LA PALABRA OCULTA!!!")
      break
    print(line)
    print(final)

def main():
  interfaz.InitWindow()
  word = createWord()
  final,line = separate(word)
  guessWord(final,line)

main()

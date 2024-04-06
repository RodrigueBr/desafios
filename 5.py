#Renan Rodrigues da Silva

#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(string):
  invertido = ""
  n = len(string)
  for i in range(n):
    invertido = invertido + (string[n - i - 1])
  return invertido

string = "dlroWolleH"
invertida = inverter_string(string)
print(f"String invertida: {invertida}")
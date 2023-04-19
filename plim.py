count = 0 

while count < 1:
  numero = int(input('Digite um número de 0 a 100: '))

  if numero >= 1 and numero <= 100:
    count1 = 0 
    count += 1
    
    while count1 < 100:
      count1 += 1
      
      if count1 % numero == 0:
        if count1 != 100:
          print("plim", end = ", ")
        else:
          print("plim")
      else:
        if count1 != 100:
          print(count1, end = ", ")
        else:
          print(count1)
  else:
    print("Você colocou um número inválido!")
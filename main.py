import random
secenek = []

a = input("BİLGE RANDOM'a hoş geldiniz eklemek istediğiniz seçeneği yazın:")
secenek.append(a)
a = input("eklemek istediğiniz seçeneği yazın:")
secenek.append(a)
a = input("eklemek istediğiniz seçeneği yazın(bitirmek için ise '1')yazın:")
if(a == 1):
 print(random.choice(secenek))
 a = input("eklemek istediğiniz seçeneği yazın(bitirmek için ise '1')yazın:")
 if(a != 1):
  a = input("eklemek istediğiniz seçeneği yazın(bitirmek için ise '1')yazın:")
  while (a != 1):
   print(secenek.append(a))
a = input("eklemek istediğiniz seçeneği yazın(bitirmek için ise '1')yazın:")

print("Le convertisseur décimal")
decimal=(int)(input("Saisir une valeur décimal : "))
base=(int)(input("Saisir une base de conversion (max 16) : "))
Reste = 0
strRes=""

while decimal>0:
    Reste = decimal % base
    decimal = decimal // base 
    if Reste<10 :
      strRes = str(Reste) + strRes
    elif Reste == 10 :
       strRes = "A" + strRes
    elif Reste == 11 :
      strRes = "B" + strRes
    elif Reste == 12 :
      strRes = "C" + strRes
    elif Reste == 13 :
      strRes = "D" + strRes
    elif Reste == 14 :
      strRes = "E" + strRes
    elif Reste == 15 :
      strRes = "F" + strRes

print("Le convertisseur en hexadécimal est de : " + strRes)
    
        


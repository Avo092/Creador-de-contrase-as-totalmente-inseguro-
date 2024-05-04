import random

contra = ("+","-","/","*","!","&","$","#","?","=","@","a", "b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s",
          "t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V",
          "W","X","Y","Z","1","2","3","4","5","6","7","8","9","0")
contraseña = ""
while True:
    largo = int(input("que tan larga quieres la contraseña? :"))

    for i in range(largo):
        contraseña += random.choice(contra)
       
    print(contraseña)

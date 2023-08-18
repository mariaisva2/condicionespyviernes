nombreUsuario = input("Digita tu nombre: ")
edadUsusario=int(input("Digita tu edad: "))
if edadUsusario>=0 and edadUsusario<= 15:
    print(f"querido {nombreUsuario},usted es un niño")
elif edadUsusario > 15 and edadUsusario<=28:
    print(f"querido {nombreUsuario},usted es un joven") 
elif edadUsusario>28 and edadUsusario<=60:
    print(f"querido {nombreUsuario},usted es un adulto") 
elif edadUsusario>60 and edadUsusario<110:    
    print(f"querido {nombreUsuario},usted es un sugar")     
else:
    print("edad invalida")    
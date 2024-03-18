bandas=[]


opcion=100 

while(opcion != 5 ):
    
    print("********FESTIVAL ALTAVOZ*******")
    print("*******************************")
    print("")
    print("1. Registrar Banda")
    print("2. Ver el Cartel del festival")
    print("3. Buscar Banda")
    print("4. Modificar Banda")
    print("5. Finalizar")    
    opcion= int(input("Digita una opcion: "))
    
    if opcion == 1:
        banda={}
        #se llena el objeto de la banda
        banda["id"]=int (input("Digite el id: "))
        banda["nombre"]=input("nombre: ")
        banda["genero"]= input("Genero: ")
        banda["costo"]=int(input("costo:"))
        ## como agrego un diccionario a una lista
        bandas.append(banda)
        
    elif opcion == 2:
       # Recorriendo una lista para imprimir sus elementos 
       for bandaAuxiliar in bandas:
           print(f"{bandaAuxiliar["id"]}--{bandaAuxiliar["nombre"]}")
    elif opcion ==3:
        # Buscando un elemento dentro de una lista 
        bandabuscada=input("Digita la banda que quieres buscar: ")
        for bandaAuxiliar in bandas:
            if bandaAuxiliar["nombre"]==bandabuscada:
                 print("oe la encontre")
            else:  
                print("no lo encontre")  
      
    elif opcion == 5:
        pass
    
    else:
        print("opcion invalida")
    

codigos = []
Nombre = []
precio = []
cantidades = []

opciones = 0

while opciones != 7:
        print("Opcion 1. Cargar productos")
        print("Opcion 2. mostrar productos")
        print("Opcion 3. buscar por codigo del productos")
        print("Opcion 4. ordenar por precio del productos")
        print("Opcion 5. mostrar menor stock")
        print("Opcion 6. Calcular valor total")
        print("Opcion 7. salir")

        opciones = int(input("Opcion: "))


        if opciones ==1: 
                

                codigo = int(input("Codigo: "))
                Nombres = input("Nombre: ")
                precios = int(input("precio: "))
                cantidad = int(input("Cantidades: "))
                
                codigos.append(codigo)
                Nombre.append(Nombres)
                precio.append(precios)
                cantidades.append(cantidad)
                
        elif opciones ==2:
                
                i = 0 
                while i <len(codigos):
                        print(codigos[i], Nombre [i], precio [i], cantidades [i])
                        i +=1

        elif opciones ==3:
                buscar = int(input("codigo: "))
                i = 0
                encontrado = False
                
                while i < len(codigos):
                        if codigos[i]== buscar:
                                print(Nombre[i], precio[i], cantidades [i])
                                encontrado = True
                                
                                i += 1
                                
                                if encontrado == False:
                                        print("No existe ese producto :(") 

        elif opciones ==4:
                 i = 0 
                 
                 while i < len(precio) -1:
                         j = 0
                         
                         while i < len(precio) -1:
                                 
                                 if precio[j] > precio[j+1]:
                                         precio[j], precio[j+1] = precio[j+1], precio [j]
                                         Nombre[j], Nombre[j+1] = Nombre[j+1], Nombre [j]
                                         codigos[j], codigos[j+1] = codigos[j+1], codigos [j]
                                         cantidades[j], cantidades[j+1] = cantidades[j+1], cantidades [j]
                                         j += 1
                                         i += 1
                                         print("Ordenado por precio")

        elif opciones == 5:
                if len(cantidades)> 0:
                        menor = cantidades[0]
                        i = 1
                        
                        while i < len(cantidades):
                                if cantidades[i]< menor:
                                        menor = cantidades[i]
                                        i += 1
                                        i = 0 
                                        
                                        while i <len(cantidades):
                                                if cantidades[i] == menor:
                                                        print(Nombre[i], "stock", cantidades [i])
                                                        i += 1
        elif opciones == 6:
                total = 0
                i = 0
                
                while i < len(precio):
                        
                        total += precio[i] * cantidades [i]
                        i += 1
                        
                        print("total: ", total )     
        elif opciones == 7:
                print("Saliste")
                                                                  




import numpy as np
print ("Calculadora\n")

print("--------------------")
print("* Menú de opciones *")
print("--------------------")

print("1. Ver texto")
print("2. Editar texto")
print("3. Operacion par")

numero = int(input("Introduce la opción deseada:"))

if numero == 1:

    # archivo-entrada.py
    with open ('codigo.txt','r') as f # Abre el archivo para lectura
    datos = ''.join(f.readlines()).replace('\n',';')
    codigo = np.matrix(datos)
    print(codigo)

elif numero == 2:
    n = int(input("Introduce la cantidad de números pares que desea imprimir: "))

    archivo = open("numero.txt", "w")  # Abre el archivo para escritura
    for num in range (1, n+1):
        if num %2 == 0:   
        # Solo los números pares para cada línea escribe los dos números
            archivo.write(f"{num}".ljust(4)+' || ' + f"{num+1} \n")    
            # Impresión con identificación de fila y con formato en 2 columnas


    archivo.close()   # Cierra el archivo
    
elif numero == 3:

    with open ('codigo.txt','r') as f # Abre el archivo para lectura
    datos = ''.join(f.readlines()).replace('\n',';')
    m = np.matrix(datos)
    f = open ('codigo.txt','r')
    codigo = f.read()
    in codigo =[[1,2],[5,7],[21,12],[4,-4]]
    resultado = []
    for fila in matriz:
      if len(fila)%2==0 : 
        suma = 0
        for elemento in fila: 
          suma += elemento 
        resultado.append(suma)       
        #si es par se hace la suma sin importar el numero de elementos que tenga solo los que estén en la fila  

      else:     
      #si es impar se multiplican todos los numeros que hay en la lista temporal 

            multi=1; 
            #auxiliar para almacenar el resultado del producto de los elementos de la lista temporal             

            for x in fila:              
            # recorremos dentro de cada listatemporal y hacemos los respectivos calculo 

                multi*=x;               
                # aqui hacemos el producto entre ellos 4x3x1 =12  

            resultado.append(multi)      
            # finalmente agregamos lo anterior a otra lista  
            
    print (resultado)                  
    #imprimimor el resutlado por pantalla 
    
else:
    print("La opción elegida no existe, vuelve a intentar.")

#Proyecto



clientes = {

}



    
def modificar_clientes():
    nombre = input("¿Que cliente quieres modificar?: ").capitalize()
    while nombre in clientes:
        dato = input("¿Que quieres modificar, teléfono o email?: ").lower()
        nuevo_valor = input("Introduce el nuevo valor: ")
        clientes[nombre][dato] = nuevo_valor
        respuesta = input("¿Quieres añadir otro cliente?: ").capitalize()
        if respuesta != ["Si","Sí"]:
            break
    else:
        print("Este cliente no existe")

    

def eliminar_clientes():
    nombre = input("¿Que cliente quieres eliminar?: ").capitalize()
    while nombre in clientes:
        del clientes[nombre]
        respuesta = input("¿Quieres eliminar otro cliente?: ").capitalize()
        if respuesta != ["Sí","Si"]:
            print("=Clientes eliminados correctamente=")
            break
    else:
        print("=Este cliente no exixste=")





def gestionar_clientes():
    opcion = 0
    while opcion != 5:
        print("1.Añadir clientes")
        print("2.Ver clientes")
        print("3.Modificar clientes")
        print("4.Eliminar clientes")
        print("5.Salir")
        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            respuesta = "Si"
            while respuesta in ["Sí","Si"]:
                cliente = input("Nombre del cliente: ").capitalize()
                telefono_cliente = int(input("Número de telefono: "))
                email_cliente = input("Introduce el email del cliente: ")
                clientes[cliente] = {
                    "telefono" :telefono_cliente,
                    "email" : email_cliente,
                    "Presupuesto":{

                    }
                }
                respuesta = input("¿Desea añadir otro cliente?: ").capitalize()
        elif opcion == 2:
            print("==CLIENTES==")
            clientes_ordenados = sorted(
            clientes.items(),
            key=lambda item:item[0]
            
        )
            
            for nombres,datos in clientes_ordenados:
                print(f"{nombres}")
                print(f"{datos["telefono"]}")
                print(f"{datos["email"]}\n")
                for producto in datos["Presupuesto"]:
                    print(producto)
                    print(f"Precio : {datos["Presupuesto"][producto]["precio"]}")
                    print(f"Cantidad : {datos["Presupuesto"][producto]["cantidad"]}")
                    print(f"Total : {datos["Presupuesto"][producto]["total"]}\n")
                    
        elif opcion == 3:
            modificar_clientes()
        elif opcion == 4:
            eliminar_clientes()
        elif opcion == 5:
            break



def crear_presupuesto():
    
    print("==CREAR PRESUPUESTO==")
    respuesta = "Sí"
    nombre = input("¿A que cliente le quieres añadir un presupuesto?: ").capitalize()
    while nombre in clientes and respuesta in ["Si","Sí"]:
        nombre_producto = input("Introduce el nombre del producto o servicio: ").capitalize()
        precio_producto = float(input("Introduce el precio del producto o servicio: "))
        cantidad_de_producto = int(input("Introduce la cantidad del producto o servicio: "))
        sub_total = cantidad_de_producto * precio_producto

        clientes[nombre]["Presupuesto"][nombre_producto] = {
                    "precio" : f"{precio_producto}€",
                    "cantidad" : f"{cantidad_de_producto}",
                    "total" : f"{sub_total}€"
                    }
        

        print("\n------RESULTADO PRODUCTO------")
        
        print(f"Producto o servicio: {nombre_producto}")
        
        print(f"Precio de producto o servicio: {precio_producto:.2f}")
        
        print(f"Cantidad de producto o servicio: {cantidad_de_producto}")

        print(f"Subtotal: {sub_total}€")

        respuesta = input("¿Desea añadir otro producto a este cliente?: ").capitalize()
        

    




def ver_presupuestos():
    if len(clientes) == 0:
        print("==PRESUPUESTOS==\n")
        print("-No hay presupuestos guardados\n")
    
    else:

        productos_ordenados = sorted(
            clientes.items(),
            key= lambda item: item[0],
            
        )
    
        for nombre,datos in productos_ordenados:
            print(f"{nombre}€")
            for producto in datos["Presupuesto"]:
                print(producto)
                print(f"{datos["Presupuesto"][producto]["precio"]}")
                print(f"{datos["Presupuesto"][producto]["cantidad"]}")
                print(f"{datos["Presupuesto"][producto]["total"]}")





        


def menu_principal():        
    opción = 0
    while opción != 4:
        print("===SISTEMA EMPRESA===")
        print("1.Gestionar clientes")
        print("2.Crear presupuesto")
        print("3.Ver presupuestos")
        print("4.Salir")
        opción = int(input("Introduce la opción: "))
        if opción == 1:
            gestionar_clientes()
        elif opción == 2:
            crear_presupuesto()
        elif opción == 3:
            ver_presupuestos
        elif opción == 4:
            break


print(menu_principal())
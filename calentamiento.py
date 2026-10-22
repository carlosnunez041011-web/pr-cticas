



'''class Gastos:
    def __init__(self):
        self.concepto = input("Introduce el concepto: ").capitalize()
        while True:
            try:
                self.importe = float(input("Introduce el importe: "))
                break
                
            except ValueError:
                print("ValueError , you must introduce a number")
                
        
        

    def final(self):
        return(f"{self.concepto}:{self.importe}€")


gasto_1 = Gastos()
print(gasto_1.final())'''



productos = {
    "pan":1.00,
    "hamburguesa":9.00,
    "leche":5.00,
    "pimiento":3.00
}


def pedir_productos(dict):
    lista_compra = {}
    while True:
        peticion = input("Introduce el producto(introduzca fin si no quiere añadir más productos): ").lower()
        if peticion == "fin":
            break
        if peticion in dict:
            precio =dict[peticion]
            lista_compra[peticion] = precio
        else:
            print("El producto no está disponible")
            
        
    return lista_compra

        



def lista_ordenada(dict): 
    print("---Lista de compra---\n")
    for producto,precio in dict.items():
        print(f"{producto}:{precio}€")
   


def suma_total(dict):
    total_sum = 0
    for num in dict.values():
        total_sum+= num
        
    return (f"\nTotal a pagar: {total_sum}€")

recibo =pedir_productos(productos)
lista_ordenada(recibo)
print(suma_total(recibo))








#peticion = "pan"
#precio = productos[peticion] te devuelve el valor de la clave "peticion" que es pan 
#print(precio) 

        





        









    
    




    

    




      
        


    
    





        

    
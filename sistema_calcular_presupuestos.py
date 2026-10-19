#sistema_calcular_presupuestos
def pedir_numero(mensaje): 
     while True: 
          try:
               numero = float(input(mensaje))
               return numero
          except ValueError:
               print("Error: introduce un número. Ej: 21")

total_presupuesto = 0

productos_o_servicios = []

cantidad = []
                                     #QUITAR LO DE def pedir_numero Y VOLVER A ESCRIBIRLO YO SOLO SIN COPIARLO
precios = []

respuesta = "si"
### MEJORAR EL PROGRAMA
while respuesta in ["si", "sí"]:
     
     nombre_unidad = input("Introduce el nombre del producto o servicio: ")

     precio_unidad = pedir_numero("Introduce el precio del producto o servicio: ")

     cantidad_de_unidad = pedir_numero("Introduce la cantidad del producto o servicio: ")

     moneda = "€"
     descuento_de_unidad = pedir_numero("Introduce el descuento del producto o servicio: ")

     gastos_adicionales = pedir_numero("Introduce los gastos adicionales (transporte; envio; etc): ")

     sub_total_1 = precio_unidad * cantidad_de_unidad

     dinero_descontado = sub_total_1 * (descuento_de_unidad / 100) 

     sub_total_2 = sub_total_1 - dinero_descontado + gastos_adicionales

     iva = sub_total_2 * (21 / 100)

     precio_final = sub_total_2 + iva

     total_presupuesto += precio_final
     # Guardar los datos en el dicconario 'catalogo'

     print("\n------RESULTADO PRODUCTO------")

     print(f"Producto o servicio: {nombre_unidad}")

     print(f"Precio de producto o servicio: {precio_unidad:.2f}")

     print(f"Cantidad de producto o servicio: {cantidad_de_unidad}")

     print(f"Dinero descontado: {dinero_descontado:.2f} {moneda}")

     print(f"IVA: {iva:.2f} {moneda}")

     print(f"Precio final del producto o servicio: {precio_final:.2f} {moneda}")

     productos_o_servicios.append(nombre_unidad)

     cantidad.append(cantidad_de_unidad)

     precios.append(precio_unidad)

     
     respuesta = input("¿Quiere añadir otro producto o servicio?, sí/no: ").strip().lower()

     

if respuesta not in ["si", "sí",]:
     
     print("\n========PRESUPUESTO FINAL========")

     print(f"\nProductos o servicios: {productos_o_servicios}")

     print(f"\nCantidad de productos o servicios: {cantidad}")

     print(f"\nPrecios por unidad de los productos o servicios: {precios}")

     print(f"\nTotal del presupuesto: {total_presupuesto:.2f} {moneda}")
         

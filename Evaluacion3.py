
lista_pedidos = []
ruta = []

nombre = None
direccion = None
comuna = None



def registar_pedidos():
    print("REGISTRO DE PEDIDO")
    print("Ingresar los datos del cliente.")
    nombre = input("Nombre y apellido: ")
    direccion = input("Dieccion: ")
    comuna = input("Comuna: ").lower()

    while True:

        CIL5 = 0
        CIL15 = 0
        CIL45 = 0


        print("Cilindros")
        print("1. 5 kg.")
        print("2. 15 kg.")
        print("3. 45 kg.")
        print("4. Terminar pedido.")
        try:
            seleccion = int(input("Ir a: "))
            if seleccion == 1:
                CIL5 = CIL5 +1 
            elif seleccion == 2:
                CIL15 = CIL15 + 1
            elif seleccion == 3:
                CIL45 == CIL45 + 1
            elif seleccion == 4:
                respuesta = input("¿Desea confirmar el pedido?(si/no): ").lower()
                if respuesta == "si":
                    print("Pedido realizado.")
                    break
                else:
                    print("No se ha realizado el pedido.")
                    return
            else: 
                print("Opción inválida. \n Debe seleccionar una opcion de 1 a 4.")


            pedido = {
                'Nombre: ': nombre,
                'Dirección: ': direccion,
                'Comuna' : comuna,
                'Cil. 5kg' : CIL5,
                'Cil 15kg' : CIL15,
                'Cil 45kg' : CIL45
                }
                
            lista_pedidos.append(pedido)
            ruta.append(comuna)

        except ValueError:
            print("Opción inválida. \n Debe seleccionar una opcion de 1 a 4. ")


def listar_pedidos():
    print("LISTA DE PEDIDOS")
    for elemento in lista_pedidos:
        print(elemento)
    

def hoja_ruta():
    print("HOJA DE RUTA")
    print("Sectores donde existen pedidos: ")
    for sectores in ruta:
        print(sectores)
    sector = input("Ir a la hoja de: ").lower()
    if sector in ruta:
        with open(f'ruta_{sector}.txt', 'w') as archivo:
            contenido = archivo.write()
    else:
        print("No se encontraron pedidos en ese sector.")
        return

def menu():
    while True:
        print("GAXPLOSIVE")
        print("1. Registrar pedido")
        print("2, Listar todos los pedidos")
        print("3. Imprimir hoja de ruta")
        print("4. Salir del programa")
        try:
            opcion = int(input("Ir a: "))
            if opcion == 1:
                registar_pedidos()
            elif opcion == 2:
                listar_pedidos()
            elif opcion == 3:
                hoja_ruta()
            elif opcion == 4:
                print("Saliendo del sistema.")
                break
            else:
                print("Opción inválida. \n Debe seleccionar una opcion de 1 a 4.")

        except ValueError:
            print("Opción inválida. \n Debe seleccionar una opcion de 1 a 4.")

menu()
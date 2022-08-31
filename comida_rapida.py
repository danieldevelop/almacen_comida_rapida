'''
Descripción:
    Almacén de comida rápida, donde se comprar productos y luego se genera un boleta
    electronica con los datos de la compra.
'''

import os;

def menu():
    print("Menu del Dia");
    print("============");
    print("1. Churrasco             $1.500");
    print("2. Completo Italiano     $2.680");
    print("3. Barros Luco           $3.580");


def boletaElectronica(cantidad):
    print("\n====== Boleta Electronica ======");
    print("Productos: \n"+
        f"Churrasco           {cantidad}  x  ${(cantidad * 1500)}\n"+
        f"Completo Italiano   {cantidad}  x  ${(cantidad * 2680)}\n"+
        f"BarrosLuco          {cantidad}  x  ${(cantidad * 3580)}"
    );
    print(f"\nSubTotal ${(cantidad * 1500) + (cantidad * 2680) + (cantidad * 3580)}");
    print("---------------------");
    print(f"Total ${(cantidad * 1500) + (cantidad * 2680) + (cantidad * 3580)}");



if __name__ == "__main__":
    os.system("cls");

    menu();
    inicioOrden = "s";
    cantidad = 0;

    while (inicioOrden == "s"):
        producto = int(input("\nQue desea ordenar: "));

        if (producto == 1):
            cantidad = cantidad + 1;
        if (producto == 2):
            cantidad = cantidad + 1;
        if (producto == 3):
            cantidad = cantidad + 1;

        inicioOrden = input("\nDesea ordenar otro producto? (s/n): ");

    boletaElectronica(cantidad);
#habitaciones disponibles en el hotel
habitaciones_dis=[1,2,3,4,5,6,7,8,9]
habitaciones_ocu=[] #se almacenará las habitaciones ya reservadas
while True:#bucle que se ejecuta despúes de cada interacción
    print("Reservas del Hotel")
    print("1.   Reservar habitación")
    print("2.   Ver habitaciones disponibles")
    print("3.   Cancelar reserva ")
    print("4.   Salir del sistema")
    opcion=int(input(""))
    
    if opcion==1:#reservar una habitación
        def reservas():
            print("Abriendo operación de reservas")
            dni = int(input("Ingrese su número de DNI: "))
            habitacion = int(input("¿Qué habitación desea?: "))
            fecha = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")

            if habitacion in habitaciones_ocu:
                print("Esta habitación ya se encuentra reservada")
            elif habitacion not in habitaciones_dis:
                print("La habitación ingresada no es válida")
            else:
                habitaciones_ocu.append(habitacion)
                habitaciones_dis.remove(habitacion)
                print("Habitación reservada con éxito")
                vacio=input()
        reservas()
    elif opcion==2:#mostrar las habitaciones que aún se encuentran disponibles
        def mostrar_habitaciones_disponibles():
            print(f"Las siguientes son las habitaciones disponibles: { habitaciones_dis}")
            vacio_=input()
        mostrar_habitaciones_disponibles()
    elif opcion==3:
        def cancelar_reserva():
            hab_cancelar = int(input("Ingresa el número de habitación a cancelar: "))
            if hab_cancelar in habitaciones_ocu:
                habitaciones_ocu.remove(hab_cancelar)
            if hab_cancelar not in habitaciones_dis:
                habitaciones_dis.append(hab_cancelar)
                print(f"Reserva de la habitación {hab_cancelar} cancelada con éxito.")
            else:
                print(f"La habitación {hab_cancelar} no está actualmente reservada.")
            vacio__=input()
        cancelar_reserva()
    elif opcion==4:
        print("Saliendo del sistema...")
        break
    
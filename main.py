from Remote.remote import Remote
from Remote.advancedremote import AdvancedRemote
from Device.radio import Radio
from Device.tv import Tv
from Device.smarttv import SmartTv


# ---------------------Integrantes---------------------
# Kathya Bilena González Coxaj - 1599019
# Diego Alejandro Hernández Hernández - 1627118
# -----------------------------------------------------

def interactuar(control) -> None:
    interaccion_dispositivo: int = 0
    tipo: str = control.__class__.__name__
    while (interaccion_dispositivo != 6 and tipo == 'Remote') or (interaccion_dispositivo != 7 and
                                                                  tipo == 'AdvancedRemote'):
        opciones: str = '\n1. Boton de apagado/encendido\n2. Bajar volumen\n3. Subir volumen\n4. Siguiente canal\n5. ' \
                        'Canal anterior'
        if tipo == 'AdvancedRemote':
            opciones += '\n6. Mutear\n7. Terminar interacción'
        else:
            opciones += '\n6. Terminar interacción'
        print(opciones)
        interaccion_dispositivo = int(input('Digite el número de la opción que desea ejecutar: '))
        if interaccion_dispositivo == 1:
            control.toggle_power()
        elif interaccion_dispositivo == 2:
            control.volume_down()
        elif interaccion_dispositivo == 3:
            control.volume_up()
        elif interaccion_dispositivo == 4:
            control.channel_up()
        elif interaccion_dispositivo == 5:
            control.channel_down()
        elif interaccion_dispositivo == 6 and tipo == 'Remote':
            print('Ha terminado de utilizar el control remoto con el dispositivo')
        elif interaccion_dispositivo == 6 and tipo == "AdvancedRemote":
            control.mute()
        elif interaccion_dispositivo == 7 and tipo == 'AdvancedRemote':
            print('Ha terminado de utilizar el control remoto avanzado con el dispositivo')
        else:
            print('Debe ingresar una opción válida para interactuar con el dispositivo')


opcion: int = 0


while opcion != 2:
    print('-----------------------------------------------------------------------------------')
    print('Bienvenido')
    print('1. Seleccionar control\n2. Salir')
    opcion = int(input('Digite el numero de la opción que desea ejecutar: '))
    opcion_control: int = -1
    if opcion == 1:
        while opcion_control == -1:
            print('\nTipos de controles disponibles\n1. Control\n2. Control avanzado')
            opcion_control = int(input('Digite el número de la opción del control que desea utilizar: '))
            if opcion_control == 1:
                control: Remote
                print('\nControl - Remote\n')
                opcion_dispositivo: int = -1
                while opcion_dispositivo == -1:
                    print('Dispositivos disponibles\n1. Radio\n2. Tv\n3. SmartTv')
                    opcion_dispositivo = int(input('Ingrese el número de la opción de dispositivo: '))
                    if opcion_dispositivo == 1:
                        print('Radio')
                        control = Remote(Radio())
                        interactuar(control)
                    elif opcion_dispositivo == 2:
                        print('Tv')
                        control = Remote(Tv())
                        interactuar(control)
                    elif opcion_dispositivo == 3:
                        print('SmartTv')
                        control = Remote(SmartTv())
                        interactuar(control)
                    else:
                        print('Ingrese una opción válida')
                        opcion_dispositivo = -1
            elif opcion_control == 2:
                control: AdvancedRemote
                print('\nControl avanzado')
                opcion_dispositivo: int = -1
                while opcion_dispositivo == -1:
                    print('\nDispositivos disponibles\n1. Radio\n2. Tv\n3. SmartTv')
                    opcion_dispositivo = int(input('Ingrese el número de la opción de dispositivo: '))
                    if opcion_dispositivo == 1:
                        print('Radio')
                        control = AdvancedRemote(Radio())
                        interactuar(control)
                    elif opcion_dispositivo == 2:
                        print('Tv')
                        control = AdvancedRemote(Tv())
                        interactuar(control)
                    elif opcion_dispositivo == 3:
                        print('SmartTv')
                        control = AdvancedRemote(SmartTv())
                        interactuar(control)
                    else:
                        print('Ingrese una opción válida')
                        opcion_dispositivo = -1
            else:
                print('Ingrese una opción válida')
                opcion_control = -1
    elif opcion == 2:
        print('Salir')
    else:
        print('Ingrese una opción válida')

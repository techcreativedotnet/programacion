#!/usr/bin/python3

from datetime import datetime, date

# Creado por Salim Tieb Mohamedi. http://www.techcreative.net

# *--------------------- CLASE UTIL ----------------------*
class Util(object):

    # Comprueba que la fecha introducida es anterior a la fecha actual
    # @staticmethod    
    def validaFecha(fecha):
        
        fecha_anterior = fecha < datetime.now()
        return fecha_anterior

    # Calcula el nº de años trascurridos hasta la fecha
    @staticmethod
    def calcularAnios(fecha):
        hoy = date.today()
        anios = hoy.year - fecha.year - ((hoy.month, hoy.day) < (fecha.month, fecha.day)) 
        return anios

    @staticmethod
    def convertirAFecha(strFecha):
        dateFormatter = "%d/%m/%Y"
        fecha= datetime.strptime(strFecha, dateFormatter)
        return fecha

    # Chequea que el NIF sea válido
    @staticmethod
    def validaDNI(nif):
        return DNI.validarNIF(nif)

# *--------------------- CLASE MENU ----------------------*
class Menu(object):

    @staticmethod
    def mostrarMenu():

        print("\nGESTIÓN DE VEHÍCULO")
        print("1. Nuevo Vehículo")
        print("2. Ver Matrícula")
        print("3. Ver Kilómetros")
        print("4. Actualizar Kilómetros")
        print("5. Ver años de antigüedad")
        print("6. Mostrar Propietario")
        print("7. Mostrar Descripción")
        print("8. Mostrar Precio")
        print("9. Salir")

        correcto=False
        while(not correcto):
            try:
                num = int(input("Introduce un numero entero: "))
                correcto=True   
            except ValueError:
                print('Error, introduce un numero entero')
        
        return num

# *--------------------- CLASE DNI ----------------------*
class DNI(object):
    
    def __init__(self):
        self.numDNI
        

    @staticmethod
    def calcularLetraNIF(dni):
        LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"
        letra = LETRAS_DNI[int(dni)%23]
        return letra

    @staticmethod
    def extraerLetraNIF(nif):
        size = len(nif)
        return nif[size-1]

    @staticmethod
    def extraerNumeroNIF(nif):
        return nif[:-1]

    @staticmethod
    def validarNIF(nif):
        valido = True
        letra_calculada = None
        letra_leida = None
        dni_leido = None

        if nif == None:
            valido = False
        elif len(nif) < 8 or len(nif) > 9:
            valido = False
        else:
            letra_leida = DNI.extraerLetraNIF(nif)
            dni_leido = DNI.extraerNumeroNIF(nif)
            letra_calculada = DNI.calcularLetraNIF(dni_leido)
            if letra_leida.upper() != letra_calculada:
                raise NameError('DNI inválido')
            
        return valido   
                


# *--------------------- CLASE VEHICULO ----------------------*
class Vehiculo(object):
    # Pueden ser moto, auto, barco...
    def __init__(self, marca, matricula, num_kms, fecha_mat, descripcion, precio, propietario, dni_propietario):
        self.marca = marca
        self.matricula = matricula
        self.num_kms = num_kms
        self.fecha_mat = fecha_mat
        self.descripcion = descripcion
        self.precio = precio
        self.propietario = propietario
        self.dni_propietario = dni_propietario
        
    # Getters
    def getMarca(self):
        print(self.marca)

    def getMatricula(self):
        return self.matricula

    def getNum_kms(self):
        return self.num_kms

    def getFecha_mat(self):
        return self.fecha_mat

    def getDescripcion(self):
        return self.descripcion

    def getPrecio(self):
        return self.precio

    def getPropietario(self):
        return self.propietario

    def getDni_propietario(self):
        return self.dni_propietario

    # Setters
    def setMarca(self, marca):
        self.marca = marca

    def setMatricula(self, matricula):
        self.matricula = matricula

    def setNum_kms(self, num_kms):
        self.num_kms = num_kms

    def setFecha_mat(self, fecha_mat):
        self.fecha_mat = fecha_mat

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setPrecio(self, precio):
        self.precio = precio

    def setPropietario(self, propietario):
        self.propietario = propietario

    def setDni_propietario(self, dni_propietario):
        self.dni_propietario = dni_propietario

    def get_Anios(self):
        if type(self.getFecha_mat()) == str:
            self.setFecha_mat(Util.convertirAFecha(self.getFecha_mat()))
        anios = Util.calcularAnios(self.getFecha_mat())
        return anios

    def act_kms(self, nuevos_kms):
        self.num_kms += nuevos_kms

    def __str__(self):
        return f"Marca: {self.marca}\
        \nMatrícula: {self.matricula}\
        \nNº de Kilómetros: {self.num_kms}\
        \nFecha de Matriculación: {self.fecha_mat}\
        \nDescripción: {self.descripcion}\
        \nprecio: {self.precio}\
        \nNombre del Propietario: {self.propietario}\
        \nDNI del Propietario: {self.dni_propietario}\n"
    
        

class Auto(Vehiculo):
    def __init__(self, tipo, marca, matricula, num_kms, fecha_mat, descripcion, precio, propietario, dni_propietario):
        self.tipo_vehiculo = tipo
        super().__init__(marca, matricula, num_kms, fecha_mat, descripcion, precio, propietario, dni_propietario)
        
    def getTipo_vehiculo(self):
        return self.tipo_vehiculo

    def __str__(self):
        output = f"Tipo de Vehículo: {self.tipo_vehiculo}\n"
        output += super().__str__()
        return output
       
    



        

# *--------------------- MAIN ----------------------*
if __name__ == '__main__':
    
    #En principio la referencia al Vehículo apuntará a null.
    objVehiculo = None

    #Descomentar las siguientes 4 líneas para Test y evitar introducir datos nuevo vehículo desde consola
    #objVehiculo = Vehiculo('Mercedes', '0718DHV', 180000, '31/12/2003', 'Mercedes clase C220', 25000, 'Salim Tieb', '45300996N')
    #objAuto = Auto('Turismo', 'Renault', '12348GHU', 1239.78, '09/10/2021', 'Renault Space Monovolumen 2 puertas', 8975, 'Tito Bluni', '45320201N')
    #print(objAuto)
    #print(objVehiculo)

    allOK = True
    salir = False
    opcion = 0

    while not salir:

        opcion = Menu.mostrarMenu()
    
        if opcion == 1:
            print("\n--- NUEVO VEHÍCLO ---")
            marca = input("Introduce la marca del vehículo: ")
            matricula = input("Introduce la matrícula del vehículo: ")
            descripcion = input("Introduce la descripción del vehículo: ")
            numkms = float(input("Introduce el número de kilómetros del vehículo: "))
            precio = int(input("Introduce el precio del vehículo: "))
            propietario = input("Introduce el propietario del vehículo: ")
            dni_propietario = input("Introduce el DNI propietario del vehículo: ")
            dia_mat = int(input("Introduce el día de matriculacion: "))
            mes_mat = int(input("Introduce el mes de matriculacion: "))
            anio_mat = int(input("Introduce el año de matriculacion: "))

            fecha_mat= datetime(anio_mat, mes_mat, dia_mat)

            # Validación de la fecha.
            if Util.validaFecha(fecha_mat):
                print('Fecha de matriculación validado con éxito')
            else:
                allOK = False
                print("Los datos de la fecha de matriculación son incorrectos o la fecha no es anterior a la actual")
            
            if numkms <= 0:
                allOK = False
                print("El número de kilómetros es incorrecto")

            # Validación de la fecha.
            if Util.validaDNI(dni_propietario):
                print('DNI validado con éxito')
            else:
                allOK = False
                print("El formato del DNI no es correcto")

            if allOK:
                objVehiculo = Vehiculo(marca, matricula, numkms, fecha_mat, descripcion, precio, propietario, dni_propietario)
                print("El vehículo ha sido creado")
            
        
        elif opcion == 2:
            print("\n--- VER MATRÍCULA ---")
            if objVehiculo != None:
                print(f'La matrícula del Vehículo es: {objVehiculo.getMatricula()}')
            else:
                print("No existe Vehículo.")
           
        elif opcion == 3:
            print("\n--- VER KILÓMETROS ---")
            if objVehiculo != None:
                output = "El número de kilómtros del Vehículo es: {:.2f}"
                print(output.format(objVehiculo.getNum_kms()))
            else:
                print("No existe Vehículo.")

        elif opcion == 4:
            print("\n--- ACTUALIZAR KILÓMETROS ---")
            if objVehiculo != None:
                nuevos_kms = float(input('Introduce el nuevo número de kilómetros: '))
                if nuevos_kms > 0:
                    objVehiculo.act_kms(nuevos_kms)
            else:
                print("No existe Vehículo.")

        elif opcion == 5:
            print("\n--- VER AÑOS DE ANTIGÜEDAD ---")
            if objVehiculo != None:
                print(f'El Vehículo tiene es: {objVehiculo.get_Anios()} años')
            else:
                print("No existe Vehículo.")

        elif opcion == 6:
            print("\n--- MOSTRAR PROPIETARIO ---")
            if objVehiculo != None:
                print('El propietario del Vehículo es: {0}, con DNI: {1}'.format(objVehiculo.getPropietario(), objVehiculo.getDni_propietario()))
            else:
                print("No existe Vehículo.")

        elif opcion == 7:
            print("\n--- MOSTRAR DESCRIPCIÓN ---")
            if objVehiculo != None:
                #print('La descripción del Vehículo con Nº Matricula: {1} es: {0}'.format(objVehiculo.getDescripcion(), objVehiculo.getMatricula()))
                print(objVehiculo)
            else:
                print("No existe Vehículo.")

        elif opcion == 8:
            print("\n--- MOSTRAR PRECIO ---")
            if objVehiculo != None:
                output = "El precio del Vehículo es: {:d} €"
                print(output.format(objVehiculo.getPrecio()))
            else:
                print("No existe Vehículo.")

        elif opcion == 9:
            salir = True

        else:
            print ("Introduce un numero válido para las opciones [1-9]")
    
    print ("Fin - Ha seleccionado la opción 9. Salir")


    

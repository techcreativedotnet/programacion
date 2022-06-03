# Enunciado
## Se pide desarrollar una aplicación Python que permita gestionar un vehículo.  
### Mediante un menú que aparecerá en pantalla se podrán realizar determinas operaciones:

- Nuevo Vehiculo.
- Ver Matrícula.
- Ver Número de Kilómetros.
- Actualizar Kilómetros.
- Ver años de antigüedad.
- Mostrar propietario.
- Mostrar descripción.
- Mostrar Precio.
- Salir.

### La funcionalidad será la siguiente:

- Al iniciar la aplicación se mostrará el menú propuesto.
- Dependiendo de la opción seleccionada por el usuario:
  - Nuevo Vehículo: Se creará un nuevo Vehículo, si los datos introducidos por el usuario son correctos, que contendrá la siguiente información (marca, matrícula, número de kilómetros, fecha de matriculación, descripción, precio, nombre del propietario, dni del propietario). Todos los datos serán solicitados por teclado y tan solo habrá que comprobar:
    - Que la fecha de matriculación es anterior a la actual: puedes solicitar por separado dia, mes y año y construir un objeto LocalDate (tienes una referencia en el apartado Consejos y recomendaciones).
    - Que el número de kilómetros es mayor que 0.
    - Que el DNI del propietario es correcto.
    - Si no se cumple algunas de las condiciones se deberá mostrar el correspondiente mensaje de error. En ese caso habrá se mostrará de nuevo el menú principal.
  - Ver Matrícula: Mostrará la matrícula del vehículo por pantalla.
  - Ver Número de Kilómetros: Mostrará el número de kilómetros por pantalla.
  - Actualiza Kilómetros: Permitirá actualizar el número de kilómetros del vehículo. Habrá que tener en cuenta que solo se podrán sumar kilómetros.
  - Ver años de antigüedad: Mostrará por pantalla el número de años del vehículo desde que se matriculó, no la fecha de matriculación.
  - Mostrar propietario: Mostrará por pantalla el nombre del propietario del vehículo junto a su dni.
  - Mostrar Descripción: Mostrará una descripción del vehículo, incluyendo su matrícula y el número de kilómetros que tiene.
  - Mostrar Pecio: se mostrará el precio del vehículo.
  - Salir: El programa finalizará.

### El taller constará de dos clases, donde se crearán las clases oportunas:

- La clase Vehiculo, clase Principal y dos clases accesorias que los conformarán métodos estáticos para validación y serán la clase DNI y la clase Util.
- La clase Vehículo dispondrá de los siguientes métodos:
- Constructor o constructores.
- Métodos get y set para acceder a sus propiedades.
- Método get_Anios(): Retorna un entero con el número de años del vehículo.
- Crear una clase hija llamada Auto que herede de Vehiculo.
- Usar el super()

### En la clase Principal crear un objeto Auto que haga por ejemplo:

objVehiculo = Vehiculo('Mercedes', '0718DHV', 180000, '31/12/2003', 'Mercedes clase C220', 25000, 'Salim Tieb', '45300996N')

objAuto = Auto('Turismo', 'Renault', '12348GHU', 1239.78, '09/10/2021', 'Renault Space Monovolumen 2 puertas', 8975, 'Tito Bluni', '45320201N')

print(objVehiculo)  # invocará el métod __str__() del clase hija

print(objAuto)

print(objAuto.getDescripcion())  # La clase Auto no tiene un método getDescripcion() pero es accesible de la clase heredada Vehiculo

print(objAuto.getTipo_vehiculo()) 

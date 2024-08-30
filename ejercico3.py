""""
Un hotel de playa cuenta con un recepcionista que se encarga de
presentar a los clientes las opciones de habitaciones disponibles junto
con sus precios. Tras la elección de la habitación, el recepcionista
solicita los datos personales del cliente y el número de noches que
permanecerá en el hotel. Finalmente, entrega al cliente una factura
detallada con el total de los gastos.
Adicionalmente, los clientes pueden solicitar servicios extra,
como el uso de la piscina o la cancha de golf, que tienen un costo
adicional. Implementa esta funcionalidad en tu programa

"""
class Habitacion:
    def __init__(self, tipo, precio):
        # Inicializa los atributos tipo y precio de la habitación
        self.tipo = tipo
        self.precio = precio

class Cliente:
    def __init__(self, nombre, apellido, contacto):
        # Inicializa el nombre, apellido y número de contacto del cliente
        self.nombre = nombre
        self.apellido = apellido
        self.contacto = contacto

    def nombre_completo(self):
        # Retorna el nombre completo del cliente
        return f"{self.nombre} {self.apellido}"

class Hotel:
    def __init__(self):
        # Inicializa la lista de habitaciones y los servicios extra con sus costos
        self.habitaciones = []
        self.servicios_extra = {
            'piscina': 20,
            'cancha de golf': 50
        }

    def agregar_habitacion(self, tipo, precio):
        # Crea una nueva habitación y la agrega a la lista de habitaciones del hotel
        nueva_habitacion = Habitacion(tipo, precio)
        self.habitaciones.append(nueva_habitacion)

    def mostrar_habitaciones(self):
        # Muestra todas las habitaciones disponibles en el hotel con su precio
        print("Habitaciones disponibles:")
        for i, habitacion in enumerate(self.habitaciones):
            print(f"{i + 1}. Tipo: {habitacion.tipo}, Precio: ${habitacion.precio}")

    def reservar_habitacion(self, cliente, eleccion, noches, servicios_seleccionados):
        # Calcula el costo total de la habitación y los servicios extra seleccionados
        habitacion = self.habitaciones[eleccion - 1]
        total = habitacion.precio * noches
        total_servicios = 0
        servicios_validos = []

        # Verifica si los servicios extra seleccionados están disponibles
        for servicio in servicios_seleccionados:
            if servicio in self.servicios_extra:
                total_servicios += self.servicios_extra[servicio]
                servicios_validos.append(servicio)
            else:
                print(f"El servicio '{servicio}' no está disponible y será excluido de la factura.")

        total_final = total + total_servicios
        
        # Imprime una factura detallada con el costo total a pagar
        print(f"\nFactura detallada para {cliente.nombre_completo()}:")
        print(f"Contacto: {cliente.contacto}")
        print(f"Habitación: {habitacion.tipo} - ${habitacion.precio} x {noches} noches")
        for servicio in servicios_validos:
            print(f"Servicio extra: {servicio} - ${self.servicios_extra[servicio]}")
        print(f"Total a pagar: ${total_final}")

# Ejemplo de uso del sistema de reservas
hotel = Hotel()
hotel.agregar_habitacion("Suite", 150)
hotel.agregar_habitacion("Doble", 100)
hotel.mostrar_habitaciones()

# Solicita la elección de la habitación y el número de noches al usuario
eleccion = int(input("Elige el número de habitación: "))
noches = int(input("Número de noches: "))

# Solicita los datos personales del cliente
nombre_cliente = input("Nombre del cliente: ")
apellido_cliente = input("Apellido del cliente: ")
contacto_cliente = input("Número de contacto: ")
cliente = Cliente(nombre_cliente, apellido_cliente, contacto_cliente)

# Solicita los servicios extra que el cliente desea
servicios = input("Servicios extra (separados por coma, ej. piscina, cancha de golf): ").split(", ")
hotel.reservar_habitacion(cliente, eleccion, noches, servicios)

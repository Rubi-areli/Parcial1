# Clase Estudiante que almacena el nombre del estudiante y sus asistencias
class Estudiante:
    def __init__(self, nombre):
        # Inicializa el nombre del estudiante y una lista vacía para almacenar asistencias
        self.nombre = nombre
        self.asistencias = []

    def registrar_asistencia(self, fecha, estado, razon=""):
        """
        Registra la asistencia del estudiante con la fecha, estado y una razón opcional.
        :parametro fecha: Fecha de la clase.
        :parametro estado: Estado de asistencia ("Asistió", "Permiso", "Inasistencia").
        :parametro razon: Razón de la inasistencia o permiso (opcional).
        """
        # Añade un diccionario con la fecha, estado y razón a la lista de asistencias
        self.asistencias.append({
            "fecha": fecha,
            "estado": estado,
            "razon": razon
        })

    def mostrar_asistencias(self):
        """
        Muestra el registro de asistencias del estudiante.
        """
        # Imprime el nombre del estudiante y recorre la lista de asistencias para mostrar cada registro
        print(f"Asistencias de {self.nombre}:")
        for asistencia in self.asistencias:
            # Si hay una razón, la añade al mensaje, de lo contrario muestra solo fecha y estado
            razon = f", Razón: {asistencia['razon']}" if asistencia['razon'] else ""
            print(f"Fecha: {asistencia['fecha']}, Estado: {asistencia['estado']}{razon}")
        print("--------------------------------------------------")


# Clase Docente que maneja a los estudiantes y sus asistencias
class Docente:
    def __init__(self, nombre):
        # Inicializa el nombre del docente y una lista vacía para almacenar estudiantes
        self.nombre = nombre
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        """
        Agrega un estudiante a la lista del docente.
        :param estudiante: Objeto de la clase Estudiante.
        """
        # Añade el objeto estudiante a la lista de estudiantes del docente
        self.estudiantes.append(estudiante)

    def registrar_asistencia_estudiante(self, nombre_estudiante, fecha, estado, razon=""):
        """
        Registra la asistencia de un estudiante específico.
        :param nombre_estudiante: Nombre del estudiante.
        :param fecha: Fecha de la clase.
        :param estado: Estado de asistencia ("Asistió", "Permiso", "Inasistencia").
        :param razon: Razón de la inasistencia o permiso (opcional).
        """
        # Busca al estudiante en la lista de estudiantes por nombre
        for estudiante in self.estudiantes:
            if estudiante.nombre == nombre_estudiante:
                # Si se encuentra, se registra la asistencia y se sale de la función
                estudiante.registrar_asistencia(fecha, estado, razon)
                return
        # Si no se encuentra el estudiante, muestra un mensaje de error
        print(f"Estudiante {nombre_estudiante} no encontrado en la lista del docente {self.nombre}.")

    def mostrar_asistencias_estudiantes(self):
        """
        Muestra el registro de asistencias de todos los estudiantes.
        """
        # Imprime el nombre del docente y recorre la lista de estudiantes para mostrar sus asistencias
        print(f"Registro de asistencias del docente {self.nombre}:")
        for estudiante in self.estudiantes:
            estudiante.mostrar_asistencias()


# Función principal que maneja la interacción con el usuario
def main():
    # Lista para almacenar los docentes registrados
    docentes = []

    while True:
        # Muestra el menú principal del sistema
        print("\n--- Sistema de Registro de Asistencias ---")
        print("1. Registrar nuevo docente")
        print("2. Agregar estudiante a docente")
        print("3. Registrar asistencia")
        print("4. Mostrar asistencias")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para registrar un nuevo docente
            nombre_docente = input("Nombre del docente: ")
            docentes.append(Docente(nombre_docente))
            print(f"Docente {nombre_docente} registrado exitosamente.")

        elif opcion == "2":
            # Opción para agregar un estudiante a un docente específico
            nombre_docente = input("Nombre del docente: ")
            # Busca al docente en la lista de docentes registrados
            docente_encontrado = next((doc for doc in docentes if doc.nombre == nombre_docente), None)
            if docente_encontrado:
                # Si se encuentra el docente, se agrega un estudiante a su lista
                nombre_estudiante = input("Nombre del estudiante: ")
                docente_encontrado.agregar_estudiante(Estudiante(nombre_estudiante))
                print(f"Estudiante {nombre_estudiante} agregado al docente {nombre_docente}.")
            else:
                # Si no se encuentra el docente, muestra un mensaje de error
                print(f"Docente {nombre_docente} no encontrado.")

        elif opcion == "3":
            # Opción para registrar la asistencia de un estudiante
            nombre_docente = input("Nombre del docente: ")
            # Busca al docente en la lista de docentes registrados
            docente_encontrado = next((doc for doc in docentes if doc.nombre == nombre_docente), None)
            if docente_encontrado:
                # Si se encuentra el docente, solicita los datos de la asistencia
                nombre_estudiante = input("Nombre del estudiante: ")
                fecha = input("Fecha (YYYY-MM-DD): ")
                estado = input("Estado (Asistió/Permiso/Inasistencia): ")
                razon = ""
                # Si el estado es "Permiso" o "Inasistencia", pide una razón
                if estado.lower() == "permiso" or estado.lower() == "inasistencia":
                    razon = input("Razón: ")
                # Registra la asistencia del estudiante
                docente_encontrado.registrar_asistencia_estudiante(nombre_estudiante, fecha, estado, razon)
            else:
                # Si no se encuentra el docente, muestra un mensaje de error
                print(f"Docente {nombre_docente} no encontrado.")

        elif opcion == "4":
            # Opción para mostrar las asistencias registradas de un docente
            nombre_docente = input("Nombre del docente: ")
            # Busca al docente en la lista de docentes registrados
            docente_encontrado = next((doc for doc in docentes if doc.nombre == nombre_docente), None)
            if docente_encontrado:
                # Si se encuentra el docente, muestra las asistencias de sus estudiantes
                docente_encontrado.mostrar_asistencias_estudiantes()
            else:
                # Si no se encuentra el docente, muestra un mensaje de error
                print(f"Docente {nombre_docente} no encontrado.")

        elif opcion == "5":
            # Opción para salir del sistema
            print("Saliendo del sistema...")
            break

        else:
            # Si se ingresa una opción no válida, muestra un mensaje de error
            print("Opción no válida. Intente nuevamente.")


# Ejecuta la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()

#Instrucciones para Usar el Sistema:
#Registrar un Nuevo Docente: Selecciona la opción "1" y proporciona el nombre del docente.
#Agregar Estudiantes: Selecciona la opción "2", ingresa el nombre del docente y luego el nombre del estudiante que deseas agregar a la lista de ese docente.
#Registrar Asistencia: Selecciona la opción "3", elige el docente, el estudiante, la fecha, el estado de la asistencia, y, si es necesario, proporciona la razón del permiso o inasistencia.
#Mostrar Asistencias: Selecciona la opción "4" e ingresa el nombre del docente para revisar las asistencias registradas para sus estudiantes.
#Salir del Sistema: Selecciona la opción "5" para cerrar el programa.
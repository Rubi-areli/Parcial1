class Animal:
    def __init__(self, nombre, especie, area):
        self.nombre = nombre
        self.especie = especie
        self.area = area

class Tratamiento:
    def __init__(self, animal, medicamento, dosis, frecuencia):
        self.animal = animal
        self.medicamento = medicamento
        self.dosis = dosis
        self.frecuencia = frecuencia

class Zoologico:
    def __init__(self):
        self.animales = []
        self.tratamientos = []

    def registrar_animal(self, animal):
        self.animales.append(animal)

    def listar_animales(self):
        for idx, animal in enumerate(self.animales, 1):
            print(f"{idx}. Nombre: {animal.nombre}, Especie: {animal.especie}, Área: {animal.area}")

    def registrar_tratamiento(self, tratamiento):
        self.tratamientos.append(tratamiento)

    def listar_tratamientos(self):
        for tratamiento in self.tratamientos:
            print(f"Animal: {tratamiento.animal.nombre}, Medicamento: {tratamiento.medicamento}, Dosis: {tratamiento.dosis}, Frecuencia: {tratamiento.frecuencia}")

# Función para registrar un nuevo animal
def registrar_nuevo_animal(zoologico):
    nombre = input("Ingrese el nombre del animal: ")
    especie = input("Ingrese la especie del animal: ")
    area = input("Ingrese el área del zoológico donde se encuentra el animal: ")
    animal = Animal(nombre, especie, area)
    zoologico.registrar_animal(animal)
    print("Animal registrado con éxito.")

# Función para registrar un nuevo tratamiento
def registrar_nuevo_tratamiento(zoologico):
    if not zoologico.animales:
        print("No hay animales registrados. Registre un animal primero.")
        return
    
    zoologico.listar_animales()
    seleccion = int(input("Seleccione el número del animal para el tratamiento: "))
    if 1 <= seleccion <= len(zoologico.animales):
        animal_seleccionado = zoologico.animales[seleccion - 1]
        medicamento = input("Ingrese el nombre del medicamento: ")
        dosis = input("Ingrese la dosis del medicamento: ")
        frecuencia = input("Ingrese la frecuencia de administración: ")
        tratamiento = Tratamiento(animal_seleccionado, medicamento, dosis, frecuencia)
        zoologico.registrar_tratamiento(tratamiento)
        print("Tratamiento registrado con éxito.")
    else:
        print("Selección no válida.")

# Menú interactivo para el veterinario
def menu_veterinario(zoologico):
    while True:
        print("\nMenú del Veterinario")
        print("1. Registrar un nuevo animal")
        print("2. Listar animales")
        print("3. Registrar un nuevo tratamiento")
        print("4. Listar tratamientos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_nuevo_animal(zoologico)
        elif opcion == "2":
            zoologico.listar_animales()
        elif opcion == "3":
            registrar_nuevo_tratamiento(zoologico)
        elif opcion == "4":
            zoologico.listar_tratamientos()
        elif opcion == "5":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejemplo de uso
zoologico = Zoologico()
menu_veterinario(zoologico)

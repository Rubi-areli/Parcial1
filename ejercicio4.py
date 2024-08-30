from datetime import datetime

class Empleado:
    def __init__(self, nombre, tipo, salario_base, comisiones=0, horas_trabajadas=0, fecha_ingreso=None):
        self.nombre = nombre
        self.tipo = tipo  # 'fijo' o 'por_horas'
        self.salario_base = salario_base
        self.comisiones = comisiones
        self.horas_trabajadas = horas_trabajadas
        self.fecha_ingreso = fecha_ingreso

    def calcular_anios_trabajo(self):
        if self.fecha_ingreso:
            hoy = datetime.now()
            anios_trabajados = hoy.year - self.fecha_ingreso.year
            return anios_trabajados
        return 0

    def calcular_pago(self):
        if self.tipo == 'fijo':
            pago = self.salario_base + self.comisiones
        elif self.tipo == 'por_horas':
            pago = self.salario_base * self.horas_trabajadas
        else:
            raise ValueError("Tipo de empleado no válido")

        # Verificar si el empleado ha trabajado más de 5 años para otorgar el bono
        if self.calcular_anios_trabajo() > 5:
            bono = 500  # Por ejemplo, un bono de 500 unidades monetarias
            pago += bono

        return pago

def ingresar_nombre():
    nombre = input("Ingrese el nombre del empleado: ")
    return nombre

def ingresar_tipo():
    while True:
        tipo = input("Ingrese el tipo de empleado ('fijo' o 'por_horas'): ").lower().strip()
        if tipo in ['fijo', 'por_horas']:
            return tipo
        else:
            print("Tipo de empleado no válido. Inténtelo de nuevo.")

def ingresar_salario_base():
    while True:
        try:
            salario_base = float(input("Ingrese el salario base: "))
            return salario_base
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def ingresar_comisiones():
    while True:
        try:
            comisiones = float(input("Ingrese las comisiones: "))
            return comisiones
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def ingresar_horas_trabajadas():
    while True:
        try:
            horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
            return horas_trabajadas
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def ingresar_fecha_ingreso():
    while True:
        fecha_ingreso_str = input("Ingrese la fecha de ingreso (formato: YYYY-MM-DD): ")
        try:
            fecha_ingreso = datetime.strptime(fecha_ingreso_str, "%Y-%m-%d")
            return fecha_ingreso
        except ValueError:
            print("Formato de fecha no válido. Inténtelo de nuevo.")

def ingresar_datos_empleado():
    nombre = ingresar_nombre()
    tipo = ingresar_tipo()
    salario_base = ingresar_salario_base()
    
    if tipo == 'fijo':
        comisiones = ingresar_comisiones()
        horas_trabajadas = 0
    elif tipo == 'por_horas':
        comisiones = 0
        horas_trabajadas = ingresar_horas_trabajadas()

    fecha_ingreso = ingresar_fecha_ingreso()

    return Empleado(nombre, tipo, salario_base, comisiones, horas_trabajadas, fecha_ingreso)

# Ejemplo de uso:
empleado = ingresar_datos_empleado()
print(f"El pago de {empleado.nombre} es: {empleado.calcular_pago()}")


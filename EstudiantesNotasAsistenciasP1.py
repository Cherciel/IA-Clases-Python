class Estudiante:
    def __init__(self, nombre, cal_IA, cal_EDA, cal_Matematica, horas_sin_asistencia):
        self.nombre = nombre
        self.calificaciones = [cal_IA, cal_EDA, cal_Matematica]
        self.horas_sin_asistencia = horas_sin_asistencia

    def promedio_calificaciones(self):
        return sum(self.calificaciones) / len(self.calificaciones)

    def evaluar(self):
        total_horas_clase = sum(self.horas_sin_asistencia)
        porcentaje_faltas = total_horas_clase / sum([20, 20, 20]) * 100

        if self.promedio_calificaciones() < 3 or porcentaje_faltas >= 20:
            print(f"{self.nombre} ha desaprobado.")
            if self.promedio_calificaciones() < 3:
                print("Sugerencia: Asistir a consultas obligatorias en sesión contraria para mejorar las notas.")
            if porcentaje_faltas >= 20:
                print("Sugerencia: Si trabaja o tiene problemas personales, considerar cambiar de modalidad de curso como: curso por encuentro.")
        else:
            print(f"{self.nombre} ha aprobado.")

def crear_estudiantes():
    cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
    estudiantes = []

    for _ in range(cantidad_estudiantes):
        nombre = input("Ingrese el nombre del estudiante: ")
        cal_IA = float(input("Ingrese la calificación de IA: "))
        cal_EDA = float(input("Ingrese la calificación de EDA: "))
        cal_Matematica = float(input("Ingrese la calificación de Matemática: "))
        horas_sin_asistencia = [int(input("Ingrese las horas sin asistencia de IA: ")),
                                int(input("Ingrese las horas sin asistencia de EDA: ")),
                                int(input("Ingrese las horas sin asistencia de Matemática: "))]

        estudiante = Estudiante(nombre, cal_IA, cal_EDA, cal_Matematica, horas_sin_asistencia)
        estudiantes.append(estudiante)

    return estudiantes

# Crear los objetos Estudiante
estudiantes = crear_estudiantes()

# Evaluar a cada estudiante
for estudiante in estudiantes:
    estudiante.evaluar()

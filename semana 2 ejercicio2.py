class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    
    def evaluar(self):
        if self.calificacion >= 6:
            return f"{self.nombre} ha aprobado  la nota {self.calificacion}."
        else:
            return f"{self.nombre} ha reprobado la nota  {self.calificacion}."

# Ejemplo de uso
estudiante1 = Estudiante("Pedro", 21, 9)
estudiante2 = Estudiante("Ana", 23, 4)

print(estudiante1.evaluar())  
print(estudiante2.evaluar())  
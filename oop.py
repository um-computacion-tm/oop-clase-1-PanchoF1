import unittest
class Alumno:
    def __init__(self, nombre, legajo, correo):
        self.__nombre__ = nombre
        self.__legajo__ = legajo
        self.__correo__ = correo

    def obtener_nombre(self):
        return self.__nombre__

    def cambiar_correo(self, correo):
        self.__correo__ = correo



class Materia:
    def __init__(self, nombre, profesores, alumnos:list[Alumno]):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_alumnos(self):
        return self.__alumnos__



class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__



class TestAlumno(unittest.TestCase):
    def test_alumno(self):
        alumno = Alumno("Francisco", "56107", "f.saldana")
        self.assertEqual(alumno.__nombre__, "Francisco")
        self.assertEqual(alumno.__legajo__, "56107")
        self.assertEqual(alumno.__correo__, "f.saldana") 

    def test_obtener_nombre(self):
        alumno = Alumno("Francisco", "56107", "f.saldana")
        self.assertEqual(alumno.obtener_nombre(), "Francisco")

    def test_cambiar_correo(self):
        correo = "f.saldana"
        alumno = Alumno("Francisco", "56107", correo)
        alumno.cambiar_correo("fsadams")
        self.assertEqual(alumno.__correo__, "fsadams")
    

class TestMateria(unittest.TestCase):
    def test_materia(self):
        nombre = "Computacion"
        profesores = "Daniel"
        alumno1 = Alumno("Francisco", "56107", "f.saldana")
        alumno2 = Alumno("Carlos", "55555", "c.sainz")
        alumnos = [alumno1,alumno2]
        materia = Materia(nombre, profesores,alumnos)
        self.assertEqual(materia.__nombre__, nombre)
        self.assertEqual(materia.__profesores__, profesores)
        self.assertEqual(materia.__alumnos__, alumnos)

    def test_obtener(self):
        profesores = "Daniel"
        alumno1 = Alumno("Francisco", "56107", "f.saldana")
        alumno2 = Alumno("Carlos", "55555", "c.sainz")
        alumnos = [alumno1,alumno2]
        materia = Materia("Computacion", profesores,alumnos)

        self.assertEqual(materia.obtener_profesores(), profesores)

    def test_cambiar(self):
        nombre = "Computacion"
        alumno1 = Alumno("Francisco", "56107", "f.saldana")
        alumno2 = Alumno("Carlos", "55555", "c.sainz")
        alumnos = [alumno1,alumno2]
        materia = Materia(nombre, "Daniel",alumnos)
        materia.cambiar_nombre("Programacion")

        self.assertEqual(materia.__nombre__, "Programacion")

    def test_obtener_alumnos(self):
        alumno1 = Alumno("Francisco", "62080", "f.saldana")
        alumno2 = Alumno("Carlos", "55555", "c.sainz")
        alumno3 = Alumno('Martin','62272','m.tarantoviez')
        alumnos = [alumno1,alumno2,alumno3]
        
        materia = Materia('Computacion','Daniel',alumnos)
        self.assertEqual(materia.obtener_alumnos(),alumnos)


class TestProfesor(unittest.TestCase):
    def test_profesor(self):
        profesores = Profesor("Daniel", "BOSS", "12345")
        self.assertEqual(profesores.__nombre__, "Daniel")
        self.assertEqual(profesores.__cargo__, "BOSS")
        self.assertEqual(profesores.__legajo__, "12345")

    def test_obtener_nombre(self):
        profesores = Profesor("Daniel", "BOSS", "12345")
        self.assertEqual(profesores.obtener_nombre(), "Daniel")

    def test_obtener_cargo(self):
        profesores = Profesor("Daniel", "BOSS", "12345")
        self.assertEqual(profesores.obtener_cargo(), "BOSS")

    def test_obtener_legajo(self):
        profesores = Profesor("Daniel", "BOSS", "12345")
        self.assertEqual(profesores.obtener_legajo(), "12345")

if __name__ == '__main__':
    unittest.main()
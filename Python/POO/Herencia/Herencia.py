class Person:      
    def __init__(self, first, last):        
        self.firstname = first        
        self.lastname = last    
    def Name(self):        
        return self.firstname  + " " + self.lastname

class Employee(Person):
    def __init__(self, first, last, id):
        # self.firstname = first        
        # self.lastname = last    
        Person.__init__(self, first, last)
        self.staffnumber = id  
    
    def GetEmployee(self):        
        #return self.firstname  + " " + \
        #       self.lastname + ", " + \
        #       self.staffnumber
        
        ''' Desde una clase hijo puedo invocar metodos de la clase padre'''
        return self.Name() + ", " +  self.staffnumber
  
class Student(Person):
    def __init__(self, first, last, carnet):
        super().__init__(first, last) # Person.__init__(self, first, last)
        self.carnet = carnet
        self.materias = []
        
    def agregarMateria(self, materia):
        self.materias.append(materia) # self.materias = self.materias + [materia]
        
    def imprimirMaterias(self):
        for materia in self.materias:
            print(materia)

class WorkerStudent(Employee, Student):
    
    def __init__(self, first, last, carnet, id):
        Student.__init__(self, first, last, carnet)
        self.staffnumber = id
        
    def GetWorkerStudent(self):
        info = self.Name() 
        info = info + "\n" + "- ID worker: " + self.staffnumber 
        info += "\n" + "- Carnet: " + self.carnet
        return info
    
    

# Constructores    
bart = Student("Bartolomeo","Simpson","SS0001")
lisa = Student(first = "Lisa", last = "Simpson",carnet= "SS0002")
maggie = Person(last = "Simpson",first = "Maggie")
print(lisa.Name())
print(lisa.imprimirMaterias())


homero = Employee("Homero","Simpson","PN0001")
print(homero.Name())
print(homero.GetEmployee())
marge = WorkerStudent("Marge", "Simpson", "U0001", "PN0002")
marge.agregarMateria("Fundamentos de programación")
marge.agregarMateria("Ingles")
print(marge.GetWorkerStudent())
marge.imprimirMaterias()
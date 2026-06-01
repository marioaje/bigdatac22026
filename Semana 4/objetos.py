#El nombre del objeto
#recuerden identar con el tab y no usando espaciador
class Objeto:
#funcion constructora la inicializadora
    def __init__(self, primerparametro, segundoparametro):
        self.primerparametro = primerparametro
        self.segundoparametro = segundoparametro

    def saludo(self):
        print("Bienvenido al sistema BigData 2026")
      
#Fin de class Objeto:
nuevo = Objeto("1", "2")   
#nuevo = 65

print(nuevo.primerparametro)
print(nuevo.segundoparametro)
nuevo.saludo()
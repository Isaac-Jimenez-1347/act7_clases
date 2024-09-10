print("introduccion a clases")
class animal:
    edad=3
    raza="pitbul terrier"
    comida="croquetas"
    def come(self):
        print("el perro come "+self.comida)
perro=animal()
print(f"el perro tiene {perro.edad} años" ) 
print(f"el perro es raza {perro.raza}" )
perro.come()
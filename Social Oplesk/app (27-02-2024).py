#clases

class Mensajes:
    
    def saludo(self):
        print("Hola, cómo estás")
        
    def despedirme(self):
        print("Hasta Luego")
        
    def pedir_comida(self):
        print("Necesito Comer")  
        
    #Funcion Contructora
    def __init__(self, n) -> None:
        self.nombre = n
        
    def pelear(self):
        print(f"{self.nombre}, Peleando")  
        

#Como ejecutar las clases

msj = Mensajes() 
    
msj.saludo()
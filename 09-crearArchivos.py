class OperasBas: 
    #declaracion de propiedades 
    num1 =0 
    num2 =0 
    num3 =0 

    #declaracion del constructor this
    # el constructor no debe llamarse igual a la clase, se usa __init__
    
    def __init__(self):
        self.num1 = 0
        self.num2 = 0   

    #declaracion de metodos de clase

    def suma(self):
        #para decir que voy a usar una propiedad de la clase uso self
        self.res=self.num1 + self.num2
        print("la suma es: {}".format(self.res))

    def resta(self):
        self.res=self.num1 - self.num2
        print("la resta es: {}".format(self.res))

    def main(): 
        obj = OperasBas()        
        obj.suma()

    if __name__ == "__main__":
        main()
        
    
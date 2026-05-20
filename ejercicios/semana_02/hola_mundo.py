class HolaMundo:

    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        """
        Este método no recibe variables, solo imprime un resultado

        """
        print("Método uno")
        
    def metodoDos(self, variable_uno:int, variable_dos:float)->int:
        """
        Este método recibe 2 variables enteras, las suma y regresa el resultado de la suma

        Args:

        variable_uno:int - Primer numero entero
        variable_dos:int - Segundo numero entero

        Return:

        suma:int - Suma de los dos numeros enteros 
        """

        suma = variable_uno + variable_dos
        return int(suma)
    
    def metodoTres(self,variable_tres:str)->None:
        """
        Este método recibe una variable tring, no regresa nada, solo imprime el numero de caracteres 
        
        
        Args:

        variable_tres:str -Caracteres de una palabra
        """
        print(f"Número de caracteres: {len(variable_tres)}")

nombre_objeto = HolaMundo()
nombre_objeto.metodoUno()
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:12:37 2021

@author: Usuario
"""

"""Clase Temperatura"""
class Temperature:
    
    def __init__(self, temperature = 75.0):
        self.temperature = temperature
        
    def __str__(self):
        pass
   
    def aboveFreezing(self): 
        pass
   
    def convertToFahren(self):
        pass
    
    def convertToCelcius(self):
        pass
    
    def convertToKelvin(self):
        pass

class Kelvin(Temperature): 
    
    def convertToFahren(self):
        temp = (9/5)*self.temperature - 459.67
        return temp       
          
    def convertToCelcius(self):
        return self.temperature - 273.15
    
    
    def convertToKelvin(self):
       return self.temperature
   
    def aboveFreezing(self): 
        # Retorna True si la temperatura está arriba del punto de congelación (273.15°F).
        if (self.temperature > 273.15):
            return True
        else:
            return False
        
    def __str__(self):
        return str(self.temperature) + " degrees Kelvin"
        

class Celcius(Temperature): 
    
    def convertToFahren(self):
        return (9/5)*self.temperature - 32
           
    def convertToCelcius(self):
        return self.temperature
    
    def convertToKelvin(self):
        return self.temperature + 273.15
    
    def aboveFreezing(self): 
        # Retorna True si la temperatura está arriba del punto de congelación (0°C).
        if (self.temperature > 0):
            return True
        else:
            return False
        
    def __str__(self):
        return str(self.temperature) + " degrees Celcius"
        
class Fahrenheit(Temperature): 
    
    def convertToFahren(self):
        return self.temperature
        
    
    def convertToCelcius(self):
        return (5/9)*(self.temperature + 32)
    
    def convertToKelvin(self):
        return (5/9)*(self.temperature + 459.67)
    
    def aboveFreezing(self): 
        # Retorna True si la temperatura está arriba del punto de congelación (32°F).
        if (self.temperature > 32):
            return True
        else:
            return False
        
    def __str__(self):
        return str(self.temperature) + " degrees Fahrenheit"
        
"""  
NO TIENE SENTIDO...
temp1 = Temperature(15)
temp2 = Temperature()
listaTemp1 = [temp1, temp2]
for T in listaTemp1:
    print(T)

"""
listaTemp2 = [Kelvin(), Celcius(), Fahrenheit()]
for T in listaTemp2:
    print(T, end = '; ')
    # print(T.aboveFreezing())
    if(T.aboveFreezing() == True):
        print("arriba del punto de congelación.")
    else:
        print("abajo del punto de congelación.")
        


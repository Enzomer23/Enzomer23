def añobisiesto():
  año: int = int(input("Introduce un año y vamos a ver si es bisiesto... "))
  if(año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
      print(f"¡El año {año} es bisiesto!")
  else:print(f"Pues no, dicho año {año} no es bisiesto!")
print({añobisiesto()})

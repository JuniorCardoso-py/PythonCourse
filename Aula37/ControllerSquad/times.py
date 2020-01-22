import MySQLdb
import sys
sys.path.append('C:/Users/900162/Documents/GitHub/PythonCourse/Aula37')
from PythonCourse.Aula37.daoSquad.Aula37 import Crud_Time
from PythonCourse.Aula37.ModelSquad.modelo_time import Model_timee

class Time_controller:
    def controlerr(self):
        lista_tuplas = []
        contador =  0
        for p in Crud_Time.listar_todos():
            pessoa = p[0+contador]
            contador = contador +1
            lista_tuplas.append(pessoa)
        print(lista_tuplas)
control = Time_controller

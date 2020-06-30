#************************************************Tarea3 - Modelos Porbabilísticos de Señales y Sistemas********************************************
# Estudiante: Bryan Carrillo Rojas - B71671
# 
# Este documento se encarga de obtener información respecto a un conjunto de datos correspondiente a 2 variables aleatorias
# El objetivo es poder obtener las conocidas funciones de densidad marginal, correlación covarianza y coeficiente 
# de correlación de los datos dados. Se deben de obtener curvas de mejor ajuste para las funciones de densidad
# marginales y se debe obtener la función de densidad conjunta.
#
# En este docuemento solo se va a hacer comentarios respecto al código empleado, la explicación detallada de
# los fundamentosde estádística se encuentran en el archivo README.md


import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import norm
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit
import statistics as stats
# importar todas las funciones de pylab
from pylab import *

# importar el módulo pyplot
import matplotlib.pyplot as plt
from matplotlib import cm

from mpl_toolkits.mplot3d import Axes3D

#########################################################Preparativos#####################################################################
# función
def gaussiana(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2/(2*sigma**2))


# se leen los archivos y se almacenan en data_frames
xy = pd.read_csv("xy.csv",  sep=',')
xyp = pd.read_csv("xyp.csv",  sep=',')

#########################################################Inciso 1#####################################################################

# se inicializan matrices para almacenar los valores marginales para X y Y
val_margx = []
val_margy = []

# Se obtienen los la sumatorias de las probabilidades (valores marginales)
val_margx = [ i for i in xy.sum(axis=1, numeric_only=True)]
val_margy= [ i for i in xy.sum(axis=0, numeric_only=True)]

# se genera un vector de valores coorespondiente al al números de valores marginales obtenidos
xcount = np.linspace(5,15, len(val_margx))
ycount = np.linspace(5,25, len(val_margy))

# se obtienen los parámetros (mu y sigma) de cada una de las curvas
paramx, _= curve_fit(gaussiana, xcount, val_margx)
mux = paramx[0]
sigmax = paramx[1]
print("El valor de mu para la función de densidad marginal de X es: ", mux, " y el valor de sigma es: ", sigmax)

paramy, _= curve_fit(gaussiana, ycount, val_margy)
muy = paramy[0]
sigmay = paramy[1]
print("El valor de mu para la función de densidad marginal de Y es: ", muy, " y el valor de sigma es: ", sigmay)


# Se grafican las funciones marginales 
##X
# gráfica discreta obtendias
plt.plot(xcount,val_margx,'--')
plt.xlabel("X")
plt.ylabel("Frecuencia relativa X")
plt.title("Función de Densidad Marginal de X")
plt.savefig("out/CurvaX.png")
plt.show()

# ajuste normal
x = np.linspace(3, 17, 1000)
temp = stats.norm.pdf(x, mux, sigmax)
plt.plot(x, temp)
plt.xlabel("X")
plt.ylabel("Frecuencia relativa X")
plt.title("Distribución para Función de Densidad Marginal X")
plt.savefig("out/AjusteX.png")

##Y
# gráfica discreta obtendias

plt.plot(ycount,val_margy,'--')
plt.xlabel("Y")
plt.ylabel("Frecuencia relativa Y")
plt.title("Función de Densidad Marginal de Y")
plt.savefig("out/CurvaY.png")
plt.show()

# ajuste normal
y = np.linspace(3, 27, 200)
plt.plot(y, stats.norm.pdf(y, muy, sigmay))
plt.xlabel("Y")
plt.ylabel("Frecuencia relativa Y")
plt.title("Distribución para Función de Densidad Marginal Y")
plt.savefig("out/AjusteY.png")

#########################################################Inciso 2#####################################################################

#Esta sección corresponde a un análisis analítico realizado en el README.md

#########################################################Inciso 3#####################################################################
# se inicializan las variables
correlación = 0
co_varianza = 0

# se calcula la correlación y la co_varianza 
for i in range(0,len(xyp)):
    correlación = correlación + xyp.x[i]*xyp.y[i]*xyp.p[i]
    co_varianza = co_varianza + (xyp.x[i] - mux)*(xyp.y[i]-muy)*(xyp.p[i])

# se calcula el coeficiente de correlación --> pearson
pearson = co_varianza / (sigmax+sigmay)
print("La correlación  es :", correlación)
print("La co-varianza  es :",co_varianza)
print("EL coeficiente de correlación es :", pearson)

#########################################################Inciso 4#####################################################################
# se realiza obtiene la función de densidad conjunta (3D)
# se debe de realizar un meshgrid para generar un espacio equidimencional antes de intentar graficar
X, Y = np.meshgrid(np.linspace(4, 16, 1000),np.linspace(4, 26, 1000))

# A se le conoce como magnitud de la función, se prefirió calcularla por aparte
A = 1/(2*np.pi*sigmax*sigmay)

# se utiliza la función gaussiana de 2 dimensiones
Z = A*np.e**(-(((X-mux)**2)/(sigmax**2)) - (((Y - muy)**2)/sigmax**2))

# se plotea
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(X, Y, Z, cmap=cm.BrBG_r)


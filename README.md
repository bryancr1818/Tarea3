# Tarea 3 - Modelos Probablilísticos de Señales y Sistemas

Estudiantes: Bryan Carrillo Rojas
Carné: B71671

## Inciso 1: Curvas de mejor ajuste para las funciones de densidad marginal
Para el presente trabajo fueron dados los archivos de `xy.csv` y `xyp.csv`,  para trabajaes estos documentos fue necesario traducirlos a a un tipo de datos manipulables, esto se logró apartir de la biblioteca de `Pandas` y se alamacenaron los datos en las varibales `valmargx`y `valmargy`:

``` python
xy = pd.read_csv("xy.csv",  sep=',')
xyp = pd.read_csv("xyp.csv",  sep=',')

# se inicializan matrices para almacenar los valores marginales para X y Y
val_margx = []
val_margy = []

# Se obtienen los la sumatorias de las probabilidades (valores marginales)
val_margx = [ i for i in xy.sum(axis=1, numeric_only=True)]
val_margy= [ i for i in xy.sum(axis=0, numeric_only=True)]
 ```
 Para mayor facilidad a la hora de utilizar los datos, se queman en el código, los vestores `xcount` y `ycount`, los cuales equivalen a la cantidad de términos en las columnas y las filas d los datos datos. Además, san a funcionar al querer representrar los valores de `X` y `Y`:

 ```python
# se genera un vector de valores coorespondiente al al números de valores marginales obtenidos
xcount = np.linspace(5,15, len(val_margx))
ycount = np.linspace(5,25, len(val_margy))
```

Para saber que tipo de ajuste se necesita, se van a graficar primero las funciones marginales:
 ```python
##X
plt.plot(xcount,val_margx,'--')
plt.xlabel("X")
plt.ylabel("Frecuencia relativa X")
plt.title("Función de Densidad Marginal de X")
plt.savefig("out/CurvaX.png")
plt.show()

##Y
plt.plot(ycount,val_margy,'--')
plt.xlabel("Y")
plt.ylabel("Frecuencia relativa Y")
plt.title("Función de Densidad Marginal de Y")
plt.savefig("out/CurvaY.png")
```

Se obtienen las siguientes gráficas:
![Figura de X original](img/xInitPlot.png)


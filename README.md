# Tarea 3 - Modelos Probablilísticos de Señales y Sistemas

Estudiantes: Bryan Carrillo Rojas
Carné: B71671

- [Tarea 3](#tarea3)
  - [Inciso 1](#inciso_1)
  - [Inciso 2](#inciso_2)
  - [Inciso 3](#inciso_3)
  - [Inciso 4](#inciso_4)

## Inciso 1: Curvas de mejor ajuste para las funciones de densidad marginal 
Para el presente trabajo fueron dados los archivos de `xy.csv` y `xyp.csv`,  para trabajar estos documentos fue necesario traducirlos a un tipo de datos manipulables, esto se logró a partir de la biblioteca de `Pandas` y se almacenaron los datos en las varibles `valmargx`y `valmargy`:

``` python
xy = pd.read_csv("xy.csv",  sep=',')
xyp = pd.read_csv("xyp.csv",  sep=',')

# se inicializan matrices para almacenar los valores marginales para X y Y
val_margx = []
val_margy = []

# Se obtienen las la sumatorias de las probabilidades (valores marginales)
val_margx = [ i for i in xy.sum(axis=1, numeric_only=True)]
val_margy= [ i for i in xy.sum(axis=0, numeric_only=True)]
 ```
 Para mayor facilidad a la hora de utilizar los datos, se queman en el código los vectores `xcount` y `ycount`, los cuales equivalen a la cantidad de términos en las columnas y las filas de los datos:

 ```python
# se genera un vector de valores coorrespondiente al números de valores marginales obtenidos
xcount = np.linspace(5,15, len(val_margx))
ycount = np.linspace(5,25, len(val_margy))
```

Para saber que tipo de ajuste se necesita, se van a graficar primero las funciones marginales crudas (solo graficar lo que se obtuvo de los datos):
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
### Función de Densidad Marginal de X
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/out/CurvaX.png) 
### Función de Densidad Marginal de X
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/out/CurvaY.png) 

Como se logra apreciar, estas gráficas tienen naturaleza de una función de distribución Gaussiana, por lo que se procede a calcular los parámetros para cada una de las distribuciones:

```python
def gaussiana(x, mu, sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(x-mu)**2/(2*sigma**2))

# se obtienen los parámetros (mu y sigma) de cada una de las curvas
paramx, _= curve_fit(gaussiana, xcount, val_margx)
mux = paramx[0]
sigmax = paramx[1]
print("El valor de mu para la función de densidad marginal de X es: ", mux, " y el valor de sigma es: ", sigmax)

paramy, _= curve_fit(gaussiana, ycount, val_margy)
muy = paramy[0]
sigmay = paramy[1]
print("El valor de mu para la función de densidad marginal de Y es: ", muy, " y el valor de sigma es: ", sigmay)
```
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/1.gif) 
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/2.gif) 
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/3.gif) 
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/4.gif) 

Al construir las funciones de densidad marginales tanto de *x* como de *y* con los datos anteriores, se tiene:

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/conjx.gif) 

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/conjy.gif) 

Ahora al graficar los ajustes se obtiene:
### Distribución de la Densidad Marginal de X
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/out/AjusteX.png) 

### Distribución de la Densidad Marginal de Y
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/out/AjusteY.png) 

## Inciso 2: Función de Densidad Conjunta
Al asumir que las funciones obtenidas son estadísticamente independientes entre sí, se puede utilizar las ecuaciones y principios presentes en la `D34-P4` del material del curso. Debido a la afirmación de la independencia se puede decir que:

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/inde1.gif)

Al utilizar las ecuaciones de las funciones de densidad marginales con la ecuación anterior, se obtiene la función de densidad conjunta:

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/conjxy.gif) 

Ahora para tener el modelo evaluado, se ingresa los valores de <img src="https://render.githubusercontent.com/render/math?math=\mu"> y <img src="https://render.githubusercontent.com/render/math?math=\sigma">:

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/conjxy_res.gif) 


## Inciso 3: Valores de Correalación, Covarianza y Coeficiente de Correlación
En esta sección se utilizaron los valores del data_frame `xyp`, para realizar la multiplicación de cada una de las combinaciones de **X** y de **Y**, con la probabilidad asociada.

```python
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
```
Como se tiene en el materia del curso, hay ecuaciones ya definidas para cada uno de los momentos principales: Covarianza, Correlación, Coeficiente de Correlación. Cada uno tiene su propio significado que al que se le puede dar un significado físico a partir de las gráficas obtenidas.

### Correlación
Según lo que dice el material del curso, este es el momento de segundo orden, expresado también como <img src="https://render.githubusercontent.com/render/math?math=R_{XY} = E[X,Y]"> y  está defindo por la siguiente ecucación:

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/correlación.gif)

En la `D6-P10`se hace referencia a la correlación como un índice de cuán asociadas o realcionadas se encuentras las variables y se especifíca claramente que esto no implica causalidad. Además, se hace mención en el material del curso, que para determinar si exite idependencia lineal entre los Variables, se realiza la prueba <img src="https://render.githubusercontent.com/render/math?math=E[X,Y] = E[X]E[Y]">, se la condición se cumple se comprueba la independencia estadística.

En nuestro caso, se trabaja con valores discretos, por lo que solo se multiplica cada "par ordenado" por su probabilidad correspondiente. En el código anterior calcula el valor de la correlación con la línea `correlación = correlación + xyp.x[i]*xyp.y[i]*xyp.p[i]` y el resultado obtenido es:

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/correlación_res.gif)

Al calcular <img src="https://render.githubusercontent.com/render/math?math=E[X,Y]"> multiplicando <img src="https://render.githubusercontent.com/render/math?math=\mu_x\cdot\mu_y"> se obtiene:

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/val_espe.gif)

De los dos resultados anteriores se puede ver que la diferencia es muy pequeña, se le puede atribuir el error a los métodos de aproximación que se utilizaron. Como conclusión, se puede decir que las variables son estadísticamente independientes ya que <img src="https://render.githubusercontent.com/render/math?math=C_{XY} \approx E[X]E[Y]">, mismos resultado de la suposición del Inciso 2.

### Covarianza
A la covarianza se le conoce como el momento conjunto de segundo orden, se expresa como <img src="https://render.githubusercontent.com/render/math?math=C_{XY}"> y está definido por la siguiente ecuación:
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/covarianza.gif).

Es un índice muy útil para analizar la relación el que crecen o decrecen los valores de una variable con respecto a otra, existen 3 posibilidades distintas para la covarianza:
*     Si C_{XY} > 0 hay dependencia directa o positiva, los grandes valores de `x` corresponden grandes valores de `y`.
*     Si C_{XY} = 0 no hay existencia de una relación lineal entre las dos variables.
*     Si C_{XY} < 0 hay dependencia inversa o negativa, a grandes valores de `x` corresponden pequeños valores de `y`.

En este caso con valores discretos, se calcula mediante la iteración de la línea `co_varianza = co_varianza + (xyp.x[i] - mux)*(xyp.y[i]-muy)*(xyp.p[i])` y generó como resultado: 

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/covarianza_res.gif)

Tomando en cuenta la explicación y el resultado anterior, se puede decir que <img src="https://render.githubusercontent.com/render/math?math=C_{XY} \approx 0">, eso implica y confirma la independencia estadística entre las variables.

### Coeficiente de Correlación
Este es el momento de segundo orden normalizado, se denota con `ρ`. Es un índice que se utiliza para medir el grado de correlación entre 2 variables. `ρ` es un índice acotado de [-1,1[, cuando `ρ = 0` las variables son estadísticamente independientes. El también llamado Coeficiente de Pearson se calcula de la siguiente manera:

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/pearson.gif)

En el caso de las variables dadas, se obtuvo:

![alt text](https://github.com/bryancr1818/Tarea3/blob/master/ecauciones/pearson_res.gif)

Al ser el resultado anterior muy cercano a cero, nuevamente se puede puede afirmar que no existe dependencia estadística entre las variables.
  
## Inciso 4: Gráficas 2D y 3D
Se agregan las gráficas exclusivas de los ajustes de las funciones marginales, obtenidas a partir del procedimineto del ``Inciso 1``:

### Distribución de la Densidad Marginal de X
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/out/AjusteXX.png) 

### Distribución de la Densidad Marginal de Y
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/out/AjusteYY.png) 

A continuación, se presenta la superficie  que modela a la función de densidad conjunta trabajada.

### Distribución de la Densidad Conjunta
![alt text](https://github.com/bryancr1818/Tarea3/blob/master/out/Distribución_conjunta.png) 







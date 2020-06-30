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


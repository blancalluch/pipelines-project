# pipelines-project
El precio del aguacate hass en cada región de Estados Unidos

El objetivo de este pipeline es poder revisar el precio medio de los aguacates de la variedad Hass durante una semana en una región. 

La información del precio medio y el volumen vendido cada semana se obtiene del data set https://www.kaggle.com/neuromusic/avocado-prices .

La cantidad de supermercados que hay en cada región se ha obtenido a partir de https://maps.googleapis.com/maps/api/place/findplacefromtext/json

Los parámetros de entrada son:
-	La fecha, siendo ésta el primer día de la semana que se quiere observar.
-	La región de Estados Unidos escogida.
-	El tipo de aguacate: convencional u orgánico.
Los datos de salida son:
-	Los parámetros de entrada.
-	El precio medio de un aguacate esa semana.
-	La cantidad de aguacates vendidos esa semana en esa región.



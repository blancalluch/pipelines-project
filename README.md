# pipelines-project
El precio del aguacate hass en cada región de Estados Unidos

El objetivo de este pipeline es poder revisar el precio medio de los aguacates de la variedad Hass durante un año en una región. 

La información del precio medio y el volumen vendido cada semana se obtiene del dataset https://www.kaggle.com/neuromusic/avocado-prices .

Una dirección y nombre de uno de los supermercados que hay en cada región se ha obtenido a partir de https://maps.googleapis.com/maps/api/place/findplacefromtext/json

Los parámetros de entrada son:
-	El año que se quiere observar.
-	La región de Estados Unidos escogida.
-	El tipo de aguacate: convencional u orgánico.
Los datos de salida son:
-	Los parámetros de entrada.
-	El precio medio de un aguacate ese año.
-	La cantidad media de aguacates vendidos por semana ese año en esa región.
-   Crea un pdf con estos datos y dos gráficas para ver la evolucion del precio medio y de la cantidad de ventas.



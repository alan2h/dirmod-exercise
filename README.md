## Ejercicio 1
 Implementar una Web Api RESTful que retorne las cotizaciones de, al menos, 3 monedas.
 ### Backend método de ejecución :

    - Api en django rest framework. ubicacion (/backend/cotizacion/)
    - 1_ instalar requerimientos: pip install -r requirements
    - 2_ ejecutar test unitarios: python manage.py test
    - 3_ poner en modo de prueba:
       - en windows: set DJANGO_SETTINGS_MODULE=cotizacion.settings.development
       - en linux  : export DJANGO_SETTINGS_MODULE=cotizacion.settings.development
    - 4_ iniciar servidor : python manage.py runserver
    - 5_ url de la api: /cotizacion/{money}/ => ejemplos: /cotizacion/dolar/
    - 6_ swagger: en el inicio.
    - 7_ archivo json en la carpeta raiz para agregar las monedas. 

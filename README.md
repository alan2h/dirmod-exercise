## Ejercicio 

 ### Backend método de ejecución :

    - Api en django rest framework. ubicacion (/backend/cotizacion/)
    - 1_ instalar requerimientos: pip install -r requirements
    - 2_ ejecutar test unitarios: python manage.py test
    - 3_ poner en modo de prueba:
       - en windows: set DJANGO_SETTINGS_MODULE=cotizacion.settings.development
       - en linux  : export DJANGO_SETTINGS_MODULE=cotizacion.settings.development
    - 4_ iniciar servidor : python manage.py runserver
    - 5_ url de la api: /cotizacion/{currency}/ => ejemplos: /cotizacion/dolar/
    - 6_ swagger: http://127.0.0.1:8000/.
    - 7_ archivo json en la carpeta raiz para agregar las monedas. 


 ### FrontEnd método de ejecución :

    - FrontEnd en Vue Js. ubicacion (/frontend/cotizacion/)
    - 1_ ejecutar instalacion de requerimientos: npm install
    - 2_ ejecutar servidor de prueba: npm run serve
    - 3_ arquitectura flux  - utilizando Vuex
    - 4_ manejo de rutas con Vue router.


### deploys en Heroku:

   - Backend: https://herokudjangocotizacion.herokuapp.com/
   - Frontend: https://herokuvuecotizacion.herokuapp.com/
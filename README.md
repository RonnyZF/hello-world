# hello-world
// Ubicación del Termostato:

var longitud1 = -83.90;

var latitud1 = 9.85;



// Arreglo para el pseudo aleatorio de las temperaturas

var temp1 = [23,23.8,24,20,22,20,19,17,16.5,16,15,15.5];



// Arreglo para el pseudo aleatorio de las humedades relativas

var humedad1 = [71,73,70,68,65,60,63,68,72,73,74,73];



// Cobtador para seleccionar desde el arreglo.

var counter1 = context.get('counter1')||0;

counter1 = counter1+1;

if(counter1 > 11) counter1 = 0;

context.set('counter1',counter1);



// Creando el mensaje MQTT en JSON

msg = {

  payload: JSON.stringify(

    {

      d:{

        "temp" : temp1[counter1],

        "humedad" : humedad1[counter1],

        "location" :

        {

          "longitud" : longitud1,

          "latitud" : latitud1

        },

      }

    }

  )

};

return msg;

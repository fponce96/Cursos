# Guion conversacional — Curso 1

Este texto está pensado como guía, no para leerlo palabra por palabra. Se puede acortar, agregar experiencias propias y detenerse cuando aparezcan preguntas.

## Apertura

“Bueno, antes de empezar, les hago una pregunta: cuando un cliente nos dice ‘no tengo Internet’, ¿qué es lo primero que revisan ustedes?”

Escuchar algunas respuestas.

“Seguramente aparecieron varias opciones: mirar las luces, reiniciar el router, revisar el cable, probar desde otro teléfono. Todas pueden servir. El problema es que, si hacemos cosas al azar, a veces solucionamos la falla pero nunca sabemos qué pasó. La idea de hoy es entender un poco mejor el recorrido de la conexión y aprender un orden para revisar.”

“No buscamos convertirnos en ingenieros de redes. Vamos a usar solamente la teoría que nos ayude en una instalación real.”

## Diapositiva 1 — Fundamentos de Internet

“Vamos a seguir el viaje de la información desde el teléfono o la computadora del cliente hasta un servidor en Internet. En el camino vamos a ver la red local, el proveedor, las direcciones IP, DNS y algunos protocolos. Después juntamos todo en una rutina de diagnóstico.”

“Si al terminar pueden mirar una falla y decir ‘esto parece físico’, ‘esto parece de IP’ o ‘esto parece de DNS’, ya cumplimos el objetivo.”

## Diapositiva 2 — Objetivos

“Estos son los puntos que vamos a llevarnos. Primero, entender qué pasa cuando alguien abre una página. Segundo, diferenciar la LAN, que es la red local, de la WAN, que nos conecta hacia afuera. Tercero, entender los cuatro datos que siempre aparecen: IP, máscara, gateway y DNS.”

“Y lo más importante: aprender una secuencia de diagnóstico. La memoria puede fallar; una buena secuencia de trabajo nos salva.”

“¿A alguno le pasó que podía hacer ping a una dirección, pero no abrir una página por su nombre? Guarden ese caso porque más adelante vamos a ver por qué ocurre.”

## Diapositiva 3 — Cómo funciona Internet

“Muchas veces dibujamos Internet como una nube. Sirve para simplificar, pero adentro de esa nube hay una enorme cantidad de routers, enlaces y redes distintas.”

“Internet es, básicamente, una red de redes. La casa del cliente tiene una red. El proveedor tiene otra red mucho más grande. Un centro de datos tiene la suya. Todos esos mundos se conectan entre sí.”

“La información tampoco viaja como una sola pieza. Se divide en paquetes. Imaginen que queremos mandar un libro, pero lo separamos en sobres numerados. Cada sobre lleva datos para saber de dónde viene y adónde va. Los routers reciben esos paquetes y los van acercando al destino. Al final, el receptor vuelve a ordenar todo.”

Señalar la imagen.

“Acá tenemos el equipo del cliente, su router, la red del proveedor, varios equipos intermedios y el servidor final. Nosotros controlamos bien esta primera parte. Más adelante dependemos de otras redes. Por eso necesitamos pruebas que nos permitan descubrir hasta dónde llegamos.”

## Diapositiva 4 — Pensar por capas

“Esta diapositiva parece teórica, pero en realidad es muy práctica. Pensar por capas significa empezar desde abajo.”

“Primero: ¿hay energía, señal y enlace físico? Después: ¿el equipo participa de la red local? Después: ¿tiene una IP válida y sabe cuál es su gateway? Y recién más arriba preguntamos si funciona DNS o una aplicación.”

“Si el cable está cortado y no hay enlace, cambiar DNS no va a hacer ninguna diferencia. Parece obvio cuando lo decimos así, pero en una visita con apuro es fácil saltear pasos.”

“Les tiro una situación: el router no enciende. ¿En qué capa buscamos? Ahora otra: hay Internet por IP, pero no abre ningún dominio. ¿Buscaríamos en el mismo lugar? No. Esa es la utilidad de separar el problema.”

## Diapositiva 5 — Direcciones IP

“Vamos con las direcciones IP. Una IP identifica a un equipo dentro de una red. No hace falta hoy calcular subredes complicadas, pero sí entender los datos básicos.”

“Podemos usar una comparación. La IP sería la dirección de una casa. La máscara nos dice qué tamaño tiene el barrio y quiénes son vecinos. El gateway es la salida del barrio para ir a otro lugar. Y DNS es como una agenda: nosotros sabemos el nombre, y la agenda nos consigue la dirección.”

“Si el equipo recibe los datos automáticamente, normalmente interviene DHCP. Si configuramos los datos a mano, tenemos que asegurarnos de que estén dentro del rango correcto y de que no repitamos una IP que ya usa otro dispositivo.”

“Cuando tengan un equipo a mano, abran la información de red y busquen estos datos: IP, máscara, gateway y DNS. Aunque la pantalla cambie entre Android, Windows o un router, la lógica es siempre la misma.”

## Diapositiva 6 — LAN

“LAN es la red de área local. En palabras simples, es la red que tenemos dentro de la casa, la oficina o el comercio. Ahí aparecen el router, el switch, los puntos de acceso, teléfonos, computadoras y cámaras.”

“Hay una confusión muy común: Wi‑Fi e Internet no son la misma cosa. El teléfono puede estar perfectamente conectado al Wi‑Fi y, aun así, no tener salida a Internet. En ese caso el enlace inalámbrico funciona, pero falla otra parte del recorrido.”

“También puede ocurrir lo contrario: el servicio llega bien al router, un equipo por cable navega perfecto, pero el teléfono tiene poca señal o mucha interferencia. Ahí no deberíamos culpar a todo el servicio de Internet.”

“Entonces, primera pregunta útil: ¿el problema afecta a un solo dispositivo o a todos? Esa respuesta ya reduce muchísimo la búsqueda.”

## Diapositiva 7 — WAN

“Cuando salimos de la red local entramos en el mundo de la WAN. Para el cliente, normalmente es la conexión hacia el proveedor y, desde allí, hacia otras redes.”

“Dentro de la casa usamos direcciones privadas. Hacia Internet aparece una dirección pública, o una dirección compartida por el proveedor. El router usa NAT para relacionar las conversaciones internas con las respuestas que vuelven.”

“No hace falta memorizar cómo funciona cada tabla. Lo importante es entender que varios equipos de la casa pueden salir por una misma conexión, y que recibir conexiones desde afuera puede necesitar una configuración especial.”

“En la LAN podemos revisar cables, Wi‑Fi, switches y configuración. En la WAN ya dependemos del enlace y de la infraestructura del proveedor. Nuestras pruebas tienen que mostrarnos de qué lado está el corte.”

## Diapositiva 8 — DNS

“DNS parece complicado, pero la idea es muy simple: las personas recordamos nombres y las redes trabajan con direcciones.”

“Cuando escribimos el nombre de una página, el equipo primero pregunta: ‘¿Qué dirección IP corresponde a este nombre?’. Un servidor DNS responde. Con esa dirección, el equipo recién se conecta al servidor de la página.”

Señalar los tres pasos de la imagen.

“Primero hacemos la consulta. Segundo, recibimos una dirección. Tercero, nos conectamos al destino. Si falla el segundo paso, podemos tener Internet y aun así sentir que ‘no abre nada’.”

“Una prueba típica es comparar. Si llegamos a una IP externa pero no podemos resolver un dominio, DNS queda como sospechoso. Ojo: eso no significa cambiarlo de inmediato. Primero confirmamos y después aplicamos el procedimiento de la empresa.”

## Diapositiva 9 — Protocolos comunes

“Un protocolo es simplemente un conjunto de reglas para que dos equipos se entiendan. Vamos a nombrar los que más van a aparecer en el trabajo.”

“DHCP entrega la configuración de red. ARP ayuda a encontrar a un vecino dentro de la LAN. ICMP se usa en pruebas y mensajes de control; el ping es el ejemplo más conocido.”

“TCP prioriza que la información llegue completa y en orden. UDP tiene menos controles y se usa cuando importa reducir la demora. HTTP y HTTPS permiten acceder a servicios web; HTTPS agrega cifrado y verificación.”

“No es necesario memorizar todos los detalles ahora. La meta es que, cuando vean uno de estos nombres en una pantalla o un diagnóstico, sepan aproximadamente de qué parte estamos hablando.”

## Diapositiva 10 — El recorrido completo

“Ahora vamos a unir todo con un ejemplo.”

“Un teléfono se conecta al Wi‑Fi. DHCP le entrega una IP, una máscara, un gateway y DNS. La persona escribe una página. El teléfono consulta DNS y obtiene la dirección del servidor. Después manda el tráfico al gateway. El router lo pasa al proveedor, otros routers lo acercan al destino, el servidor responde y la información vuelve.”

“Ahora cortemos la historia en distintos lugares. Si DHCP falla, ¿qué dato le falta al teléfono? Si el teléfono tiene IP pero no llega al gateway, ¿miramos primero Internet o la LAN? Si llega a una IP externa pero no resuelve el nombre, ¿qué servicio revisamos?”

Dejar que el grupo responda. Volver a contar el recorrido si alguna etapa no quedó clara.

## Diapositiva 11 — Diagnóstico ordenado

“Esta es probablemente la diapositiva más importante del curso.”

“Primero escuchamos bien el síntoma. ‘No anda Internet’ puede significar muchas cosas. Preguntemos desde qué equipo, desde cuándo, si ocurre siempre y si afecta a todos.”

“Después revisamos lo físico: energía, conectores, fibra, cable de red, luces y señal. Luego miramos la configuración IP. Probamos el gateway. Si responde, probamos una IP externa permitida por nuestro procedimiento. Si eso funciona, probamos un dominio y DNS.”

“Si por cable funciona y por Wi‑Fi no, ya tenemos una comparación muy útil. Si ningún dispositivo recibe IP, también aparece una pista clara.”

“Y algo fundamental: anoten el resultado antes de cambiar algo. Si modificamos tres parámetros juntos y empieza a funcionar, no sabemos cuál era el problema. Además, podríamos haber creado otro.”

Plantear casos:

“Un solo teléfono falla y todos los demás navegan. ¿Dónde empezarían?”

“Todos tienen Wi‑Fi, pero ninguno llega al gateway. ¿Qué revisarían?”

“El gateway responde, una IP externa responde, pero los nombres no. ¿Cuál es el sospechoso principal?”

## Diapositiva 12 — Cierre

“Vamos a resumir. Internet es una red de redes. La información viaja en paquetes. La LAN es el entorno local; la WAN nos conecta con redes lejanas. IP identifica y permite encaminar. DNS transforma nombres en direcciones.”

“Pero la idea más importante no es una definición. Es el método: empezar por lo físico, avanzar hacia lo lógico, cambiar una cosa por vez y registrar lo que encontramos.”

“Al principio les pregunté qué hacían cuando un cliente decía que no tenía Internet. ¿Cambiarían algo en ese orden después de esta charla?”

Escuchar respuestas y cerrar:

“Un buen instalador no adivina. Observa, prueba, compara y documenta.”

## Práctica sugerida

“Ahora vamos a trabajar con una instalación simple. Queremos encontrar IP, gateway y DNS, probar la red local y después la salida a Internet. En cada ronda va a existir una sola falla. El objetivo no es encontrarla rápido por suerte, sino demostrar con pruebas dónde está.”

Preparar distintas rondas: cable desconectado, IP fija fuera de rango, gateway incorrecto, DNS incorrecto o mala señal Wi‑Fi.

Al terminar cada ronda preguntar: “¿Qué síntoma vimos? ¿Qué prueba descartó cada parte? ¿Qué dato deberíamos dejar registrado?”.

# Guion docente integral INSYCOM

Instructor: Facundo Ponce.

El reclamo no empieza con el cliente.

Este documento contendrá el guion completo, desarrollado para Zoom.

## 1. Presentaciones y apertura

[Portada: INSYCOM — Instructor Facundo Ponce]

«Buenas, ¿cómo están? Antes de arrancar, me gustaría conocerlos un poquito. ¿De dónde son? ¿Trabajan con Wireless, FTTH o ambas? ¿Cuánto tiempo llevan haciendo instalaciones?».

[Escuchar dos o tres respuestas.]

«La idea de este curso no es convertirnos en ingenieros. Queremos entender qué estamos mirando cuando instalamos un servicio y reconocer las señales de que algo puede fallar.

¿A alguno le pasó que instaló, el cliente abrió una página, todo parecía andar y a los pocos días llegó un reclamo? A veces la antena conectaba pero modulaba mal. O la ONT registraba pero la potencia estaba baja. O Internet llegaba bien por cable, pero el Wi-Fi no alcanzaba la habitación donde se usaba.

Por eso elegimos una frase: **El reclamo no empieza con el cliente**. Muchas veces podemos detectar problemas antes de que el cliente reclame. No siempre los vamos a poder resolver, pero sí medir, registrar y comunicar».

[Pregunta: «¿Alguna vez vieron algo que no estaba bien aunque el servicio funcionara?»]

«Cada operadora tiene sus equipos, presupuestos y procedimientos. No estamos acá para criticar eso ni imponer una única forma de trabajar. Queremos diagnosticar mejor dentro de la realidad de cada empresa».

## 2. ¿Qué es Internet?

[Mostrar diagrama: teléfono → router/ONT → red del ISP → Internet → servidor.]

«Cuando un cliente dice “no tengo Internet”, ¿qué significa exactamente? ¿Que no conecta al Wi-Fi? ¿Que no recibe una IP? ¿Que no abre una página? ¿O que falla una sola aplicación?

Internet es una red de redes. En la casa tenemos la LAN; desde allí salimos al proveedor y después a otras redes. La IP es una dirección en una red. La máscara indica quiénes son vecinos de esa red. El gateway es la salida hacia otros destinos. DNS es como una agenda que traduce nombres a direcciones.

Si el teléfono está conectado al Wi-Fi pero no navega, no significa automáticamente que falle la radio. Si una IP responde pero un dominio no resuelve, investigamos DNS. Si no hay enlace físico, cambiar DNS no va a arreglar el cable».

[Pregunta: «Si la computadora por cable navega y el celular no, ¿por dónde empezarían?»]

«El objetivo es separar las etapas y evitar cambios al azar».

## 3. Recta numérica y dBm

[Mostrar recta −100 a 0, señalando −85, −80, −75, −60, −55 y −45.]

«Antes de Wireless y fibra, repasemos los negativos. ¿Qué número es mayor: −55 o −80? −55, porque está más a la derecha y más cerca de cero.

En mediciones comparables, −55 dBm es más potencia recibida que −80 dBm. Pero no confundan más potencia con mejor calidad: también hay ruido, interferencias y posibilidad de saturar un receptor.

dBm expresa potencia; dB expresa una relación o diferencia. Si medimos −19 dBm en la NAP y −24 dBm en la ONT, tenemos 5 dB de diferencia».

[Ejercicio: ordenar −45, −60 y −75. Esperar respuestas.]

«No hace falta aprender logaritmos para interpretar la pantalla. Sí hay que saber qué se está midiendo».

## 4. Wireless — El enlace tiene dos direcciones

[Mostrar AP sectorial y CPE, flechas en ambos sentidos.]

«Cuando instalamos una CPE, necesitamos que ella escuche al AP y que el AP la escuche. En airOS podemos encontrar la señal local y la remota. No son la misma medición. Una buena recepción en la CPE no demuestra que el AP reciba bien la subida».

### Alineación y Fresnel

«No alcanza con ver la torre. También tenemos que despejar, en lo posible, la zona de Fresnel alrededor de la línea de vista. Árboles, techos o estructuras pueden afectar el enlace. Y la antena debe quedar firme: si mañana gira con el viento, el reclamo ya empezó a gestarse».

[Pregunta: «¿Una potencia aceptable garantiza una modulación estable?» No.]

### TX y recepción remota

«Pensemos en un aula. Yo soy el AP y los alumnos son CPE. Si un alumno cerca de mí grita, no necesariamente lo voy a entender mejor. El AP suele tener TX definido por ingeniería y no lo cambiamos por nuestra cuenta. Según el procedimiento, ajustamos TX de la CPE para que el AP la reciba adecuadamente.

En algunas redes se busca como referencia interna alrededor de −55 a −60 dBm de recepción en AP. No es una regla universal. Si la remota está en −45 dBm, quizás corresponda bajar gradualmente el TX de la CPE, incluso probar unos 10 dB menos si el procedimiento lo admite, y volver a revisar señal, modulación y estabilidad.

Subir la potencia al máximo no corrige obstáculos ni garantiza mejor descarga: el TX de la CPE influye principalmente en cómo la recibe el AP».

### Airtime: los turnos para hablar

«En esa aula hay diez alumnos. Si uno habla despacio o necesita repetir cada frase, ocupa más tiempo y los demás esperan. En Wireless compartimos tiempo de aire. Una CPE con baja modulación o muchas retransmisiones puede consumir más airtime para transportar los mismos datos y perjudicar a otros clientes».

[Pregunta: «¿Importa solamente cuántos clientes hay asociados?» No: también su calidad y consumo.]

### Modulación

«Imaginen que podemos codificar más información en cada símbolo, como usar sobres con mayor capacidad. En 16-QAM y 256-QAM tenemos distintas cantidades de estados de símbolo, no paquetes individuales. Cuantos más estados distinguimos, más bits por símbolo podemos representar, pero necesitamos condiciones de señal y ruido adecuadas.

Si la modulación local o remota cae, revisamos alineación, ruido, interferencia, obstáculos y potencias. No empezamos subiendo TX sin diagnóstico».

### Sectores, capacidad y herramientas

«Los AP pueden cubrir sectores de 30, 45, 60, 90 o más grados. En muchas redes se utilizan canales de 20 MHz para planificar reutilización. Un sector muy abierto puede concentrar más clientes, pero cada diseño es distinto.

Como referencias de campo, ciertos AP básicos pueden funcionar bien con unos 10–15 abonados y equipos superiores con 30–40 o más, según carga y condiciones. No son límites garantizados. Discovery puede mostrar dispositivos visibles, SSID, MAC o IP, pero no es un conteo confiable de asociados. AirView, cuando está disponible, ayuda a observar espectro. Si sospechamos saturación, informamos con evidencia».

### Configuración de CPE

«Antes de irnos comprobamos modo Station, SSID y seguridad, ancho de 20 MHz y frecuencia Auto cuando así lo indique la operadora, IP, máscara, gateway, DNS, Device ID identificable, ubicación GPS si corresponde y nodo/AP asociado. Guardamos y verificamos reconexión, recepción local/remota y modulación. No modificamos parámetros de ingeniería sin autorización».

### Actividad y FAQ Wireless

«Tómense cinco minutos y armen su checklist: fijación, Fresnel, alineación, señales, modulación, identificación, configuración, prueba y documentación».

[Escuchar propuestas.]

«¿Más TX es siempre mejor? No. ¿Discovery cuenta todos los clientes? No. ¿Si la CPE conecta está todo terminado? Tampoco. Lo que no podamos resolver, lo registramos y escalamos».

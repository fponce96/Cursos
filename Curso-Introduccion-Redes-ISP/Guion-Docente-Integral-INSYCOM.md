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

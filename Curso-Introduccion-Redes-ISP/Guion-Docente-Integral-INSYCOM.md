# Guion docente integral INSYCOM

Instructor: Facundo Ponce.

El reclamo no empieza con el cliente.

Este documento contendrá el guion completo, desarrollado para Zoom.

## 1. Presentación del instructor y de INSYCOM

[Diapositiva de portada: logotipo INSYCOM, nombre del curso, lema e instructor Facundo Ponce.]

«Buenas, ¿cómo están? Bienvenidos a esta capacitación. Antes de meternos en los temas técnicos, quiero presentarme y contarles quiénes somos y por qué decidimos preparar este curso.

Mi nombre es **Facundo Ponce**. Soy **cofundador de INSYCOM junto con Héctor** y, dentro de la empresa, me desempeño como **ingeniero principal de infraestructura**.

Trabajo en redes de proveedores de Internet, redes empresariales e infraestructura de redes móviles. También soy instructor de redes y cuento con certificaciones de **MikroTik (MTCNA y MTCNC), Cisco CCNA y Huawei**, además de la certificación de ciberseguridad **OCCP**. También soy **Fortinet Partner**.

Gran parte de lo que vamos a conversar hoy viene del trabajo en campo, de instalaciones, mantenimiento, diagnóstico y de situaciones reales que aparecen cuando una red empieza a tener problemas. Por eso quiero que este espacio sea práctico: que podamos hablar de lo que vemos en los equipos y de lo que nos pasa cuando estamos frente a un cliente».

[Pausa breve. Mostrar diapositiva de INSYCOM.]

«Ahora, ¿qué es INSYCOM? Somos una empresa dedicada a infraestructura y servicios de telecomunicaciones. Trabajamos con **redes ISP, redes empresariales e infraestructura de redes móviles**.

Actualmente, una parte de nuestro trabajo consiste en **proveer infraestructura, alquilar puertos PON y comercializar conectividad a Internet al por mayor**. Es decir, nuestro enfoque en esa actividad no está en vender Internet directamente al usuario final, sino en brindar infraestructura y capacidad a otros prestadores.

Esto nos permite ver la red desde una perspectiva un poco más amplia: no solamente el equipo que se instala en una casa, sino también lo que ocurre en la distribución, en los nodos, en los enlaces y en la infraestructura que hay detrás del servicio.

Y justamente por eso quisimos hacer esta capacitación. Muchas veces el técnico que está instalando es la primera persona que puede detectar un problema que, si no se informa, después termina afectando al cliente o incluso a otros abonados».

[Mostrar el lema.]

«La idea que quiero que nos acompañe hoy es: **El reclamo no empieza con el cliente**. Si una potencia está fuera de los valores que utiliza la empresa, si una CPE modula mal, si una fibra tiene demasiada pérdida o si el Wi-Fi no cubre donde el cliente necesita, son cosas que podemos advertir antes de que llegue un reclamo.

No significa que el instalador tenga que solucionar todo, ni que pueda cambiar parámetros de ingeniería sin autorización. Significa que tiene que saber observar, medir, documentar y avisar».

### Presentación de los participantes

«Ahora sí, me gustaría conocerlos un poquito. ¿De dónde son? ¿Trabajan principalmente con Wireless, FTTH o ambas tecnologías? ¿Hace cuánto están haciendo instalaciones?».

[Escuchar dos o tres respuestas o usar el chat si el grupo es grande.]

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

## 5. FTTH — Desde la OLT hasta la ONT

[Diagrama: OLT → ODF → splitter PLC → NAP → drop → roseta opcional → ONT.]

«Ahora cambiamos de tecnología. En vez de ondas de radio, la información viaja mediante luz por una fibra. Para diagnosticar, necesitamos conocer el recorrido completo. Puede haber uno, dos o más niveles de splitters según la ingeniería, no necesariamente tres».

### GPON, turnos y longitudes de onda

«Varias ONT comparten un puerto PON. Si todas hablaran al mismo tiempo hacia la OLT, se superpondrían. La OLT organiza turnos de subida, lo que relacionamos con TDMA, y puede asignar capacidad dinámicamente mediante DBA.

En GPON clásico, la OLT transmite hacia las ONT en 1490 nm y recibe en 1310 nm; la ONT hace lo contrario. Algunas redes agregan 1550 nm para CATV. Son como idiomas distintos para cada dirección. Podemos transmitir y recibir simultáneamente usando longitudes diferentes, aunque el ascendente se comparte por turnos».

[Pregunta: «¿Qué longitud recibe normalmente la ONT?» 1490 nm.]

«Un medidor óptico común puede medir la potencia descendente si soporta la longitud adecuada. Para medir correctamente la transmisión ascendente en ráfagas hace falta un medidor PON en línea con una ONT activa. Nunca mirar dentro de una fibra que pueda estar activa».

### Presupuesto óptico

«La potencia TX depende de la clase óptica del equipo. Cada splitter introduce una pérdida esperada. Como ejemplos: 1:2 unos 3,5–4 dB; 1:4 unos 7–7,5; 1:8 unos 10–11; 1:16 unos 13–14; 1:32 unos 16,5–18. También perdemos en fibra, conectores y empalmes. Comparar lo esperado con lo medido ayuda a localizar anomalías».

### Conectores y limpieza

[Mostrar fotografías SC, LC, FC, ST, E2000, MPO/MTP; APC y UPC.]

«En FTTH vemos mucho SC/APC, generalmente verde. Otros equipos utilizan LC y otros formatos. No debemos unir pulidos APC con UPC. Una férula sucia o dañada puede producir pérdidas y reflexiones.

Si contamos con microscopio y elementos adecuados, inspeccionamos y limpiamos siguiendo el procedimiento. Si solo tenemos power meter, podemos medir y comparar, pero reconocemos lo que no podemos confirmar. No vamos a afirmar que cualquier conector sucio perjudica a todos ni que necesariamente quema una óptica».

### Refracción, reflexión y curvas

[Mostrar lápiz dentro de vaso de agua.]

«El lápiz parece doblarse por refracción: la luz cambia dirección al pasar entre materiales. En fibra, la reflexión interna total, relacionada con los índices del núcleo y revestimiento, ayuda a guiar la luz. Si curvamos demasiado la fibra, podemos producir pérdidas.

Respetamos el radio mínimo indicado por fabricante. Como ejemplo, algunos cables permiten radios del orden de 30 mm durante tendido y 15 mm instalados, pero no son valores universales. Radio no es diámetro».

### Instalación del drop

[Fotografías de tendidos, anclajes y reservas.]

«Al instalar el drop cuidamos recorrido, tensión, viento, vanos, roces y entrada al domicilio. En algunos despliegues se utilizan vanos cercanos a 50–60 m como referencia conservadora, no como máximo universal. El diseño depende del cable y sus especificaciones.

Algunas operadoras usan grampas; otras anclan el mensajero integrado de acero o aramida conforme a procedimientos aprobados. No vamos a imponer un único método, pero sí exigir que la fijación no dañe la fibra. La roseta también depende del operador: si no se usa, igual hay que proteger curvas y conectores».

### Medir en NAP y ONT: tres casos

«En nuestra referencia preventiva, una ONT peor que −22 dBm se informa aunque esté online. No es un límite universal GPON.

Caso uno: NAP −18, ONT −19. Hay 1 dB de diferencia: el último tramo no muestra una pérdida llamativa.

Caso dos: NAP −19, ONT −24. Hay 5 dB de pérdida. Investigamos drop, conectores, curvaturas y empalmes. En tramos cortos, más de 2 dB puede justificar revisión como criterio práctico, no absoluto.

Caso tres: NAP −24, ONT −25. La diferencia local es de solo 1 dB, pero la señal ya llega débil a la NAP. Revisamos distribución aguas arriba, posiblemente con otros abonados afectados.

Las mediciones deben compararse en la misma longitud de onda con instrumento adecuado».

[Dejar que los participantes expliquen cada caso antes de dar la respuesta.]

### Registro, LEDs y servicio

«Una ONT puede recibir luz sin estar registrada, y estar registrada sin navegar. En muchos modelos LOS rojo indica pérdida de señal, PON intermitente búsqueda o registro y PON fijo registro; pero los LEDs varían según fabricante.

La autorización puede ser automática o mediante soporte. El instalador no necesariamente configura la OLT. Si la ONT no registra, verificamos potencia y entregamos serial o identificador a la mesa de ayuda. Si registra pero no navega, revisamos provisión y conectividad según el procedimiento».

### Prueba final FTTH

«No terminamos cuando prende una luz verde. Verificamos protección del drop, potencia, registro PON, enlace Ethernet, navegación, velocidad y documentación. Después necesitamos comprobar cómo el cliente usa la conexión dentro de su casa».

## 6. Wi-Fi dentro del domicilio

[Diagrama de casa con ONT, TV, habitaciones y paredes.]

«Una fibra excelente no garantiza Wi-Fi excelente en toda la casa. La conexión del proveedor termina en la ONT; la cobertura inalámbrica depende de ubicación, paredes, interferencias y dispositivos.

Cuando elegimos dónde instalar la ONT, preguntamos qué necesita el cliente. ¿Dónde está el televisor principal? ¿Hay una computadora fija? ¿Qué ambientes necesitan cobertura? Un televisor que consume mucho contenido puede funcionar más estable por Ethernet. Cablear equipos fijos reduce la competencia por airtime y la variación de latencia, aunque no significa que todo cable siempre mida más que cualquier Wi-Fi moderno.

Nosotros recomendamos y explicamos. Pero el cliente decide la ubicación dentro de lo técnicamente seguro y viable. Si elige un lugar que perjudica cobertura, lo explicamos sin discutir y documentamos la decisión».

### Bandas y señal

«En 2,4 GHz generalmente tenemos más alcance y más interferencias; en 5 GHz suele haber más capacidad cerca del equipo y menor alcance. Algunos equipos también usan 6 GHz.

Volvemos a la recta numérica: −45 dBm suele ser fuerte, −60 bueno, −75 débil y −85 muy débil. Son referencias, no sentencias: el ruido y el dispositivo también importan».

### Extender Wi-Fi

«Si una habitación no recibe bien, primero verificamos señal y necesidades. Un AP cableado suele ser una excelente solución. Mesh con backhaul cableado también. Un repetidor puede ayudar si recibe buena señal, pero no puede crear calidad donde no la recibe y puede consumir más airtime.

No recomendamos cambiar el plan de Internet o reemplazar la ONT automáticamente por un problema de cobertura».

### Speedtest

«¿Un Speedtest lento demuestra que el proveedor entrega menos velocidad? No necesariamente. Depende del dispositivo, el puerto, la banda Wi-Fi, otras descargas y el servidor.

Para evaluar el acceso empezamos, cuando se puede, por Ethernet con equipo capaz y enlace Gigabit si queremos medir más de 100 Mbps. Luego probamos Wi-Fi. Miramos descarga, subida, ping y repetimos resultados anómalos.

Caso: plan de 300 Mbps. Ethernet 290, Wi-Fi cerca de la ONT 250, dormitorio 25. ¿Dónde investigarían primero? En la cobertura y condiciones Wi-Fi de la habitación».

[Escuchar respuestas por Zoom.]

## 7. Checklist y verificación final

«¿Cuándo termina una instalación? No cuando la CPE se asocia, la ONT registra o el cliente abre YouTube. Termina cuando verificamos parámetros, funcionamiento real y documentación.

Les propongo que cada uno construya su checklist: instalación física, señal o potencia, configuración, identificación, pruebas por cable, cobertura Wi-Fi y observaciones. No sirve marcar casilleros sin medir. La lista debe adaptarse a cada empresa».

[Dar cinco minutos; escuchar dos o tres listas.]

«Si no tenemos OTDR, microscopio o analizador, hacemos lo que sí podemos con nuestras herramientas, registramos limitaciones y escalamos lo que no podemos confirmar. Pedir ayuda es parte del diagnóstico».

## 8. Preguntas frecuentes finales

**¿Una señal fuerte siempre es buena?** «No; puede haber ruido, mala modulación o saturación».

**¿La recepción local y remota deben coincidir?** «No necesariamente: son extremos distintos».

**¿Discovery muestra todos los clientes asociados?** «No».

**¿PON fija equivale a Internet?** «No; registro y servicio son etapas distintas».

**¿Una ONT en −23 dBm está necesariamente fuera de norma?** «No universalmente; en nuestra referencia preventiva corresponde informarla».

**¿NAP −19 y ONT −24?** «Cinco dB en último tramo: investigar drop y conectores».

**¿NAP −24 y ONT −25?** «Poca pérdida local, pero señal débil desde distribución».

**¿La roseta es obligatoria?** «Depende del procedimiento; proteger fibra sí es esencial».

**¿El cliente puede elegir dónde poner la ONT?** «Sí, con asesoramiento y dentro de condiciones seguras».

**¿Speedtest lento por Wi-Fi demuestra falla de fibra?** «No».

## 9. Cierre

[Diapositiva final INSYCOM.]

«Quiero que se queden con una idea: un buen instalador no es solamente el que consigue que funcione. Es quien sabe interpretar lo que ve, reconocer una anomalía y comunicarla.

Tal vez mañana revisen una modulación, una potencia, una curva del drop o una habitación con poca cobertura antes de retirarse. Ese minuto extra puede evitar un reclamo futuro.

**El reclamo no empieza con el cliente.** Muchas veces empieza mucho antes, en algo que podríamos haber detectado.

Gracias por participar. Ahora dejamos espacio para preguntas y experiencias».

[INSYCOM puede orientar consultas preliminares; los trabajos detallados de ingeniería se evalúan aparte, sin convertir el cierre en publicidad.]

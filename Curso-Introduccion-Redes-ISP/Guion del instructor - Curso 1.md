# Guion del instructor — Curso 1

## Fundamentos de Internet para instaladores

Duración sugerida: 75 a 90 minutos de explicación, más 30 minutos de práctica y preguntas.

Objetivo general: que el instalador comprenda el recorrido básico de una conexión y pueda diagnosticar una falla siguiendo un orden, sin memorizar teoría innecesaria.

## Antes de comenzar

Explicar que este curso no busca formar ingenieros de redes. Busca dar un lenguaje común y una forma ordenada de pensar. La regla central será: ir de lo físico a lo lógico y probar una cosa por vez.

Preguntar al grupo: “Cuando un cliente dice que no tiene Internet, ¿qué es lo primero que revisan?”. Anotar dos o tres respuestas para retomarlas al final.

## Diapositiva 1 — Presentación

### Qué decir

“En una instalación no alcanza con conectar cables y ver luces. Tenemos que entender, al menos por arriba, qué sucede desde el dispositivo del cliente hasta el servidor al que quiere acceder. Eso nos permite distinguir si el problema está en el cableado, en la red local, en el proveedor, en DNS o en el servicio final.”

Presentar el recorrido del curso: Internet, capas, IP, LAN, WAN, DNS, protocolos y diagnóstico.

### Mensaje clave

No hace falta saberlo todo de memoria; hace falta saber en qué orden revisar.

## Diapositiva 2 — Objetivos

Leer cada objetivo y vincularlo con una situación real. Por ejemplo: una IP incorrecta impide llegar al gateway; un DNS incorrecto permite tener conectividad pero no abrir páginas por nombre.

Pregunta al grupo: “¿Alguna vez pudieron hacer ping a una IP, pero no abrir una página?”. Esa experiencia introduce DNS sin explicarlo todavía.

Evitar profundizar aquí. Esta diapositiva funciona como mapa de la charla.

## Diapositiva 3 — Cómo funciona Internet

### Desarrollo sugerido

“Internet no es una nube mágica ni una sola red. Es una red de redes. La casa del cliente es una red; el proveedor tiene otra; los grandes operadores y centros de datos tienen otras. Todas se conectan mediante equipos que encaminan tráfico.”

Explicar la idea de paquetes con una analogía: enviar un libro dividido en sobres numerados. Cada paquete contiene información de origen y destino. Los routers eligen el próximo camino y el equipo receptor vuelve a ordenar la información.

Señalar en la imagen: dispositivo, router del cliente, red del proveedor, Internet y servidor. Explicar que la ida y la vuelta pueden atravesar varios equipos y que una falla en cualquier tramo afecta el resultado.

### Preguntas

- ¿Qué elementos controla el instalador?
- ¿Dónde termina normalmente la responsabilidad de la red local?
- ¿Que una página falle significa necesariamente que no hay Internet?

### Evitar

No entrar todavía en tablas de ruteo, BGP ni detalles de operadores. Nombrarlos solamente si alguien pregunta.

## Diapositiva 4 — Modelo por capas

Presentar las capas como una lista de verificación, no como teoría abstracta.

“Abajo está el medio físico: fibra, cable de red o radio. Encima está la comunicación local. Luego IP permite llegar a otras redes. TCP o UDP organizan el intercambio. Arriba están los servicios que usa el cliente.”

Ejemplo: si no hay luz de enlace, no tiene sentido cambiar DNS. Si se llega al gateway pero no a Internet, el problema está más arriba o fuera de la LAN.

Actividad breve: mencionar una falla y pedir al grupo que diga en qué capa empezaría a buscarla.

## Diapositiva 5 — Direcciones IP

### Qué explicar

Una IP identifica una interfaz dentro de una red. Usar `192.168.1.20` como ejemplo de dirección privada.

- IP: identifica al equipo.
- Máscara: indica qué equipos se consideran vecinos dentro de la misma red.
- Gateway: es la puerta de salida hacia otras redes.
- DNS: traduce nombres a direcciones.
- DHCP: entrega estos datos automáticamente.

Analogía: la IP es la dirección de una casa; la máscara delimita el barrio; el gateway es la salida del barrio; DNS es la agenda que permite buscar una dirección por nombre.

### Demostración sugerida

Mostrar la configuración de red de una notebook o teléfono. Pedir que identifiquen IP, gateway y DNS. Comparar una configuración correcta con una dirección automática de falla.

### Evitar

No enseñar cálculos complejos de subredes en este primer curso. Sí aclarar que IPs duplicadas o fuera del rango generan problemas.

## Diapositiva 6 — Red LAN

“La LAN es la red que está del lado del cliente: equipos conectados por cable o Wi‑Fi dentro de una vivienda, comercio u oficina.”

Identificar router, switch, punto de acceso, computadora, teléfono y cámara. Aclarar que Wi‑Fi no es sinónimo de Internet: puede existir buena conexión Wi‑Fi con una salida a Internet caída.

Preguntas: “¿Qué equipo entrega las IP? ¿Qué ocurre si conectamos dos servidores DHCP sin planificarlo? ¿Un switch común entrega Internet por sí mismo?”.

Mensaje clave: primero comprobar que el dispositivo participa correctamente de la LAN.

## Diapositiva 7 — Red WAN

Explicar que WAN es la red que conecta ubicaciones a distancia. Para el cliente, suele comenzar en el enlace hacia el proveedor.

Introducir IP pública y NAT: “Los equipos de la casa usan direcciones privadas. El router representa a esos equipos hacia afuera mediante una dirección pública. NAT mantiene la relación entre cada conversación interna y su respuesta.”

No prometer que todos los clientes poseen una IP pública exclusiva; algunos proveedores usan NAT compartido. Explicar que esto puede afectar apertura de puertos o accesos entrantes.

Comparar LAN y WAN: control local frente a infraestructura del proveedor; distancia corta frente a alcance amplio.

## Diapositiva 8 — DNS

### Speech sugerido

“Las personas recuerdan nombres; las redes trabajan con direcciones. DNS funciona como una agenda distribuida. El dispositivo pregunta qué dirección corresponde a un nombre, recibe una respuesta y recién entonces inicia la conexión al servidor.”

Recorrer los tres pasos de la imagen. Aclarar que las respuestas se guardan temporalmente para acelerar consultas futuras.

Caso práctico: si funciona un ping a una IP de Internet pero falla la resolución de un dominio, la conectividad existe y el siguiente sospechoso es DNS.

Evitar afirmar que cambiar a un DNS público soluciona todo. Primero hay que confirmar la causa y respetar la configuración definida por la empresa.

## Diapositiva 9 — Protocolos frecuentes

Explicar cada uno con una frase y un caso de uso:

- DHCP: entrega la configuración de red.
- ARP: encuentra la dirección física asociada a una IP dentro de la LAN.
- ICMP: informa y permite pruebas como ping.
- TCP: confirma entrega y orden; se usa cuando la confiabilidad importa.
- UDP: reduce controles y latencia; es habitual en voz, video y DNS.
- HTTP/HTTPS: transporta contenido web; HTTPS agrega cifrado y validación.

Mensaje clave: un protocolo es un conjunto de reglas compartidas. No es un cable ni una aplicación específica.

## Diapositiva 10 — Recorrido completo

Contar el recorrido como una historia:

“Un teléfono se conecta al Wi‑Fi. DHCP le entrega IP, máscara, gateway y DNS. El usuario escribe un sitio. DNS devuelve su dirección. El teléfono envía los paquetes al gateway. El router los entrega al proveedor y diferentes routers los acercan al servidor. El servidor responde y el proceso vuelve.”

Luego repetir el recorrido introduciendo una falla en cada etapa. Preguntar qué observaría el usuario y qué prueba haría el instalador.

## Diapositiva 11 — Diagnóstico básico

### Secuencia recomendada

1. Escuchar el síntoma exacto y determinar si afecta a uno o a todos los dispositivos.
2. Revisar alimentación, conectores, fibra, Ethernet, LEDs y nivel de señal.
3. Confirmar conexión a la LAN y configuración IP.
4. Probar el gateway.
5. Probar una IP externa conocida según el procedimiento de la empresa.
6. Probar resolución DNS y acceso por nombre.
7. Comparar cable y Wi‑Fi si corresponde.
8. Registrar resultados y recién después cambiar configuraciones.

Recalcar: modificar varias cosas a la vez impide saber cuál era la causa y puede agregar nuevas fallas.

### Casos para debatir

- Un solo teléfono no navega, pero los demás sí.
- Ningún equipo recibe IP.
- Se llega al gateway, pero no a una IP externa.
- Se llega a una IP externa, pero los dominios no resuelven.
- Por cable funciona bien y por Wi‑Fi hay cortes.

## Diapositiva 12 — Cierre

Retomar las respuestas iniciales del grupo. Ordenarlas según la secuencia aprendida.

Cerrar con cuatro ideas:

1. Internet es una red de redes y la información viaja en paquetes.
2. LAN es el entorno local; WAN conecta esa red con otras.
3. IP identifica y encamina; DNS traduce nombres.
4. El diagnóstico eficaz avanza de lo físico a lo lógico y deja registro.

Frase de cierre sugerida: “Un buen instalador no adivina: observa, prueba, compara y documenta.”

## Práctica final sugerida

Armar una instalación simple con router, switch y dos dispositivos. Pedir a los participantes que identifiquen IP, gateway y DNS; prueben conectividad local y externa; y diagnostiquen una falla preparada previamente.

Fallas posibles: cable desconectado, IP fija fuera de rango, gateway incorrecto, DNS incorrecto o Wi‑Fi con señal débil. Realizar una sola falla por ronda.

## Qué no conviene decir o hacer

- No asegurar que reiniciar siempre soluciona el problema.
- No cambiar configuraciones sin registrar el estado anterior.
- No confundir Wi‑Fi con Internet.
- No culpar al proveedor o al cliente sin pruebas.
- No usar términos técnicos sin explicar su utilidad práctica.
- No compartir contraseñas, direcciones públicas sensibles ni datos de clientes en ejemplos.

## Material que conviene preparar

- Router y switch de demostración.
- Notebook con herramientas básicas de red.
- Latiguillos Ethernet en buen y mal estado, claramente identificados.
- Capturas de configuraciones correctas e incorrectas.
- Hoja de diagnóstico para registrar síntoma, pruebas, resultados y resolución.

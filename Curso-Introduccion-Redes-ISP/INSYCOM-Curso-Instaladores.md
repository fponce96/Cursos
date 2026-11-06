# INSYCOM | Instalaciones ISP: diagnóstico preventivo
**Instructor: Facundo Ponce**  
**Lema: El reclamo no empieza con el cliente**  
Modalidad: capacitación por Zoom. Material didáctico; los valores de referencia no sustituyen los procedimientos de cada operadora.

## 01 — Guion del instructor
### Apertura
«¿Cuándo termina una instalación: cuando conecta, cuando navega o cuando comprobamos que funciona correctamente?». Escuchar respuestas. El propósito es anticipar fallas, medir y documentar, no solamente conseguir conectividad.

### Internet y redes
Internet es una red de redes. Repasar recorrido: dispositivo → LAN → gateway → ISP → otras redes → servidor. Separar enlace físico, configuración IP, gateway, DNS y aplicación. Pregunta: «Si abre por IP pero no por nombre, ¿qué investigarían?».

### Recta numérica
Los dBm suelen ser negativos: −55 dBm es una señal más fuerte que −80 dBm. Comparar valores en una recta numérica; explicar que 0 está a la derecha de los negativos. La diferencia entre dos potencias expresadas en dBm se expresa en dB. No interpretar −80 como mejor que −55 por tener 80 mayor valor absoluto.

### Wireless: señal, airtime y modulación
Analogía de aula: un docente y varios alumnos comparten turnos para hablar. Un alumno con señal deficiente ocupa más tiempo de aire para transmitir la misma información. AP y CPE muestran potencias recibidas distintas: señal local AP→CPE y remota CPE→AP. El TX de la CPE modifica principalmente la recepción en el AP; no arregla una mala alineación ni garantiza mejor descarga. Ajustar conforme a parámetros de ingeniería; referencia interna habitual de recepción en AP cercana a −55/−60 dBm, no umbral universal.
Modulación: constelaciones como 16-QAM y 256-QAM codifican distinta cantidad de bits por símbolo, pero exigen distintas condiciones de señal y ruido. Usar analogía de sobres de información sin confundir símbolos con paquetes.
Verificar alineación, obstáculos, Fresnel, ruido, interferencias, modulación local/remota y airtime. En sectores de 20 MHz la capacidad depende de AP, clientes y entorno; no existe un número fijo de abonados garantizado.
Configuración de CPE: modo Station, SSID, seguridad, ancho de 20 MHz y frecuencia Auto cuando lo exige la operadora, IP/máscara/gateway/DNS, Device ID identificable, ubicación GPS, nodo/AP asociado, guardar y verificar. No cambiar ajustes de ingeniería por iniciativa propia.
Pregunta: «¿Qué informarían si la CPE conecta pero el sector parece saturado?». Registrar indicios y escalar; Discovery no equivale a un censo completo de asociados.

### FTTH: recorrido y óptica
OLT → ODF → splitters PLC → NAP → drop → roseta opcional → ONT. GPON comparte la capacidad mediante turnos de transmisión ascendente (TDMA/DBA). En GPON clásico, OLT transmite 1490 nm y recibe 1310 nm; ONT transmite 1310 nm y recibe 1490 nm. Puede haber 1550 nm para CATV. Los valores ópticos dependen de la clase y del diseño.
Medidor convencional: normalmente mide downstream en 1490 nm; para upstream de ráfagas se requiere medidor PON adecuado, en línea con ONT activa. Nunca mirar dentro de una fibra.
Pérdidas ilustrativas PLC: 1:2 ~3,5–4 dB; 1:4 ~7–7,5; 1:8 ~10–11; 1:16 ~13–14; 1:32 ~16,5–18. Sumarlas a fibra, conectores y empalmes según el diseño.
Conectores: SC, LC, FC, ST, E2000 y MPO/MTP; distinguir UPC/APC. No acoplar APC con UPC. Suciedad puede generar pérdida y reflexión. Explicar refracción con lápiz en vaso de agua, luego reflexión interna total y por qué las curvaturas pronunciadas pueden aumentar pérdidas.
Drop: fijación mecánica conforme al cable y procedimiento de la operadora, con mensajero o grampas aprobadas; respetar radios de curvatura del fabricante, protección y recorrido. Roseta opcional según instalación.
Política preventiva de ejemplo: reportar RX ONT peor que −22 dBm aunque registre, sin confundirlo con límite universal. Comparar potencia NAP/ONT en 1490 nm. Ejemplos: −18/−19 = 1 dB normal; −19/−24 = 5 dB revisar último tramo; −24/−25 = 1 dB pero la potencia ya llega débil a NAP. Pérdida >2 dB entre NAP y ONT amerita revisión en el ejemplo, no regla universal.
Registro ONT: potencia óptica, estado PON y servicio de Internet son cosas diferentes. Interpretar LEDs según fabricante; autorización automática o mesa de ayuda según operador. Verificar serie, registro, provisión, Ethernet y navegación.

### Wi-Fi en el domicilio
Fibra y Wi-Fi no son equivalentes. Ubicación de ONT: equilibrar entrada de fibra, cobertura y cable Ethernet para TV y equipos fijos exigentes. Recomendar cableado cuando sea viable, explicar ventajas y respetar decisión del cliente, documentando limitaciones.
2,4 GHz suele tener mayor alcance pero más interferencia; 5 GHz suele ofrecer más capacidad a distancias cortas. Referencias de RSSI: −45 fuerte, −60 bueno, −75 débil, −85 muy débil; contexto y ruido importan. Para extender cobertura: AP por Ethernet, mesh con backhaul cableado si es posible, o repetidor con señal de entrada adecuada.
Speedtest: primero Ethernet Gigabit y equipo capaz, después Wi-Fi; revisar negociación del puerto, otras descargas, servidor, ping, subida, bajada y repetibilidad. Caso: plan 300 Mbps, Ethernet 292, Wi-Fi junto a ONT 255, dormitorio 28: investigar cobertura y condiciones Wi-Fi, no cambiar automáticamente el plan.

### Cierre
«Una instalación no termina cuando prende una luz verde. Termina cuando medimos, verificamos, documentamos y comunicamos anomalías. Pedir ayuda es parte del diagnóstico. El reclamo no empieza con el cliente».

## 02 — Manual técnico del participante
### Secuencia de diagnóstico
1. Seguridad y estado físico: energía, fijaciones, cables, conectores y radios de curvatura.
2. Capa de acceso: señal, RX local/remoto y modulación en Wireless; RX óptica y PON en FTTH.
3. Configuración: identificación, IP, máscara, gateway, DNS, SSID/seguridad o provisión ONT.
4. Conectividad: enlace LAN, gateway, DNS, navegación, velocidad y latencia.
5. Experiencia del cliente: Wi-Fi en ambientes relevantes, dispositivos fijos y necesidades.
6. Evidencia: lecturas, pruebas, ubicación, fotos cuando correspondan, anomalías y escalamiento.

### Tabla de interpretación
- dBm: potencia absoluta expresada en escala logarítmica.
- dB: relación o diferencia de niveles, útil para pérdidas.
- RX local y remoto en Wireless: cada dirección puede tener condiciones distintas.
- ONT con luz PON fija: normalmente registrada, pero no prueba que exista Internet.
- Speedtest lento solo en Wi-Fi: no demuestra por sí solo falla de proveedor.
- Pérdidas y umbrales: aplicar valores y márgenes aprobados por cada operador.

### Casos guiados
A. Wireless: local −55 dBm, remoto −45 dBm. Revisar TX de CPE según procedimiento, sin tocar AP; observar modulación y estabilidad.
B. FTTH: NAP −19 dBm, ONT −24 dBm. Diferencia 5 dB: revisar drop, conectores, curvas y empalmes.
C. FTTH: NAP −24, ONT −25. Diferencia 1 dB: revisar distribución aguas arriba; no culpar primero al drop.
D. Wi-Fi: 290 Mbps por Ethernet y 25 Mbps en habitación alejada. Verificar banda, RSSI, interferencias y capacidad del cliente.

## 03 — Actividades, checklist y preguntas frecuentes
### Actividad: diseñá tu checklist
En cinco minutos cada participante redacta verificaciones para sus instalaciones. Compartir dos o tres propuestas. Comparar contra los controles de seguridad, acceso, configuración, servicio, experiencia y documentación. No marcar casillas sin medir.

### Checklist adaptable
- [ ] Alimentación y montaje seguros.
- [ ] Cableado, conectores y recorrido inspeccionados.
- [ ] Señal o potencia dentro de criterios del operador.
- [ ] Equipo identificado y ubicación registrada.
- [ ] Configuración y autorización verificadas.
- [ ] Ethernet, gateway, DNS y navegación comprobados.
- [ ] Velocidad medida con dispositivo y conexión adecuados.
- [ ] Cobertura Wi-Fi revisada en áreas acordadas.
- [ ] Cliente informado de recomendaciones y decisiones.
- [ ] Anomalías documentadas y escaladas.

### Preguntas frecuentes
**¿Más potencia TX siempre mejora Wireless?** No. Puede saturar el receptor remoto y aumentar interferencias; seguir parámetros de ingeniería.
**¿Por qué señal local y remota difieren?** Son dos enlaces de recepción con potencias, ganancias y condiciones diferentes.
**¿Un AP visible en Discovery demuestra capacidad disponible?** No; es solo un indicio de presencia, no medición completa de carga.
**¿PON encendida significa Internet?** No. Registro óptico y servicio provisionado son etapas distintas.
**¿Qué hago con ONT en −23 dBm?** Aplicar criterio del operador; en este curso, informar y revisar aunque esté online.
**¿Qué significa 5 dB entre NAP y ONT?** Pérdida del último tramo a investigar, comparando misma longitud de onda.
**¿Siempre se instala roseta?** No; depende del operador, pero la fibra debe quedar protegida.
**¿Un Speedtest por Wi-Fi certifica el plan?** No por sí solo; depende de equipo, banda, interferencias y servidor.
**¿Cablear la TV es obligatorio?** No. Recomendar Ethernet cuando sea viable, explicar beneficios y respetar elección del cliente.
**¿Si no tengo OTDR o microscopio no puedo diagnosticar?** Sí se puede avanzar con inspección, medidor de potencia, pruebas y escalamiento, reconociendo limitaciones.
**¿Qué hago si no puedo resolver una anomalía?** Registrar mediciones y pedir soporte con evidencia.

### Preguntas finales para Zoom
1. ¿Qué revisarías antes de modificar el TX de una CPE?
2. ¿Qué diferencia hay entre dBm y dB?
3. ¿Qué significa que una ONT tenga potencia pero no registre?
4. ¿Cómo separarías una falla del ISP de una mala cobertura Wi-Fi?
5. ¿Qué dato registrarías para que el próximo técnico no empiece de cero?

### Nota del instructor
Curso introductorio y transversal. Las referencias de potencia, distancias, radios y capacidad son ejemplos y deben contrastarse con manuales, normas y criterios de cada operadora.

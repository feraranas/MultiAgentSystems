##  TC2008B. Modelación de Sistemas Multiagentes con Gráficas

### Computacionales Actividad Integradora

# Parte 1. Sistemas multiagentes Descripción del problema

#### Descripción:

¡Felicidades! Eres el orgulloso propietario de 5 robots nuevos y un almacén lleno de cajas. 

El dueño anterior del almacén lo dejó en completo desorden, por lo que depende de tus robots organizar las cajas en algo parecido al orden y convertirlo en un negocio exitoso.

Cada robot está equipado con ruedas omnidireccionales y, por lo tanto, puede conducir en las cuatro direcciones. Pueden recoger cajas en celdas de cuadrícula adyacentes con sus manipuladores, luego llevarlas a otra ubicación e incluso construir pilas de hasta cinco cajas. 

Todos los robots están equipados con la tecnología de sensores más nueva que les permite recibir datos de sensores de las cuatro celdas adyacentes. Por tanto, es fácil distinguir si un campo está libre, es una pared, contiene una pila de cajas (y cuantas cajas hay en la pila) o está ocupado por otro robot. Los robots también tienen sensores de presión equipados que les indican si llevan una caja en ese momento.

Lamentablemente, tu presupuesto resultó insuficiente para adquirir un software de gestión de agentes múltiples de última generación. Pero eso no debería ser un gran problema ... ¿verdad? Tu tarea es enseñar a sus robots cómo ordenar su almacén. La organización de los agentes depende de ti, siempre que todas las cajas terminen en pilas ordenadas de cinco en cinco.
Realiza la siguiente simulación:

- Inicializa las posiciones iniciales de las K cajas. Todas las cajas están a nivel de piso, es decir, no hay pilas de cajas.
- Todos los agentes empiezan en posición aleatorias vacías.
- Se ejecuta en el tiempo máximo establecido.

Deberás recopilar la siguiente información durante la ejecución:

- Tiempo necesario hasta que todas las cajas están en pilas de máximo 5 cajas.
- Número de movimientos realizados por todos los robots.
- Analiza si existe una estrategia que podría disminuir el tiempo dedicado, así como la cantidad de movimientos realizados. ¿Cómo sería? Descríbela.

Para los agentes:
-  Diseña la arquitectura del tipo de agente que usarás (BDI, basado en lógica, un híbrido, reactivo, etc.), incluyendo cómo funciona en cada sistema que lo compone.
- Diseña una ontología para los agentes, al menos en forma de Taxonomía Informal.

- Para esta Actividad, no es necesario que la uses en la implementación.
- Para esta actividad, no se toma en cuenta la comunicación e interacción entre agentes.

# Parte 2. Gráficas Computacionales

#### Descripción:

Aplica la misma descripción de la actividad en la Parte 1.

Tu trabajo consiste en modelar y desplegar la representación en 3D del mismo. El diseño y despliegue debe incluir:
- Modelos con materiales (colores):
- Caja
- Robot (robots tipo plataforma de carga, al menos 5 robots).
- Almacén (piso, paredes y puerta).
- Animación
- Los robots deberán desplazarse sobre el piso del almacén, en los pasillos que forman los estantes.
- Los robots se moverán con velocidad predeterminada (aleatoria).
- Los robots comenzarán a operar en posiciones predeterminadas (aleatorias).
- Detección de colisiones básica
- Los robots detectarán y reaccionarán a colisiones (detección de robot - caja). Determina e implementa un sistema básico para esto (por ejemplo, detenerse previo a una colisión, recoger la caja). Una vez que el robot tiene la caja, transportarla al lugar de descarga y simular su proceso de descarga.

# Especificaciones de entrega

- Para la Parte 1, un documento PDF con los diagramas de los sistemas de cada tipo de agente, así como la descripción de cada sistema, *por ejemplo, si es un agente BDI, describe cuáles son sus creencias, deseos e intenciones*, y cómo está diseñados sus **funciones brf**, **options**, **filter**.

- También agrega el **diagrama de la ontología de los agentes**, así como una breve descripción de ésta.

Para ambas partes del problema, considera que:
• Tienes un almacén de MxN espacios.
• K cajas iniciales, en posiciones aleatorias. • 5 robots.
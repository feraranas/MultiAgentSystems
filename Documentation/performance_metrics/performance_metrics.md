# Performance metrics

## Q & A

### 1. ¿Cuál es la definición formal de la utilidad basada en corridas?

> A. Una función que va de el conjunto de Corridas al conjunto de los números reales

> B. Una tupla compuesta por el conjunto de corridas y el conjunto de números reales

*Respuesta B*

### 2. ¿Qué es un agente óptimo, con respecto a la utilidad?

> El agente que tiene la mayor esperanza de utilidad entre los agentes

### 3. ¿Qué es un Predicado de Tarea?

> A. Una función que va del conjunto de tareas a un conjunto de estados

> B. Una función que va del conjunto de corridas al conjunto compuesto por el 0 y el 1

*Respuesta B*

### 4. ¿Cuál es la definición formal de la utilidad basada en estados?

> Una función que va del conjunto de estados al conjunto de los números reales

### 5. Imagine dos agentes jugando ajedrez, ¿cuál métrica de desempeño sería adecuada?

> Ambientes de tarea (Task Environment)

### 6. Considere un ambiente definido de la siguiente forma:

$ E = \{e_0, e_1, e_2, e_3, e_4, e_5\} $

$ \tau(e_0 \rightarrow \alpha_0) = \{e_1, e_2, e_3\} $

$ \tau(e_0 \rightarrow \alpha_1) = \{e_4, e_5\} $

- También considere dos agentes definidos como:

$ \text{Ag}_1(e_0) = \alpha_0 $

$ \text{Ag}_2(e_0) = \alpha_1 $

- Las probabilidades de las corridas consideradas son las siguientes:

$ P(e_0 \rightarrow \alpha_0 | \text{Ag}_1, \text{Env}) = 0.4 $

$ P(e_0 \rightarrow \alpha_0 | \text{Ag}_1, \text{Env}) = 0.6 $

$ P(e_0 \rightarrow \alpha_0 | \text{Ag}_1, \text{Env}) = 0.1 $

$ P(e_0 \rightarrow \alpha_1 | \text{Ag}_2, \text{Env}) = 0.2 $

$ P(e_0 \rightarrow \alpha_1 | \text{Ag}_2, \text{Env}) = 0.7 $

Asuma que la función de utilidad está definida como sigue:

$ u(e_0 \rightarrow \alpha_0 \rightarrow e_1) = 8 $

$ u(e_0 \rightarrow \alpha_0 \rightarrow e_2) = 11 $

$ u(e_0 \rightarrow \alpha_0 \rightarrow e_3) = 70 $

$ u(e_0 \rightarrow \alpha_1 \rightarrow e_4) = 9 $

$ u(e_0 \rightarrow \alpha_1 \rightarrow e_5) = 15 $

#### R: Determinación del Agente Óptimo

Para determinar qué agente es óptimo, calculamos la utilidad esperada para cada agente y comparamos los resultados.

##### Agente 1 ($\text{Ag}_1$)

$ U(\text{Ag}_1) = P(e_0 \rightarrow \alpha_0 | \text{Ag}_1, \text{Env}) \cdot u(e_0 \rightarrow \alpha_0 \rightarrow e_1) + P(e_0 \rightarrow \alpha_0 | \text{Ag}_1, \text{Env}) \cdot u(e_0 \rightarrow \alpha_0 \rightarrow e_2) + P(e_0 \rightarrow \alpha_0 | \text{Ag}_1, \text{Env}) \cdot u(e_0 \rightarrow \alpha_0 \rightarrow e_3) $

$ U(\text{Ag}_1) = (0.4 \cdot 8) + (0.6 \cdot 11) + (0.1 \cdot 70) $

$ U(\text{Ag}_1) = 3.2 + 6.6 + 7 $

$ U(\text{Ag}_1) = 16.8 $

## Agente 2 ($\text{Ag}_2$)

$ U(\text{Ag}_2) = P(e_0 \rightarrow \alpha_1 | \text{Ag}_2, \text{Env}) \cdot u(e_0 \rightarrow \alpha_1 \rightarrow e_4) + P(e_0 \rightarrow \alpha_1 | \text{Ag}_2, \text{Env}) \cdot u(e_0 \rightarrow \alpha_1 \rightarrow e_5) $

$ U(\text{Ag}_2) = (0.2 \cdot 9) + (0.7 \cdot 15) $

$ U(\text{Ag}_2) = 1.8 + 10.5 $

$ U(\text{Ag}_2) = 12.3 $

Comparando las utilidades esperadas, vemos que $ U(\text{Ag}_1) = 16.8 $ y $ U(\text{Ag}_2) = 12.3 $. Por lo tanto, el Agente 1 ($\text{Ag}_1$) es óptimo en este contexto.

### 7. ¿Cuál es el propósito de obtener la Esperanza de Utilidad de un agente?

> Para entender qué tan útil podría ser antes de correr la simulación, sí se espera no ser útil, entonces reevaluar el diseño del agente

### 8. Imagine a dos agentes jugando un juego de mini golf sencillo. ¿Cuál sería una métrica de desempeño adecuada?

> A. Corridas exitosas 

> B. Utilidad sobre corridas 

*Respuesta B*
##  TC2008B. Modelación de Sistemas Multiagentes con Gráficas

### Computacionales Actividad Integradora

# Parte 1. Sistemas multiagentes Descripción del problema

#### Descripción:

¡Felicidades! Eres el orgulloso propietario de 5 robots nuevos y un almacén lleno de cajas.

El dueño anterior del almacén lo dejó en completo desorden, por lo que depende de tus robots organizar las cajas en algo parecido al orden y convertirlo en un negocio exitoso.

Cada robot está equipado con ruedas omnidireccionales y, por lo tanto, puede conducir en las cuatro direcciones. Pueden recoger cajas en celdas de cuadrícula adyacentes con sus manipuladores, luego llevarlas a otra ubicación e incluso construir pilas de hasta cinco cajas.

Todos los robots están equipados con la tecnología de sensores más nueva que les permite recibir datos de sensores de las cuatro celdas adyacentes. Por tanto, es fácil distinguir si un campo está libre, es una pared, contiene una pila de cajas (y cuantas cajas hay en la pila) o está ocupado por otro robot. Los robots también tienen sensores de presión equipados que les indican si llevan una caja en ese momento.


```python

# Preguntas:
# ¿Los Montacargas son los agentes, o las cajas son los agentes?
# ¿Las cajas son obstáculos en el modelo?

class MontacargasAgent(ap.Agent):
     """ An Montacargas Cleaner Agent. """

     def setup(self):
          pass

     def move_randomly(self):
          pass

     def collision_detection(self):
          pass

     def agent_pickup(self):
          pass

     def agent_move_to_destiny(self):
          pass

     def agent_deposits(self):
          pass
```

Lamentablemente, tu presupuesto resultó insuficiente para adquirir un software de gestión de agentes múltiples de última generación. Pero eso no debería ser un gran problema ... ¿verdad? Tu tarea es enseñar a sus robots cómo ordenar su almacén. La organización de los agentes depende de ti, siempre que todas las cajas terminen en pilas ordenadas de cinco en cinco.

Realiza la siguiente simulación:

- Inicializa las posiciones iniciales de las K cajas. Todas las cajas están a nivel de piso, es decir, no hay pilas de cajas.
- Todos los agentes empiezan en posición aleatorias vacías.
- Se ejecuta en el tiempo máximo establecido.

```python
# Define parameters

parameters = {
    'Densidad Cajas': 0.3, # Porcentaje del grid cubierto por cajas
    'size': 15, # Altura y Longitud del grid
    'steps': 100,
    'montacargas': 5,
}
```

```python
class AlmacenModel(ap.Model):
     
     def setup(self):
          """ Definimos 2 cosas importantes:
               1. Cuántos montacargas vamos a crear en el modelo.
               2. La cantidad de cajas a ser ordenadas por los montacargas. 
          """
          
          # Calculamos el número de cajas dado un valor de densidad.
          n_cajas = int(self.p['Densidad Cajas'] * (self.p.size ** 2))
          
          # Creamos 2 listas de agentes, una lista para cajas y otra lista de montacargas.
          montacargas = self.montacargas = ap.AgentList(self, self.p.montacargas, MontacargasAgent)
          cajas = self.cajas = ap.AgentList(self, n_cajas)

          # Creamos un ambiente tipo grid (almacen).
          self.almacen = ap.Grid(self, [self.p.size] * 2, track_empty = True)

          # Agregamos los agentes cajas y robots al grid en posición aleatoria.
          # ¿Cómo distinguir que uno es `montacarga` y otro es `caja`? => esto es
          #  importante porque cuando buscamos vecinos de un montacargas, nos
          #  debemos cerciorar que buscamos `cajas` y no otro `montacargas`. 
          self.almacen.add_agents(cajas, random = True, empty = True)
          self.almacen.add_agents(montacargas, random = True, empty = True)

          # Inicializamos una variable dinámica para todas las cajas.
          # Condicion 0: desordenada
          # Condicion 1: colisionada
          # Condicion 2: recogida
          # Condicion 3: ordenada
          self.cajas.condition = 0

          # Inicializamos una variable dinámica para todos los agentes.
          # Condicion 0: en_movimiento
          # Condicion 1: en_colision
          # Condicion 2: en_pickup
          # Condicion 3: en_movimiento_pickup
          # Condicion 4: en_dropdown
          self.montacargas.condition = 0

     def step(self):
          # Seleccionamos todas las cajas desordenadas.
          cajas_desordenadas = self.cajas.select(select.cajas.condition == 0)

          # Seleccionamos los montacargas en movimiento.
          montacargas_en_movimiento = self.montacargas.select(select.montacargas.condition == 0)

          # Para cada montacarga en estado de movimiento, vemos si tiene cajas
          # vecinas a una distancia de 1 (en cada dirección, diagonal incluída).
          for montacarga in montacargas_en_movimiento:
               for neighbor in self.almacen.neighbors(agent=montacarga, distance=1):
                    if neighbor.condition 


          # Detenemos simulación si no hay cajas desordenadas
          if len(cajas_desordenadas) == 0:
               self.stop()

     def end(self):
          pass
```

```python
def animation_plot(model, ax):

     # Grid de atributos para cajas y montacargas
     attr_grid_montacargas = model.montacargas.attr_grid('condition')
     attr_grid_cajas = model.almacen.attr_grid('condition')

     # Mapa de colores para los estados de las cajas
     color_dict_cajas = {  0: '#cc0000', # rojo claro: caja desordenada
                           1: '#b4a7d6', # morado claro: caja colisionada
                           2: '#b6d7a8', # verde claro: caja recogida
                           3: '#ffd966', # amarillo: caja ordenada
                         }

     # Mapa de colores para los estados de los montacargas
     color_dict_montacargas = { 0: '#9fc5e8', # azul claro: robot en movimiento
                                1: '#351c75', # morado fuerte: robot en colisión con caja
                                2: '#38761d', # verde fuerte: robot haciendo pickup
                                3: '#073763', # azul fuerte: robot en movimiento al objetivo
                                4: '#0606060', # gris: robot haciendo dropdown
                              }

     # Dibujamos el grid
     ap.gridplot(attr_grid_montacargas,
                 ax = ax,
                 color_dict = color_dict_montacargas, 
                 convert = True
               )

     # Etiquetas dinámicas
     ax.set_title(f"Simulacion de montacargas\n"
                  f"Time-step: {model.t}, Cajas por ordenar: "
                  f"{len(model.cajas.select(model.cajas.condition == 0))}")
```

```python
# Instancia del modelo y Gráfica animada
fig, ax = plt.subplots()
model = AlmacenModel(parameters)
animation = ap.animate(model, fig, ax, animation_plot)
IPython.display.HTML(animation.to_jshtml(fps=15))
```

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

- Tienes un almacén de MxN espacios.
- K cajas iniciales, en posiciones aleatorias.
- 5 robots.

## Referencias para armar el modelo:

[Modelo Forest Fire](https://agentpy.readthedocs.io/en/latest/agentpy_forest_fire.html)

[Espacios Discretos en AgentPy - Grid](https://agentpy.readthedocs.io/en/latest/reference_grid.html#agentpy.Grid)

[Iterators en AgentPy - AgentIter](https://agentpy.readthedocs.io/en/latest/reference_sequences.html#agentpy.AgentIter)

[Sequencias para manejar grupos de agentes](https://agentpy.readthedocs.io/en/latest/reference_sequences.html#agentpy.AgentDList)

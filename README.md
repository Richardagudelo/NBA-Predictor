# 🏀🏀 NBA-Predictor 🏀🏀
#### Proyecto final Simulación de computadores
##### Simula **1000** temporadas de la NBA y predice un ganador para la proxima temporada.

## Contenido

- [Enunciado](#enunciado)
- [¿ Cómo usar este proyecto ?](#usar-este-proyecto)
  - [Construir el proyecto](#construir-el-proyecto)
- [Dependencias](#dependencias)
- [Integrantes del equipo](#integrantes)

## Enunciado
Se propone predecir el ganador de la siguiente temporada de la NBA, para ello se simulan 1000 temporadas, donde en cada una sale un ganador. Teniendo esto, se consulta el equipo que gano mas temporadas de las mil simuladas y este será el ganador que predice el software, para la siguiente temporada.
Para ello usamos la libreria [nba_api](https://pypi.org/project/nba-api/) que nos permite obtener datos de las distintas temporadas de la nba, así como sus participantes, usando distintos [endpoints](https://github.com/swar/nba_api/tree/master/docs/nba_api/stats/endpoints) que provee, como las [metricas](https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/teamestimatedmetrics.md) estimadas de los distintos equipos.
Así se arman los distintos componentes de una temporada de la NBA, como los son:
- Conferencias: Existen dos conferencias
  - Western Conference
  - Eastern Conference

- Divisiones: Hay 3 divisiones por cada conferencia
  - Western Conference
    - Northwest
    - Pacific
    - Southwest
  - Eastern Conference
    - Atlantic
    - Central
    - Southeast
- Equipos: Cada division tiene 5 equipos, así tenemos un total de 30 equipos para una temporada

## Usar este proyecto

El uso de este proyecto se explica a continuación:

### Construir el proyecto

1. Instala las [dependencias](#dependencias) del proyecto

2. Clona el proyecto
```
git clone https://github.com/Richardagudelo/NBA-Predictor.git
```

3. Desde una terminal, navega hasta el script [run.py](runner/run.py), allí ejecuta:
```
python run.py
```
4. Se mostrara una ventana en la cuál puedes iniciar la simulación y visualizar los resultados

5. A jugar ! 🏟🏀🧺⛹️‍♀️⛹️‍♂️⛹🏻‍♀️⛹🏻‍♂️⛹🏿‍♀️⛹🏿‍♂️🧺🏀🏟

## Dependencias

Detalle de las dependencias del proyecto:
Es necesario instalar la libreria [nba_api](https://github.com/swar/nba_api), de la cuál se extrae la data para la simulación

```
pip install nba_api
```

## Integrantes

- [Oscar Rojas](https://github.com/augusticor)
- [Christian Chamorro](https://github.com/cris2014971130)
- [Richard Agudelo](https://github.com/Richardagudelo)
- [Luis Torres](https://github.com/luisTorres14)
- [Daniel Pinto](https://github.com/danielpinto01)

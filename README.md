# Calorímetro portable de bajo costo

Este repositorio contiene el código fuente de un proyecto de calorímetro digital desarrollado en Python. El proyecto está dividido en dos partes principales:

1. **Medición de Temperatura**: Utilizando un sensor de temperatura, este código captura la temperatura de una muestra en intervalos regulares de tiempo.
2. **Cálculo de Capacidad Calorífica**: Con los datos de temperatura obtenidos, este código calcula el tiempo necesario para cambios específicos en la temperatura y, posteriormente, determina la capacidad calorífica de la muestra.

## Estructura del Repositorio

- **medicion_temperatura.py**: Este script se encarga de la interfase con el sensor de temperatura, obteniendo las lecturas necesarias y guardándolas en un archivo de datos.
- **calculo_capacidad_calorifica.py**: Este script utiliza los datos obtenidos por `medicion_temperatura.py` para calcular el tiempo transcurrido durante el experimento y, finalmente, calcula la capacidad calorífica de la muestra.

## Instrucciones de Uso

### Requisitos

- CMake
- Python 3.x
- Librerías necesarias: `numpy`, `matplotlib` (opcional, para visualización de datos), y cualquier librería específica del sensor de temperatura utilizado (por ejemplo, `Adafruit_DHT` para sensores DHT).

### Ejecución

1. **Medición de Temperatura**:
   - Conecte su sensor de temperatura a su dispositivo.
   - Ejecute el script `medicion_temperatura.py`:
     ```bash
     python medicion_temperatura.py
     ```
   - Este script almacenará las lecturas de temperatura en un archivo `datos_temperatura.csv`.

2. **Cálculo de Capacidad Calorífica**:
   - Asegúrese de tener el archivo `datos_temperatura.csv` generado en el paso anterior.
   - Ejecute el script `calculo_capacidad_calorifica.py`:
     ```bash
     python calculo_capacidad_calorifica.py
     ```
   - El script procesará los datos y calculará la capacidad calorífica, mostrando los resultados en la terminal y opcionalmente generando gráficos si se habilita la visualización.

## Contribución

Las contribuciones son bienvenidas. Siéntase libre de abrir issues y pull requests para mejoras, corrección de errores o nuevas funcionalidades.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para más detalles.

---

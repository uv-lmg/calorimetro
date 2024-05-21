# Calorímetro portable de bajo costo

Este repositorio contiene el código fuente de un proyecto de calorímetro digital desarrollado en Python. El proyecto está dividido en dos partes principales:

1. **Medición de Temperatura**: Utilizando un sensor de temperatura DS18B20, este código captura la temperatura de una muestra en intervalos regulares de tiempo.
2. **Cálculo de Capacidad Calorífica**: Con los datos de temperatura obtenidos, este código calcula el tiempo necesario para cambios específicos en la temperatura y, posteriormente, determina la capacidad calorífica de la muestra.

## Estructura del Repositorio

- **medicion_temperatura.py**: Este script se encarga de la interfase con el sensor de temperatura, obteniendo las lecturas necesarias y guardándolas en un archivo de datos.
- **calculo_capacidad_calorifica.py**: Este script utiliza los datos obtenidos por `medicion_temperatura.py` para calcular el tiempo transcurrido durante el experimento y, finalmente, calcula la capacidad calorífica de la muestra.

## Instrucciones de Uso

### Requisitos
- CMake
- Arduino IDE

### Ejecución

1. **Medición de Temperatura**:
   
   Si es la primera vez que ejecuta el código:
      - Conecte su sensor de temperatura a su dispositivo.
      - Abra el código `calorimetro.ino` con Arduino IDE:
      - Presione en el boton de ejecutar y correr.
        
   Si no es la primera vez:
      - Conecte el sensore de temperatura al dispositivo
     
3. **Recolección de datos**:
   - Abrir coolterm
   - Presionar conectar o CTRL+K
   - Seleccionar coneccion > capturar a archivo de texto > start o CTRL+R

4. **Cálculo de Capacidad Calorífica**:
   - Asegúrese de tener el archivo `datos.txt` generado en el paso anterior.
   - Compile el código de `capacidad_calorifica.c` utilizando:
   ```bash
   gcc capacidad_calorifica.c -o capacidad_calorifica
   ```
   - Ejecutar el código compilado con ./capacidad_calorifica
   - El script procesará los datos y calculará la capacidad calorífica, mostrando los resultados en la terminal y generando la gráfica si se habilita la visualización.

## Contribución

Las contribuciones son bienvenidas. Siéntase libre de abrir issues y pull requests para mejoras, corrección de errores o nuevas funcionalidades.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para más detalles.

---

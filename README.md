# Calorímetro portable de bajo costo

Este repositorio contiene el código del proyecto de calorímetro digital basado en Arduino. El proyecto está dividido en dos partes principales:

1. **Medición de Temperatura**: Utilizando un sensor de temperatura DS18B20 y la placa Arduino, este código captura la temperatura de una muestra en intervalos regulares de tiempo.
2. **Cálculo de Capacidad Calorífica**: Con los datos de temperatura obtenidos, este código calcula el tiempo necesario para cambios específicos en la temperatura y, posteriormente, determina la capacidad calorífica de la muestra.

## Estructura del Repositorio

- **calorimetro.ino**: Contiene el código necesario para ejecutar en el Arduino IDE, se encarga de obtener la temperatura y el tiempo de la medición de ésta.
- **capacidad_calorifica.c**: Este script utiliza los datos obtenidos por el calorímetro y guardados en un archivo de texto o csv para calcular el tiempo transcurrido durante el experimento y, finalmente, calcular la capacidad calorífica de la muestra.

## Instrucciones de Uso

### Requisitos
- CMake
- Arduino IDE
- Coolterm o cualquier otro programa similar

### Ejecución

1. **Medición de Temperatura**:
   
   Si es la primera vez que ejecuta el código:
      - Conecte su sensor de temperatura a su dispositivo.
      - Abra el código `calorimetro.ino` con Arduino IDE:
      - Presione en el boton de ejecutar y correr.
        
   Si no es la primera vez:
      - Conecte el sensore de temperatura al dispositivo
     
2. **Recolección de datos**:
   - Abrir coolterm
   - Presionar conectar o CTRL+K
   - Seleccionar coneccion > capturar a archivo de texto > start o CTRL+R

3. **Cálculo de Capacidad Calorífica**:
   - Asegúrese de tener el archivo `output.txt` generado en el paso anterior en la misma carpeta del código.
   - Ejecute el código de `cp.py` utilizando:
     
   ```bash
   python3 cp.py
   ```
   
   - El script procesará los datos y calculará su capacidad calorífica, mostrando los resultados en la terminal y generando una gráfica si se habilita su visualización.


## Contribución

Las contribuciones son bienvenidas. Cualquier crítica, error encontrado o mejoras son bienvenidas, así como su modificación para agregar nuevas funcionalidades.

## Licencia

Este proyecto está bajo la The Unlicense. Consulte el archivo `LICENSE` para más detalles.

---

# Sistema Experto Automotriz

Un sistema experto desarrollado en Python con interfaz gráfica en Tkinter y motor de inferencia basado en CLIPS. Permite ayudar al usuario a diagnosticar fallas comunes en automóviles a partir de síntomas seleccionados en la interfaz.

---

## Tabla de contenidos

- [Sistema Experto Automotriz](#sistema-experto-automotriz)
  - [Tabla de contenidos](#tabla-de-contenidos)
  - [Introducción](#introducción)
  - [Características](#características)
  - [Instalación](#instalación)
  - [Uso](#uso)
  - [Síntomas soportados](#síntomas-soportados)
    - [Arranque y Eléctricos](#arranque-y-eléctricos)
    - [Motor y Rendimiento](#motor-y-rendimiento)
    - [Conducción y Frenos](#conducción-y-frenos)
  - [Base de Conocimiento (Reglas)](#base-de-conocimiento-reglas)

---

## Introducción

El Sistema Experto Automotriz permite diagnosticar problemas mecánicos y eléctricos comunes en vehículos mediante la selección de síntomas observados.  
El sistema utiliza reglas de inferencia CLIPS para generar un diagnóstico probable acompañado de una causa y recomendaciones de acción.

---

## Características

- Interfaz gráfica intuitiva con Tkinter.  
- Motor de reglas experto implementado con CLIPS.  
- Diagnóstico basado en selección de síntomas.  
- Resultados explicativos: causa probable y recomendaciones.  
- Funcionalidad para limpiar y reiniciar la consulta.  

---

## Instalación

1. **Clona el repositorio en tu máquina:**

    ```bash
    git clone https://github.com/jpchavarria2/sistema-experto-automotriz.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd sistema-experto-automotriz
    ```

3. **Instala la dependencia `clipspy`:**

    ```bash
    pip install clipspy
    ```  

---

## Uso

1. Ejecutar `se_autos.py` con Python.

    ```bash
    python sd_autos.py
    ```  

2. Seleccionar los síntomas que presenta el vehículo.  
3. Pulsar el botón **Obtener Diagnóstico**.  
4. Revisar el resultado en la sección **Resultado del Diagnóstico**.  
5. Usar el botón **Limpiar** para reiniciar la consulta.  

---

## Síntomas soportados

### Arranque y Eléctricos

- El auto no enciende  
- Se escucha un "clic" al arrancar  
- No se escucha ningún sonido  
- Luces del tablero tenues  

### Motor y Rendimiento

- Aguja de temperatura alta  
- Sale vapor del capó  
- Luz de aceite encendida  
- Golpeteo en el motor  

### Conducción y Frenos

- Los frenos rechinan  
- El volante tiembla  

---

## Base de Conocimiento (Reglas)

El sistema puede identificar los siguientes problemas basándose en los síntomas:

| Síntomas Seleccionados                               | Diagnóstico Potencial                 |
| ---------------------------------------------------- | ------------------------------------- |
| `El auto no enciende` + `Se escucha un 'clic'`       | Problema de Batería Agotada           |
| `El auto no enciende` + `No se escucha ningún sonido` | Falla en el Motor de Arranque         |
| `Aguja de temperatura alta` + `Sale vapor del capó`  | Sobrecalentamiento del Motor          |
| `El auto no enciende` + `Luces del tablero tenues`   | Falla del Alternador                  |
| `Luz de aceite encendida` + `Golpeteo en el motor`   | Nivel de Aceite Críticamente Bajo     |
| `Los frenos rechinan`                                | Pastillas de Freno Desgastadas        |
| `El volante tiembla`                                 | Problema de Balanceo de Llantas       |

# Agente Automático BM Cargo

Un agente web automático que procesa registros de carga de BM Cargo. Automatiza el llenado de formularios en sistemas web con datos predefinidos.

## 📦 Características

- **Dataset incluido**: 80 registros de prueba (valijas, discontainers, piezas)
- **Controles intuitivos**: Iniciar, pausar y reanudar procesamiento
- **Log en vivo**: Terminal visual con eventos en tiempo real
- **Guía fija**: 810-5066-0000

## 🚀 Uso

1. Abre `index.html` en tu navegador
2. Haz clic en "Iniciar agente"
3. El agente abrirá una nueva ventana y procesará los 80 registros automáticamente
4. Monitorea el log de ejecución para ver el progreso

## 📝 Tipos de Registros

### Valijas (40)
- Consecutivos: 1340000–1340039
- Campos: peso, warehouse_qty, iniciales

### Discontainers (20)
- Consecutivos: 1340040–1340059
- Medidas: 58x42x45
- Campos: warehouse_qty, peso, piezas

### Piezas (20)
- Consecutivos: 1340060–1340079
- Medidas: 85x20x8
- Campos: warehouse_qty, peso

## ⚙️ Configuración

Para integrar con tu sistema real:

1. Cambia la URL en la línea de `window.open()`:
   ```javascript
   winRef = window.open("https://TU-SISTEMA-AQUI.com", "_blank");
   ```

2. Descomenta y personaliza la función `inyectarEnSistema()` con los selectores de tu formulario

3. Nota: Si tu sistema está en un dominio diferente, enfrentarás restricciones de cross-origin

## 📌 Notas

- Los datos se simulan inicialmente (sin envío real a un servidor)
- Requiere un navegador moderno
- Permite pop-ups para este sitio
- Delay entre registros: 800ms (configurable)

## 👨‍💻 Autor

Proyecto de prueba para automatización de carga de datos BM Cargo

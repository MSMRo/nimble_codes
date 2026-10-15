## Comando para arrancar el servidor de jupyter

uv run jupyter lab --ip='*' --port=1611 --no-browser

---

## Comandos para usar tmux

En tmux, casi todos los atajos se ejecutan mediante un prefijo:
Presiona Ctrl + b, suelta ambas teclas, y luego presiona la tecla de la acción deseada.

### 1. Gestión de sesiones (desde tu terminal habitual)

Antes de entrar a tmux, controlas las sesiones con comandos normales de la terminal:

Comando,Acción
- tmux, Inicia una nueva sesión anónima
- tmux new -s nombre_sesion, Inicia una sesión con un nombre identificable
- tmux ls, Lista todas las sesiones activas
- tmux attach -t nombre_sesion (o tmux a -t ...), Se reconecta a una sesión existente
- tmux kill-session -t nombre_sesion,Cierra y destruye la sesión indicada

Crea o abre el archivo de configuración en tu directorio raíz:

```Bash
nano ~/.tmux.conf
Añade la siguiente línea:
```

```Bash
set -g mouse on
```

Guarda los cambios. Para aplicarlos inmediatamente en una sesión abierta, presiona Ctrl + b, escribe :, luego teclea source-file ~/.tmux.conf y presiona Enter.
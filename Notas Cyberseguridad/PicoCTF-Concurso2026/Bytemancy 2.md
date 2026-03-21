# Descripción
>Can you conjure the right bytes?
>The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_lonely_island/039824f3cb8b548ad4b65964931d08a2c1b808848a0ed6b0c7adbdd1831d75e8/app.py).
>Connect to the program with netcat:`$ nc lonely-island.picoctf.net 63658`
>(el puerto puede cambiar, es una instancia)

---
# Solución
Para este reto, debemos de analizar primero el código fuente que se nos da:
```python
import sys

while(True):
  try:
    print('⊹──────[ BYTEMANCY-2 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me the HEX BYTE 0xFF 3 times, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    print('==> ', end='', flush=True)
    user_input = sys.stdin.buffer.readline().rstrip(b"\n")
# Aquí lo cortaré ya que lo demás no tiene mucha importancia.
```
Podemos ver que nos solicita el valor de los bytes de `0xff`, entonces, aquí no hay de otra que hacer un script de python como el siguiente:
```python
from pwn import *

p = remote("lonely-island.picoctf.net", 63658)

p.recvuntil(b"==> ")
p.sendline(b"\xff\xff\xff")

print(p.recvall().decode())
```
Lo cual nos ejecutará el script con nuestros bytes de 0xff, mandará el mensaje y recibiremos nuestra flag.

---
# Flag del reto
>picoCTF{3ff5_4_d4yz_fa2f490f}

---
# Notas adicionales

---
# Referencias


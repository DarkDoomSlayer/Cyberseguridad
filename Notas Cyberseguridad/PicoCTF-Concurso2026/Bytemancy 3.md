# Descripción
>Can you conjure the right bytes?
>The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_green_hill/29ba59568a474aeca8400b8209c1dc9a758ac1871419c5d18c2872cc343fd25c/app.py) and the compiled spellbook binary can be downloaded [here](https://challenge-files.picoctf.net/c_green_hill/29ba59568a474aeca8400b8209c1dc9a758ac1871419c5d18c2872cc343fd25c/spellbook).
>Connect to the program with netcat:
>`$ nc green-hill.picoctf.net 65220`
>(El puerto puede cambiar ya que es una instancia)

---
# Solución
Para este reto, debemos de analizar lo que se nos pide:
```python
            print(BANNER)
            print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
            print()
            print("I will name four procedures hidden inside spellbook.")
            print(
                f"Each round, send me their *raw* 4-byte addresses "
                f"in little-endian form. {QUESTION_COUNT} correct answers unlock the flag."
            )
            print()
            print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
            print('⊹─────────────⟡─────────────⊹')
```
Podemos ver que nos solicita el nombre de algunos procedimientos escondidos en el spellbook (el segundo link de descarga), entonces al entrar (`objdump -t spellbook`) encontraremos direcciones tal que así: 080491e3, entonces, vemos que debemos de mandarlo en el formato de little-endian convertida a 4 bytes, para esto se "invierten" los bytes para que queden: e3 91 04 08. Esto se puede hacer con una herramienta como la siguiente:
```python
from pwn import *
import re

elf = ELF("spellbook")
p = remote("green-hill.picoctf.net", 55221)

for _ in range(3):
    line = p.recvline().decode()
    while "procedure '" not in line:
        print(line, end="")
        line = p.recvline().decode()

    print(line, end="")

    name = re.search(r"'(.*?)'", line).group(1)
    addr = elf.symbols[name]

    p.recvuntil(b"==> ")
    p.send(p32(addr))

p.interactive()
```
Lo cual nos resolverá el reto fácilmente. Al final solo se deberá usar ctrl + c para cancelar el modo interactivo.

---
# Flag del reto
>picoCTF{0bjdump_m4g1c_9ee35d3a}

---
# Notas adicionales

---
# Referencias


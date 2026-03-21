# Descripción
>Can you conjure the right bytes?
>The program's source code can be downloaded [here](https://challenge-files.picoctf.net/c_foggy_cliff/51942c7b5e398fe37f39beef2365716ac6cf1d68fba0b9cf7c7035dee3f302f3/app.py).
>Connect to the program with netcat:`$ nc foggy-cliff.picoctf.net 49597` (el puerto puede cambiar, es una instancia)

---
# Solución
Para este reto, debemos de analizar primero el código fuente que se nos da:
```python
while(True):
  try:
    print('⊹──────[ BYTEMANCY-1 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    user_input = input('==> ')
# Aquí lo cortaré ya que lo demás no tiene mucha importancia.
```
Podemos ver que nos solicita el valor decimal del número ascii 101, para esto, podemos buscar en una tabla ascii, la cual nos dirá que es la e. Aquí podemos hacer varias cosas, y es que al conectarnos al servidor se ejecutará automáticamente el script, a partir de aquí podemos realizar comandos como:
```bash
python -c "print('e'*1751)" | nc servidor puerto
```
Lo cual nos ejecutará el script con nuestra cadena de 1751 e lista para darnos la flag.

---
# Flag del reto
>picoCTF{h0w_m4ny_e's???_0c1ad83a}

---
# Notas adicionales

---
# Referencias


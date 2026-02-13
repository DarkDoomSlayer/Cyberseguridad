# fixme1.py
# Descripción del reto:
Fix the syntax error in this Python script to print the flag. [Download Python script](https://artifacts.picoctf.net/c/26/fixme1.py)
# Solución:
python3 fixme1.py
  File "/home/dark/Descargas/fixme1.py", line 20
    print('That is correct! Here\'s your flag: ' + flag)
IndentationError: unexpected indent
nano fixme1.py
python3 fixme1.py
That is correct! Here's your flag: picoCTF{1nd3nt1ty_cr1515_09ee727a}

'picoCTF{1nd3nt1ty_cr1515_09ee727a}'
# Notas adicionales
Borramos la indentación del código Python para que funcione correctamente.
# Referencias
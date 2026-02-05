# what's a net cat?
# Descripción del reto: 
### Our flag printing service has started glitching! Additional details will be available after launching your challenge instance.
Our flag printing service has started glitching! `$ nc saturn.picoctf.net 63969
# Solucion
nc saturn.picoctf.net 63969

'picoCTF{gl17ch_m3_n07_' + chr(0x61) + chr(0x34) + chr(0x33) + chr(0x39) + chr(0x32) + chr(0x64) + chr(0x32) + chr(0x65) + '}'

nc saturn.picoctf.net 63969 | python3 -c "print(eval(input()))"

'picoCTF{gl17ch_m3_n07_a4392d2e}'

picoCTF{gl17ch_m3_n07_a4392d2e}

# Notas adicionales

# Referencias
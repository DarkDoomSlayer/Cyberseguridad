# Static ain't always noise
# Descripción del reto:
Can you look at the data in this binary? The bash script might help! static, ltdis.sh
# Solución:
chmod +x static ltdis.sh
./ltdis.sh static

Attempting disassembly of static ...
Disassembly successful! Available at: static.ltdis.x86_64.txt
Ripping strings from binary with file offsets...
Any strings found in static have been written to static.ltdis.strings.txt with file offset

grep picoCTF static.ltdis.strings.txt
   3020 picoCTF{d15a5m_t34s3r_20335e41}

'picoCTF{d15a5m_t34s3r_20335e41}'
# Notas adicionales
# Referencias
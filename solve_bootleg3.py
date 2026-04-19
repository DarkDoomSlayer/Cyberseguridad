from pwn import *
import subprocess
import re
from Crypto.Util.number import inverse, long_to_bytes

# 1. Nos conectamos al servidor
r = remote("fickle-tempest.picoctf.net", 65478)
print("[+] Recibiendo datos del servidor...")
text = r.recvall(timeout=5).decode()

try:
    c = int(re.search(r'c:\s*(\d+)', text, re.IGNORECASE).group(1))
    n = int(re.search(r'n:\s*(\d+)', text, re.IGNORECASE).group(1))
    e = int(re.search(r'e:\s*(\d+)', text, re.IGNORECASE).group(1))
except AttributeError:
    print("[-] Error parseando los números. Salida cruda:")
    print(text)
    exit()

print(f"[+] Valores obtenidos. ¡Invocando a PARI/GP para destrozar N a la velocidad de C!")

# 2. Le inyectamos un script matemático a PARI/GP directamente desde Python
# Esto le dice a GP que factorice N y nos imprima los primos en formato "primo:cantidad"
gp_script = f'f = factor({n}); for(i=1, matsize(f)[1], print(f[i,1], ":", f[i,2])); quit();\n'

process = subprocess.Popen(['gp', '-q'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
out, err = process.communicate(gp_script)

# 3. Parseamos la salida usando Expresiones Regulares
factors = re.findall(r'(\d+):(\d+)', out)

if not factors:
    print("[-] PARI/GP falló o no devolvió el formato esperado.")
    print("Salida de GP:", out)
    exit()

print(f"[+] ¡Módulo roto en {len(factors)} fracciones de segundo! Se encontraron {len(factors)} factores primos.")

# 4. Calculamos el totiente (phi) multiplicando (p - 1) de todos los factores
print("[+] Calculando el Totiente (phi) Multi-prime...")
phi = 1
for p_str, count_str in factors:
    p = int(p_str)
    count = int(count_str)
    phi *= (p**(count - 1)) * (p - 1)

# 5. Magia RSA estándar
print("[+] Calculando llave privada 'd' y descifrando...")
d = inverse(e, phi)
m = pow(c, d, n)

flag = long_to_bytes(m).decode('utf-8', errors='ignore')

print(f"\n[+++] ¡AQUÍ ESTÁ LA BANDERA! -> {flag}\n")

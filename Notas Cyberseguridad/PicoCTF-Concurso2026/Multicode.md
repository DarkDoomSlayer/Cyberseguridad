# Descripción
We intercepted a suspiciously encoded message, but it’s clearly hiding a flag. No encryption, just multiple layers of obfuscation. Can you peel back the layers and reveal the truth?
Download the [message](https://challenge-files.picoctf.net/c_plain_mesa/67ac0960ab56cd43a4566c1425e713ab6b422eec4f822b3c3e6c1dff07557524/message.txt).
# Solución
Al entrar al archivo, vemos que este es su contenido
```
NjM3NjcwNjI1MDQ3NTMyNTM3NDI2MTcyNjY2NzcyNzE1ZjcyNjE3MDMwNzE3NjYxNzQ1ZjczMzM2ZTMyMzQ3MzM3MzMyNTM3NDQ=
```

La pista del reto nos habla de capas, y para identificar la primera nos fijamos en el **'='**, que nos indica que es de Base64

Usando CyberChef, obtenemos esta salida en hexadecimal:
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)From_Hex('None'/disabled)&input=TmpNM05qY3dOakkxTURRM05UTXlOVE0zTkRJMk1UY3lOalkyTnpjeU56RTFaamN5TmpFM01ETXdOekUzTmpZeE56UTFaamN6TXpNMlpUTXlNelEzTXpNM016TXlOVE0zTkRRPQ
```
637670625047532537426172666772715f72617030717661745f73336e3234733733253744
```

Siguiente capa, pasando de hexadecimal a algo parecido a URL Encode:
https://gchq.github.io/CyberChef/#recipe=From_Hex('None')&input=NjM3NjcwNjI1MDQ3NTMyNTM3NDI2MTcyNjY2NzcyNzE1ZjcyNjE3MDMwNzE3NjYxNzQ1ZjczMzM2ZTMyMzQ3MzM3MzMyNTM3NDQ
```
cvpbPGS%7Barfgrq_rap0qvat_s3n24s73%7D
```

Siguiente capa, usando el URL Decode de CyberChef:
https://gchq.github.io/CyberChef/#recipe=URL_Decode(true)&input=Y3ZwYlBHUyU3QmFyZmdycV9yYXAwcXZhdF9zM24yNHM3MyU3RA
```
cvpbPGS{arfgrq_rap0qvat_s3n24s73}
```

Y como nos dice una de las pistas, pasamos a la última capa con ROT13:
https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)&input=Y3ZwYlBHU3thcmZncnFfcmFwMHF2YXRfczNuMjRzNzN9
```
picoCTF{nested_enc0ding_f3a24f73}
```

picoCTF{nested_enc0ding_f3a24f73}
# Notas
link del reto:
https://play.picoctf.org/events/79/challenges/710?page=3
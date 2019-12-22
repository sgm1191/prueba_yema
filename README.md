# Prueba Ejercicio YEMA
## Descripción del problema
Crear una aplicación usando el framework Django que permite agendar citas con el pediatra.
- [x] Crear los modelos necesarios y visualizarlos en el admin de Django.
- [x] Configurar zona horaria como "America/Mexico_City".
- [x] Configurar código de idioma como "es-mx".
- [x] Agregar traducciones.
- [x] Cambiar título en admin de Django "Django administration" a "Yema Test - [Nombre Candidato]".
- [x] Exponer una API REST con un endpoint que permita solicitar una cita.
- [x] Desde el admin de Django, poder agregar el nombre del pediatra, un comentario y la fecha y hora de la cita agendada.
- [x] Desde el admin de Django, poder enviar un correo con el nombre del pediatra, un comentario y la fecha y hora asignada para la cita.
- [x] Pruebas unitarias
- **Opcional**
- [] Funcionalidad para usuario final (Templates y views fuera de admin site de Django)
- [x] Empaquetar aplicación en un contenedor docker
- [] Integración con servidor web (Nginx)
- **Tecnologías**
- [x] Python 3.7
- [x] Django >= 2.2
- [] JS (React.js o similar)

## Manual de uso

Se tiene que crear las migraciones de la base de datos, para ello dentro del directoio del proyecto `/pediatria` se corre el comando

``` bash
python manage.py migrate
```

Para usar el administrador de DJango en la url `/admin` se tiene que crear un super usuario con el comando

``` bash
python manage.py createsuperuser
```
Dentro del administrador de Django se tienen que crear objetos para **pediatras** y **pacientes** antes de poder agendar una **cita**

### Idioma

Para cambiar el idioma se necesita primero compilar los archivos de traducciones con el comando

``` bash
python manage.py compilemessages
```

después hay que camiar el código de lenguaje a inglés asignando el valor de la variable 

``` python
LANGUAGE_CODE = 'en'
```
en el archivo `settings.py`.

### Correo

Para configurar el(los) correo(s) a los que se enviará el recordatorio de la cita agregar los destinatarios en la variable

``` python
EMAIL_TO_LIST = [
    'santiago.gm1191@gmail.com',
    ...
]
```
en el archivo `settings.py`.

### API REST Documentation

#### /citas

##### /agendar : post
Crea una cita en una **fecha** y **hora** con un **pediatra** y un **paciente**. En el **comentario** se describe el asunto de la cita. Después de registrar la cita, envía un correo al correo especificado en la variable `EMAIL_TO` en el archivo `settings.py`
request post body:

``` json
{
    "fecha" : "2020-12-12",
    "hora" : "12:00:00",
    "comentario" : "cita con pediatra para yema",
    "pediatra_nombre": "martha",
    "pediatra_apellido_paterno": "mama de batman",
    "paciente_nombre": "ana",
    "paciente_apellido_paterno": "garrido"
}
```

###### respuestas
Si se agendó la cita correctamente se mandará un mensaje con la leyenda 'cita creada' con el id de la cita, sino se mandara un mensaje de error

**mensaje exitoso**
``` json
{
    "message": "cita creada",
    "id_cita": 3
}
```

**mensaje fallido**
``` json
{
    "status": "internal error",
    "message": "Paciente matching query does not exist."
}
```
### Contenerizado con Docker

La aplicación se encuentra contenida en una imagen de Docker para compilarla correr dentro del directorio `prueba_yema/pediatria` los comandos

``` bash
docker-compose build
docker-compose up
```
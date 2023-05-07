#INICIO DEL SERVIDOR Y ENTRADA

1)Ejecutar el servidor usando el archivo manage.py "python manage.py runserver"

##USO DE LA PAGINA

###LOGIN Y REGISTER

1) los usuarios que no esten logeados no pueden usar las funciones de la pagina como los blogs o la mensajeria, para ello primero deben logearse o registrarse

2) para registrarse tocar el boton en la navbar [REGISTRARSE] y completar el formulario con los datos

3) una vez registrado se puede proceder al login, tocar el boton en la navbar [INICIAR SESION] y completar el formulario con los datos pedidos

4) al estar logeado y usar el boton [CERRAR SESION], se hara un logout y se podra registrar o iniciar sesion con otro usuario.

###BLOGS

1) al usar la opcion de [BLOGS] de la navbar, llevara al usuario a una lista de todos los blogs de la pagina web. Haciendo clic izquierdo en ellos se los permitira leer en una pagina aparte
2) se pueden editar o eliminar los blogs que haya creado el usuario, los que no sean del usuario solo se pueden eliminar desde el panel de administracion de django
3) al usar la opcion [CREAR] se puede crear un blog utilizando un formulario donde se colocaran los datos de este mismo, al hacerlo quedara publicado en la ventana [BLOGS] para que lo lean los demas usuarios

###MENSAJERIA

1) al usar la opcion [MENSAJERIA] llevara al menu de la mensajeria, donde en la navbar se encontraran las distintas opciones de esta.

2) al usar la opcion [ENVIAR MENSAJE] se podra completar un formulario para enviar un mensaje a un usuario utilizando su mail.

3) al usar la opcion [BANDEJA DE ENTRADA] se podra leer los mensajes que fueron enviados al mail que tiene el perfil del usuario, si no
tiene mensajes aparecera vacia.

###PERFIL

1) al usar la opcion con el nombre de usuario del usuario, se lo llevara a una pagina donde se mostrara su foto de perfil y sus datos (nombre, email)
2) al usar el boton [EDITAR PERFIL] se podran cambiar los datos del perfil del usuario, a excepcion de la foto de perfil.

3) al usar el boton [EDITAR FOTO] se podra cambiar la foto de perfil del usuario por una seleccionada del disco.


##ADMINISTRACION

1) para acceder al panel de administracion de django se debe poner /admin en la url de la ventana [INICIO]

2) el superuser actual es admin, sus datos respectivos son

    usuario: admin
    contrasena: admin

#LINK DE VIDEO DE DESMOSTRACION

-) https://youtu.be/uT-UsJ6Rf6k




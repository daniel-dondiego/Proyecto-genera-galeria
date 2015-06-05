# coding=utf-8
import os
import shutil
import sys


class Peticiones:

    def __init__(self):
        pass

    @classmethod
    def pedir_numero(cls, mensaje, limite_izquierda, limite_derecha):
        """
        Función que pide número y lo devuelve
        :param mensaje: String que se mostrará para pedir número
        :param limite_izquierda: Número más pequeño que será aceptado
        :param limite_derecha: Número más grande que será aceptado
        :return: Número leído
        """
        while True:
            numero = raw_input(mensaje)
            try:
                numero = int(numero)
                if limite_izquierda <= numero <= limite_derecha:
                    return numero
                else:
                    print('Error introduce un número válido')
            except ValueError:
                print('Error introduce un número válido')
            except Exception, e:
                print 'Error peticiones la clase es: ' + str(e.__class__)

    @classmethod
    def es_numero(cls, numero):
        """
        Función que verifica sí el parametro recibido es un número o no
        :param numero:
        :return: Si es número True
        """
        try:
            num = int(numero)
            return num
        except Exception, e:
            print('No es un número: {0}'.format(e.message))
            return False

    @classmethod
    def limpiar_pantalla(cls):
        """
        Función que limpia la pantalla del shell(Unix) o consola(Windows)
        """
        if os.name == "posix":
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"):
            os.system("cls")

    @classmethod
    def copiar_archivos_responsive(cls, nombre_proyecto):
        """
        Copia los archivos necesarios para que la página HTML se vea correctamente
        :param nombre_proyecto: Nombre de la carpeta del proyecto generado
        """
        try:
            a = sys.path
            archivos = str(a[0])+'/model/Skeleton'
            proyecto = str(a[0])+'/' + nombre_proyecto
            shutil.copytree(archivos, proyecto)
        except Exception, e:
            print('Error al copiar directorio: ' + str(e))

    @classmethod
    def log_twitter(cls, error):
        """
        Log de errores, relacionado a Twitter
        :param error: Error que se guardará
        """

        try:
            archivo_log = open('logs/twitter.error', 'a+')
            archivo_log.write(error + '\n')
            archivo_log.close()
        except IOError, e:
            print('Error al abrir archivo de log (Clase LogError): ' + str(e))

    @classmethod
    def log_instagram(cls, error):
        """
        Log de errores, relacionado a Instagram
        :param error: Error que se guardará
        """
        try:
            archivo_log = open('logs/instagram.error', 'a+')
            archivo_log.write(error + '\n')
            archivo_log.close()
        except IOError, e:
            print('Error al abrir archivo de log (Clase LogError): ' + str(e))

    @classmethod
    def log(cls, error):
        """
        Log de errores generales
        :param error: Error que se guardará
        """
        try:
            archivo_log = open('logs/log.error', 'a+')
            archivo_log.write(error + '\n')
            archivo_log.close()
        except IOError, e:
            print('Error al abrir archivo de log (Clase LogError): ' + str(e))

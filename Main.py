#!/usr/bin/env python
# coding=utf-8

from controller.Peticiones import Peticiones
from controller.MediaInstagram import BusquedaMedia
from controller.MediaTwitter import MediaTwitter
from model.GeneradorHTML import GeneradorHTML
from controller.Ordenacion import OrdenadorImagenes
from termcolor import *


# Clase Run, combinación de los componenetes y generar el programa
class Run:
    def __init__(self):
        print('Cargando...')  # Mensaje mientras instacia API Instagram y Twitter
        self.lista_imagenes = []  # Lista que guarda cada una de las imágenes
        self.token_instagram = '1750630587.ee26789.814d1f9eef7b47acb90a958dedcb7af7'  # Access Token de Instagram
        self.datos_twitter = {
            'c_key': 'zAS0Nqxy38IybYdvtd5p4UcOB',
            'c_secret': 'JPh1abxusINcSfRlfS0VF1bgPU45iQkYrWlyZh7yFa1JlS9gpx',
            'token': '135695196-oLyFTOofiBnlAc3eO9l3asDbd8aKeCAx8KZHQINb',
            'token_secret': 'gJw2oZmcPQK7tRfItvTntItoQnu8AVTjnF269dEoug2JT'
            }  # Diccionario con los datos de Twitter
        self.search_t = MediaTwitter(self.datos_twitter)  # Instancia de Api Twitter
        self.search_i = BusquedaMedia(self.token_instagram)  # Instancia de Api Instagram

    def menu_busqueda(self):
        Peticiones.limpiar_pantalla()  # "Limpia" la consola
        cprint('\t\t\tGenerador de Galería ordenada', 'yellow', attrs=['bold'])  # Título
        self.__menu_tipo_busqueda__()  # Muestra el menú
        modo_busqueda = Peticiones.pedir_numero('Elige una opcion: ', 1, 3)  # Pide y guarda la opción elegida
        if modo_busqueda is 1:
            self.__busqueda_tag__()  # Si eligió opción 1 buscar por tag
        elif modo_busqueda is 2:
            self.__busqueda_popular__()  # Si eligió opción 2 buscar popular
        else:
            self.__busqueda_coordenadas__()  # Si eligió opción 3 buscar por coordenadas
        self.generar_html()  # Llamada a la función que genera el HTML

    def __busqueda_tag__(self):
        tag = raw_input('Introduce el Hashtag: ')  # Pedir y guardar el hashtag
        print('Espere un momento...')  # Mensaje de espera
        self.__agregar_imagenes__(self.search_i.por_tag(tag))  # Realiza la busqueda en Instagram y guarda las imágenes

        self.__agregar_imagenes__(self.search_t.buscar_por_tags(tag))  # Realiza busqueda en Twitter
                                                                       # y guarda las imágenes

    def __busqueda_popular__(self):
        print('Espere un momento...')  # Mensaje de espera
        self.__agregar_imagenes__(self.search_i.media_popular())  # Realiza la busqueda en Instagram y
                                                                  #  guarda las imágenes

        self.__agregar_imagenes__(self.search_t.buscar_popular())  # Realiza la busqueda en Twitter
                                                                   #  y guarda las imágenes

    def __busqueda_coordenadas__(self):
        print('Mapa: http://www.bufa.es/google-maps-latitud-longitud/')  # Muestra link de mapa
        latitud = float(raw_input('\tLatitud: '))  # Pide latitud y guarda
        longitud = float(raw_input('\tLongitud: '))  # Pide longitud y guarda
        print('Espere un momento...')  # Mensaje de espera
        self.__agregar_imagenes__(self.search_i.por_coordenadas(latitud, longitud))  # Realiza la busqueda en Instagram
                                                                                     # y guarda las imágenes

        self.__agregar_imagenes__(self.search_t.buscar_por_cordenadas(latitud, longitud))  # Realiza la busqueda en
                                                                                    # Instagram y guarda las imágenes

    def __agregar_imagenes__(self, lista_datos):

        """
        Función que recibe una lista con los datos de las imágenes y las guarda en la lista de la clase
        :type lista_datos: list
        """
        if lista_datos is not None:
            for datos in lista_datos:  # Recorre la lista y guarda los elementos
                self.lista_imagenes.append(datos)  # Agrega el elemento a la lista de la clase

    def generar_html(self):
        Peticiones.limpiar_pantalla()  # "Limpa" el shell
        ordenador = OrdenadorImagenes(self.lista_imagenes)  # Crea objeto para ordenar las imágenes
        print('Se encontraron: {0} imágenes.'.format(len(self.lista_imagenes)))  # Muestra num  de imágenes
        respuesta = self.__menu_ordenamiento__()  # Muestra menú de ordenamiento y guarda respuesta
        respuesta2 = self.__menu_forma_ord__()  # Muestra menú de forma de ordenar y guarda respuesta

        respuesta2 = False if respuesta2 is 1 else True  # Forma Ascendente es False si respuesta2 es 1 ó True si es 2

        lista_ordenada = ordenador.por_fecha(respuesta2) if respuesta is 1 else ordenador.por_usuario(respuesta2)
        # Guarda la lista ya ordenada

        nombre = raw_input('Nombre del proyecto: ')  # Pedir y guardar nombre del Proyecto para la carpeta
        Peticiones.copiar_archivos_responsive(nombre)  # Copia los archivos necesarios para el HTML en la carpeta
                                                       # del proyeto

        generador = GeneradorHTML(nombre, lista_ordenada)  # Crea objeto para generar el HTML
        generador.generar_archivo()  # Crea el archivo HTML

    @staticmethod
    def __menu_forma_ord__():
        Peticiones.limpiar_pantalla()  # "Limpia" el shell
        print('\t1. Ascendente')
        print('\t2. Descendente')
        return Peticiones.pedir_numero('Elige tipo de orden: ', 1, 2)  # Devuelve la opción elegida

    @staticmethod
    def __menu_ordenamiento__():
        Peticiones.limpiar_pantalla()  # "Limpia" el shell
        cprint('\t\tOrdenar Por: ', 'yellow', attrs=['bold'])  # Muestra el mensaje con color y bold
        print('\t1. Fecha')
        print('\t2. Nombre de usuario')
        return Peticiones.pedir_numero('Elige una opcion: ', 1, 2)  # Devuelve la opción elegida

    @staticmethod
    def __menu_tipo_busqueda__():
        cprint('1. Por hashtag')
        cprint('2. Popular ')
        cprint('3. Por coordenadas')

run = Run()
run.menu_busqueda()




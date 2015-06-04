# coding=utf-8


class GeneradorHTML:
    def __init__(self, nombre_de_archivo, datos):
        self.name_index = nombre_de_archivo + '/' + 'index.html'  # Guarda ruta para el archivo index.html
        self.datos = datos  # guarda los datos de las imágenes

    def generar_archivo(self):
        archivo_html = open(self.name_index, 'w')  # Crea el index.html
        with open('BaseHTML/base_html', 'r') as file_codigo:  # Abre archivo del código base HTML
            for linea in file_codigo:
                if '<!--aqui-->' in linea:  # Cuando llegue a la etiqueta '<!--aqui-->' copiará las imágenes
                    for elemento in self.datos:  # Para recorrer cada una de las imágenes
                        row = self.__crear_row__(elemento)  # Crea el codigó HTML para cada imagen y lo guarda
                        archivo_html.write(row)  # Escribe el código de la imagen en el index.html
                else:
                    archivo_html.write(linea)  # Copia código base
        archivo_html.close()  # Cierra el index.html

    def pasar_datos_dic(self, datos_tupla):
        #  Recibe los datos de cada imagen en una tupla y lo devuelve en un diccionario
        dic = {'url': datos_tupla[0],  # Url de la imagen
               'usuario': datos_tupla[1],  # Nombre de usuario autor de la imagen
               'fecha': '{0}/{1}/{2}'.format(self.formato_numero(datos_tupla[4]),  # Día
                                             self.formato_numero(datos_tupla[5]),  # Mes
                                             datos_tupla[6]),  # Año
               'descripcion': datos_tupla[2],  # Descripcion
               'tags': datos_tupla[3],  # Tags o Filtros
               'hora': '{0}:{1}:{2}'.format(self.formato_numero(datos_tupla[7]),  # Hora
                                            self.formato_numero(datos_tupla[8]),  # Minutos
                                            self.formato_numero(datos_tupla[9])),  # Segundos
               'link': datos_tupla[10]}  # Link al perfil del usuario
        return dic  # Devuelve el diccionario con los datos

    @staticmethod
    def formato_numero(numero):
        # Da formato a los numero si son menores que 9; Ejemplo si numero = 8, devuelve 08
        if numero <= 9:
            return '0{0}'.format(numero)
        else:
            return str(numero)

    def __crear_row__(self, datos_tupla):
        # Código HTML que tendrá cada una de las imágenes con sus respectivos datos
        datos = self.pasar_datos_dic(datos_tupla)  # Pasa los datos de la tupla a diccionario apra poder usarlos
        row = '\t<div class="row">\n' \
                    '\t\t<div class="col-lg-3 col-md-4 col-sm-6 col-xs-12">\n' \
                        '\t\t\t<a class="thumbnail" href="http://{0}">\n'\
                            '\t\t\t\t<img class="img-responsive" src="{1}" alt="">\n'\
                        '\t\t\t</a>\n' \
                    '\t\t</div>\n' \
                    '\t\t<div class="col-lg-9 col-md-8 col-sm-6 col-xs-6">\n' \
                        '\t\t\t<br><li>\n' \
                            '\t\t\t\t<ul><b>{2}</b>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{3} {4}</ul>\n' \
                            '\t\t\t\t<ul class="informacion">{5}</ul>\n' \
                            '\t\t\t\t<ul class="informacion">{6}</ul>\n' \
                        '\t\t\t</li>\n' \
                    '\t\t</div>\n' \
                '\t</div>\n'.format(datos['link'], datos['url'], datos['usuario'], datos['fecha'], datos['hora'],
                                    datos['descripcion'], datos['tags'])
        return row  # Devuelve el código

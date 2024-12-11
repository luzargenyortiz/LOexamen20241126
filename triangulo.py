from http.server import HTTPServer , BaseHTTPRequestHandler

import urllib.parse

class LMCDPRequestHandler(BaseHTTPRequestHandler): 

    """ Aqui hacemos un manejador de solicitudes para el servidor LMCDP. 

    En este manejador sirve un formulario HTML simple para calcular el área de un triángulo. 
    Maneja solicitudes GET para servir el formulario y solicitudes POST para calcular y mostrar el resultado. """   

    """
    Clase que maneja las solicitudes HTTP GET y POST para calcular el área de un triángulo.
    """
    html_calc_triangulo = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculador de Área de Triángulos</title>
    </head>
    <body>
        <h1>Calculador de Área de Triángulos LO</h1> <!-- Personalizado con tus iniciales -->
        <form action="/calcular_area" method="POST">
            <label for="base">Base:</label>
            <input type="number" id="base" name="base" required>

            <label for="altura">Altura:</label>
            <input type="number" id="altura" name="altura" required>

            <button type="submit">Calcular</button>
        </form>
    </body>
    </html>"""

    def genera_resultado(self, base, altura):
        """
        Genera una respuesta HTML con el resultado del cálculo del área de un triángulo.

        Args:
            base (float): La base del triángulo.
            altura (float): La altura del triángulo.

        Returns:
            str: HTML con el resultado del área calculada.
        """
        resultado = (base * altura) / 2
        html_area = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Calculador de Área de Triángulos</title>
    </head>
    <body>
        <h1>Calculador de Área de Triángulos LO</h1> <!-- Personalizado con tus iniciales -->
        <h3>El área de un triángulo de base {base} y altura {altura} es: {resultado}</h3>
    </body>
    </html>
    """
        return html_area
    
    """ Se maneja las solicitudes GET 
        En este método sirve el formulario HTML al cliente """


    def do_GET(self):
        """
        Maneja las solicitudes GET enviando el formulario HTML al cliente.
        """
        # Responder a la solicitud GET con el formulario HTML
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(self.html_calc_triangulo, 'utf-8')) # Uso de utf-8 para la codificación

    
        """ Se maneja las solicitudes POST.
        En este método procesa el formulario enviado para calcular y mostrar el area de un triangulo """

    def do_POST(self):
        print("------- Contenido del request POST -------")
        print(f"path = {self.path}")
        for key, value in self.__dict__.items():
            print (f"Atributo de instancia ='{key}' contiene {value}")
        content_length = int(self.headers.get('Content-Length'))
        post_data = self.rfile.read(content_length)
        print(f"post data = {post_data}")
        params = urllib.parse.parse_qs(post_data.decode('utf-8'))
        print(f"parametros ={params}")
                # Extract base and height
        base = float(params['base'][0])
        altura = float(params['altura'][0])
        print("------- Contenido del request -------")                    

        # Send the response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response_html = self.genera_resultado(base, altura)
        self.wfile.write(bytes(response_html, 'utf-8')) # Uso de utf-8 para la codificación
       
        """
        UTF-8 es un estándar de codificación de caracteres que se utiliza para representar texto en muchos idiomas diferentes.
        Su nombre significa 8-bit Unicode Transformation Format (Formato de Transformación Unicode de 8 bits). 
        Aquí tienes algunas razones por las cuales se utiliza UTF-8:
        self.wfile.write(bytes(self.genera_resultado(base, altura), 'utf-8'))
        """

        """ Ejecuta el servidor HTTP. 
        Args: 
        server_class (type): La clase del servidor a usar.
        handler_class (type): La clase del manejador de solicitudes a usar. +
        puerto (int): El número de puerto para escuchar.
        """

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler, puerto=8000):
        server_address = ('', puerto)
        httpd = server_class(server_address, handler_class)
        print(f"Servidor levantado en http://localhost:{puerto}")
        httpd.serve_forever()

run(handler_class = LMCDPRequestHandler, puerto=8027)

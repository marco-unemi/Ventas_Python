from components import Menu,Valida
from utilities import borrarPantalla, gotoxy, marco_lateral, mensaje, confirmacion, marco_inferior
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color, white_color
from clsJson import JsonFile
from company  import Company
from customer import RegularClient, VipClient
from sales import Sale
from product  import Product
from iCrud import ICrud
import datetime
import time,os
from functools import reduce

path, _ = os.path.split(os.path.abspath(__file__))

# Procesos de las Opciones del Menu Facturacion
class CrudClients(ICrud):
    def create(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102+reset_color)
        gotoxy(2,2);print(f"{green_color}*{reset_color}{' '*45}{cyan_color}NEW CLIENT{reset_color}{' '*45}{green_color}*{reset_color}") 
        gotoxy(2,3);print(f"{green_color}*{'*'*100}*{reset_color}")       
        content_width = 100
        content_height = 30
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        mensaje(content_width, 4, f'{green_color}Elija el tipo de cliente a registrar:{reset_color}')
        gotoxy(40,6);print(f'{yellow_color}1. Regular client')
        gotoxy(40,8);print(f'2. VIP client{reset_color}')
        gotoxy(3,9);print('-'*100)
        
        gotoxy(80,10);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(40,10);tipo_cliente = int(input(f'{purple_color}Tipo cliente: {reset_color}'))
        gotoxy(3,11);print('-'*100)
        
        if tipo_cliente == 0:
            gotoxy(10,13);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2)
        elif tipo_cliente != 1 and tipo_cliente != 2:
            self.create()
        elif tipo_cliente == 1:
            gotoxy(80,10);print(' '*21)
            while True:
                gotoxy(10,13);dni = input(purple_color+"DNI: "+reset_color)
                if validar.verificar_cedula(dni):
                    break
                else:
                    gotoxy(15,13)
                    print("                     ------><  | {} ".format("La cédula no es válida."))
                    time.sleep(2) 
                    gotoxy(15,13)
                    print(' '*70)
            
            json_file = JsonFile(path+'/archivos/clients.json')
            
            client_existe = json_file.find("dni",dni)
            
            if not client_existe:
                gotoxy(10, 15);first_name = input(purple_color+"First_name: "+reset_color).capitalize()
                gotoxy(10, 17);last_name = input(purple_color+"Last_name: "+reset_color).capitalize()
                gotoxy(10, 19);card = input(purple_color+"Card: "+reset_color).capitalize()

                client = RegularClient(first_name, last_name, dni, card)
                
                procesar = confirmacion(content_width, 22, "Esta seguro de guardar el cliente(s/n):")
                
                if procesar == "s":
                    clients = json_file.read()
                    data = client.getJson()
                    clients.append(data)
                    json_file.save(clients)
                    mensaje(content_width, 25, "😊 Cliente Grabado satisfactoriamente 😊")
                else:
                    mensaje(content_width, 25, "🤣 Cliente Cancelado 🤣")
                time.sleep(2)  
            else:
                gotoxy(80,10);print(' '*21)
                gotoxy(35, 16)
                print(yellow_color+"Cliente ya existe!!"+reset_color) 
                for i in range(3, 0, -1):
                    gotoxy(20, 18);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                    time.sleep(1)
                self.create()
                
        elif tipo_cliente == 2:
            gotoxy(80,10);print(' '*21)
            while True:
                gotoxy(10,13);dni = input(purple_color+"DNI: "+reset_color)
                if validar.verificar_cedula(dni):
                    break
                else:
                    gotoxy(15,13)
                    print("                     ------><  | {} ".format("La cédula no es válida."))
                    time.sleep(2) 
                    gotoxy(15,13)
                    print(' '*70)
            
            json_file = JsonFile(path+'/archivos/clients.json')
            
            client_existe = json_file.find("dni",dni)
            
            if not client_existe:
                gotoxy(10, 15);first_name = input(purple_color+"First_name: "+reset_color).capitalize()
                gotoxy(10, 17);last_name = input(purple_color+"Last_name: "+reset_color).capitalize()
                gotoxy(10, 19);valor = int(input(purple_color+"Valor de crédito: "+reset_color))
                client = VipClient(first_name, last_name, dni)
                
                client.limit = valor if valor else None

                procesar = confirmacion(content_width, 22, "Esta seguro de guardar el cliente(s/n):")
                
                if procesar == "s":
                    clients = json_file.read()
                    data = client.getJson()
                    clients.append(data)
                    json_file.save(clients)
                    mensaje(content_width, 25, "😊 Cliente Grabado satisfactoriamente 😊")
                else:
                    mensaje(content_width, 25, "🤣 Cliente Cancelado 🤣")   
                time.sleep(2)  
            else:
                gotoxy(80,10);print(' '*21)
                gotoxy(35, 16)
                print(yellow_color+"Cliente ya existe!!"+reset_color) 
                for i in range(3, 0, -1):
                    gotoxy(20, 18);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                    time.sleep(1)
                self.create()
        

    def update(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102+reset_color)
        gotoxy(2,2);print(f"{green_color}*{reset_color}{' '*43}{cyan_color}UPDATE CLIENT{reset_color}{' '*44}{green_color}*{reset_color}") 
        gotoxy(2,3);print(f"{green_color}*{'*'*100}*{reset_color}")       
        content_width = 100
        content_height = 20
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(80,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
    
        while True:
            gotoxy(10,4);dni = input(purple_color+"DNI: "+reset_color)
            if validar.verificar_cedula(dni):
                break
            else:
                gotoxy(15,4)
                print("                     ------><  | {} ".format("La cédula no es válida."))
                time.sleep(2) 
                gotoxy(15,4)
                print(' '*60)
                
        json_file = JsonFile(path+'/archivos/clients.json')
        client_existe = json_file.find("dni",dni)
        client = client_existe
        if dni == '0':
            gotoxy(15,6);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2)  
        elif client_existe:
            client = client_existe[0]
            if client['tipo_cliente'] == 'Cliente REGULAR':
                gotoxy(80,4);print(' '*21)            
                gotoxy(40,4);print(f"{blue_color}Client:{reset_color} {white_color}{client['nombre']} {client['apellido']}{reset_color}")
                gotoxy(3,6);print('-'*100)
                
                gotoxy(10,8);print(f'{cyan_color}DNI: {reset_color}') 
                while True:
                    gotoxy(10,8);new_dni = input(purple_color+"DNI: "+reset_color) or client['dni']
                    if validar.verificar_cedula(new_dni):
                        break
                    else:
                        gotoxy(15,8)
                        print("                     ------><  | {} ".format("La cédula no es válida."))
                        time.sleep(2) 
                        gotoxy(15,8)
                        print(' '*70)
                gotoxy(10,10);new_first_name = input(purple_color+"First_name: "+reset_color).capitalize()  or client['nombre']
                gotoxy(10,12);new_last_name = input(purple_color+"Last_name: "+reset_color).capitalize()  or client['apellido'] 
                gotoxy(10,14);card = input(purple_color+"Card (True/False): "+reset_color).capitalize() or client['card']
                valor = 0.10 if card else 0
                procesar = confirmacion(content_width, 16, "Esta seguro de Actualizar el cliente(s/n):")
                
                if procesar == "s":
                    new_values = {'dni': new_dni, 'nombre': new_first_name, 'apellido': new_last_name, 'valor_descuento': valor, 'card': card}
                    json_file.update('dni', dni, new_values)
                    mensaje(content_width, 18, "😊 Cliente actualizado satisfactoriamente 😊")

                else:
                    mensaje(content_width, 18, "🤣 Actualización Cancelada 🤣")
                time.sleep(2)  
            
            elif client['tipo_cliente'] == 'Cliente VIP':
                gotoxy(80,4);print(' '*21)            
                gotoxy(40,4);print(f"{blue_color}Client:{reset_color} {white_color}{client['nombre']} {client['apellido']}{reset_color}")
                gotoxy(3,6);print('-'*100)
                
                gotoxy(10,8);print(f'{cyan_color}DNI: {reset_color}') 
                while True:
                    gotoxy(10,8);new_dni = input(purple_color+"DNI: "+reset_color) or client['dni']
                    if validar.verificar_cedula(new_dni):
                        break
                    else:
                        gotoxy(15,8)
                        print("                     ------><  | {} ".format("La cédula no es válida."))
                        time.sleep(2) 
                        gotoxy(15,8)
                        print(' '*70)
                gotoxy(10,10);new_first_name = input(purple_color+"First_name: "+reset_color).capitalize()  or client['nombre']
                gotoxy(10,12);new_last_name = input(purple_color+"Last_name: "+reset_color).capitalize()  or client['apellido'] 
                gotoxy(10,14);limit = int(input(purple_color+"Limit: "+reset_color)) or client['valor_credito']
                new_limit = client['valor_credito'] if limit < 10000 or limit > 20000 else limit
                
                procesar = confirmacion(content_width, 16, "Esta seguro de Actualizar el cliente(s/n):")
                
                if procesar == "s":
                    new_values = {'dni': new_dni, 'nombre': new_first_name, 'apellido': new_last_name, 'valor_credito': new_limit}
                    json_file.update('dni', dni, new_values)
                    mensaje(content_width, 18, "😊 Cliente actualizado satisfactoriamente 😊")

                else:
                    mensaje(content_width, 18, "🤣 Actualización Cancelada 🤣")
                time.sleep(2)    
            
        else: 
            gotoxy(80,4);print(' '*21)
            clients = json_file.read()
            
            long = len(clients)
            marco_lateral(content_width, content_height+long)
            marco_inferior(content_width, content_height+long)
            
            mensaje(content_width, 5, 'Cliente no existe!!')
            
            gotoxy(2,7);print(f'{green_color}{"*"*102}{reset_color}')
            
            mensaje(content_width+10, 9, f'{white_color} Clientes disponibles {reset_color}') 
            
            gotoxy(3,10);print('-'*100)     
             
            gotoxy(35,12);print(f'{blue_color} Cliente {reset_color}')
            gotoxy(60,12);print(f'{blue_color} Tipo de cliente {reset_color}')
            fila = 14
            item = 1
            for cli in clients:
                gotoxy(20,fila);print(f"{purple_color} {item}. {reset_color}")
                gotoxy(35,fila);print(f"{white_color} {cli['nombre']} {cli['apellido']} {reset_color}")
                gotoxy(60,fila);print(f"{white_color} {cli['tipo_cliente']} {reset_color}")
                fila += 1
                item += 1     
            gotoxy(3,fila+1);print('-'*100)
            gotoxy(20,fila+3);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.update()
      
        
    def delete(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102+reset_color)
        gotoxy(2,2);print(f"{green_color}*{reset_color}{' '*43}{cyan_color}DELETE CLIENT{reset_color}{' '*44}{green_color}*{reset_color}") 
        gotoxy(2,3);print(f"{green_color}*{'*'*100}*{reset_color}")       
        content_width = 100
        content_height = 20
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(80,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
    
        while True:
            gotoxy(10,4);dni = input(purple_color+"DNI: "+reset_color)
            if validar.verificar_cedula(dni):
                break
            else:
                gotoxy(15,4)
                print("                     ------><  | {} ".format("La cédula no es válida."))
                time.sleep(2) 
                gotoxy(15,4)
                print(' '*60)
                
        json_file = JsonFile(path+'/archivos/clients.json')
        data = json_file.read()
        cliente_a_eliminar = json_file.find("dni",dni)
        
        if dni == '0':
            gotoxy(15,6);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2)  
            
        elif cliente_a_eliminar:
            gotoxy(80,4);print(' '*21)
            client = cliente_a_eliminar[0]
            
            gotoxy(10,6);print(f"{blue_color} Client: {reset_color} {client['nombre']} {client['apellido']}")
            if client['tipo_cliente'] == 'Cliente REGULAR':
                gotoxy(10,8);print(f"{blue_color} Valor: {reset_color} {client['valor_descuento']}")
                gotoxy(10,10);print(f"{blue_color} Tipo de cliente: {reset_color} {client['tipo_cliente']}")
            else:
                gotoxy(10,8);print(f"{blue_color} Valor: {reset_color} {client['valor_credito']}")
                gotoxy(10,10);print(f"{blue_color} Tipo de cliente: {reset_color} {client['tipo_cliente']}")
                
            procesar = confirmacion(content_width, 12, f"Esta seguro de ELIMINAR el Cliente (s/n):")

            if procesar == "s":
                data.remove(client)
                json_file.save(data)
                mensaje(content_width, 14, '😊 Cliente Eliminado satisfactoriamente 😊')
            else:
                mensaje(content_width, 14, '🤣 Eliminación Cancelada 🤣')
            time.sleep(2)         
        else: 
            gotoxy(80,4);print(' '*21)
            clients = json_file.read()
            
            long = len(clients)
            marco_lateral(content_width, content_height+long)
            marco_inferior(content_width, content_height+long)
            
            mensaje(content_width, 5, 'Cliente no existe!!')
            
            gotoxy(2,7);print(f'{green_color}{"*"*102}{reset_color}')
            
            mensaje(content_width+10, 9, f'{white_color} Clientes disponibles {reset_color}') 
            
            gotoxy(3,10);print('-'*100)     
             
            gotoxy(35,12);print(f'{blue_color} Cliente {reset_color}')
            gotoxy(60,12);print(f'{blue_color} Tipo de cliente {reset_color}')
            fila = 14
            item = 1
            for cli in clients:
                gotoxy(20,fila);print(f"{purple_color} {item}. {reset_color}")
                gotoxy(35,fila);print(f"{white_color} {cli['nombre']} {cli['apellido']} {reset_color}")
                gotoxy(60,fila);print(f"{white_color} {cli['tipo_cliente']} {reset_color}")
                fila += 1
                item += 1     
            gotoxy(3,fila+1);print('-'*100)
            gotoxy(20,fila+3);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.delete()
            
            
    def consult(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102+reset_color)
        gotoxy(2,2);print(f"{green_color}*{reset_color}{' '*43}{cyan_color}CONSULT CLIENT{reset_color}{' '*43}{green_color}*{reset_color}")
        gotoxy(2,3);print(f"{green_color}*{'*'*100}*{reset_color}")
        content_width = 100
        content_height = 25
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
    
        gotoxy(80,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
    
        while True:
            gotoxy(10,4);dni = input(purple_color+"DNI: "+reset_color)
            if validar.verificar_cedula(dni):
                break
            else:
                gotoxy(15,4)
                print("                     ------><  | {} ".format("La cédula no es válida."))
                time.sleep(2) 
                gotoxy(15,4)
                print(' '*60)        

        json_file = JsonFile(path+'/archivos/clients.json')
        client_existe = json_file.find("dni",dni)
        
        if dni == '0':
            gotoxy(15,6);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2) 
        elif client_existe:
            gotoxy(80,4);print(' '*21)
            client = client_existe[0]
            
            gotoxy(10,6);print(f"{blue_color} DNI: {reset_color} {client['dni']}")
            gotoxy(10,8);print(f"{blue_color} Client: {reset_color} {client['nombre']} {client['apellido']}")
            if client['tipo_cliente'] == 'Cliente REGULAR':
                gotoxy(10,10);print(f"{blue_color} Valor: {reset_color} {client['valor_descuento']}")
                gotoxy(10,12);print(f"{blue_color} Tipo de cliente: {reset_color} {client['tipo_cliente']}")
            else:
                gotoxy(10,10);print(f"{blue_color} Valor: {reset_color} {client['valor_credito']}")
                gotoxy(10,12);print(f"{blue_color} Tipo de cliente: {reset_color} {client['tipo_cliente']}")
                             
            gotoxy(12,14);x=input(red_color+"presione una tecla para continuar..."+reset_color)
                
        else: 
            gotoxy(80,4);print(' '*21)
            clients = json_file.read()
            
            long = len(clients)
            marco_lateral(content_width, content_height+long+10)
            marco_inferior(content_width, content_height+long+10)
            
            mensaje(content_width, 5, 'Cliente no existe!!')
            
            gotoxy(2,7);print(f'{green_color}{"*"*102}{reset_color}')
            gotoxy(3,8);print(f'{"-"*100}')
            
            mensaje(content_width+10, 9, f'{white_color} Clientes disponibles: {reset_color}') 
            
            gotoxy(3,10);print('-'*100)     
             
            gotoxy(35,12);print(f'{blue_color} Cliente {reset_color}')
            gotoxy(60,12);print(f'{blue_color} Tipo de cliente {reset_color}')
            fila = 14
            item = 1
            for cli in clients:
                gotoxy(20,fila);print(f"{purple_color} {item}. {reset_color}")
                gotoxy(35,fila);print(f"{white_color} {cli['nombre']} {cli['apellido']} {reset_color}")
                gotoxy(60,fila);print(f"{white_color} {cli['tipo_cliente']} {reset_color}")
                fila += 1
                item += 1     
            gotoxy(3,fila);print(f'{"-"*100}')
            
            suma_clients_vip = reduce(lambda total, client: total + client["valor_credito"] if client['tipo_cliente'] == 'Cliente VIP' else total, clients,0)
            suma_clients_regular = reduce(lambda total, client: total + client["valor_descuento"] if client['tipo_cliente'] == 'Cliente REGULAR' else total, clients,0)
            totales_map = list(filter(lambda total: total != 0, map(lambda client: client["valor_credito"] if client['tipo_cliente'] == 'Cliente VIP' else 0, clients)))
            filter_clientes_vip = list(filter(lambda client: client['tipo_cliente'] == 'Cliente VIP', clients))
            filter_clientes_regular = list(filter(lambda client: client['tipo_cliente'] == 'Cliente REGULAR', clients))
            total_clients_vip = sum(1 for client in filter_clientes_vip)
            total_clients_regular = sum(1 for client in filter_clientes_regular)

            max_client = max(totales_map)
            min_client = min(totales_map)
            tot_clients = round(sum(totales_map), 2)
            
            gotoxy(5,fila+2);print(f"{cyan_color} map Clients: {reset_color}{totales_map}")
            gotoxy(5,fila+4);print(f"{cyan_color} max credito Client VIP: {reset_color}{max_client}")
            gotoxy(5,fila+6);print(f"{cyan_color} min credito Client VIP: {reset_color}{min_client}")
            gotoxy(5,fila+8);print(f"{cyan_color} sum creditos Clients VIP: {reset_color}{tot_clients}")
            gotoxy(5,fila+10);print(f"{cyan_color} reduce Client VIP: {reset_color}{suma_clients_vip}")
            gotoxy(5,fila+12);print(f"{cyan_color} reduce Client REGULAR: {reset_color}{suma_clients_regular}")
            gotoxy(5,fila+14);print(f"{cyan_color} TOTAL DE CLIENTES VIP: {reset_color}{total_clients_vip}")
            gotoxy(5,fila+16);print(f"{cyan_color} TOTAL DE CLIENTES REGULARES: {reset_color}{total_clients_regular}")
            
            gotoxy(20,fila+18);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.consult()
            

class CrudProducts(ICrud):
    def create(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102+reset_color)
        gotoxy(2,2);print(f"{green_color}*{reset_color}{' '*45}{cyan_color}NEW PRODUCT{reset_color}{' '*44}{green_color}*{reset_color}") 
        gotoxy(2,3);print(f"{green_color}*{'*'*100}*{reset_color}")       
        content_width = 100
        content_height = 12
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(80,5);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,5);print(purple_color+"Description:"+reset_color)
        descripcion = validar.solo_letras("Error: Solo letras", 23, 5)
        json_file = JsonFile(path+'/archivos/products.json')
        product = json_file.find("descripcion",descripcion)
      
        if descripcion == 0:
            gotoxy(15,7);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif not product:
            gotoxy(80,5);print(' '*21)
            gotoxy(10, 7);print(purple_color+"Price: "+reset_color)
            price = validar.solo_decimales("Error: Solo decimales", 17, 7)
            gotoxy(10, 9);print(purple_color+"Stock: "+reset_color)
            stock = validar.solo_numeros("Error: Solo numeros", 17, 9)

            product = Product(None, descripcion, price, stock)

            procesar = confirmacion(content_width, 11, "Esta seguro de grabar el producto(s/n):")
            
            if procesar == "s":
                products = json_file.read()
                last_id = products[-1]["id"]+1
                product_data = product.getJson()
                product_data["id"] = last_id
                products.append(product_data)
                json_file.save(products)
                mensaje(content_width, 14, "😊 Producto Grabado satisfactoriamente 😊")

            else:
                mensaje(content_width, 14, "🤣 Producto Cancelado 🤣")    
            time.sleep(2)  
        else:
            gotoxy(80,5);print(' '*21)
            gotoxy(35, 8);print(yellow_color+"Producto ya existe!!"+reset_color) 
            for i in range(3, 0, -1):
                gotoxy(20, 12);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                time.sleep(1)
            self.create() 


    def update(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102)
        gotoxy(2,2);print(f"*{' '*41}{cyan_color}ACTUALIZAR PRODUCTO{reset_color}{' '*40}{green_color}*{reset_color}")
        gotoxy(2,3);print(f"{green_color}*{'*'*100}*{reset_color}")  
        content_width = 100
        content_height = 20
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(80,5);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,5);print(purple_color+"Ingrese ID del Producto: "+reset_color)
        
        product_id = validar.solo_numeros("Error: Solo numeros",35,5)
        json_file = JsonFile(path+'/archivos/products.json')
        product = json_file.find("id",product_id )
        
        if product_id == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif product:
            gotoxy(80,5);print(' '*21)
            product = product[0]
            
            gotoxy(10,7);print(blue_color+f"Producto: {product['id']}" +reset_color)
            
            gotoxy(10,9);new_description = input(cyan_color + "Descripcion: " + reset_color)  or product['descripcion']
            gotoxy(10,11);new_price = input(cyan_color + "Precio: " +reset_color)  or product['precio']
            gotoxy(10,13);new_stock = input(cyan_color + "Stock: " +reset_color)  or product['stock']      
            
            procesar = confirmacion(content_width, 16, "Esta seguro de grabar el producto(s/n):")
            
            if procesar == "s":
                new_values = {'descripcion': new_description.capitalize(), 'precio': float(new_price), 'stock': int(new_stock)}
                json_file.update('id', product_id, new_values)
                mensaje(content_width, 19, "😊 Producto Actualizado satisfactoriamente 😊")
            else:
                mensaje(content_width, 19, "Actualizacion Cancelada!!")
            time.sleep(2)  
            
        else: 
            gotoxy(80,5);print(' '*21)
            gotoxy(2,29);print(' '*102)
            productos = json_file.read()
            total_id = len(productos)
            
            marco_lateral(content_width, content_height+total_id-10)
            marco_inferior(content_width, content_height+total_id-10)
            mensaje(content_width, 5, "Producto no existe!!")
            gotoxy(2,7);print(green_color+'*'*102+reset_color)
            mensaje(content_width, 9, white_color+'Productos disponibles'+reset_color)
            gotoxy(3,11);print('-'*100)
            
            fila = 13
            for prod in productos:
                gotoxy(20,fila);print(f"{purple_color} {prod['id']}. {reset_color}")
                gotoxy(30,fila);print(f"{blue_color} {prod['descripcion']} {reset_color}")
                fila += 1
            gotoxy(3,fila+1);print('-'*100)
            
            gotoxy(20,fila+3);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.update()
    
    
    def delete(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102)
        gotoxy(2,2);print(f"*{' '*41}{cyan_color}ELIMINAR PRODUCTO{reset_color}{' '*42}{green_color}*{reset_color}")
        gotoxy(2,3);print(f"{green_color}*{'*'*100}*{reset_color}")  
        content_width = 100
        content_height = 20

        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(80,5);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,5);print(purple_color+"Ingrese ID del Producto: "+reset_color)
        product_id = validar.solo_numeros("Error: Solo numeros",35,5)
        
        json_file = JsonFile(path+'/archivos/products.json')
        data = json_file.read()
        producto_a_eliminar = json_file.find("id",product_id )
        
        fila = 10
        if product_id == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif producto_a_eliminar:
            gotoxy(80,5);print(' '*21)
            product = producto_a_eliminar[0]
            
            gotoxy(10,7);print(f"{cyan_color} Producto: {reset_color} {product['id']}")
            gotoxy(10,9);print(f"{cyan_color} Descripcion: {reset_color} {product['descripcion']}")
            gotoxy(10,11);print(f"{cyan_color} Precio: {reset_color} {product['precio']}")
            gotoxy(10,13);print(f"{cyan_color} Stock: {reset_color} {product['stock']}")      
            
            procesar = confirmacion(content_width, 16, "Esta seguro de Eliminar el producto(s/n):")
            
            if procesar == "s":
                data.remove(product)
                json_file.save(data)
                mensaje(content_width, 19, "😊 Producto Eliminado satisfactoriamente 😊")
            else:
                mensaje(content_width, 19, "Actualizacion Cancelada!!")
            time.sleep(2)  
            
        else: 
            gotoxy(80,5);print(' '*21)
            long = len(data)
            
            marco_lateral(content_width, content_height+long)
            marco_inferior(content_width, content_height+long)
            gotoxy(40,2);print(yellow_color+"Producto no existe!!"+reset_color)
            
            gotoxy(30,5);print('Productos disponibles')
            fila = 8
            for prod in data:
                gotoxy(20,fila);print(f"{purple_color} {prod['id']}. {reset_color} {blue_color} {prod['descripcion']} {reset_color}")
                fila += 1
            
            
            gotoxy(20,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.delete()
    
    
    def consult(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102)
        gotoxy(2,2);print(f"*{' '*41}{cyan_color}CONSULTAR PRODUCTO{reset_color}{' '*41}{green_color}*{reset_color}")
        gotoxy(2,3);print(f"{green_color}{'*'*102}{reset_color}")  
        content_width = 100
        content_height = 25

        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(80,5);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,5);print(purple_color+"Ingrese ID del Producto: "+reset_color)
        product_id = validar.solo_numeros("Error: Solo numeros",35,5)
        
        json_file = JsonFile(path+'/archivos/products.json')
        product = json_file.find("id",product_id)
        
        fila = 10
        if product_id == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
            
        elif product:
            gotoxy(80,5);print(' '*21)
            producto = product[0]
            
            gotoxy(3,7);print('-'*100) 
            gotoxy(20,8);print(cyan_color+f"ID:{reset_color}")
            gotoxy(35,8);print(cyan_color+f"Descripcion:{reset_color}")
            gotoxy(60,8);print(cyan_color+f"Precio:{reset_color}")
            gotoxy(80,8);print(cyan_color+f"Stock:{reset_color}") 
            gotoxy(3,9);print('-'*100)
            gotoxy(20,10);print(f"{white_color}{producto['id']}")  
            gotoxy(35,10);print(f"{producto['descripcion']}")  
            gotoxy(60,10);print(f"{producto['precio']}")  
            gotoxy(80,10);print(f"{producto['stock']} {reset_color}")  
            gotoxy(3,11);print('-'*100)
            
            gotoxy(2,13);print(green_color+'*'*102+reset_color)  
            productos = json_file.read()
            suma = reduce(lambda total, product: round(total+ product["precio"],2), productos,0)
            totales_map = list(map(lambda product: product["precio"], productos))
            max_product = max(totales_map)
            min_product = min(totales_map)
            tot_products = round(sum(totales_map), 2)
            gotoxy(5,15);print(f"{cyan_color} map Precio Productos: {reset_color}{totales_map}")
            gotoxy(5,17);print(f"{cyan_color} max Precio Producto: {reset_color}{max_product}")
            gotoxy(5,19);print(f"{cyan_color} min Precio Producto: {reset_color}{min_product}")
            gotoxy(5,21);print(f"{cyan_color} sum Precio Producto: {reset_color}{tot_products}")
            gotoxy(5,23);print(f"{cyan_color} reduce Precio Producto: {reset_color}{suma}")
            
            gotoxy(10,26);x=input(red_color+"presione una tecla para continuar..."+reset_color)
                         
        else:  
            gotoxy(80,5);print(' '*21)
            productos = json_file.read()
            long = len(productos)

            marco_lateral(content_width, content_height+long)
            marco_inferior(content_width, content_height+long)
            mensaje(content_width, 1, 'Producto no existe!!')
            mensaje(content_width, 3, 'Productos disponibles', white_color)
            gotoxy(3,4);print('-'*100)
            gotoxy(20,5);print(f'{cyan_color}NO.          Descripción          Precio          Stock{reset_color}')
            gotoxy(3,6);print('-'*100)
            fila = 8
            for prod in productos:
                gotoxy(20,fila);print(f"{purple_color}{prod['id']}{reset_color}")
                gotoxy(33,fila);print(f"{purple_color}{prod['descripcion']}{reset_color}")
                gotoxy(54,fila);print(f"{purple_color}{prod['precio']}{reset_color}")
                gotoxy(70,fila);print(f"{purple_color}{prod['stock']}{reset_color}")
                fila += 1
            fila +=1
            gotoxy(3,fila);print('-'*100)  
            
            gotoxy(20,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.consult()            


class CrudSales(ICrud):
    def create(self):
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')        
        gotoxy(2,1);print(green_color+"*"*102+reset_color)
        gotoxy(2,2);print(f"{green_color}*{reset_color}{' '*41}{cyan_color}NEW SALES REGISTER{reset_color}{' '*41}{green_color}*{reset_color}") 
        gotoxy(2,3);print(green_color+"*"*102+reset_color) 
        content_width = 100
        content_height = 24
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height + 1)
        company = Company()
        gotoxy(3,4);print('-'*100)
        gotoxy(20,5);print(f'{cyan_color}Empresa:{reset_color} {white_color}{company.business_name}{reset_color}')
        gotoxy(60,5);print(f'{cyan_color}Ruc:{reset_color} {white_color}{company.ruc}{reset_color}')
        gotoxy(3,6);print('-'*100)
        gotoxy(20,7);print(f"{cyan_color}Factura#:{reset_color} {white_color}F0999999{reset_color}")
        gotoxy(60,7);print(f"{cyan_color}Fecha:{reset_color} {white_color}{datetime.datetime.now()}{reset_color}")
        gotoxy(3,8);print('-'*100)
        
        gotoxy(80,9);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        
        while True:
            gotoxy(20,9);dni = input(cyan_color+"Cedula: "+reset_color + white_color)
            if validar.verificar_cedula(dni):
                break
            else:
                gotoxy(30,9)
                print("          ------>< | {}".format("La cédula no es válida."))
                time.sleep(2) 
                gotoxy(20,9)
                print(' '*56)
        
        if dni == '0':
            gotoxy(15,12);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        else:
            gotoxy(80,9);print(' '*21)
            json_file = JsonFile(path+'/archivos/clients.json')
            client = json_file.find("dni",dni)
            if not client:
                mensaje(content_width, 12, "Cliente no existe!!")
                return
            client = client[0]
            cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
            sale = Sale(cli)
            gotoxy(60,9);print(f'{cyan_color}Cliente: {white_color}{cli.fullName()}{reset_color}')
            gotoxy(3,10);print("-"*100) 
            gotoxy(6,11);print(purple_color+"Linea") 
            gotoxy(15,11);print("Id_Articulo") 
            gotoxy(30,11);print("Descripcion") 
            gotoxy(48,11);print("Precio") 
            gotoxy(58,11);print("Cantidad") 
            gotoxy(70,11);print("Subtotal") 
            gotoxy(82,11);print("n->Terminar Venta)"+reset_color)
            gotoxy(3,12);print("-"*100)
            # detalle de la venta
            follow ="s"
            line=1
            
            while follow.lower()=="s":
                gotoxy(7,12+line);print(f'{white_color}{line}')
                gotoxy(15,12+line);
                id=int(validar.solo_numeros("Error: Solo numeros",15,12+line))
                json_file = JsonFile(path+'/archivos/products.json')
                prods = json_file.find("id",id)
                if not prods:
                    gotoxy(24,12+line);print("Producto no existe")
                    time.sleep(1)
                    gotoxy(24,12+line);print(" "*20)
                else:    
                    prods = prods[0]
                    product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                    gotoxy(30,12+line);print(product.descrip)
                    gotoxy(48,12+line);print(product.preci)
                    gotoxy(58,12+line);qyt=int(validar.solo_numeros("Error:Solo numeros",58,12+line))
                    gotoxy(70,12+line);print(product.preci*qyt)
                    sale.add_detail(product,qyt)
                    gotoxy(3,14+line-1);print(" "*100)
                    
                    gotoxy(66,15+line-1);print(' '*20)
                    gotoxy(66,16+line-1);print(' '*20)
                    gotoxy(66,17+line-1);print(' '*20)
                    gotoxy(66,18+line-1);print(' '*20)
                    
                    gotoxy(3,14+line);print("-"*100)
                    
                    gotoxy(70,15+line);print(f"{blue_color}Subtotal: {white_color}{round(sale.subtotal,2)}{reset_color}")
                    gotoxy(70,16+line);print(f"{blue_color}Decuento: {white_color}{round(sale.discount,2)}{reset_color}")
                    gotoxy(70,17+line);print(f"{blue_color}Iva     : {white_color}{round(sale.iva,2)}{reset_color}")
                    gotoxy(70,18+line);print(f"{blue_color}Total   : {white_color}{round(sale.total,2)}{reset_color}")
                    gotoxy(3,20+line);print("-"*100)
                    gotoxy(3,20+line-1);print(' '*100)
                    gotoxy(3, content_height+4+line-1);print(' '*100)
                    marco_inferior(content_width, content_height + line)

                    gotoxy(90,12+line);follow=input() or "s"  
                    gotoxy(90,12+line);print(green_color+"✔"+reset_color)  
                    line += 1
                    
            procesar = confirmacion(content_width, 21+line, "Esta seguro de grabar la venta(s/n):")

            if procesar == "s":
                json_file = JsonFile(path+'/archivos/invoices.json')
                invoices = json_file.read()
                ult_invoices = invoices[-1]["factura"]+1
                data = sale.getJson()
                data["factura"]=ult_invoices
                invoices.append(data)
                json_file.save(invoices)
                mensaje(content_width, 24+line, "😊 Venta Grabada satisfactoriamente 😊")
            else:
                mensaje(content_width, 24+line, "🤣 Venta Cancelada 🤣")
            time.sleep(2)    
    
    def update(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')        
        gotoxy(2,1);print(green_color+"*"*102+reset_color)
        gotoxy(2,2);print(f"{green_color}*{reset_color}{' '*44}{cyan_color}DELETE SALES{reset_color}{' '*44}{green_color}*{reset_color}") 
        gotoxy(2,3);print(green_color+"*"*102+reset_color) 
        content_width = 100
        content_height = 25
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(65,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,4);print(f'{purple_color}Ingrese el NO. de la Factura: {reset_color}')
        id_fact = validar.solo_numeros("Error: Solo numeros", 40, 4)
        
        json_file = JsonFile(path+'/archivos/invoices.json')       
        factura_a_modificar = json_file.find("factura", id_fact)
        
        fila = 10
        if id_fact == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif factura_a_modificar:
            gotoxy(65,4);print(' '*21)
            invoice = factura_a_modificar[0]  # Extrae la primera factura encontrada
            company = Company()
            gotoxy(3,6);print('-'*100)
            gotoxy(20,7);print(f'{cyan_color} Empresa: {reset_color} {white_color}{company.business_name}{reset_color}')
            gotoxy(60,7);print(f'{cyan_color} Ruc: {reset_color} {white_color}{company.ruc}{reset_color}')
            gotoxy(3,8);print('-'*100)
            
            gotoxy(10,9);new_id = input(f"{cyan_color} Factura: #{reset_color}") or invoice['factura']
            gotoxy(35,9);new_fecha = input(f"{cyan_color} Fecha: {reset_color}") or invoice['Fecha']
            gotoxy(60,9);new_client = input(f"{cyan_color} Cliente: {reset_color}") or invoice['cliente']
            
            gotoxy(3,10);print('-'*100)
            gotoxy(10,11);print(f"{purple_color}Detalle: {reset_color}")
            gotoxy(25,11);print(f"{cyan_color}Producto:{reset_color}")
            gotoxy(55,11);print(f"{cyan_color}Precio:{reset_color}")
            gotoxy(80,11);print(f"{cyan_color}Cantidad:{reset_color}")
            
            fila = 12
            for detail in invoice['detalle']:
                gotoxy(26,fila);print(f'{white_color}{detail["producto"]}{reset_color}')
                gotoxy(56,fila);print(f'{white_color}{detail["precio"]}{reset_color}')
                gotoxy(81,fila);print(f'{white_color}{detail["cantidad"]}{reset_color}')
                fila += 1
                
            gotoxy(3,fila);print('-'*100)
            gotoxy(60,fila+1);print(f"{cyan_color} Subtotal:  {reset_color} {white_color}{invoice['subtotal']}{reset_color}")      
            gotoxy(60,fila+2);print(f"{cyan_color} Descuento: {reset_color} {white_color}{invoice['descuento']}{reset_color}")      
            gotoxy(60,fila+3);print(f"{cyan_color} IVA:       {reset_color} {white_color}{invoice['iva']}{reset_color}")      
            gotoxy(60,fila+4);print(f"{cyan_color} Total:     {reset_color} {white_color}{invoice['total']}{reset_color}")
            gotoxy(3,fila+5);print('-'*100)
            
            
            gotoxy(3,29);print(' '*100)
            for i in range(content_height, fila+14):
                gotoxy(2,i);print(f"{green_color}*")
                gotoxy(103,i);print(f"{green_color}*")
                
            marco_inferior(content_width, content_height+fila+12)
            
            procesar = confirmacion(content_width, fila+7, '¿Está seguro de ELIMINAR la factura? (s/n): ')

            if procesar == "s":
                new_values = {'factura': int(new_id), 'Fecha': new_fecha, 'cliente': new_client}
                json_file.update('factura', id_fact, new_values)
                mensaje(content_width, fila+9, '😊 Factura Modificada satisfactoriamente 😊')
            else:
                mensaje(content_width, fila+9, 'Modificación Cancelada!!')
            time.sleep(2)  
            
        else: 
            gotoxy(65,4);print(' '*21)
            invoices = json_file.read()
            
            mensaje(content_width, 6, "Factura no existe!!")
            gotoxy(3,8);print('-'*100)
            mensaje(content_width, 10, "Facturas disponibles")
            
            gotoxy(33,12);print(f'{cyan_color}NO.                Fecha              Total{reset_color}')
            fila = 14
            for fac in invoices:
                gotoxy(33,fila);print(f"{purple_color}{fac['factura']}               {fac['Fecha']}            {fac['total']}{reset_color}")
                fila += 1
                
            gotoxy(3,29);print(' '*100)
            for i in range(content_height, fila):
                gotoxy(2,i);print(f"{green_color}*")
                gotoxy(103,i);print(f"{green_color}*")
                
            marco_inferior(content_width, fila+2)
                
            gotoxy(3,fila+1);print('-'*100)
            
            gotoxy(20,fila+3);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.update()
    
    def delete(self):
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')        
        gotoxy(2,1);print(green_color+"*"*102+reset_color)
        gotoxy(2,2);print(f"{green_color}*{reset_color}{' '*44}{cyan_color}DELETE SALES{reset_color}{' '*44}{green_color}*{reset_color}") 
        gotoxy(2,3);print(green_color+"*"*102+reset_color) 
        content_width = 100
        content_height = 25
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(65,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,4);print(f'{purple_color}Ingrese el NO. de la Factura: {reset_color}')
        id_fact = validar.solo_numeros("Error: Solo numeros", 40, 4)
        json_file = JsonFile(path+'/archivos/invoices.json')
        
        data = json_file.read()
        
        factura_a_eliminar = json_file.find("factura", id_fact)
        
        fila = 10
        if id_fact == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif factura_a_eliminar:
            gotoxy(65,4);print(' '*21)
            invoice = factura_a_eliminar[0]  # Extrae la primera factura encontrada
            company = Company()
            gotoxy(3,6);print('-'*100)
            gotoxy(20,7);print(f'{cyan_color} Empresa: {reset_color} {white_color}{company.business_name}{reset_color}')
            gotoxy(60,7);print(f'{cyan_color} Ruc: {reset_color} {white_color}{company.ruc}{reset_color}')
            gotoxy(3,8);print('-'*100)
            gotoxy(10,9);print(f"{cyan_color} Factura: #{reset_color} {white_color}{invoice['factura']}{reset_color}")
            gotoxy(35,9);print(f"{cyan_color} Fecha: {reset_color} {white_color}{invoice['Fecha']}{reset_color}")
            gotoxy(60,9);print(f"{cyan_color} Cliente: {reset_color} {white_color}{invoice['cliente']}{reset_color}")
            gotoxy(3,10);print('-'*100)
            gotoxy(10,11);print(f"{purple_color}Detalle: {reset_color}")
            gotoxy(25,11);print(f"{cyan_color}Producto:{reset_color}")
            gotoxy(55,11);print(f"{cyan_color}Precio:{reset_color}")
            gotoxy(80,11);print(f"{cyan_color}Cantidad:{reset_color}")
            
            fila = 12
            for detail in invoice['detalle']:
                gotoxy(26,fila);print(f'{white_color}{detail["producto"]}{reset_color}')
                gotoxy(56,fila);print(f'{white_color}{detail["precio"]}{reset_color}')
                gotoxy(81,fila);print(f'{white_color}{detail["cantidad"]}{reset_color}')
                fila += 1
                
            gotoxy(3,fila);print('-'*100)
            gotoxy(60,fila+1);print(f"{cyan_color} Subtotal:  {reset_color} {white_color}{invoice['subtotal']}{reset_color}")      
            gotoxy(60,fila+2);print(f"{cyan_color} Descuento: {reset_color} {white_color}{invoice['descuento']}{reset_color}")      
            gotoxy(60,fila+3);print(f"{cyan_color} IVA:       {reset_color} {white_color}{invoice['iva']}{reset_color}")      
            gotoxy(60,fila+4);print(f"{cyan_color} Total:     {reset_color} {white_color}{invoice['total']}{reset_color}")
            gotoxy(3,fila+5);print('-'*100)
                
            long = len(invoice['detalle'])
            gotoxy(3,29);print(' '*100)
            marco_inferior(content_width, content_height+long)
            
            procesar = confirmacion(content_width, fila+7, '¿Está seguro de ELIMINAR la factura? (s/n): ')

            if procesar == "s":
                data.remove(invoice)
                json_file.save(data)
                mensaje(content_width, fila+9, '😊 Factura Eliminada satisfactoriamente 😊')
            else:
                mensaje(content_width, fila+9, 'Eliminación Cancelada!!')
            time.sleep(2)  
            
        else: 
            gotoxy(65,4);print(' '*21)
            invoices = json_file.read()
            gotoxy(3,29);print(' '*100)
            mensaje(content_width, 6, "Factura no existe!!")
            gotoxy(3,8);print('-'*100)
            mensaje(content_width, 10, "Facturas disponibles")
            
            gotoxy(33,12);print(f'{cyan_color}NO.                Fecha              Total{reset_color}')
            fila = 14
            for fac in invoices:
                gotoxy(33,fila);print(f"{purple_color}{fac['factura']}               {fac['Fecha']}            {fac['total']}{reset_color}")
                fila += 1
                
            for i in range(content_height, fila):
                gotoxy(2,i);print(f"{green_color}*")
                gotoxy(103,i);print(f"{green_color}*")
                
            marco_inferior(content_width, fila+2)
                
            gotoxy(3,fila+1);print('-'*100)
            
            gotoxy(20,fila+3);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.delete()
    
    def consult(self):        
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*102)
        gotoxy(2,2);print(f"*{' '*41}{cyan_color}CONSULTA DE VENTA{reset_color}{' '*42}{green_color}*{reset_color}")
        gotoxy(2,3);print(f"{green_color}*{'*'*100}*{reset_color}")  
        content_width = 100
        content_height = 25
        marco_lateral(content_width, content_height)
        marco_inferior(content_width, content_height)
        
        gotoxy(80,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,4);print(purple_color+"Ingrese el NO. de la Factura: "+reset_color)
        id_fact = validar.solo_numeros("Error: Solo numeros",40,4)
        
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoice = json_file.find("factura",id_fact)
        invoices = json_file.read()

        
        if id_fact == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif invoice:
            gotoxy(80,4);print(' '*21)
            gotoxy(3,29);print(' '*100) 
            gotoxy(2,5);print(f"{green_color}*{'*'*100}*{reset_color}")
            invoice = invoice[0]
            company = Company()
            gotoxy(3,6);print('-'*100)
            gotoxy(20,7);print(f'{cyan_color} Empresa: {reset_color} {white_color}{company.business_name}{reset_color}')
            gotoxy(60,7);print(f'{cyan_color} Ruc: {reset_color} {white_color}{company.ruc}{reset_color}')
            gotoxy(3,8);print('-'*100)
            gotoxy(10,9);print(f"{cyan_color} Factura: #{reset_color} {white_color}{invoice['factura']}{reset_color}")
            gotoxy(35,9);print(f"{cyan_color} Fecha: {reset_color} {white_color}{invoice['Fecha']}{reset_color}")
            gotoxy(60,9);print(f"{cyan_color} Cliente: {reset_color} {white_color}{invoice['cliente']}{reset_color}")
            gotoxy(3,10);print('-'*100)
            gotoxy(10,11);print(f"{purple_color}Detalle: {reset_color}")
            gotoxy(25,11);print(f"{cyan_color}Producto:{reset_color}")
            gotoxy(55,11);print(f"{cyan_color}Precio:{reset_color}")
            gotoxy(80,11);print(f"{cyan_color}Cantidad:{reset_color}")
                
            fila = 1
            for detail in invoice['detalle']:
                gotoxy(26,11+fila);print(f'{white_color}{detail["producto"]}{reset_color}')
                gotoxy(56,11+fila);print(f'{white_color}{detail["precio"]}{reset_color}')
                gotoxy(81,11+fila);print(f'{white_color}{detail["cantidad"]}{reset_color}')
                fila += 1
                
            gotoxy(3,12+fila);print('-'*100)
            gotoxy(60,13+fila);print(f"{cyan_color} Subtotal:  {reset_color} {white_color}{invoice['subtotal']}{reset_color}")      
            gotoxy(60,14+fila);print(f"{cyan_color} Descuento: {reset_color} {white_color}{invoice['descuento']}{reset_color}")      
            gotoxy(60,15+fila);print(f"{cyan_color} IVA:       {reset_color} {white_color}{invoice['iva']}{reset_color}")      
            gotoxy(60,16+fila);print(f"{cyan_color} Total:     {reset_color} {white_color}{invoice['total']}{reset_color}")
            gotoxy(3,17+fila);print('-'*100)
            gotoxy(2,18+fila);print(f"{green_color}*{'*'*100}*{reset_color}")
            
            # Obtener el cliente de la factura consultada
            cliente_factura = invoice['cliente']
            mensaje(content_width+10, 20+fila, f'Facturas del cliente: {white_color}{cliente_factura}{reset_color}')
                
            total_fact_client = list(filter(lambda facturas_cliente: facturas_cliente['cliente'] == invoice['cliente'], invoices))
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), total_fact_client,0)
            totales_map = list(map(lambda invoice: invoice["total"], total_fact_client))
            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = sum(totales_map)
            
            gotoxy(3,21-fila);print('-'*100)
            gotoxy(33,fila+22);print(f'{cyan_color}NO.{reset_color}')
            gotoxy(50,fila+22);print(f'{cyan_color}Fecha{reset_color}')
            gotoxy(69,fila+22);print(f'{cyan_color}Total{reset_color}')
            gotoxy(3,21+fila);print('-'*100)
            
            for fac in total_fact_client:
                gotoxy(33,fila+23);print(f"{purple_color}{fac['factura']}")
                gotoxy(50,fila+23);print(f"{fac['Fecha']}")
                gotoxy(69,fila+23);print(f"{fac['total']}{reset_color}")
                fila += 1
            gotoxy(3,24+fila);print('-'*100)

            gotoxy(2,fila+25);print(f"{green_color}*{'*'*100}*{reset_color}")  
            gotoxy(5,fila+26);print(f"{cyan_color} map Facturas: {reset_color}{totales_map}")
            gotoxy(5,fila+28);print(f"{cyan_color} max Factura: {reset_color}{max_invoice}")
            gotoxy(5,fila+30);print(f"{cyan_color} min Factura: {reset_color}{min_invoice}")
            gotoxy(5,fila+32);print(f"{cyan_color} sum Factura: {reset_color}{tot_invoices}")
            gotoxy(5,fila+34);print(f"{cyan_color} reduce Facturas: {reset_color}{suma}")
            gotoxy(3,fila+35);print('-'*100)
            
            for i in range(content_height, fila+39):
                gotoxy(2,i);print(f"{green_color}*")
                gotoxy(103,i);print(f"{green_color}*")   
                         
            gotoxy(10,fila+37);x=input(red_color+"presione una tecla para continuar..."+reset_color) 

            marco_inferior(content_width, fila+40)
        else: 
            gotoxy(80,4);print(' '*21)  
            gotoxy(3,29);print(' '*100)             
            mensaje(content_width, 7, "Factura no existe!!")
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), invoices,0)
            totales_map = list(map(lambda invoice: invoice["total"], invoices))

            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = round(sum(totales_map), 2)
            
            gotoxy(3,9);print('-'*100)
            gotoxy(33,10);print(f'{cyan_color}NO.{reset_color}')
            gotoxy(50,10);print(f'{cyan_color}Fecha{reset_color}')
            gotoxy(69,10);print(f'{cyan_color}Total{reset_color}')
            gotoxy(3,11);print('-'*100)
            
            fila = 12
            for fac in invoices:
                gotoxy(33,fila);print(f"{purple_color}{fac['factura']}")
                gotoxy(50,fila);print(f"{fac['Fecha']}")
                gotoxy(69,fila);print(f"{fac['total']}{reset_color}")
                fila += 1
            
            gotoxy(2,fila+1);print(f"{green_color}*{'*'*100}*{reset_color}")  
            gotoxy(5,fila+3);print(f"{cyan_color} map Facturas: {reset_color}{totales_map}")
            gotoxy(5,fila+5);print(f"{cyan_color} max Factura: {reset_color}{max_invoice}")
            gotoxy(5,fila+7);print(f"{cyan_color} min Factura: {reset_color}{min_invoice}")
            gotoxy(5,fila+9);print(f"{cyan_color} sum Factura: {reset_color}{tot_invoices}")
            gotoxy(5,fila+11);print(f"{cyan_color} reduce Facturas: {reset_color}{suma}")
            gotoxy(3,fila+12);print('-'*100)
            
            for i in range(content_height, fila+17):
                gotoxy(2,i);print(f"{green_color}*")
                gotoxy(103,i);print(f"{green_color}*")
                
            marco_inferior(content_width, fila+12)
            
            gotoxy(20,fila+14);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.consult()


#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu("Menu Facturacion",["Clientes","Productos","Ventas","Salir"],50,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()    
            clients = CrudClients()
            menu_clients = Menu("Menu Cientes",["Ingresar","Actualizar","Eliminar","Consultar","Salir"],50,10)
            opc1 = menu_clients.menu()
            if opc1 == "1":
                clients.create()
                
            elif opc1 == "2":
                clients.update()
                
            elif opc1 == "3":
                clients.delete()
                
            elif opc1 == "4":
                clients.consult()          
    
    elif opc == "2":
        opc2 = ''
        while opc2 !='5':
            borrarPantalla()    
            product = CrudProducts()
            menu_products = Menu("Menu Productos",["Ingresar","Actualizar","Eliminar","Consultar","Salir"],50,10)
            opc2 = menu_products.menu()
            if opc2 == "1":
                product.create()
                
            elif opc2 == "2":
                product.update()
                
            elif opc2 == "3":
                product.delete()
                
            elif opc2 == "4":
                product.consult()
                
    elif opc == "3":
        opc3 =''
        while opc3 !='5':
            borrarPantalla()
            sales = CrudSales()
            menu_sales = Menu("Menu Ventas",["Registro Venta","Modificar","Eliminar","Consultar","Salir"],50,10)
            opc3 = menu_sales.menu()
            if opc3 == "1":
                sales.create()
                
            elif opc3 == "2":
                sales.update()
                
            elif opc3 == "3":
                sales.delete()
                
            elif opc3 == "4":
                sales.consult()
     
    print("Regresando al menu Principal...")
    # time.sleep(2)            


borrarPantalla()
input("Presione una tecla para salir...")
borrarPantalla()
from components import Menu,Valida
from utilities import borrarPantalla,gotoxy
from utilities import reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color
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
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(cyan_color+"New client"+reset_color)
        gotoxy(10,4);print(f'{green_color}Elija el tipo de cliente a registrar:{reset_color}')
        gotoxy(10,6);print(f'{yellow_color}1. Regular client')
        gotoxy(10,8);print(f'2. VIP client{reset_color}')
        gotoxy(40,9);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,10);tipo_cliente = int(input(f'{green_color}Tipo cliente: {reset_color}'))
        
        if tipo_cliente == 0:
            gotoxy(10,12);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2)  

        elif tipo_cliente == 1:
            gotoxy(10,9);print(' '*100)
            gotoxy(10,12);print(purple_color+"DNI:"+reset_color)
            dni = validar.solo_numeros("Error: Solo numeros", 15, 12)
            
            json_file = JsonFile(path+'/archivos/clients.json')
            
            client_existe = json_file.find("dni",dni)
            
            if not client_existe:
                gotoxy(10, 14);first_name = input(purple_color+"First_name: "+reset_color).capitalize()
                gotoxy(10, 16);last_name = input(purple_color+"Last_name: "+reset_color).capitalize()
                gotoxy(10, 18);card = input(purple_color+"Card: "+reset_color).capitalize()

                client = RegularClient(first_name, last_name, dni, card)

                gotoxy(10, 20);procesar = input(red_color+"Esta seguro de grabar el Client(s/n): "+reset_color).lower()
                gotoxy(52, 20);print(green_color+"✔"+reset_color)
                
                if procesar == "s":
                    clients = json_file.read()
                    data = client.getJson()
                    clients.append(data)
                    json_file.save(clients)
                    gotoxy(30,23);print(yellow_color+"😊 Client Grabado satisfactoriamente 😊"+reset_color)
                else:
                    gotoxy(30,23);print(red_color+"🤣 Client Cancelado 🤣"+reset_color)    
                time.sleep(2)  
            else:
                gotoxy(35, 14)
                print(yellow_color+"Cliente ya existe!!"+reset_color) 
                for i in range(3, 0, -1):
                    gotoxy(20, 16);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                    time.sleep(1)
                self.create()
                
        elif tipo_cliente == 2:
            gotoxy(10,9);print(' '*100)
            gotoxy(10,12);print(purple_color+"DNI:"+reset_color)
            dni = validar.solo_numeros("Error: Solo numeros", 15, 12)
            
            json_file = JsonFile(path+'/archivos/clients.json')
            
            client_existe = json_file.find("dni",dni)
            
            if not client_existe:
                gotoxy(10, 14);first_name = input(purple_color+"First_name: "+reset_color).capitalize()
                gotoxy(10, 16);last_name = input(purple_color+"Last_name: "+reset_color).capitalize()
                gotoxy(10, 18);valor = int(input(purple_color+"Valor: "+reset_color))
                client = VipClient(first_name, last_name, dni)
                
                client.limit = valor if valor else None

                gotoxy(10, 20);procesar = input(red_color+"Esta seguro de grabar el Client(s/n): "+reset_color).lower()
                gotoxy(52, 20);print(green_color+"✔"+reset_color)
                
                if procesar == "s":
                    clients = json_file.read()
                    data = client.getJson()
                    clients.append(data)
                    json_file.save(clients)
                    gotoxy(30,23);print(yellow_color+"😊 Client Grabado satisfactoriamente 😊"+reset_color)
                else:
                    gotoxy(30,23);print(red_color+"🤣 Client Cancelado 🤣"+reset_color)    
                time.sleep(2)  
            else:
                gotoxy(35, 14)
                print(yellow_color+"Cliente ya existe!!"+reset_color) 
                for i in range(3, 0, -1):
                    gotoxy(20, 16);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                    time.sleep(1)
                self.create()
        

    def update(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(cyan_color+"Update client"+reset_color)
        gotoxy(30,3);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,4);print(purple_color+"DNI:"+reset_color)
    
        dni = validar.solo_numeros("Error: Solo numeros", 15, 4)
        json_file = JsonFile(path+'/archivos/clients.json')
        client_existe = json_file.find("dni",dni)
        
        if int(dni) == 0:
            gotoxy(15,6);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2)  
        elif client_existe:
            gotoxy(10,3);print(' '*100)
            client = client_existe[0]
            
            gotoxy(10,6);print(blue_color+f"Client: {client['nombre']} {client['apellido']}" +reset_color)
            
            gotoxy(10,8);new_dni = (input(cyan_color + "DNI: " + reset_color)) or client['dni']
            gotoxy(10,10);new_first_name = input(purple_color+"First_name: "+reset_color).capitalize()  or client['nombre']
            gotoxy(10,12);new_last_name = input(purple_color+"Last_name: "+reset_color).capitalize()  or client['apellido'] 
            gotoxy(10,14);new_valor = input(purple_color+"Valor: "+reset_color)
            if new_valor:
                new_valor = float(round(new_valor,0))
            else:
                new_valor = float(client['valor'])
                
            gotoxy(10, 16);print(red_color+"Esta seguro de grabar el Cliente(s/n):"+reset_color)
            gotoxy(49, 16);procesar = input().lower()
            gotoxy(52, 16);print(green_color+"✔"+reset_color)
            
            if procesar == "s":
                new_values = {'dni': new_dni, 'nombre': new_first_name, 'apellido': new_last_name, 'valor': new_valor}
                json_file.update('dni', dni, new_values)
                gotoxy(30,18);print(yellow_color+"😊 Cliente actualizado satisfactoriamente 😊"+reset_color)

            else:
                gotoxy(30,18);print(red_color+"🤣 Actualización Cancelada 🤣"+reset_color)    
            time.sleep(2)  
                
        else: 
            gotoxy(10,3);print(' '*100)
            gotoxy(15,6);print(f'{yellow_color} Cliente no existe!! {reset_color}')
            clients = json_file.read()
            gotoxy(15,8);print('Clientes disponibles')
                        
            fila = 10
            item = 1
            for cli in clients:
                gotoxy(20,fila);print(f"{purple_color} {item}. {reset_color} {blue_color} {cli['nombre']} {cli['apellido']} {reset_color}")
                fila += 1
                item += 1
                        
            gotoxy(20,fila+2);x=input(f'{red_color} Presione una tecla para continuar... {reset_color}')
            self.update()
      
        
    def delete(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(cyan_color+"Delete client"+reset_color)
        gotoxy(30,3);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,4);print(purple_color+"DNI:"+reset_color)
        dni = validar.solo_numeros("Error: Solo numeros", 15, 4)
        json_file = JsonFile(path+'/archivos/clients.json')
        data = json_file.read()
        cliente_a_eliminar = json_file.find("dni",dni)
        
        if int(dni) == 0:
            gotoxy(15,6);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2)  
        elif cliente_a_eliminar:
            gotoxy(10,3);print(' '*100)
            client = cliente_a_eliminar[0]
            
            gotoxy(10,6);print(f"{blue_color} Client: {reset_color} {client['nombre']} {client['apellido']}")
            gotoxy(10,8);print(f"{blue_color} Valor: {reset_color} {client['valor']}")

            gotoxy(20, 10);procesar = input(f"{red_color}Esta seguro de ELIMINAR el Cliente (s/n): {reset_color}").lower()
            gotoxy(65, 10);print(green_color+"✔"+reset_color)

            if procesar == "s":
                data.remove(client)
                json_file.save(data)
                gotoxy(30,12);print(yellow_color+"😊 Cliente Eliminado satisfactoriamente 😊"+reset_color)
            else:
                gotoxy(30,12);print(red_color+"🤣 Eliminación Cancelada 🤣"+reset_color)    
            time.sleep(2)         
        else: 
            gotoxy(10,3);print(' '*100)
            gotoxy(15,6);print(yellow_color+"Cliente no existe!!"+reset_color)
            clients = json_file.read()
            gotoxy(15,8);print('Clientes disponibles')        
            
            fila = 10
            item = 1
            for cli in clients:
                gotoxy(20,fila);print(f"{purple_color} {item}. {reset_color} {blue_color} {cli['nombre']} {reset_color}")
                fila += 1
                item += 1     
                
            gotoxy(20,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.delete()
            
            
    def consult(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(cyan_color+"Consulta client"+reset_color)
        gotoxy(30,3);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,4);print(purple_color+"DNI:"+reset_color)
        dni = validar.solo_numeros("Error: Solo numeros", 15, 4)
        json_file = JsonFile(path+'/archivos/clients.json')
        client_existe = json_file.find("dni",dni)
        
        if int(dni) == 0:
            gotoxy(15,6);print(f"{red_color} Regresando al menu Clientes... {reset_color}")
            time.sleep(2) 
        elif client_existe:
            gotoxy(10,3);print(' '*100)
            client = client_existe[0]
            
            gotoxy(10,6);print(f"{blue_color} DNI: {reset_color} {client['dni']}")
            gotoxy(10,8);print(f"{blue_color} Client: {reset_color} {client['nombre']} {client['apellido']}")
            gotoxy(10,10);print(f"{blue_color} Valor: {reset_color} {client['valor']}")
             
            gotoxy(12,12);x=input(red_color+"presione una tecla para continuar..."+reset_color)    
        else: 
            gotoxy(10,3);print(' '*100)
            gotoxy(15,6);print(f'{yellow_color} Cliente no existe!! {reset_color}')
            clients = json_file.read()
            gotoxy(15,8);print('Clientes disponibles')
                        
            fila = 10
            item = 1
            for cli in clients:
                gotoxy(18,fila);print(f"{purple_color} {item}. {reset_color} {blue_color} {cli['nombre']} {reset_color}")
                fila += 1
                item += 1
                        
            gotoxy(12,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.consult()
            

class CrudProducts(ICrud):
    def create(self):
        validar = Valida()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(cyan_color+"New product"+reset_color)
        gotoxy(50,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(10,4);print(purple_color+"Description:"+reset_color)
        descripcion = validar.solo_letras("Error: Solo letras", 23, 4)
        json_file = JsonFile(path+'/archivos/products.json')
        product = json_file.find("descripcion",descripcion)
      
        if descripcion == 0:
            gotoxy(15,6);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif not product:
            gotoxy(50,4);print(' '*100)
            gotoxy(10, 6);print(purple_color+"Price: "+reset_color)
            gotoxy(17, 6);price = float(input())
            gotoxy(10, 8);print(purple_color+"Stock: "+reset_color)
            gotoxy(17, 8);stock = int(input())

            product = Product(None, descripcion, price, stock)

            gotoxy(10, 10);print(red_color+"Esta seguro de grabar el producto(s/n):"+reset_color)
            gotoxy(50, 10);procesar = input().lower()
            gotoxy(52, 10);print(green_color+"✔"+reset_color)
            
            if procesar == "s":
                products = json_file.read()
                last_id = products[-1]["id"]+1
                product_data = product.getJson()
                product_data["id"] = last_id
                products.append(product_data)
                json_file.save(products)
                gotoxy(30,13);print(yellow_color+"😊 Producto Grabado satisfactoriamente 😊"+reset_color)
                
            else:
                gotoxy(30,13);print(red_color+"🤣 Producto Cancelado 🤣"+reset_color)    
            time.sleep(2)  
        else:
            gotoxy(50,4);print(' '*100)
            gotoxy(35, 6);print(yellow_color+"Producto ya existe!!"+reset_color) 
            for i in range(3, 0, -1):
                gotoxy(20, 8);print(f"{green_color} Espere {i} segundos... {reset_color}", end="\r")
                time.sleep(1)
            self.create() 


    def update(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Actualizar Producto"+" "*33+"██" +reset_color)
        gotoxy(50,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(2,4);product_id = int(input(purple_color+"Ingrese ID del Producto: "+reset_color))
        json_file = JsonFile(path+'/archivos/products.json')
        product = json_file.find("id",product_id )
        
        fila = 10
        if product_id == 0:
            gotoxy(15,6);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif product:
            gotoxy(50,4);print(' '*100)
            product = product[0]
            
            gotoxy(2,6);print(blue_color+f"Producto: {product['id']}" +reset_color)
            
            gotoxy(2,8);new_description = input(cyan_color + "Descripcion: " + reset_color)  or product['descripcion']
            gotoxy(2,10);new_price = input(cyan_color + "Precio: " +reset_color)  or product['precio']
            gotoxy(2,12);new_stock = input(cyan_color + "Stock: " +reset_color)  or product['stock']      
            
            gotoxy(10, 15);print(red_color+"Esta seguro de grabar la actualizacion del producto(s/n):"+reset_color)
            gotoxy(68, 15);procesar = input().lower()
            gotoxy(70, 15);print(green_color+"✔"+reset_color)
            
            if procesar == "s":
                new_values = {'descripcion': new_description.capitalize(), 'precio': float(new_price), 'stock': int(new_stock)}
                json_file.update('id', product_id, new_values)
                gotoxy(30,18);print(yellow_color+"😊 Producto Actualizado satisfactoriamente 😊"+reset_color)
            else:
                gotoxy(30,18);print(red_color+"Actualizacion Cancelada!!"+reset_color)
                    
            time.sleep(2)  
            
        else: 
            gotoxy(50,4);print(' '*100)
            gotoxy(15,6);print(yellow_color+"Producto no existe!!"+reset_color)
            productos = json_file.read()
            gotoxy(15,8);print('Productos disponibles')
            for prod in productos:
                gotoxy(20,fila);print(f"{purple_color} {prod['id']}. {reset_color} {blue_color} {prod['descripcion']} {reset_color}")
                fila += 1
                        
            gotoxy(20,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.update()
    
    
    def delete(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Eliminar Producto"+" "*35+"██" +reset_color)
        gotoxy(50,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(2,4);product_id = int(input(purple_color+"Ingrese ID del Producto: "+reset_color))
        json_file = JsonFile(path+'/archivos/products.json')
        data = json_file.read()
        
        producto_a_eliminar = json_file.find("id",product_id )
        
        fila = 10
        if product_id == 0:
            gotoxy(15,6);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif producto_a_eliminar:
            gotoxy(50,4);print(' '*100)
            product = producto_a_eliminar[0]
            
            gotoxy(2,6);print(f"{cyan_color} Producto: {reset_color} {product['id']}")
            gotoxy(2,8);print(f"{cyan_color} Descripcion: {reset_color} {product['descripcion']}")
            gotoxy(2,10);print(f"{cyan_color} Precio: {reset_color} {product['precio']}")
            gotoxy(2,12);print(f"{cyan_color} Stock: {reset_color} {product['stock']}")      
            
            gotoxy(10, 15);print(red_color+"Esta seguro de ELIMINAR el producto(s/n):"+reset_color)
            gotoxy(52, 15);procesar = input().lower()
            gotoxy(54, 15);print(green_color+"✔"+reset_color)
            

            if procesar == "s":
                data.remove(product)
                json_file.save(data)
                
                gotoxy(20,18);print(yellow_color+"😊 Producto Eliminado satisfactoriamente 😊"+reset_color)

            else:
                gotoxy(20,18);print(yellow_color+"Eliminacion Cancelada!!"+reset_color)
                    
            time.sleep(2)  
            
        else: 
            gotoxy(50,4);print(' '*100)
            gotoxy(15,6);print(yellow_color+"Producto no existe!!"+reset_color)
            productos = json_file.read()
            gotoxy(15,8);print('Productos disponibles')
            for prod in productos:
                gotoxy(20,fila);print(f"{purple_color} {prod['id']}. {reset_color} {blue_color} {prod['descripcion']} {reset_color}")
                fila += 1
                        
            gotoxy(20,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.delete()
    
    
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Producto"+" "*32+"██" +reset_color)
        gotoxy(50,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(2,4);product_id = int(input(purple_color+"Ingrese ID del Producto: "+reset_color))
        json_file = JsonFile(path+'/archivos/products.json')
        product = json_file.find("id",product_id)
        
        fila = 10
        if product_id == 0:
            gotoxy(15,6);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif product:
            gotoxy(50,4);print(' '*100)
            producto = product[0]
            
            gotoxy(4,6);print(yellow_color+f"Producto:{reset_color} {producto['id']}")
            gotoxy(4,8);print(cyan_color+f"Descripcion:{reset_color} {producto['descripcion']}")
            gotoxy(4,10);print(cyan_color+f"Precio:{reset_color} {producto['precio']}")
            gotoxy(4,12);print(cyan_color+f"Stock:{reset_color} {producto['stock']}")  
            
            gotoxy(4,15);x=input(red_color+"presione una tecla para continuar..."+reset_color)             
        else: 
            gotoxy(50,4);print(' '*100)
            gotoxy(15,6);print(yellow_color+"Producto no existe!!"+reset_color)
            productos = json_file.read()
            gotoxy(15,8);print('Productos disponibles')
            for prod in productos:
                gotoxy(20,fila);print(f"{purple_color} {prod['id']}. {reset_color} {blue_color} {prod['descripcion']} {reset_color}")
                fila += 1
                        
            gotoxy(20,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.consult()


class CrudSales(ICrud):
    def create(self):
        # cabecera de la venta
        validar = Valida()
        borrarPantalla()
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"*"*90+reset_color)
        gotoxy(30,2);print(blue_color+"Registro de Venta")
        gotoxy(17,3);print(blue_color+Company.get_business_name())
        gotoxy(5,4);print(f"Factura#:F0999999 {' '*3} Fecha:{datetime.datetime.now()}")
        gotoxy(66,4);print("Subtotal:")
        gotoxy(66,5);print("Decuento:")
        gotoxy(66,6);print("Iva     :")
        gotoxy(66,7);print("Total   :")
        gotoxy(35,6);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(15,6);print("Cedula:")
        dni=validar.solo_numeros("Error: Solo numeros",23,6)
        
        if int(dni) == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        else:
            gotoxy(35,6);print(' '*100)
            json_file = JsonFile(path+'/archivos/clients.json')
            client = json_file.find("dni",dni)
            if not client:
                gotoxy(35,6);print("Cliente no existe")
                return
            client = client[0]
            cli = RegularClient(client["nombre"],client["apellido"], client["dni"], card=True) 
            sale = Sale(cli)
            gotoxy(35,6);print(cli.fullName())
            gotoxy(2,8);print(green_color+"*"*90+reset_color) 
            gotoxy(5,9);print(purple_color+"Linea") 
            gotoxy(12,9);print("Id_Articulo") 
            gotoxy(24,9);print("Descripcion") 
            gotoxy(38,9);print("Precio") 
            gotoxy(48,9);print("Cantidad") 
            gotoxy(58,9);print("Subtotal") 
            gotoxy(70,9);print("n->Terminar Venta)"+reset_color)
            # detalle de la venta
            follow ="s"
            line=1
            while follow.lower()=="s":
                gotoxy(7,9+line);print(line)
                gotoxy(15,9+line);
                id=int(validar.solo_numeros("Error: Solo numeros",15,9+line))
                json_file = JsonFile(path+'/archivos/products.json')
                prods = json_file.find("id",id)
                if not prods:
                    gotoxy(24,9+line);print("Producto no existe")
                    time.sleep(1)
                    gotoxy(24,9+line);print(" "*20)
                else:    
                    prods = prods[0]
                    product = Product(prods["id"],prods["descripcion"],prods["precio"],prods["stock"])
                    gotoxy(24,9+line);print(product.descrip)
                    gotoxy(38,9+line);print(product.preci)
                    gotoxy(49,9+line);qyt=int(validar.solo_numeros("Error:Solo numeros",49,9+line))
                    gotoxy(59,9+line);print(product.preci*qyt)
                    sale.add_detail(product,qyt)
                    gotoxy(76,4);print(round(sale.subtotal,2))
                    gotoxy(76,5);print(round(sale.discount,2))
                    gotoxy(76,6);print(round(sale.iva,2))
                    gotoxy(76,7);print(round(sale.total,2))
                    gotoxy(74,9+line);follow=input() or "s"  
                    gotoxy(76,9+line);print(green_color+"✔"+reset_color)  
                    line += 1
            gotoxy(15,9+line);print(red_color+"Esta seguro de grabar la venta(s/n):")
            gotoxy(54,9+line);procesar = input().lower()
            if procesar == "s":
                json_file = JsonFile(path+'/archivos/invoices.json')
                invoices = json_file.read()
                ult_invoices = invoices[-1]["factura"]+1
                data = sale.getJson()
                data["factura"]=ult_invoices
                invoices.append(data)
                json_file.save(invoices)
                gotoxy(15,10+line);print(yellow_color+"😊 Venta Grabada satisfactoriamente 😊"+reset_color)
            else:
                gotoxy(20,10+line);print(red_color+"🤣 Venta Cancelada 🤣"+reset_color)    
            time.sleep(2)    
    
    def update(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Editar Factura"+" "*38+"██" +reset_color)
        gotoxy(65,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(6,4);id_fact = int(input(purple_color+'Ingrese el numero de la factura: '+reset_color))
        json_file = JsonFile(path+'/archivos/invoices.json')       
        factura_a_modificar = json_file.find("factura", id_fact)
        
        fila = 10
        if id_fact == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif factura_a_modificar:
            gotoxy(65,4);print(' '*100)
            invoice = factura_a_modificar[0]  # Extrae la primera factura encontrada
            company = Company()
            gotoxy(6,4);print('-'*100)
            gotoxy(20,5);print(f'{cyan_color} Empresa: {reset_color} {company.business_name}')
            gotoxy(60,5);print(f'{cyan_color} Ruc: {reset_color} {company.ruc}')
            gotoxy(6,6);print('-'*100)
            gotoxy(10,7);new_id = input(f"{cyan_color} Factura: #{reset_color}") or invoice['factura']
            gotoxy(35,7);new_fecha = input(f"{cyan_color} Fecha: {reset_color}") or invoice['Fecha']
            gotoxy(60,7);new_client = input(f"{cyan_color} Cliente: {reset_color}") or invoice['cliente']
            gotoxy(6,8);print('-'*100)
            gotoxy(10,9);print(f"{cyan_color} Detalle: {reset_color}")
            
            fila = 10
            for detail in invoice['detalle']:
                gotoxy(20,fila);print(f'{cyan_color} Producto: {reset_color} {detail["producto"]}')
                gotoxy(20+30,fila);print(f'{cyan_color} Precio: {reset_color} {detail["precio"]}')
                gotoxy(20+55,fila);print(f'{cyan_color} Cantidad: {reset_color} {detail["cantidad"]}')
                fila += 1
                
            gotoxy(6,fila);print('-'*100)
            gotoxy(60,fila+1);new_subtotal = input(f"{cyan_color} Subtotal:  {reset_color}") or invoice['subtotal']      
            gotoxy(60,fila+2);new_descuento = input(f"{cyan_color} Descuento: {reset_color}") or invoice['descuento']     
            gotoxy(60,fila+3);new_iva = input(f"{cyan_color} IVA:       {reset_color}") or invoice['iva']    
            gotoxy(60,fila+4);new_total = input(f"{cyan_color} Total:     {reset_color}") or invoice['total']
            gotoxy(6,fila+5);print('-'*100)
                
            gotoxy(10, fila+7);print(red_color+"¿Está seguro de Modificar la factura? (s/n): "+reset_color)
            gotoxy(55, fila+7);procesar = input().lower()
            gotoxy(57, fila+7);print(red_color+"✔"+reset_color)

            if procesar == "s":
                new_values = {'factura': int(new_id), 'Fecha': new_fecha, 'cliente': new_client, 'subtotal': float(new_subtotal), 'descuento': float(new_descuento), 'iva': float(new_iva), 'total': float(new_total)}
                json_file.update('factura', id_fact, new_values)
                gotoxy(20,fila+9);print(yellow_color+"😊 Factura Modificada satisfactoriamente 😊"+reset_color)
            else:
                gotoxy(20,fila+9);print(yellow_color+"Modificación Cancelada!!"+reset_color)
                    
            time.sleep(2)  
            
        else: 
            gotoxy(65,4);print(' '*100)
            gotoxy(6,6);print(yellow_color+"Factura no existe!!"+reset_color)
            invoices = json_file.read()
            gotoxy(4,8);print('No. Facturas disponibles')
                        
            for fact in invoices:
                gotoxy(6,fila);print(blue_color+ str(fact['factura'])+reset_color)
                fila += 1
                        
            gotoxy(4,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.update()
    
    def delete(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Eliminar Factura"+" "*35+"██" +reset_color)
        gotoxy(65,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(2,4);id_fact = int(input(purple_color+'Ingrese el numero de la factura: '+reset_color))
        json_file = JsonFile(path+'/archivos/invoices.json')
        
        data = json_file.read()
        
        factura_a_eliminar = json_file.find("factura", id_fact)
        
        fila = 10
        if id_fact == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif factura_a_eliminar:
            gotoxy(65,4);print(' '*100)
            invoice = factura_a_eliminar[0]  # Extrae la primera factura encontrada
            company = Company()
            gotoxy(2,4);print('-'*100)
            gotoxy(20,5);print(f'{cyan_color} Empresa: {reset_color} {company.business_name}')
            gotoxy(60,5);print(f'{cyan_color} Ruc: {reset_color} {company.ruc}')
            gotoxy(2,6);print('-'*100)
            gotoxy(10,7);print(f"{cyan_color} Factura: #{reset_color} {invoice['factura']}")
            gotoxy(35,7);print(f"{cyan_color} Fecha: {reset_color} {invoice['Fecha']}")
            gotoxy(60,7);print(f"{cyan_color} Cliente: {reset_color} {invoice['cliente']}")
            gotoxy(2,8);print('-'*100)
            gotoxy(10,9);print(f"{cyan_color} Detalle: {reset_color}")
            
            fila = 10
            for detail in invoice['detalle']:
                gotoxy(20,fila);print(f'{cyan_color} Producto: {reset_color} {detail["producto"]}')
                gotoxy(20+30,fila);print(f'{cyan_color} Precio: {reset_color} {detail["precio"]}')
                gotoxy(20+55,fila);print(f'{cyan_color} Cantidad: {reset_color} {detail["cantidad"]}')
                fila += 1
                
            gotoxy(2,fila);print('-'*100)
            gotoxy(60,fila+1);print(f"{cyan_color} Subtotal:  {reset_color} {invoice['subtotal']}")      
            gotoxy(60,fila+2);print(f"{cyan_color} Descuento: {reset_color} {invoice['descuento']}")      
            gotoxy(60,fila+3);print(f"{cyan_color} IVA:       {reset_color} {invoice['iva']}")      
            gotoxy(60,fila+4);print(f"{cyan_color} Total:     {reset_color} {invoice['total']}")
            gotoxy(2,fila+5);print('-'*100)
                
                
            gotoxy(10, fila+7);print(red_color+"¿Está seguro de ELIMINAR la factura? (s/n): "+reset_color)
            gotoxy(54, fila+7);procesar = input().lower()
            gotoxy(56, fila+7);print(red_color+"✔"+reset_color)

            if procesar == "s":
                data.remove(invoice)
                json_file.save(data)
                gotoxy(20,fila+9);print(yellow_color+"😊 Factura Eliminada satisfactoriamente 😊"+reset_color)
            else:
                gotoxy(20,fila+9);print(yellow_color+"Eliminación Cancelada!!"+reset_color)
                    
            time.sleep(2)  
            
        else: 
            gotoxy(65,4);print(' '*100)
            gotoxy(6,6);print(yellow_color+"Factura no existe!!"+reset_color)
            invoices = json_file.read()
            gotoxy(4,8);print('No. Facturas disponibles')
                        
            for fact in invoices:
                gotoxy(6,fila);print(blue_color+ str(fact['factura'])+reset_color)
                fila += 1
                        
            gotoxy(4,fila+2);x=input(red_color+"presione una tecla para continuar..."+reset_color)
            self.delete()
    
    def consult(self):
        print('\033c', end='')
        gotoxy(2,1);print(green_color+"█"*90)
        gotoxy(2,2);print("██"+" "*34+"Consulta de Venta"+" "*35+"██" + reset_color)
        gotoxy(65,4);print(f'{red_color}Ingrese 0 para salir.{reset_color}')
        gotoxy(2,4);id_fact= int(input(f"{purple_color} Ingrese el numero de la Factura: {reset_color}"))
        json_file = JsonFile(path+'/archivos/invoices.json')
        invoice = json_file.find("factura",id_fact)
        gotoxy(2,4);print(' '*100)
        if id_fact == 0:
            gotoxy(15,8);print(f"{red_color} Regresando al menu Productos... {reset_color}")
            time.sleep(2)
        elif invoice:
            gotoxy(65,4);print(' '*100)
            invoice = invoice[0]
            company = Company()
            gotoxy(2,4);print('-'*100)
            gotoxy(20,5);print(f'{cyan_color} Empresa: {reset_color} {company.business_name}')
            gotoxy(60,5);print(f'{cyan_color} Ruc: {reset_color} {company.ruc}')
            gotoxy(2,6);print('-'*100)
            gotoxy(10,7);print(f"{cyan_color} Factura: #{reset_color} {invoice['factura']}")
            gotoxy(35,7);print(f"{cyan_color} Fecha: {reset_color} {invoice['Fecha']}")
            gotoxy(60,7);print(f"{cyan_color} Cliente: {reset_color} {invoice['cliente']}")
            gotoxy(2,8);print('-'*100)
            gotoxy(10,9);print(f"{cyan_color} Detalle: {reset_color}")
            
            fila = 10
            for detail in invoice['detalle']:
                gotoxy(20,fila);print(f'{cyan_color} Producto: {reset_color} {detail["producto"]}')
                gotoxy(20+30,fila);print(f'{cyan_color} Precio: {reset_color} {detail["precio"]}')
                gotoxy(20+55,fila);print(f'{cyan_color} Cantidad: {reset_color} {detail["cantidad"]}')
                fila += 1
                
            gotoxy(2,fila);print('-'*100)
            gotoxy(60,fila+1);print(f"{cyan_color} Subtotal:  {reset_color} {invoice['subtotal']}")      
            gotoxy(60,fila+2);print(f"{cyan_color} Descuento: {reset_color} {invoice['descuento']}")      
            gotoxy(60,fila+3);print(f"{cyan_color} IVA:       {reset_color} {invoice['iva']}")      
            gotoxy(60,fila+4);print(f"{cyan_color} Total:     {reset_color} {invoice['total']}")
            gotoxy(2,fila+5);print('-'*100)
                
            gotoxy(10,fila+7);x=input(red_color+"presione una tecla para continuar..."+reset_color)  
             
        else: 
            gotoxy(65,4);print(' '*100)   
            invoices = json_file.read()
            print("Consulta de Facturas")
            for fac in invoices:
                print(f"{fac['factura']}   {fac['Fecha']}   {fac['cliente']}   {fac['total']}")
            
            suma = reduce(lambda total, invoice: round(total+ invoice["total"],2), 
            invoices,0)
            totales_map = list(map(lambda invoice: invoice["total"], invoices))
            total_client = list(filter(lambda invoice: invoice["cliente"] == "Dayanna Vera", invoices))

            max_invoice = max(totales_map)
            min_invoice = min(totales_map)
            tot_invoices = sum(totales_map)
            print("filter cliente: ",total_client)
            print(f"map Facturas:{totales_map}")
            print(f"              max Factura:{max_invoice}")
            print(f"              min Factura:{min_invoice}")
            print(f"              sum Factura:{tot_invoices}")
            print(f"              reduce Facturas:{suma}")
            x=input("presione una tecla para continuar...")    
            self.consult()


#Menu Proceso Principal
opc=''
while opc !='4':  
    borrarPantalla()      
    menu_main = Menu("Menu Facturacion",["1) Clientes","2) Productos","3) Ventas","4) Salir"],20,10)
    opc = menu_main.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='5':
            borrarPantalla()    
            clients = CrudClients()
            menu_clients = Menu("Menu Cientes",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
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
            menu_products = Menu("Menu Productos",["1) Ingresar","2) Actualizar","3) Eliminar","4) Consultar","5) Salir"],20,10)
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
            menu_sales = Menu("Menu Ventas",["1) Registro Venta","2) Modificar","3) Eliminar","4) Consultar","5) Salir"],20,10)
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
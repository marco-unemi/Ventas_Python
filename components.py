from utilities import borrarPantalla, gotoxy, reset_color,red_color,green_color,yellow_color,blue_color,purple_color,cyan_color,black_color, white_color
import time


class Menu:
    def __init__(self, titulo="", opciones=[], col=6, fil=1):
        self.titulo = titulo
        self.opciones = opciones
        self.col = col
        self.fil = fil

    def menu(self):
        gotoxy(25,8);print(yellow_color+"█"*35+reset_color)
        gotoxy(60,8);print(green_color+"█"*35+reset_color)
        for i in range(8,27):
            gotoxy(25,i);print(green_color+"██"+reset_color)
            gotoxy(95,i);print(green_color+"██"+reset_color)
            gotoxy(25,26);print(green_color+"█"*35+reset_color)
            gotoxy(60,26);print(yellow_color+"█"*35+reset_color)
        
        gotoxy(self.col, self.fil)
        print(f'{red_color}{self.titulo}{reset_color}')
        self.col -= 5
        i = 1
        for opcion in self.opciones:
            self.fil += 2
            gotoxy(self.col, self.fil)
            print(f'{purple_color}{i}){reset_color} {white_color}{opcion}{reset_color}')
            i += 1
        gotoxy(self.col+5, self.fil+2)
        opc = input(f"{blue_color}Elija opcion[{purple_color}1...{len(self.opciones)}{purple_color}]: {reset_color}")
        return opc


class Valida:
    def solo_numeros(self, mensaje, col, fil):
        while True:
            gotoxy(col, fil)
            valor = input()
            try:
                valor_entero = int(valor)
                if valor_entero == 0:
                    return valor_entero
                elif valor_entero > 0:
                    return valor_entero
                else:
                    gotoxy(col, fil)
                    print("          ------><  | {} ".format(mensaje))
                    time.sleep(1)
                    gotoxy(col, fil)
                    print(" "*41)
            except ValueError:
                gotoxy(col, fil)
                print("          ------><  | {} ".format(mensaje))
                time.sleep(1)
                gotoxy(col, fil)
                print(" "*41)
            

    def solo_letras(self, mensajeError, col, fil):
        while True:
            gotoxy(col, fil)
            valor = str(input().capitalize())
            if valor.strip() == '0':  # Verificar si se ingresó '0'
                return int(valor)  # Devolver '0' como cadena
            try:
                if valor.replace(" ", "").isalpha():
                    break
                else:
                    raise ValueError  # Lanzar una excepción si no son letras
            except ValueError:
                gotoxy(col, fil)
                print("          ------><  | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col, fil)
                print(" "*50)
        return valor
    
    
    def solo_decimales(self, mensajeError, col, fil):
        while True:
            gotoxy(col, fil)
            valor = str(input())
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                gotoxy(col, fil)
                print("          ------><  | {} ".format(mensajeError))
                time.sleep(1)
                gotoxy(col, fil)
                print(" "*50)
        return valor

    def verificar_cedula(self, cedula):
        if cedula == '0':
            return True
        
        elif len(cedula) != 10:
            return False
        
        coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
        suma = 0
        for i in range(9):
            digito = int(cedula[i])
            resultado = digito * coeficientes[i]
            if resultado > 9:
                resultado -= 9
            suma += resultado
        
        verificador = 10 - (suma % 10)
        if verificador == 10:
            verificador = 0
        
        return verificador == int(cedula[9])
    
class otra:
    pass



# if __name__ == '__main__':
    # instanciar el menu
    # opciones_menu = ["1. Entero", "2. Letra", "3. Decimal"]
    # menu = Menu(titulo="-- Mi Menú --", opciones=opciones_menu, col=10, fil=5)
    # llamada al menu
    # opcion_elegida = menu.menu()
    # print("Opción escogida:", opcion_elegida)
    # valida = Valida()
    # if (opciones_menu == 1):
        # numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
        # print("Número validado:", numero_validado)

    # numero_validado = valida.solo_numeros("Mensaje de error", 10, 10)
    # print("Número validado:", numero_validado)

    # letra_validada = valida.solo_letras(
        # "Ingrese una letra:", "Mensaje de error")
    # print("Letra validada:", letra_validada)

    # decimal_validado = valida.solo_decimales(
        # "Ingrese un decimal:", "Mensaje de error")
    # print("Decimal validado:", decimal_validado)

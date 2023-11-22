finalizar_programa = False
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
class Cliente (Persona):
    def __init__(self, nombre, apellido, numero_cuenta,balance = 0):
        super().__init__(nombre,apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return(f'{self.nombre} {self.apellido} su número de cuenta es: {self.numero_cuenta} \n su saldo es de: ${self.balance}')
    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print('Deposito aceptado')
    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondos insuficientes")

def crear_cliente():
    nombre_nuevo = input('Ingrese su nombre: ')
    apellido_nuevo = input('Ingrese su apellido: ')
    numero_cuenta = input('Ingrese su cuenta: ')
    cliente_creado = Cliente(nombre_nuevo,apellido_nuevo,numero_cuenta)
    return cliente_creado


def inicio ():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    eleccion = 0
    while eleccion != 'S':
        print("Elige una opción: ")
        print('''[D] - Depositar\n[R] - Retirar\n[S] - Salir''')
        opciones = input()
        if opciones == 'D':
            monto_dep = int(input('Monto a despositar: '))
            mi_cliente.depositar(monto_dep)
        elif opciones == 'R':
            monto_ret = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_ret)
        print(mi_cliente)
    print("Gracias por operar en Eche's Bank")





inicio()





























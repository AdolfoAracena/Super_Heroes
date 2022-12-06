class Human:
    def __init__(self, name, occupation, location):
        self._name = name
        self._occupation = occupation
        self._location = location

    def set_identity(self, name, occupation, location):
        self._name = name
        self._occupation = occupation
        self._location = location

    def print_info(self):
        return print("Nombre", name, "ocupacion", occupation, "Localizacion", location)


class SuperHero(Human):

    def __init__(self, name_super, origin, super_power, weakness):
        super().__init__(name, occupation, location)
        self.name_super = name_super
        self.origin = origin
        self.super_power = super_power
        self.weakness = weakness

    def get_heroes(self, name_super, origin, super_power):
        self._name_super = name_super
        self._origin = origin
        self._super_power = super_power
        self._weakness = weakness

    def print_super(self):
        return print("Nombre super heroe ", name_super, "Origen: ", origin, "Super poder: ", super_power, "Debilidad: ", weakness)


list = []
while True:
    print("Ingresar la informacion\n")
    print("1=Ciudadano")
    print("2=Super heroe")
    opcion = input("Ingrese Opción\n")

    name = input("Ingrese el nombre de la persona\n")
    occupation = input("Ocupacion de la persona\n")
    location = input("Localizacion de la persona\n")
    if (opcion == '1'):
        employee_1 = Human(name, occupation, location)
        employee_1.print_info()

    elif (opcion == '2'):
        name_super = input("Nombre de super heroe\n")
        origin = input("Origen\n")
        super_power = input("Super poder\n")
        weakness = input("debilidad\n")
        developer_1 = SuperHero(name_super, origin, super_power, weakness)
        developer_1.print_super()
    else:
        print("Ingrese una opcion correcta")

    if input("Desea continuar:").lower() == "no":
        print("Saldra del sistema")
        break

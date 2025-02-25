from modelos.carro import Carro
from modelos.moto import Moto

moto1 = Moto('Honda', 'Lead', 'Scooter')
moto2 = Moto('Honda', 'Elite', 'Scooter')
carro1 = Carro('GM', 'Classic', 4 )
carro2= Carro('Toyota', 'Etios', 2)

print(carro1.__str__())

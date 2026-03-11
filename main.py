from faker import Faker
import random

fake = Faker()

usuarios = {}

for i in range(1, 16):
    usuarios[i] = [
        fake.name(),
        fake.address(),
        fake.email(),
        fake.phone_number(),
    ]

for usuario in usuarios:
    name, address, email, phone_number = usuarios[usuario]
    print(f"Código: {usuario}")
    print(f"Nombre: {name}")
    print(f"Dirección: {address}")
    print(f"Email: {email}")
    print(f"Número de teléfono: {phone_number}")

winner = random.choice(range(1, 16))

print(f"O usuario chamado {usuarios[winner][0]} foi o afortunado!")

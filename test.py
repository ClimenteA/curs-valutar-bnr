import time
from src.cursvalutarbnr import Currency, ron_exchange_rate


start = time.perf_counter()

eur_to_ron = ron_exchange_rate(
    ammount=1,              # suma pe care vrei sa o convertesti la 'currency'
    currency=Currency.EUR,  # valuta (curency) in care vrei sa fie convertita suma specificata in 'ammount'
    date="2022-01-01"       # poti specifica si data in isoformat pentru care vrei sa fie convertita suma
)


print("eur_to_ron", eur_to_ron)
print("1. It took ", time.perf_counter() - start, " seconds!")


start = time.perf_counter()

eur_to_ron = ron_exchange_rate(
    ammount=1,              # suma pe care vrei sa o convertesti la 'currency'
    currency=Currency.EUR,  # valuta (curency) in care vrei sa fie convertita suma specificata in 'ammount'
    date="2022-01-01"       # poti specifica si data in isoformat pentru care vrei sa fie convertita suma
)


print("eur_to_ron", eur_to_ron)
print("2. It took ", time.perf_counter() - start, " seconds!")

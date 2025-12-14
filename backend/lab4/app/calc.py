def calc(forecast):
    price = 0

    tariffs = forecast["tariffs"]
    for tariff in tariffs:
        price += tariff['price'] * tariff['count'] * forecast["days"]

    return price
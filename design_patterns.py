# Iterator
class Radio:

    def __init__(self):
        # double underline make the variable private
        self.__stations = [
            {"frequencia": 89.1, "nome": "Rádio Rock"},
            {"frequencia": 92.5, "nome": "Sertaneja FM"},
            {"frequencia": 97.7, "nome": "Energia Pop"},
        ]
        self.__index = 0

    # Iterator accesses the values without exposing the entire content
    def next_station(self):
        """Retorna a próxima rádio e volta ao início quando chega ao fim."""
        estacao = self.__stations[self.__index]
        self.__index = (self.__index + 1) % len(self.__stations)
        return estacao


# Decorator adiciona um comportamento sem alterar o codigo da classe original
class LogRadioDecorator:

    def __init__(self, radio: Radio):
        self._radio = radio

    def next_station(self):
        estacao = self._radio.next_station()
        # Adiciona o comportamento extra diretamente aqui
        print(f"[SINTONIZANDO] -> {estacao['nome']}")
        return estacao


if __name__ == "__main__":
    my_radio = Radio()

    # Decoramos a rádio com a única classe necessária
    radio_decorado = LogRadioDecorator(my_radio)

    for _ in range(5):
        estacao = radio_decorado.next_station()
        print(f"Tocando: {estacao['nome']} em {estacao['frequencia']} MHz\n")
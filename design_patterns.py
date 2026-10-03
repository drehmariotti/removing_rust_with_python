from fastapi import FastAPI
import uvicorn

# ---------------------------------------------------------
# 1. Iterator
# ---------------------------------------------------------
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


# ---------------------------------------------------------
# 2. Decorator
# ---------------------------------------------------------
class LogRadioDecorator:

    def __init__(self, radio: Radio):
        self._radio = radio

    def next_station(self):
        estacao = self._radio.next_station()
        # Adiciona o comportamento extra diretamente aqui (aparece no terminal da API)
        print(f"[SINTONIZANDO VIA API] -> {estacao['nome']}")
        return estacao


# ---------------------------------------------------------
# 3. FastAPI App
# ---------------------------------------------------------
app = FastAPI(title="API do Rádio")

# Instância global: preserva o índice atual a cada chamada
my_radio = LogRadioDecorator(Radio())


@app.get("/")
def home():
    return {"mensagem": "API de Rádio ativa. Acesse /proxima para trocar de estação."}


@app.get("/proxima")
def proxima_estacao():
    # Executa o decorator que chama o next_station() do Radio
    estacao = my_radio.next_station()
    return {
        "status": "sucesso",
        "estacao": estacao
    }


# Execução do servidor local
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
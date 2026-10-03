from fastapi import FastAPI
import uvicorn

# ---------------------------------------------------------
# 1. Iterator (Sua Rádio Local)
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
# 2. Classe Externa Incompatível (Adaptee)
# ---------------------------------------------------------
class WebRadioService:
    """Simula um serviço/biblioteca externa com formato e métodos em inglês."""

    def __init__(self):
        self.streams = [
            {"freq_mhz": 105.3, "station_title": "BBC World Stream"},
            {"freq_mhz": 99.9, "station_title": "Jazz FM Web"},
        ]
        self.cursor = 0

    def get_next_stream(self):
        """Método com nome e estrutura de chaves diferentes!"""
        stream = self.streams[self.cursor]
        self.cursor = (self.cursor + 1) % len(self.streams)
        return stream


# ---------------------------------------------------------
# 3. Adapter
# ---------------------------------------------------------
class WebRadioAdapter:
    """Adapta o WebRadioService para funcionar como um Radio normal (next_station)."""

    def __init__(self, web_service: WebRadioService):
        self.web_service = web_service

    def next_station(self):
        # Obtém o dado no formato antigo/externo
        raw_stream = self.web_service.get_next_stream()
        
        # Traduz para o formato de dicionário esperado pelo nosso sistema
        return {
            "frequencia": raw_stream["freq_mhz"],
            "nome": raw_stream["station_title"]
        }


# ---------------------------------------------------------
# 4. Decorator
# ---------------------------------------------------------
class LogRadioDecorator:

    def __init__(self, radio):
        self._radio = radio

    def next_station(self):
        estacao = self._radio.next_station()
        # Adiciona o comportamento extra diretamente aqui
        print(f"[SINTONIZANDO VIA API] -> {estacao['nome']}")
        return estacao


# ---------------------------------------------------------
# 5. FastAPI App
# ---------------------------------------------------------
app = FastAPI(title="API do Rádio")

# Rádio Local (usando Iterator + Decorator)
my_local_radio = LogRadioDecorator(Radio())

# Rádio Web (usando Serviço Externo -> Adapter -> Decorator)
external_web_service = WebRadioService()
adapted_web_radio = WebRadioAdapter(external_web_service)
my_web_radio = LogRadioDecorator(adapted_web_radio)


@app.get("/")
def home():
    return {"mensagem": "API de Rádio ativa. Acesse /proxima ou /proxima-web."}


@app.get("/proxima")
def proxima_estacao_local():
    """Toca a próxima rádio local."""
    estacao = my_local_radio.next_station()
    return {
        "fonte": "Local",
        "status": "sucesso",
        "estacao": estacao
    }


@app.get("/proxima-web")
def proxima_estacao_web():
    """Toca a próxima rádio web usando o Adapter."""
    estacao = my_web_radio.next_station()
    return {
        "fonte": "Web (via Adapter)",
        "status": "sucesso",
        "estacao": estacao
    }


# Execução do servidor local
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
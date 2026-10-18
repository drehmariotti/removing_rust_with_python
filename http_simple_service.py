# Como executar:
# 1. Instale as dependências: pip install flask fastapi uvicorn
# 2. Para rodar o serviço Flask: python http_simple_service.py
# 3. Para acessar a rota principal: http://localhost:5000/
# 4. Para testar a predição do modelo: POST em http://localhost:5000/predict com JSON como {"features": [...]}
# 5. Para rodar o serviço FastAPI, execute a classe SimpleFastAPIService em seu próprio contexto.

import os
import pickle

from flask import Flask, request
from fastapi import FastAPI


class SimpleHTTPService:
    def __init__(self):
        self.app = Flask(__name__)
        self.model = None
        self._configure_routes()

    def _configure_routes(self):
        @self.app.route("/", methods=["GET"])
        def hello_world():
            return {"message": "Hello, World!"}, 200

        @self.app.route("/predict", methods=["POST"])
        def predict_online():
            if self.model is None:
                return {"error": "Modelo ainda não foi carregado. Chame load_model() primeiro."}, 400

            payload = request.get_json(silent=True) or {}
            try:
                prediction = self.predict(payload)
                return {"prediction": prediction}, 200
            except Exception as exc:
                return {"error": f"Erro na predição: {str(exc)}"}, 500

    def load_model(self, model_filename="model.pkl"):
        """Carrega um modelo pickle salvo no mesmo diretório deste arquivo."""
        model_path = os.path.join(os.path.dirname(__file__), model_filename)

        with open(model_path, "rb") as model_file:
            self.model = pickle.load(model_file)

        return self.model

    def predict(self, payload):
        """Executa a predição usando o modelo carregado."""
        if self.model is None:
            raise ValueError("Modelo não carregado. Primeiro execute load_model().")

        if isinstance(payload, dict) and "features" in payload:
            data = payload["features"]
        else:
            data = payload

        prediction = self.model.predict(data)
        return prediction.tolist() if hasattr(prediction, "tolist") else prediction

    def run(self, host="0.0.0.0", port=5000, debug=False):
        self.app.run(host=host, port=port, debug=debug)


class SimpleFastAPIService:
    def __init__(self):
        self.app = FastAPI(title="Simple FastAPI Service")
        self._configure_routes()

    def _configure_routes(self):
        @self.app.get("/")
        async def hello_world():
            return {"message": "Hello, World!"}

    def run(self, host="0.0.0.0", port=8000, debug=False):
        import uvicorn

        uvicorn.run(self.app, host=host, port=port, reload=debug)


if __name__ == "__main__":
    service = SimpleHTTPService()
    service.run()

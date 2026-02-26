from fastapi import FastAPI
from fastapi.testclient import TestClient


def create_app():
    app = FastAPI()

    @app.get("/health")
    def health():
        return {"ok": True}

    return app


def test_health():
    client = TestClient(create_app())
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"ok": True}

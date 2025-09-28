from flask import Flask, request, Response
import requests

app = Flask(__name__)

OLLAMA_API = "http://localhost:11434/api/generate"

@app.after_request
def add_cors_headers(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    resp.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
    return resp

@app.route("/api/generate", methods=["POST", "OPTIONS"])
def generate():
    if request.method == "OPTIONS":
        return Response(status=200)  # Handle preflight

    # Forward request to Ollama
    r = requests.post(OLLAMA_API, json=request.json, stream=True)

    def stream():
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                yield chunk

    return Response(stream(), content_type="application/json")

if __name__ == "__main__":
    app.run(port=3000)

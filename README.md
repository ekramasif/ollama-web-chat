## 🧠 Local ChatGPT Clone with Ollama

A modern ChatGPT-style web interface powered by Ollama and open-source LLMs like `llama3.2`.  
Chat with AI offline, directly on your machine.

---

## 🚀 Features

- ✅ Full ChatGPT-like UI (dark mode, sidebar, copy/regenerate buttons)
- ✅ Local LLMs with no internet required
- ✅ Markdown + code highlighting in chat responses
- ✅ Works with any Ollama model (e.g. llama3.2, mistral, codellama)

---

## 📦 Installation

### 1. Install Ollama

Ollama is required to run models locally.

- **Windows / Mac:**  
  Download from 👉 [https://ollama.ai/download](https://ollama.ai/download)

- **Linux:**  
  Run:
  ```sh
  curl -fsSL https://ollama.ai/install.sh | sh
  ```

After installation, check Ollama is running:
```sh
ollama --version
```

### 2. Download a Model

Pull a model directly:
```sh
ollama pull llama3.2
```

Other models:
```sh
ollama pull mistral
ollama pull codellama
ollama pull gemma
```

List installed models:
```sh
ollama list
```

### 3. Run Ollama Server

Ollama serves a local API at [http://localhost:11434](http://localhost:11434).  
Run this in one terminal:
```sh
ollama serve
```

### 4. Run the Chat Web UI

Open your HTML file (`ollama.html`) in a browser.

Or use a simple Python HTTP server:
```sh
python3 -m http.server 8000
```
Then visit 👉 [http://localhost:8000/ollama.html](http://localhost:8000/ollama.html)

---

## 🖥️ Usage

- Type your message in the input box and press **Send**
- The model will stream responses just like ChatGPT
- You can **Copy** or **Regenerate** messages

---

## 🔧 Customization

Change which model you use in `ollama.html`:

```js
body: JSON.stringify({
  model: "llama3.2",
  prompt: userInput
}),
```

Replace `"llama3.2"` with `"mistral"`, `"codellama"`, etc.

---

## 📚 Documentation

For more details, see the official Ollama docs:  
👉 [https://github.com/ollama/ollama](https://github.com/ollama/ollama)

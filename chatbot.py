import importlib

try:
    ollama = importlib.import_module("ollama")
except ModuleNotFoundError as exc:
    raise SystemExit("Required package 'ollama' is not installed. Install it with 'pip install ollama'.") from exc

MODEL = "qwen2.5-coder:7b"
history = []


def ensure_ollama_ready() -> None:
    try:
        ollama.list()
    except Exception as exc:
        raise RuntimeError(
            "Ollama is not reachable. Start the service with 'ollama serve' and make sure it is running."
        ) from exc


try:
    ensure_ollama_ready()
except RuntimeError as exc:
    raise SystemExit(str(exc)) from exc

print("Local chatbot - type 'quit' to exit")
while True:
    user = input("\nYou: ")
    if user.lower() == "quit":
        break

    history.append({"role": "user", "content": user})
    try:
        reply = ollama.chat(model=MODEL, messages=history)
    except Exception as exc:
        print(f"\nAI: I could not reach Ollama. Error: {exc}")
        print("Try running 'ollama serve' and ensure the model is installed with 'ollama pull qwen2.5-coder:7b'.")
        break

    text = reply["message"]["content"]
    history.append({"role": "assistant", "content": text})
    print(f"\nAI: {text}")
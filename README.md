# Nostr‑KeyGen

A tiny, interactive command‑line tool that lets you generate a Nostr key pair from any file you choose. It works on macOS, Linux and (with a few tweaks) Windows. The script is intentionally lightweight – no fancy GUI, just an easy‑to‑follow wizard run from your terminal.

## Features

- **Drag‑and‑drop friendly**: on macOS and Linux you can simply drop the file into the Terminal window.
- **Clear, step‑by‑step tutorial**: every run prints a short intro, an explanation, a quick demo, asks for your file and finishes with the key‑pair in *both* Nostr‑Bech32 and raw hex.
- **No external binaries** – it just uses the pure‑Python `ecdsa` and `bech32` packages.
- **Portable**: you can ship it as a single Python file or compile to a binary with tools such as PyInstaller.

## Install

### 1. Clone the repo
```bash
git clone https://github.com/btcforplebs/nostr-keygen.git
cd nostr-keygen
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install ecdsa bech32
```

### 4. Make it executable and optional symlink
```bash
chmod +x nostr-keygen
```

## Usage

Run the script directly from the project directory:
```bash
./nostr-keygen
```
or, if you added the symlink:
```bash
nostr-keygen
```
You’ll be guided through the following steps:

1. Welcome screen – press **Enter** to continue.
2. Tool overview – press **Enter** to continue.
3. Demo key generation using a temporary file – press **Enter** to continue.
4. Prompt for the path to your entropy file. You can drop a file into the terminal on macOS/Linux or type the absolute/relative path.
5. The script shows you the generated `nsec`, `npub`, and the hex representation of both keys.
6. Press **Enter** again, the terminal is cleared and the program exits.

## Example Output

```
🛠️  Welcome to Nostr‑KeyGen

This tool will:
- Pick any file as your entropy source
- Hash the file → 32‑byte seed
- Derive a secp256k1 key pair
- Print the Nostr `nsec`/`npub` and the raw hex values

💡 Demo (using a random file in /tmp)...
  Demo nsec: nsec1q4...
  Demo npub: npub1p8...
  Demo priv hex: 1f4c...
  Demo pub hex: 03a1...

📂 Enter the path to your entropy file: /Users/me/secret.txt

✅  Your new key pair:
    - nsec : nsec1q8...
    - npub : npub1p9...
    - priv hex : 7c2d...
    - pub hex  : 029b...

🧹 Cleaning up...
🚀 Done. Goodbye!
```

## FAQs

| Question | Answer |
|----------|--------|
| Why does it read *any* file as entropy? | Nostr requires a 32‑byte seed. Hashing a file guarantees a deterministic, pseudo‑random 32‑byte output irrespective of the file size or content. |
| Will it always produce the same key for the same file? | Yes – the seed is derived from a SHA‑256 hash of the file contents. |
| Can I use a password instead? | The current script accepts files only, but you could easily pipe a password string using `echo -n 'mypassword' > pwd.txt` first. |

## Contributing

Pull requests are welcome! Just make sure the code passes `flake8`/`black` and contains an updated README.

## License

MIT – see [LICENSE](LICENSE).


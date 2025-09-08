# README.md
# nostr-keygen

A tiny command‑line utility written in Python that generates an Nostr **npub** (public key) and **nsec** (private key) pair from a single file that you drop into the terminal.

## How it works

1. **Entropy** – The contents of the file you provide are read in binary mode.
2. **Hash** – The data is hashed with SHA‑256 to produce a 32‑byte seed.
3. **Key generation** – The seed is fed to the secp256k1 curve to create an ECDSA private key.
4. **Bech32 encoding** – The private key is encoded as `nsec`; the compressed public key is encoded as `npub`.

The utility is intentionally lightweight; it has no external configuration and works on any platform with Python 3.8+.

## Installation

```bash
# Clone the repo
git clone https://github.com/yourname/nostr-keygen.git
cd nostr-keygen

# Create a virtualenv and install deps
python3 -m venv venv
source venv/bin/activate
pip install -e .  # installs the program and its deps
```

After that you can run it with:

```bash
# Replace file.txt with the path to any file you want to use as entropy
nostr-keygen file.txt
```

## Using drag‑and‑drop in the terminal

On macOS (and most X11 terminals) you can simply drag a file into the terminal prompt. The terminal translates that to the file’s full path. For example:

```
$ nostr-keygen <dragged file>
```

This will invoke the program using the path of the dropped file.

## License

MIT

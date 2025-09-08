# nostr-keygen

A tiny command‑line utility written in Python that generates an Nostr **npub** (public key) and **nsec** (private key) pair from a single file that you drop into the terminal.

> **NOTE:** The instructions below work on **macOS** and **Linux**. If you’re on Windows you’ll need a compatible terminal (e.g. WSL, Git‑Bash, or PowerShell with Python).

---

## 🚀 Run

```bash
# Drop any file into the terminal prompt!
# macOS (most terminals) and many Linux terminals allow drag‑and‑drop.

nostr-keygen <filepath>
```

> The terminal prompt you see (``$`` on macOS, ``username@host:~$`` on Linux) accepts drag‑and‑drop of any file. The script will read that file path and produce key strings.

---

### 📄 Quick test

```bash
# Create a tiny dummy file
printf "random entropy" > /tmp/dummy.bin

# Run the program
nostr-keygen /tmp/dummy.bin
```

You should see two lines outputted: an `nsec` string and an `npub` string.

## 🛠️ Installation

### 1️⃣ Install Python

- **macOS**: Use Homebrew
  ```bash
  brew install python@3.12
  ```
  (If you already have Python, skip this step.)

- **Linux (Ubuntu / Debian‑based)**:
  ```bash
  sudo apt-get update
  sudo apt-get install python3 python3-venv
  ```
  (Other distros may use `yum`, `dnf`, or your package manager of choice.)

- **Linux (Arch)**:
  ```bash
  sudo pacman -S python
  ```

> **Tip** – On macOS the `python3` binary is typically symlinked to `python`, but on many Linux systems you’ll need `python3` explicitly.

### 2️⃣ Clone the repo

```bash
git clone https://github.com/your‑github‑handle/nostr-keygen.git
cd nostr-keygen
```

### 3️⃣ Create a virtual‑environment (recommended)

```bash
python3 -m venv .venv          # create a venv in the repo directory
source .venv/bin/activate      # activate it (both on macOS and Linux)
```

> The virtual‑environment isolates third‑party libraries (`ecdsa`, `bech32`, etc.) from the system‑wide Python installation, ensuring that installing or updating them won’t accidentally break other projects. It also guarantees that anyone who checks out the repo can recreate the exact same runtime environment.

### 4️⃣ Install the tool in editable mode (development) or normally

- **Editable (work on the code as you edit it)**
  ```bash
  pip install -e .
  ```

- **Normal installation**
  ```bash
  pip install .
  ```

Both forms install the console‑script `nostr‑keygen` into `./.venv/bin`.

## 🚫 Key‑string safety

> Keep your `nsec` secret in a secure, offline location. Anyone with that string can sign Nostr events or spend Nostr‑based funds.


## 🔧 How the code works (quick dive)

```python
# main.py
import argparse, hashlib
from ecdsa import SigningKey, SECP256k1
from bech32 import bech32_encode, convertbits

NSEC_PREFIX, NPUB_PREFIX = "nsec", "npub"

def _to_bech32(data: bytes, hrp: str) -> str:
    five_bits = convertbits(list(data), 8, 5, True)
    return bech32_encode(hrp, five_bits)

# … (rest unchanged) …
```

### Why the key‑gen algorithm matters

1. **Read file in binary** – We need raw entropy; reading as text would truncate or encode the file in an unexpected way. Binary mode is the most faithful representation of the file’s content.
2. **SHA‑256 hash** – Provides a *deterministic* 32‑byte seed from any file. Different inputs yield different seeds, and the same input always yields the same seed.
3. **Create a secp256k1 signing key** – The curve used by Nostr (and Bitcoin) for ECDSA. The secret key is derived directly from the seed bytes.
4. **Bech32 encoding** – Nostr keys are human‑readable Bech32 strings prefixed with `nsec` or `npub`. `_to_bech32` converts 8‑bit byte streams to 5‑bit groups and encodes them.
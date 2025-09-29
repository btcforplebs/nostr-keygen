# nostr-keygen

🔐 A minimal CLI tool to generate Nostr-compatible key pairs using file-based entropy.

## ✨ Features

- Uses the contents of any file as a secure entropy source
- Outputs:
  - `nsec` (private key)
  - `npub` (public key)
- Drag and drop file support on macOS/Linux Terminal

---

## 🚀 Install

##

### 1. Clone & Set Up

```bash
git clone https://github.com/btcforplebs/nostr-keygen.git
cd nostr-keygen
chmod +x nostr-keygen
sudo ln -s "$PWD/nostr-keygen" /usr/local/bin/nostr-keygen

# Activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages globally
pip3 install ecdsa bech32

Now just run:
nostr-keygen

Returns
🔐 Drop a file to use as entropy (or enter path):

Drop file to use as entropy: /Users/username/Desktop/file.txt



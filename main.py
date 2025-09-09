#!/usr/bin/env python3
"""Generate a fresh Nostr key (npub/nsec) using a file as entropy source.

Usage:
  nostr-keygen <path-to-file>

The file is read in binary mode and its bytes are hashed with SHA‑256 to
produce the 32‑byte seed which is then used to generate a secp256k1
private key. The private key is hex‑encoded as an nsec, and the
corresponding public key is converted to a Bech32 npub. The example
uses the official Nostr prefix "nsec"/
"""

import argparse
import hashlib
import os
import sys

from ecdsa import SigningKey, SECP256k1
from bech32 import bech32_encode, convertbits

# Constants for Nostr bech32 encoding
NSEC_PREFIX = "nsec"
NPUB_PREFIX = "npub"

# convertbits helper adapted from bech32 library; using provided function for clarity

def _to_bech32(data: bytes, hrp: str) -> str:
    """Encode raw bytes into a Bech32 string with the given human‑readable part."""
    # Convert 8‑bit bytes to 5‑bit groups
    five_bits = convertbits(list(data), 8, 5, True)
    if five_bits is None:
        raise ValueError("Error converting data to 5‑bit groups")
    return bech32_encode(hrp, five_bits)


def _entropy_to_pri_key(entropy: bytes) -> SigningKey:
    """Return an ECDSA SECP256k1 private key derived from entropy."""
    # Use SHA‑256 of the provided entropy for deterministic key generation
    seed = hashlib.sha256(entropy).digest()
    return SigningKey.from_string(seed, curve=SECP256k1)


def generate_key_from_file(file_path: str) -> (str, str):
    """Return (nsec, npub) for the key derived from the file content."""
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "rb") as f:
        data = f.read()

    sk = _entropy_to_pri_key(data)
    vk = sk.get_verifying_key()
    # Private key bytes
    private_bytes = sk.to_string()
    # Public key bytes, compressed (33 bytes)
    public_bytes = vk.to_string("compressed")
    nsec = _to_bech32(private_bytes, NSEC_PREFIX)
    npub = _to_bech32(public_bytes, NPUB_PREFIX)
    return nsec, npub



def main():
    parser = argparse.ArgumentParser(description="Generate Nostr key pair from file entropy")
    parser.add_argument("file", help="Path to file used as entropy source")
    args = parser.parse_args()

    try:
        nsec, npub = generate_key_from_file(args.file)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    print("nsec:", nsec)
    print("npub:", npub)


if __name__ == "__main__":
    main()

"""
Key Management module for UIM Mock Agent.

This module provides functionality for generating, storing, and retrieving
cryptographic key pairs used for signing and verifying UIM protocol messages.
"""
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_key_pair(service_url):
    """
    Generate a new RSA key pair for a given service URL.

    Args:
        service_url: The URL of the service to generate keys for

    Returns:
        None: The keys are saved to disk

    Raises:
        Exception: If there's an error generating or saving the keys
    """
    try:
        # Generate a new RSA key pair
        private_key = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )
        public_key = private_key.public_key()

        # Create the directory structure
        key_dir = os.path.join(
            "keys", service_url.replace("://", "_").replace(":", "_")
        )
        os.makedirs(key_dir, exist_ok=True)

        # Serialize and save the private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption(),
        )
        with open(os.path.join(key_dir, "private_key.pem"), "wb") as f:
            f.write(private_pem)

        # Serialize and save the public key
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        )
        with open(os.path.join(key_dir, "public_key.pem"), "wb") as f:
            f.write(public_pem)
        print(f"Key pair generated and saved for service URL: {service_url}")
    except Exception as e:
        print(f"Error generating key pair for service URL {service_url}: {e}")
        raise


def get_key_pair(service_url):
    """
    Get the RSA key pair for a given service URL.

    If the key pair doesn't exist, it will be generated.

    Args:
        service_url: The URL of the service to get keys for

    Returns:
        tuple: (private_key, public_key) - The loaded RSA key pair

    Raises:
        Exception: If there's an error loading or generating the keys
    """
    try:
        key_dir = os.path.join(
            "keys", service_url.replace("://", "_").replace(":", "_")
        )
        private_key_path = os.path.join(key_dir, "private_key.pem")
        public_key_path = os.path.join(key_dir, "public_key.pem")

        if not os.path.exists(private_key_path) or not os.path.exists(public_key_path):
            print(
                f"Key pair not found for service URL {service_url}, "
                f"generating new key pair."
            )
            generate_key_pair(service_url)

        with open(private_key_path, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(), password=None, backend=default_backend()
            )

        with open(public_key_path, "rb") as f:
            public_key = serialization.load_pem_public_key(
                f.read(), backend=default_backend()
            )

        print(f"Key pair loaded for service URL: {service_url}")
        return private_key, public_key
    except Exception as e:
        print(f"Error loading key pair for service URL {service_url}: {e}")
        raise

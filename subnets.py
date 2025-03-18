"""
generate_subnets.py

This script prompts for a student's email address and returns three
distinct private IP subnets (LAN A, LAN B, and an Interconnection)
deterministically derived from the last two hex digits of a SHA-256 hash.

Run this code exactly ONCE with your official email. Use the subnets
it provides in your Cisco Packet Tracer coursework.
"""

import hashlib

def generate_subnets(student_email: str):
    """
    Returns a tuple of three subnets (LAN A, LAN B, Interconnection)
    based on the student's email. The subnets are guaranteed to be
    deterministic for each unique email and valid for typical home-lab use:
        LAN A: 10.<H>.0.0/24
        LAN B: 172.16.<H>.0/24
        Interconnection: 192.168.<H>.0/30

    Where <H> is an integer derived from the last two hex chars
    of the SHA-256 hash of the email address, in range [0..255].
    """
    # Ensure consistent handling of whitespace
    email_bytes = student_email.strip().encode('utf-8')

    # Compute SHA-256 of the email
    hash_hex = hashlib.sha256(email_bytes).hexdigest()

    # Get the last two hex digits
    last_two_hex = hash_hex[-2:]

    # Convert them from hex to an integer [0..255]
    H = int(last_two_hex, 16)

    # Define subnets
    lan_a = f"10.{H}.0.0/24"
    lan_b = f"172.16.{H}.0/24"
    interconnection = f"192.168.{H}.0/30"

    return (lan_a, lan_b, interconnection)

if __name__ == "__main__":
    email = input("Enter your email: ").strip()
    la, lb, inter = generate_subnets(email)
    print(f"LAN A subnet:          {la}")
    print(f"LAN B subnet:          {lb}")
    print(f"Interconnection subnet: {inter}")
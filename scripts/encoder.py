import base64
import json
import os

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

# Параметры из кода игры
KEY = b"panzer_w"
IV = bytes([0x04, 0x02, 0x02, 0x03, 0x05, 0x02, 0x04, 0x04])


def encode():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("--- ENCODER Panzer War ---")
    input_path = "/Users/seronez/trash/py_json_decoder/scripts/achievements_decoded.json"  # In this line, specify the path to the file that needs to be encrypted!!!

    if not os.path.exists(input_path):
        print("error: file not found!")
        return

    try:
        # reading JSON
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # simple write like unity
        json_string = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
        json_bytes = json_string.encode("utf-8")

        # encode DES
        cipher = DES.new(KEY, DES.MODE_CBC, IV)
        padded_data = pad(json_bytes, DES.block_size)
        encrypted_bytes = cipher.encrypt(padded_data)

        # package to Base64
        final_base64 = base64.b64encode(encrypted_bytes)

        output_path = os.path.join(script_dir, "achievements.json")
        with open(output_path, "wb") as f:
            f.write(final_base64)

        print("-" * 30)
        print(f"succesfully! encrypted file: {output_path}")
        print("Now you can copy this file in to game folder.")

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    encode()

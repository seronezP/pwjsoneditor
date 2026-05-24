import base64
import json
import os

from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

# parameters from game
KEY = b"panzer_w"  # first 8 bytes from "panzer_war_lock"
IV = bytes([0x04, 0x02, 0x02, 0x03, 0x05, 0x02, 0x04, 0x04])


def decode():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("--- decoder Panzer War ---")
    input_path = (
        ""  # In this line, specify the path to the file that çneeds to be decrypted!!!
    )

    if not os.path.exists(input_path):
        print("error: file not find!")
        return

    try:
        with open(input_path, "rb") as f:
            raw_data = f.read()

        # try to decode now
        try:
            encrypted_data = base64.b64decode(raw_data)
        except:
            encrypted_data = raw_data

        # encode DES
        cipher = DES.new(KEY, DES.MODE_CBC, IV)
        decrypted_raw = cipher.decrypt(encrypted_data)

        # un - Padding and convert to text
        decrypted_text = unpad(decrypted_raw, DES.block_size).decode("utf-8")

        # change for simply to reading and editing JSON
        json_obj = json.loads(decrypted_text)
        output_path = os.path.join(script_dir, "achievements_decoded.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_obj, f, indent=4, ensure_ascii=False)

        print("-" * 30)
        print(f"succesfully! decrypted file: {output_path}")
        print("now you can change it.")

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    decode()

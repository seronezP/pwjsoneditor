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

    print("--- ЭНКОДЕР Panzer War ---")
    input_path = ""

    if not os.path.exists(input_path):
        print("Ошибка: Файл не найден!")
        return

    try:
        # Читаем JSON
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Компактная запись (без пробелов), как делает движок Unity
        json_string = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
        json_bytes = json_string.encode("utf-8")

        # Шифрование DES
        cipher = DES.new(KEY, DES.MODE_CBC, IV)
        padded_data = pad(json_bytes, DES.block_size)
        encrypted_bytes = cipher.encrypt(padded_data)

        # Упаковка в Base64
        final_base64 = base64.b64encode(encrypted_bytes)

        output_path = os.path.join(script_dir, "achievements.json")
        with open(output_path, "wb") as f:
            f.write(final_base64)

        print("-" * 30)
        print(f"ГОТОВО! Зашифрованный файл: {output_path}")
        print("Можете копировать его обратно в папку игры.")

    except Exception as e:
        print(f"ОШИБКА: {e}")


if __name__ == "__main__":
    encode()

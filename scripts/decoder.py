import base64
import json
import os

from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad

# Параметры из кода игры
KEY = b"panzer_w"  # Первые 8 байт от "panzer_war_lock"
IV = bytes([0x04, 0x02, 0x02, 0x03, 0x05, 0x02, 0x04, 0x04])


def decode():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("--- ДЕКОДЕР Panzer War ---")
    input_path = ""

    if not os.path.exists(input_path):
        print("Ошибка: Файл не найден!")
        return

    try:
        with open(input_path, "rb") as f:
            raw_data = f.read()

        # Пробуем декодировать Base64. Если файл бинарный — используем как есть.
        try:
            encrypted_data = base64.b64decode(raw_data)
        except:
            encrypted_data = raw_data

        # Расшифровка DES
        cipher = DES.new(KEY, DES.MODE_CBC, IV)
        decrypted_raw = cipher.decrypt(encrypted_data)

        # Снятие Padding (набивки) и конвертация в текст
        decrypted_text = unpad(decrypted_raw, DES.block_size).decode("utf-8")

        # Превращаем в красивый JSON для редактирования
        json_obj = json.loads(decrypted_text)
        output_path = os.path.join(script_dir, "achievements_decoded.json")

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_obj, f, indent=4, ensure_ascii=False)

        print("-" * 30)
        print(f"ГОТОВО! Расшифрованный файл: {output_path}")
        print("Теперь вы можете открыть его и изменить данные.")

    except Exception as e:
        print(f"ОШИБКА: {e}")


if __name__ == "__main__":
    decode()

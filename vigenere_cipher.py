def detect_language(text: str) -> str:
    ru_chars = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    en_chars = set('abcdefghijklmnopqrstuvwxyz')
    
    text_lower = text.lower()
    has_ru = any(char in ru_chars for char in text_lower)
    has_en = any(char in en_chars for char in text_lower)
    
    if has_ru and not has_en:
        return 'ru'
    elif has_en and not has_ru:
        return 'en'
    return 'ru' 

def process_text(text: str, lang: str):
    """Обрабатывает текст, сохраняя не-буквенные символы и регистр"""
    result = []
    letters = []
    
    if lang == 'ru':
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    else:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    
    for char in text:
        if char in alphabet:
            letters.append(char)
            result.append({'char': char, 'original': char, 'is_letter': True})
        else:
            result.append({'char': char, 'original': char, 'is_letter': False})
    
    return result, letters

def restore_text(processed_text, processed_letters):
    result = []
    letter_index = 0
    
    for item in processed_text:
        if item['is_letter']:
            original_char = item['original']
            if original_char.isupper():
                result.append(processed_letters[letter_index].upper())
            else:
                result.append(processed_letters[letter_index].lower())
            letter_index += 1
        else:
            result.append(item['char'])
    
    return ''.join(result)

def vigenere_encrypt(plaintext: str, key: str) -> str:
    lang = detect_language(plaintext + key)
    processed_text, letters_to_encrypt = process_text(plaintext, lang)
    key_letters = [c for c in key if c.isalpha()]
    
    if not letters_to_encrypt:
        return plaintext
    if not key_letters:
        raise ValueError("Ключ должен содержать хотя бы одну букву")
    
    encrypted_letters = []
    key_len = len(key_letters)
    
    if lang == 'ru':
        alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        alphabet_size = 33
    else:
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet_size = 26
    
    for i, char in enumerate(letters_to_encrypt):
        key_char = key_letters[i % key_len]
        
        if char.isupper():
            alphabet = alphabet_upper
            base = ord('А') if lang == 'ru' else ord('A')
        else:
            alphabet = alphabet_lower
            base = ord('а') if lang == 'ru' else ord('a')
        
        if lang == 'ru' and char.lower() == 'ё':
            char = 'е' if char.islower() else 'Е'
        
        char_index = alphabet.find(char)
        if char_index == -1:
            continue
            
        key_char = key_char.upper() if char.isupper() else key_char.lower()
        key_index = alphabet.find(key_char)
        if key_index == -1:
            continue
            
        encrypted_index = (char_index + key_index) % alphabet_size
        encrypted_char = alphabet[encrypted_index]
        encrypted_letters.append(encrypted_char)
    
    return restore_text(processed_text, encrypted_letters)

def vigenere_decrypt(ciphertext: str, key: str) -> str:
    lang = detect_language(ciphertext + key)
    processed_text, letters_to_decrypt = process_text(ciphertext, lang)
    key_letters = [c for c in key if c.isalpha()]
    
    if not letters_to_decrypt:
        return ciphertext
    if not key_letters:
        raise ValueError("Ключ должен содержать хотя бы одну букву")
    
    decrypted_letters = []
    key_len = len(key_letters)
    if lang == 'ru':
        alphabet_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        alphabet_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        alphabet_size = 33
    else:
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet_size = 26
    
    for i, char in enumerate(letters_to_decrypt):
        key_char = key_letters[i % key_len]
        
        if char.isupper():
            alphabet = alphabet_upper
            base = ord('А') if lang == 'ru' else ord('A')
        else:
            alphabet = alphabet_lower
            base = ord('а') if lang == 'ru' else ord('a')
        
        char_index = alphabet.find(char)
        if char_index == -1:
            continue
            
        key_char = key_char.upper() if char.isupper() else key_char.lower()
        key_index = alphabet.find(key_char)
        if key_index == -1:
            continue
            
        decrypted_index = (char_index - key_index) % alphabet_size
        decrypted_char = alphabet[decrypted_index]
        decrypted_letters.append(decrypted_char)
    
    return restore_text(processed_text, decrypted_letters)

def main_menu():
    print("Шифр Виженера")
    
    while True:
        print("\n1. Зашифровать текст")
        print("2. Расшифровать текст")
        print("3. Выход")
        
        choice = input("Выберите действие (1-3): ").strip()
        
        if choice == '1':
            print("\n--- Шифрование ---")
            text = input("Введите текст для шифрования: ")
            key = input("Введите ключ: ")
            
            try:
                encrypted = vigenere_encrypt(text, key)
                print("\nРезультат шифрования:")
                print(encrypted)
            except ValueError as e:
                print(f"\nОшибка: {e}")
        
        elif choice == '2':
            print("\n--- Дешифрование ---")
            text = input("Введите текст для расшифровки: ")
            key = input("Введите ключ: ")
            
            try:
                decrypted = vigenere_decrypt(text, key)
                print("\nРезультат расшифровки:")
                print(decrypted)
            except ValueError as e:
                print(f"\nОшибка: {e}")
        
        elif choice == '3':
            print("\nВыход из программы...")
            break
        
        else:
            print("Неверный выбор. Пожалуйста, введите 1, 2 или 3.")

if __name__ == "__main__":
    main_menu()
import unittest
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

class TestVigenereCipher(unittest.TestCase):
    def test_russian_encrypt(self):
        test_cases = [
            ("ПРИВЕТ", "КЛЮЧ", "ЪЬЖЩПЮ"),
            ("КОД", "ШИФР", "ГЧШ"),
            ("ТЕСТ", "ДЛИННЫЙКЛЮЧ", "ЦРЪА"),
            ("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", "А", "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
            ("ЗАЩИТАИНФОРМАЦИИ", "ПАРОЛЬ", "ЧАЙЧЮЬШНЕЭЬИПЦЩЧ")
        ]
        
        for text, key, expected in test_cases:
            with self.subTest(text=text, key=key):
                result = vigenere_encrypt(text, key)
                self.assertEqual(result, expected)

    def test_russian_decrypt(self):
        test_cases = [
            ("ЪЬЖЩПЮ", "КЛЮЧ", "ПРИВЕТ"),
            ("ГЧШ", "ШИФР", "КОД"),
            ("ЦРЪА", "ДЛИННЫЙКЛЮЧ", "ТЕСТ"),
            ("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", "А", "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"),
            ("ЧАЙЧЮЬШНЕЭЬИПЦЩЧ", "ПАРОЛЬ", "ЗАЩИТАИНФОРМАЦИИ")
        ]
        
        for ciphertext, key, expected in test_cases:
            with self.subTest(ciphertext=ciphertext, key=key):
                result = vigenere_decrypt(ciphertext, key)
                self.assertEqual(result, expected)

    def test_english_encrypt(self):
        test_cases = [
            ("ATTACK", "LEMON", "LXFOPV"),
            ("HELLO", "KEY", "RIJVS"),
            ("CRYPTO", "SECRET", "UVAGXH"),
            ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "A", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            ("TESTING", "LONGKEY", "ESFZSRE")
        ]
        
        for text, key, expected in test_cases:
            with self.subTest(text=text, key=key):
                result = vigenere_encrypt(text, key)
                self.assertEqual(result, expected)

    def test_english_decrypt(self):
        test_cases = [
            ("LXFOPV", "LEMON", "ATTACK"),
            ("RIJVS", "KEY", "HELLO"),
            ("UVAGXH", "SECRET", "CRYPTO"),
            ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "A", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            ("ESFZSRE", "LONGKEY", "TESTING")
        ]
        
        for ciphertext, key, expected in test_cases:
            with self.subTest(ciphertext=ciphertext, key=key):
                result = vigenere_decrypt(ciphertext, key)
                self.assertEqual(result, expected)

    def test_preserve_formatting(self):
        test_cases = [
            ("Привет, мир!", "ключ", "Ъьжщпю, каы!"),
            ("Hello, World!", "secret", "Zincs, Pgvnu!"),
            ("Тест: 100%", "пароль", "Вевб: 100%"),
            ("ABCdef", "key", "KFAnid"),
            ("12345", "key", "12345")
        ]
        
        for text, key, expected in test_cases:
            with self.subTest(text=text, key=key):
                result = vigenere_encrypt(text, key)
                self.assertEqual(result, expected)

    def test_error_handling(self):
        self.assertEqual(vigenere_encrypt("123!@#", "key"), "123!@#")
        self.assertEqual(vigenere_decrypt("123!@#", "key"), "123!@#")
        
        with self.assertRaises(ValueError):
            vigenere_encrypt("Текст", "")
            
        with self.assertRaises(ValueError):
            vigenere_decrypt("Текст", "")

if __name__ == "__main__":
    unittest.main()
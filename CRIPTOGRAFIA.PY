from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import base64

# Função para criptografar
def encrypt_aes(data, key):
    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
    iv = base64.b64encode(cipher.iv).decode('utf-8')
    ct = base64.b64encode(ct_bytes).decode('utf-8')
    return iv, ct

# Dados a serem criptografados
data_name = "Arthur Alexandre"
data_course = "Engenharia de Software"
data_expectation = "Tudo por Hobby"

# Chave secreta (deve ter 16, 24 ou 32 bytes)
key = "minhachavesecreta"  # Chave de 16 caracteres (128 bits)

# Criptografando cada parte
iv_name, encrypted_name = encrypt_aes(data_name, key)
iv_course, encrypted_course = encrypt_aes(data_course, key)
iv_expectation, encrypted_expectation = encrypt_aes(data_expectation, key)

# Resultados criptografados
print("Nome Criptografado:", encrypted_name)
print("Curso Criptografado:", encrypted_course)
print("Expectativa Criptografada:", encrypted_expectation)


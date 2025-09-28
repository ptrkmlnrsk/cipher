from cipher_decipher import CipherData
from encrypt_decrypt import InputToEncrypt

def main():

    cipher_data = CipherData(text = 'test1', rot_type = 'encrypt', status = 'encrypted')
    print(cipher_data.text)
    encrypt1 = InputToEncrypt(cipher_data)
    print(encrypt1.encrypt_data('blablalba'))

if __name__ == '__main__':
    main()
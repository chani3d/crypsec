# Yepzhapp Chat App 📱💬 | SJCG - ISC 2023 | 103.2 - Cryptographie et sécurité - Chat app project

### Features 🔒

- Sending messages using ISCP (ISC Protocol) ✅
- Receiving messages using ISCP ✅
- Sending pictures using ISCP ✅
- Receiving pictures using ISCP ❌
- Shift ✅
- Shift Vigenere ✅
- RSA ✅
- Linear Congruential Generator of Knuth & Lew ✅
- Diffie-Hellman key exchange ❌
- Hashing ✅

## How to use it 🤔
1. Go to *TCP_Client.py*, inside the method *server_connection* that is in the class *TCPClient* change the port number to whatever you want to use. The default one is 6000.
2. Compile *Main.py* to run the app. The following interface will pop up :
<img width="991" alt="1" src="https://user-images.githubusercontent.com/106392221/236731714-655b950b-4917-4bf8-978e-7a54ce8d4e0b.png">

To the left we have a "main type box" with a text box to show the messages and to the right we have the different encryption methods.

3. To send a message to the server write something in the main type box and click the send button or press enter. To encrypt a message write something in the main type box but don't send it.
4. To encrpyt or decrypt using **shift** or **vigenere shift** write a key in the box *Enter key* then write the text to encrypt or decrypt in the main type box. The encrypted or decrpyted text will appear in the desired section (the right of the GUI). If it doesn't work, write a space after the text in the main type box and then errase it to refresh it.
5. To obtain a public and private using **RSA**, write two prime numbers in the *P and Q boxes* and a seed in the *Seed box*. The keys should appear in the *Public and Private key boxes*.
6. Once we have the public and private keys, write the desired message to encrypt in the main type box to encrypt using **RSA**.

**Note** : The **hash** section will change every time the main type box is modified.

## Technical info 🔧

- All the files of the app are located in *Crypsec_project/src*
- All the files located inside *Crypsec_project/src/test* aren't relevant to the project.
- Inside *ISC_protocol.py* there's the ISCP and all the encryption methods.
- Diffie-Hellman key exchange is in the code but not implemented in the GUI.

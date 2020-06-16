# image-encryption
Encrypt your image! Protect your personal image with this small project =)
Feel free to make any changes!

to import the module to your project:
```
from encrypt_image import *
```

to encrypt the image:
```
encrypt(imagefilename, outputcodefilename, outputkeyfilename)
```

to decrypt the encrypted crazy amount of numbers:
```
decrypt(inputcodefilename, inputkeyfilename, outputimagefilename)
```

**encrypt** the image required you to give 3 parameters, which are the imagefilename, outputcodefilename, and outputkeyfilename.
  - **imagefilename**: the image file that you want to encrypt, can be any type of image (eg. jpg, png, etc.)
  - **outputcodefilenam**e: the output code file (this code doesn't mean the code we wrote usually, it means something like secret code). This file contain the most important things of the image, which is the crazy amount of numbers
  - **outputkeyfilename**: the output key file (don't throw this because the image won't be decrypted without this file)
  
**decrypt** the image required you to give 3 parameters, which are the inputcodefilename, inputkeyfilename, and outputimagefilename.
  - **inputcodefilename**: the code file that you created when encrypt the image.
  - **inputkeyfilename**: the key file that you created when you encrypt the image.
  - **outputimagefilename**: can be any name, just make sure that the extension of the image file is same as your image when encrypted.

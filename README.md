# Image hiding using watermark Steganography
INFORMATION HIDING USING INVISIBLE WATERMARK 

This code covers the idea of hiding an information which is an image🖼️ into ➡️ another image 🖼️ using Steganography way by the libraries 

From Python(for encoding and decoding):
* OpenCV 📚
* numpy 🔢
 
The GUI:
* TKinter 🇹🇰

You can clone the project and either 
* Run it from the cmd using the command "python 'projectname'.py" 📟
* Put it on vs code and install tkinter library on your pc using "pip install tk" and run ▶️


**This is the view of the image encryption 🔐 program**

![Screenshot 2023-10-23 052511](https://github.com/Kidzantso/Image-hiding-using-watermark--Steganography-/assets/116034195/36ded716-ce25-4204-a2e8-849bc59ddd53)

 

**This is the view of the image decryption 🔓 program**

![Screenshot 2023-10-23 052447](https://github.com/Kidzantso/Image-hiding-using-watermark--Steganography-/assets/116034195/8edb484f-591b-47a2-a9c6-49ffe689a2df)


# Methodology

* Encryption 

First you choose 2 pictures for example i will use these 2(The first picture must be bigger ⏫ in scale than the second picture):

**First image 🖼️**

![download](https://github.com/Kidzantso/Image-hiding-using-watermark--Steganography-/assets/116034195/fe71d815-ab61-40fd-a2b9-d36ed6e9d1b4)

**Second image 🖼️**

![download1](https://github.com/Kidzantso/Image-hiding-using-watermark--Steganography-/assets/116034195/5fcfb992-3c5a-4abe-bed5-af163d3926bf)



Then you press encrypt and the code start running 

1. Let img1[i][j][l] and img2[i][j][l] be some pixel value of each image.

2. Let v1 be 8 bits binary representation of img1[i][j][l] and v2 be 8 bits binary representation of img2[i][j][l].

3. Therefore, v3=v1[:4]+v2[:4], where, v3 is the first 4 bits of v1 and v2.

4. Then we assign img1[i][j][l] to v3.

* Decryption 

And for decrypting the image you choose the encrypted image you got as a a result 

**Encrypted image 🔐🖼️**

![enc](https://github.com/Kidzantso/Image-hiding-using-watermark--Steganography-/assets/116034195/545f2941-a78f-493e-ab8e-cb0c81631f2f)



And when yoy press decrypt you choose a folder to save 💾 the 2 original photos in it (with extra random colors in the smaller image) and the process runs the opposite way

1. Let img[i][j][l] be the pixel value of the image.
   
2. Let v1 be 8 bits binary representation of img[i][j][l].
   
3. Let v2=v1[:4]+4 random bits and v3=v1[4:]+4 random bits.
   
4. Then we assign img1[i][j][l] to v2 and img2[i][j][l] to v3.

# References
Here are some of my references 📖

* https://www.geeksforgeeks.org/image-steganography-using-opencv-in-python/

* Pria Bharti and Roopali Soni. A new approach of data hiding in images using cryptography and
steganography. International Journal of Computer Applications, 58(18), 2012.

* Nilanjan Dey, Anamitra Bardhan Roy, and Sayantan Dey. A novel approach of color image hiding
using rgb color planes and dwt. arXiv preprint arXiv:1208.0803, 2012.

* Nagham Hamid, Abid Yahya, R Badlishah Ahmad, and Osamah M Al-Qershi. Image steganography
techniques: an overview. International Journal of Computer Science and Security (IJCSS), 6(3):
168–187, 2012.

* Rosziati Ibrahim and Teoh Suk Kuan. Steganography algorithm to hide secret message inside an
image. arXiv preprint arXiv:1112.2809, 2011.

* Arvind Kumar and Km Pooja. Steganography-a data hiding technique. International Journal of
Computer Applications, 9(7):19–23, 2010

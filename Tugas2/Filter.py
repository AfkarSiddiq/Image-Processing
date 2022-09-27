from PIL import ImageEnhance, Image

def Brightness(path_gambar, level):
    '''
    Method untuk Meningkatkan kecerahan gambar. ini 
    dicapai dengan meningkatkan nilai RGB setiap pixel 
    sedikit ke arah putih.

    :param path_gambar: letak gambar dalam direktori
    :param level : tingkat kecerahan tipe: num
    :output : gambar setelah dan sebelum proses Filtering
    '''
    image = Image.open(path_gambar)
    converter = ImageEnhance.Brightness(image)
    image_after = converter.enhance(level)
    image_after.show()
    image.show()

def Sharpen(path_gambar, level):
    '''
    Mempertajam gambar meningkatkan tampilan detail 
    dalam gambar. Ini dilakukan dengan melebih-lebihkan 
    perbedaan kecerahan di sepanjang tepi.

    :param path_gambar, string: letak gambar dalam direktori
    :param level : tingkat ketajaman type: num
    :output : gambar setelah dan sebelum proses Filtering
    '''
    image = Image.open(path_gambar)
    converter = ImageEnhance.Sharpness(image)
    image_after = converter.enhance(level)
    image_after.show()
    image.show()

def Contrast(path_gambar, level):
    '''
    Kontras adalah pemisahan antara area paling gelap 
    dan paling terang dari suatu gambar. Untuk meningkatkan 
    kontras, dilakukan dengan mengambil beberapa piksel dari tengah dan 
    mendorongnya ke tepi. Penurunan kontras menarik piksel di tepi ke arah tengah. 
    Dengan meningkatkan kontras, atrinya secara de facto juga meningkatkan ketajaman.

    :param path_gambar, string: letak gambar dalam direktori
    :param level : tingkat contrast type: num
    :output : gambar setelah dan sebelum proses Filtering 
    '''
    image = Image.open(path_gambar)
    converter = ImageEnhance.Contrast(image)
    image_after = converter.enhance(level)
    image_after.show()
    image.show()

def Saturation(path_gambar, level):
    '''
    Saturasi warna adalah intensitas dan kemurnian warna seperti 
    yang ditampilkan dalam sebuah gambar. Semakin tinggi saturasi warna, 
    semakin jelas dan intens warnanya. Semakin rendah saturasi warna, 
    semakin dekat ke abu-abu murni.

    :param path_gambar, string: letak gambar dalam direktori
    :param level : tingkat saturasi warna type: num
    :output : gambar setelah dan sebelum proses Filtering
    '''
    image = Image.open(path_gambar)
    converter = ImageEnhance.Color(image)
    image_after = converter.enhance(level)
    image_after.show()
    image.show()
    
# ini test 
Saturation('foto/badoots.jpeg', 4)

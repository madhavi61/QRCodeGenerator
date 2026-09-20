import qrcode

if __name__ == "__main__":

    url = input("Enter the URL you want to create a QR code for: ")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    file_name = input("Enter a name for the QR code file: ")

    img.save(file_name + ".png")

    print("QR code was created and saved as " + file_name + ".png")
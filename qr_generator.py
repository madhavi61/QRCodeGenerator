import qrcode

# Run the QR code generator
if __name__ == "__main__":

    # Ask the user to enter the website URL
    url = input("Enter the URL you want to create a QR code for: ")

    # Set up the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    # Add the URL and generate the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Ask the user for a file name
    file_name = input("Enter a name for the QR code file: ")

    # Save the QR code as a PNG file
    img.save(file_name + ".png")

    print("QR code was created and saved as " + file_name + ".png")
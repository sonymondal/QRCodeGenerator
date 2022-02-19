import qrcode 

code = qrcode.QRCode(
    version=10,
    box_size=5,
    border=3,
)

message = input("Enter message or paste link : ")
name = input("Enter a name for your file : ")
extensions = input("Enter a extenstins (jpg / png) : ")

data = f"{message}"

code.add_data(data)
code.make(fit=True)

image = code.make_image(fill_color="red", back_color="white")

# image.save(f"{name}.{extensions}")
image.show()

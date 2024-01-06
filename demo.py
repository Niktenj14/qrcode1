import qrcode
qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20,border=1)
qr.add_data("Name: Tenjarla Nikita \n USN: 1BI21ET047 \n Branch: ETE")
qr.make(fit=True)
img = qr.make_image(fill_color= "black" , back_color= "white" )
img.save("advanced.png")

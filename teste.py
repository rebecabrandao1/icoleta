import jwt
import datetime
import random
import qrcode

weight_random = weight_random = round(random.uniform(0.0, 15.0), 2) 
payload = {
    "weight": weight_random,
    "point_id": 1,
    "iat": 1710497928
}

secret_key = "açDlkfAd4lfadfKja4dklakdF-(*&#@jadnfja)afd3254745412"

token = jwt.encode(payload, secret_key, algorithm="HS256")
print(token)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data(token)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

# Salvar o QR Code como uma imagem
img.save("token_qr.png")

print("QR Code gerado com sucesso e salvo como 'token_qr.png'.")

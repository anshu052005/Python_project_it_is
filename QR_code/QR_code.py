import qrcode as qr 
# making qr code
image = qr.make("https://www.youtube.com/watch?v=awYJWalvK_0")
image.save("sourav_joshi.png")
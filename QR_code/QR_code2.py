import qrcode
from PIL import ImageChops

qr = qrcode.QRCode(
    version=1 ,
    error_correction = qrcode.constants.ERROR_CORRECT_H ,
    box_size = 10 ,
    border = 4 ,
)

qr.add_data("https://github.com/anshu052005?tab=repositories")
qr.make(fit=True)

image = qr.make_image(fill_color="black", back_color="pink")

image.save("anshu_github_qr.png")


# # qrcode library ko import kar rahe hain.
# # Ye library Python mein QR Code generate karne ke liye use hoti hai.
# # Iske andar QRCode naam ka class hai jisse hum customized QR bana sakte hain.

# import qrcode


# # Pillow(PIL) ek image processing library hai.
# # ImageChops images ko compare ya manipulate karne ke kaam aata hai.
# #
# # Lekin IMPORTANT:
# # Is code mein ImageChops ka kahin bhi use nahi hua.
# # Matlab ye import unnecessary hai.
# # Is line ko hata bhi doge to code bilkul same chalega.

# from PIL import ImageChops


# # -------------------------------------------------------------
# # QRCode object create kar rahe hain.
# #
# # Class = Blueprint
# # Object = Real instance
# #
# # qrcode.QRCode() ek QR Code object banata hai jisme hum
# # QR ke saare settings define karte hain.
# # -------------------------------------------------------------

# qr = qrcode.QRCode(

#     # ---------------------------------------------------------
#     # version
#     #
#     # QR Code kitna bada hoga.
#     #
#     # Version 1 = 21 x 21 boxes
#     #
#     # Version 2 = 25 x 25
#     #
#     # Version 3 = 29 x 29
#     #
#     # ...
#     #
#     # Maximum Version = 40
#     #
#     # Version jitni badhegi
#     # utna zyada data store kar paoge.
#     #
#     # Agar data version 1 se bada hua to fit=True
#     # automatically version increase kar dega.
#     # ---------------------------------------------------------

#     version=1,


#     # ---------------------------------------------------------
#     # Error Correction
#     #
#     # QR Code ki sabse powerful feature.
#     #
#     # Agar QR ka kuch part phat jaye,
#     # scratch ho jaye,
#     # ya uspe logo laga do,
#     #
#     # tab bhi scanner QR ko read kar sakta hai.
#     #
#     # ERROR_CORRECT_L
#     # lagbhag 7% damage tolerate karta hai.
#     #
#     # ERROR_CORRECT_M
#     # lagbhag 15%
#     #
#     # ERROR_CORRECT_Q
#     # lagbhag 25%
#     #
#     # ERROR_CORRECT_H
#     # lagbhag 30%
#     #
#     # H sabse safest option hai.
#     #
#     # Isi wajah se log custom QR Codes
#     # (logo wale QR) mein mostly H use karte hain.
#     # ---------------------------------------------------------

#     error_correction=qrcode.constants.ERROR_CORRECT_H,


#     # ---------------------------------------------------------
#     # box_size
#     #
#     # QR Code ke har ek square ka pixel size.
#     #
#     # box_size=10
#     #
#     # matlab
#     #
#     # har black ya white box
#     # 10 x 10 pixels ka hoga.
#     #
#     # Agar
#     #
#     # box_size=20
#     #
#     # to QR aur bada banega.
#     # ---------------------------------------------------------

#     box_size=10,


#     # ---------------------------------------------------------
#     # border
#     #
#     # QR Code ke around white space.
#     #
#     # Scanner ko QR detect karne ke liye
#     # ye white border bahut important hota hai.
#     #
#     # Minimum recommended = 4
#     #
#     # Isliye mostly examples mein border=4 hota hai.
#     # ---------------------------------------------------------

#     border=4,
# )



# # -------------------------------------------------------------
# # QR ke andar data add kar rahe hain.
# #
# # Ye URL ho sakta hai.
# #
# # Text ho sakta hai.
# #
# # Number ho sakta hai.
# #
# # WiFi password ho sakta hai.
# #
# # Email
# #
# # Contact
# #
# # Location
# #
# # Kuch bhi.
# # -------------------------------------------------------------

# qr.add_data("https://github.com/anshu052005?tab=repositories")



# # -------------------------------------------------------------
# # QR generate karo.
# #
# # fit=True ka matlab
# #
# # Agar data version 1 mein fit nahi hua
# #
# # to automatically version bada do.
# #
# # Agar fit=False hota
# #
# # aur data bada hota
# #
# # to error aa sakta tha.
# # -------------------------------------------------------------

# qr.make(fit=True)



# # -------------------------------------------------------------
# # Ab QR ko image mein convert kar rahe hain.
# #
# # make_image() image object return karta hai.
# #
# # fill_color
# # = QR ke black boxes ka color.
# #
# # back_color
# # = Background color.
# #
# # Hum black ki jagah blue
# # red
# # green
# # purple
# #
# # kuch bhi de sakte hain.
# # -------------------------------------------------------------

# image = qr.make_image(
#     fill_color="black",
#     back_color="pink"
# )



# # -------------------------------------------------------------
# # Image ko disk mein save kar rahe hain.
# #
# # Ye current folder mein
# #
# # anshu_github_qr.png
# #
# # naam ki file bana dega.
# # -------------------------------------------------------------

# image.save("anshu_github_qr.png")
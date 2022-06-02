#Generate qr-code

import qrcode

data = 'hello'
img =  qrcode.make(data)
img.save('D:/documents/test/img/test.png')

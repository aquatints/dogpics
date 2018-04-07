import pyimgur

CLIENT_ID = 'd88ae1ac1e85343'

q = pyimgur.Imgur(CLIENT_ID)
image = q.get_image('5NR01Pc')

print(image.link)

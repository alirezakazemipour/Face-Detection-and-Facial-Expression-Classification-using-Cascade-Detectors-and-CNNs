from PIL import Image
import PIL
import glob
import cv2

i=1
for j in range(1,7):

  fnames=glob.glob("/home/alireza/Documents/cv-final-project/CroppedYale/yaleB0"+str(j)+"/file-*.pgm")
  fnames.sort()
  print(len(fnames))


  for fname in fnames:
    print(fname[0:-3])
    im=Image.open(fname)
    im.convert('RGB')
    im.save("/home/alireza/Documents/cv-final-project/positiveSamples/"+str(i)+".jpg")
    i+=1

for j in range(11,40):

  fnames=glob.glob("/home/alireza/Documents/cv-final-project/CroppedYale/yaleB"+str(j)+"/file-*.pgm")
  fnames.sort()
  print(len(fnames))


  for fname in fnames:
    print(fname[0:-3])
    im=Image.open(fname)
    im.convert('RGB')
    im.save("/home/alireza/Documents/cv-final-project/positiveSamples/"+str(i)+".jpg")
    i+=1
#
# print(i)
#
# fnames=glob.glob("/home/alireza/Documents/cv-final-project/yalefaces/file-*.gif")
# fnames.sort()
# print(len(fnames))
#
# for fname in fnames:
#     print(fname[0:-3])
#     im=Image.open(fname)
#     im.convert('RGB')
#     im=im.resize( (168,192), PIL.Image.ANTIALIAS )
#     im.save("/home/alireza/Documents/cv-final-project/positiveSamples/"+str(i)+".jpg")
#     print(im.size)
#     i+=1
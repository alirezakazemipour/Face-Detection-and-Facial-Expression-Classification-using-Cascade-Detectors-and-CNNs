from PIL import Image
import PIL
import glob
import cv2

i=1

fnames=glob.glob("/home/alireza/Documents/cv-final-project/download_neg_samples/*.jpg")
fnames.sort()
print(len(fnames))


for fname in fnames:
  print(fname[0:-3])
  try:
      im=Image.open(fname)
      im=im.convert('LA')
      im=im.resize((168,192),Image.ANTIALIAS)
      im.save("/home/alireza/Documents/cv-final-project/negativeSamples/"+str(i)+".png")
      i+=1
  except:
      pass

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
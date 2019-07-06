from PIL import Image
import glob

fnames=glob.glob("/home/alireza/Documents/cv-final-project/CroppedYale/yaleB02/file-*.pgm")
fnames.sort()
print(len(fnames))

i=231

for fname in fnames:
    print(fname[0:-3])
    im=Image.open(fname)
    im.convert('RGB')
    im.save("/home/alireza/Documents/cv-final-project/positiveSamples/"+str(i)+".jpg")
    i+=1

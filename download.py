import urllib.request


f=open("/home/alireza/imgList.txt", "r")
contents = f.readlines()

i=0
for x in contents:
    print(x)
    try:
        urllib.request.urlretrieve(x,"/home/alireza/PycharmProjects/download_neg_samples/"+str(i)+".jpg")
    except:
        pass
    i=i+1

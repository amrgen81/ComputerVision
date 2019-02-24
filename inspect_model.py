
from keras.applications import VGG16
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--include_top",type=int,default=1)
args = vars(ap.parse_args())

print("[INFO] loading model")
#rmember how we are getting boolean value here...

model = VGG16(weights="imagenet",include_top=args["include_top"]>0)

for (i,layer) in enumerate(model.layers):

    ## printing the layers of model , o that we can  slice off properly
    print("[INFO] {}\t{}".format(i,layer.__class__.__name__))



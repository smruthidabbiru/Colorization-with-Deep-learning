from PIL import Image
import os
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Resize all colorful imgs to 256*256 for training")
    parser.add_argument("-d",
                        "--dir",
                        required=True,
                        default="train\\",
                        type=str,
                        help="The directory includes all jpg images")
    args = parser.parse_args()
    return args

def doit(x):
    a=Image.open(x)
    if a.getbands()!=('R','G','B'):
        os.remove(x)
        return
    a.resize((256,256),Image.BICUBIC).save(x)
    return

args=parse_args()
jpgs = []
flist = os.listdir(args.dir)
full_flist = [os.path.join(args.dir,x) for x in flist]
for x in full_flist:
    doit(x)
    print("Done "+str(x))
print('done')

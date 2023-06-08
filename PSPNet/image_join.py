import os

import cv2
import numpy as np
from PIL import Image


def join(dirpath1, dirpath2, resultpath):
    img_names1 = os.listdir(dirpath1)
    img_names2 = os.listdir(dirpath2)

    for img_name1 in img_names1:
        for img_name2 in img_names2:
            if img_name1 == img_name2:
                imgpath1 = os.path.join(dirpath1, img_name1)
                imgpath2 = os.path.join(dirpath2, img_name2)
                img1 = cv2.imread(imgpath1).astype('float64')/255
                img2 = cv2.imread(imgpath2).astype('float64')/255
                imgs = np.hstack([img1, img2])
                #cv2.imshow("compare", imgs)
                #cv2.waitKey()
                rpath = os.path.join(resultpath, img_name1)
                cv2.imwrite(rpath, imgs*255)

    print("Finished !\n")
    return 0



if __name__ == '__main__':
    join('./img', './img_out', './img_joint')


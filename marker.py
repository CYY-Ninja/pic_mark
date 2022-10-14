import cv2
from watermarker.marker import add_mark
import numpy as np
import matplotlib.pyplot as plt


def pic_marker_by_cv2(path, text):
    path = path.replace('\\', '/')
    img = cv2.imread(path)
    RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR TO RGB
    print('RGB_img.shape[0]:', RGB_img.shape[0])   # width
    print('RGB_img.shape[1]', RGB_img.shape[1])  # height

    # zero array
    # dimension: width * height
    # data length 8 bits
    blank_img = np.zeros(shape=(RGB_img.shape[0], RGB_img.shape[1], 3), dtype=np.uint8)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(blank_img, text=text, org=(30, 100),
                fontFace=font, fontScale=2,
                color=(255, 0, 0), thickness=10, lineType=cv2.LINE_4)

    blended = cv2.addWeighted(src1=RGB_img, alpha=0.7,
                              src2=blank_img, beta=1, gamma=2)
    plt.imshow(blended)
    plt.show()


def pic_marker_by_filestools(path, out_path, text):
    add_mark(file=path, out=out_path,
             mark=text, color=(255, 0, 0),
             opacity=0.2, angle=30, space=30)


if __name__ == '__main__':
    # pic_marker_by_cv2(input('添加水印的图片路径:\n'), 'DC industry')
    pic_marker_by_filestools(input('添加水印的图片路径:\n'), input('保存路径：'), 'DC industry')

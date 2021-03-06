#剪裁训练和验证数据集
import json
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
#train_json = json.load(open('D:/data/SVHN/val/mchar_val.json'))   #需要裁剪的图片的标签

# 数据标注处理
def parse_json(d):
   arr = np.array([
       d['top'], d['height'], d['left'], d['width'], d['label']
   ])
   arr = arr.astype(int)
   return arr


def list_sum(a, b):
   c = []
   for i in range(len(a)):
      c.append(a[i] + b[i])
   return c

# def hebing(d):
#
#    return arr
qushu_dir = 'D:/data/SVHN/test/yolo3/qushu/'

imagedir = 'D:/data/SVHN/test/mchar_test_a' #需要裁剪的图片路径
for item in os.listdir(imagedir):
    if item.endswith('.png'):
       #print(item)
       new_dict = {}
       image = imagedir + '/' + item
       img = cv2.imread(image)
       # biaoqian = {'height': [62, 63, 69], 'label': [6, 3, 9], 'left': [6, 43, 74], 'top': [16, 22, 21], 'width': [41, 30, 41]}
       #biaoqian = {'height': [69], 'label': [1], 'left': [6], 'top': [16], 'width': [112]}
       #arr = parse_json(biaoqian)
       #print(train_json[item])
       #print(train_json[item]['height'])
       txt_num = item
       txt_num = txt_num.replace('.png','')
       txt_dir = qushu_dir + txt_num + '.txt'
       f = open(txt_dir)  # 如果你的x.txt文件不在python的路径下,那么必须用绝对路径
       l1 = f.readlines()

       l1 = [x.split(' ') for x in l1]
       l1 = [[x[0], x[1], x[2],x[3], x[4], x[5].replace('/n', '')] for x in l1]  # 这里去掉了每行的'/n'符号
       # print(l1)
       l2 = [[int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), int(x[5])] for x in l1]
       #print(l2)

       label = []
       left = []
       top = []
       width = []
       height = []
       for i in range(len(l2)):
           label.append(l2[i][0])
           left.append(l2[i][2])
           top.append(l2[i][3])
           width.append(l2[i][4])
           height.append(l2[i][5])
       # print(label)
       # print(left)
       # print(top)
       # print(width)
       # print(height)
       if len(left) != 0:
           new_dict['height'] = [max(list_sum(top, height)) - min(top)]
           new_dict['label'] = [1]
           new_dict['left'] = [max(0, min(left))]
           new_dict['top'] = [max(0, min(top))]
           new_dict['width'] = [max(list_sum(width, left)) - min(left)]
           arr = parse_json(new_dict)

       #print(new_dict)

       # print(item)
       # print(arr.shape[1])
       # print(arr)
       #plt.figure(figsize=(10, 10))
       #plt.subplot(1, arr.shape[1] + 1, 1)
       # plt.imshow(img)
       # plt.show()
       plt.xticks([]);plt.yticks([])

       # for idx in range(arr.shape[1]):
       for idx in range(1):
          #plt.subplot(1, arr.shape[1] + 1, idx + 2)
          if len(left) == 0:
              item = item.replace('.png', '')
              cropdir = "D:/data/SVHN/test/crop_test/" + item  # 存储剪裁图片的路径
              #print(cropdir)
              cv2.imwrite(cropdir + '.png',img)
          else:
              test = img[arr[0, idx]:arr[0, idx] + arr[1, idx], arr[2, idx]:arr[2, idx] + arr[3, idx]]
              # plt.imshow(test)
              # plt.show()
              # plt.savefig()
              item = item.replace('.png', '')
              cropdir = "D:/data/SVHN/test/crop_test/" + item  # 存储剪裁图片的路径
              #print(cropdir)
              cv2.imwrite(cropdir + '.png',test)
              # plt.title(arr[4, idx])
              # print(arr[4, idx])
              plt.xticks([]);
              plt.yticks([])









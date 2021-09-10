# -*- coding:utf-8 -*-
import os

from PIL import Image


def blend_two_images(f1, f2):
    img1 = Image.open(f1)
    img1 = img1.convert('RGBA')
    img2 = Image.open(f2)
    img2 = img2.convert('RGBA')
    img = Image.blend(img1, img2, 0.1)
    img.show()
    img.save("tmp.png")
    return


def getFileList(dir, Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)

    return Filelist


# TODO:four figs
f1 = 'tmp.png'
filelist = []
filelist = getFileList('img_01', filelist, ext='png')
for file in filelist:
    if 'A' in file:
        blend_two_images(f1, file)

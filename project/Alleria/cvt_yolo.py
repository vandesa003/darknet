"""
convert wheat data to yolo format.

Created On 27th Jul, 2020
Author: bohang.li
"""
import os
import pandas as pd
import argparse
from tqdm import tqdm
from glob import glob
import numpy as np


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-csv", "--csv_file", type=str,
        required=True, help="train.csv file path"
        )
    parser.add_argument(
        "-img", "--image_path", type=str,
        required=True, help="train images path"
        )
    return parser.parse_args()


if __name__ == "__main__":
    args = parser()
    train_set = pd.read_csv(args.csv_file)
    [os.remove(x) for x in glob(os.path.join(args.image_path, "*.txt"))]
    for item in tqdm(train_set.values):
        raw_w = int(item[1])
        raw_h = int(item[2])
        bbox = eval(item[3])
        x_center = np.float32(bbox[0] + bbox[2]/2)
        y_center = np.float32(bbox[1] + bbox[3]/2)
        norm_x = np.float32(x_center / raw_w)
        norm_y = np.float32(y_center / raw_h)
        norm_w = np.float32(bbox[2] / raw_w)
        norm_h = np.float32(bbox[3] / raw_h)
        with open(os.path.join(args.image_path, item[0]+".txt"), "a+") as f:
            f.write("0 {x:.4f} {y:.4f} {w:.4f} {h:.4f}\n".format(x=norm_x, y=norm_y, w=norm_w, h=norm_h))

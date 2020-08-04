"""
generate train.txt for yolo training.

Created On 27th Jul, 2020
Author: bohang.li
"""
import os
import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-img", "--image_path", type=str,
        required=True, help="train images path"
        )
    parser.add_argument(
        "-name", "--filename", type=str,
        required=True, help="txt filename, eg. train.txt / valid.txt"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parser()
    cur_dir = os.path.split(os.path.realpath(__file__))[0]
    if os.path.isfile(os.path.join(cur_dir, "data/{}".format(args.filename))):
        os.remove(os.path.join(cur_dir, "data/{}".format(args.filename)))
    for i in os.listdir(args.image_path):
        if i.endswith(".jpg"):
            with open(os.path.join(cur_dir, "data/{}".format(args.filename)), "a+") as f:
                f.write(os.path.join(args.image_path, i)+"\n")

import argparse
import glob
from pathlib import Path

import mayavi.mlab as mlab
import numpy as np
import torch

from pcdet.config import cfg, cfg_from_yaml_file
from visual_utils import visualize_utils as V

def parse_config():
    parser = argparse.ArgumentParser(description='arg parser')
    # parser.add_argument('--cfg_file', type=str, default='cfgs/kitti_models/second.yaml',
    #                     help='specify the config for demo')
    parser.add_argument('--data_path', type=str, default='000008.bin',
                        help='specify the point cloud data file or directory')
    # parser.add_argument('--ckpt', type=str, default=None, help='specify the pretrained model')
    # parser.add_argument('--ext', type=str, default='.bin', help='specify the extension of your point cloud data file')

    args = parser.parse_args()

    cfg_from_yaml_file(args.cfg_file, cfg)

    return args, cfg


# def save(pred):
#     with open('结果存放.txt', 'w') as file_handle:  # .txt可以不自己新建,代码会自动新建
#         for fp in pred:
#             file_handle.write(fp)  # 写入
#             file_handle.write('\n')  # 有时放在循环里面需要自动转行，不然会覆盖上一条数据
#     file.close()


def main():

    pointcloud = np.fromfile(str("000008.bin"), dtype=np.float32, count=-1).reshape([-1, 4])
    print(pointcloud.shape)
    x = pointcloud[:, 0]  # x position of point
    y = pointcloud[:, 1]  # y position of point
    z = pointcloud[:, 2]  # z position of point
    r = pointcloud[:, 3]  # reflectance value of point
    d = np.sqrt(x ** 2 + y ** 2)  # Map Distance from sensor

    vals = 'height'
    if vals == "height":
        col = z
    else:
        col = d

    fig = mlab.figure(bgcolor=(0, 0, 0), size=(640, 500))

    mlab.points3d(x, y, z,
                  col,  # Values used for Color
                  mode="point",
                  colormap='spectral',  # 'bone', 'copper', 'gnuplot'
                  # color=(0, 1, 0),   # Used a fixed (r,g,b) instead
                  figure=fig,
                  )

    x = np.linspace(5, 5, 50)
    y = np.linspace(0, 0, 50)
    z = np.linspace(0, 5, 50)
    mlab.plot3d(x, y, z)

    pred_dicts = torch.load('data.pth', map_location='cpu')
    print(f"pred_dicts:{pred_dicts}")
    V.draw_scenes(
        points=pointcloud, ref_boxes=pred_dicts[0]['pred_boxes'],
        ref_scores=pred_dicts[0]['pred_scores'], ref_labels=pred_dicts[0]['pred_labels']
    )
    mlab.show(stop=True)


if __name__ == '__main__':
    main()
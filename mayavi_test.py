import numpy as np
import mayavi.mlab as mlab
import torch
from visual_utils import visualize_utils as V

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
mlab.show()

pred_dicts = torch.load('data.pth', 'rb')
# V.draw_scenes(
#     points=data_dict['points'][:, 1:], ref_boxes=pred_dicts[0]['pred_boxes'],
#     ref_scores=pred_dicts[0]['pred_scores'], ref_labels=pred_dicts[0]['pred_labels']
#             )
mlab.show(stop=True)

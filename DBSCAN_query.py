import sklearn.cluster as sc

from open3d_usage import *

file_number = 1  # len(filename)

pcd = open3d.geometry.PointCloud()

path = 'D:\\Ghostear\\OpenPCDet\\data\\kitti\\training\\velodyne\\000000.bin'
print(path)
example = read_bin_velodyne(path)
# example_test = read_bin_velodyne(path)
#print(len(example_test[:, 0]))
    # print(f"len(example):{len(example)}")

# clustering = sc.dbscan(eps=0.5, min_samples=5).fit(example_test)
# print(f"len(clustering):{clustering}")
# # From numpy to Open3D
# pcd.points = open3d.utility.Vector3dVector(example)
# open3d.visualization.draw_geometries([pcd])
# open3d.io.write_image('/disk7/lhy/OpenPCDet/data/003.jpg', pcd)

# X1, y1 = make_circles(n_samples=5000, factor=0.6, noise=0.05)
# X2, y2 = make_blobs(n_samples=1000, n_features=2, centers=[[1.2, 1.2]], cluster_std=[[.1]], random_state=9)

# X = np.r_[X1, X2]
# plt.scatter(X[:, 0], X[:, 1], marker='o')
# plt.show()
#
# y_pred = sc.DBSCAN(eps=0.1, min_samples=10).fit_predict(X)
# plt.scatter(X[:, 0], X[:, 1], c=y_pred)
# plt.show()

y2_pred = sc.DBSCAN(eps=0.3, min_samples=10).fit_predict(example)
# plt.scatter(example[:, 0], example[:, 1], c=y_pred)
# plt.show()
vis(example, y2_pred)
# ax = plt.figure().add_subplot(111, projection = '3d')
# ax.scatter(example[:, 0], example[:, 1], example[:, 2], c = y2_pred, marker = '^') #点为红色形
# ax.set_xlabel('X Label')
# ax.set_ylabel('Y Label')
# ax.set_zlabel('Z Label')
# plt.show()
# ax = plt.figure().add_subplot(111, projection='3d')
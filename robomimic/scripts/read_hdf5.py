import h5py  #导入工具包  
import numpy as np  
# 读取HDF5文件中的所有数据集
def traverse_datasets(hdf_file):
    def h5py_dataset_iterator(g, prefix=''):
        for key in g.keys():
            item = g[key]
            path = '{}/{}'.format(prefix, key)
            if isinstance(item, h5py.Dataset): # test for dataset
                yield (path, item)
            elif isinstance(item, h5py.Group): # test for group (go down)
                yield from h5py_dataset_iterator(item, path)

    with h5py.File(hdf_file, 'r') as f:
        for (path, dset) in h5py_dataset_iterator(f):
            print(path, dset)

    return None

# 传入路径即可
traverse_datasets('/root/autodl-tmp/ROBOMIMIC_/robomimic/datasets/lift/ph/abs_image.hdf5')

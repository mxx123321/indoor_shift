import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
import h5py
import numpy as np
from torch.utils.data import random_split
    
path1 ='/root/mxx/indoor/SNR10.mat'
path2 ='/root/mxx/indoor/SNR20.mat'
path3 ='/root/mxx/indoor/SNR50.mat'
data1 = h5py.File(path1,mode='r')
data2 = h5py.File(path2,mode='r')
data3 = h5py.File(path3,mode='r')
    
    
class Dataset_SNR10(Dataset):
    def __init__(self):
        super().__init__()
        # 使用sin函数返回10000个时间序列,如果不自己构造数据，就使用numpy,pandas等读取自己的数据为x即可。
        # 以下数据组织这块既可以放在init方法里，也可以放在getitem方法里
        self.x = data1["features"]
        self.y = data1['labels']["position"]
        self.src, self.trg = [], []
        for i in range(4816):
            self.src.append(self.x[i])
            self.trg.append(self.y[i][:3])

    def __getitem__(self, index):
        return self.src[index], self.trg[index]

    def __len__(self):
        return len(self.src)
    
class Dataset_SNR20(Dataset):
    def __init__(self):
        super().__init__()
        # 使用sin函数返回10000个时间序列,如果不自己构造数据，就使用numpy,pandas等读取自己的数据为x即可。
        # 以下数据组织这块既可以放在init方法里，也可以放在getitem方法里
        self.x = data2["features"]
        self.y = data2['labels']["position"]
        self.src, self.trg = [], []
        for i in range(4816):
            self.src.append(self.x[i])
            self.trg.append(self.y[i][:3])

    def __getitem__(self, index):
        return self.src[index], self.trg[index]

    def __len__(self):
        return len(self.src)
    
class Dataset_SNR50(Dataset):
    def __init__(self):
        super().__init__()
        # 使用sin函数返回10000个时间序列,如果不自己构造数据，就使用numpy,pandas等读取自己的数据为x即可。
        # 以下数据组织这块既可以放在init方法里，也可以放在getitem方法里
        self.x = data3["features"]
        self.y = data3['labels']["position"]
        self.src, self.trg = [], []
        for i in range(4816):
            self.src.append(self.x[i])
            self.trg.append(self.y[i][:3])

    def __getitem__(self, index):
        return self.src[index], self.trg[index]

    def __len__(self):
        return len(self.src)
    
    
    
    
    

    
    
    
    
    
    
    
# class SourceDataset(Dataset):
#     def __init__(self):
#         self.data   =  torch.randn(1000,5,16,193)
#         self.label  =  torch.randn(1000,3)
        

#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, idx):
#         data = self.data[idx]
#         label = self.label[idx]

#         return data, label
# class TargetDataset(Dataset):
#     def __init__(self):
#         self.data   =  torch.randn(1000,5,16,193)


#     def __len__(self):
#         return len(self.data)

#     def __getitem__(self, idx):
#         data = self.data[idx]
        

#         return data  








# from torch.utils.data import DataLoader
# # dataloader = DataLoader(SourceDataset(),10)
## TODO: define the convolutional neural network architecture

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
# can use the below import should you choose to initialize the weights of your Net
import torch.nn.init as I


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        
        ## TODO: Define all the layers of this CNN, the only requirements are:
        ## 1. This network takes in a square (same width and height), grayscale image as input
        ## 2. It ends with a linear layer that represents the keypoints
        ## it's suggested that you make this last layer output 136 values, 2 for each of the 68 keypoint (x, y) pairs
        
        # As an example, you've been given a convolutional layer, which you may (but don't have to) change:
        # 1 input image channel (grayscale), 32 output channels/feature maps, 5x5 square convolution kernel
        self.conv1 = nn.Conv2d(1, 32, 3)
        self.maxpool1 = nn.MaxPool2d(3)
        
        self.conv2 = nn.Conv2d(32, 64, 3)
        self.maxpool2 = nn.MaxPool2d(3)
        self.dropout2 = nn.Dropout2d(p = .1)

        self.conv3 = nn.Conv2d(64, 256, 3)
        self.maxpool3 = nn.MaxPool2d(3)
        self.dropout3 = nn.Dropout2d(p = .2)
        
        self.conv4 = nn.Conv2d(256, 512, 3)
        #self.maxpool4 = nn.MaxPool2d(5)
        self.dropout4 = nn.Dropout2d(p = .3)
        
        self.linear1 = nn.Linear(12800, 4096)
        self.dropout5 = nn.Dropout(p = .3)
        self.linear2 = nn.Linear(4096, 8192)
        self.dropout6 = nn.Dropout(p = .3)
        
        self.linear3 = nn.Linear(8192, 136)
        
        ## Note that among the layers to add, consider including:
        # maxpooling layers, multiple conv layers, fully-connected layers, and other layers (such as dropout or batch normalization) to avoid overfitting
        

        
    def forward(self, x):
        ## TODO: Define the feedforward behavior of this model
        ## x is the input image and, as an example, here you may choose to include a pool/conv step:
        ## x = self.pool(F.relu(self.conv1(x)))
        
        x = self.maxpool1(F.relu(self.conv1(x)))
        x = self.dropout2(self.maxpool2(F.relu(self.conv2(x))))
        x = self.dropout3(self.maxpool3(F.relu(self.conv3(x))))
        x = self.dropout4(F.relu(self.conv4(x)))
        
        x = self.dropout5(F.relu(self.linear1(x.view(x.size(0), -1))))
        x = self.dropout6(F.relu(self.linear2(x)))
        x = self.linear3(x)
        
        
        # a modified x, having gone through all the layers of your model, should be returned
        return x

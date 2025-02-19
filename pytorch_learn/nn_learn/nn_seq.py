import torch
from torch import nn
from torch.nn import Sequential
from torch.nn import Conv2d
from torch.nn import Flatten
from torch.nn import Linear
from torch.nn import MaxPool2d
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader

import torchvision


dataset = torchvision.datasets.CIFAR10(
    "./data",
    train=False,
    transform=torchvision.transforms.ToTensor(),
    download=True
)


dataloader = DataLoader(batch_size=4, dataset=dataset)


class MM(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = Sequential(
            Conv2d(3, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(1024, 64),
            Linear(64, 10)
        )

    def forward(self, input):
        out = self.model(input)
        return out


mm = MM()
# print(mm)
# input = torch.ones((64, 3, 32, 32))
# print(input.shape)
# out = mm(input)
# print(out.shape)


# writer = SummaryWriter("./log_seq")
#
# writer.add_graph(mm, input)
# writer.close()

# tensorboard --logdir log_seq

loss = nn.CrossEntropyLoss()
for data in dataloader:
    imgs, targets = data
    out = mm(imgs)
    ret_loss = loss(out, targets)
    ret_loss.backward()
    print("")



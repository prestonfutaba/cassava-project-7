import torch
import pandas as pd
from PIL import Image
import torchvision.transforms as transforms

  # Use GPU
if torch.cuda.is_available(): # Check if GPU is available
    device = torch.device('cuda')
else:
    device = torch.device('cpu')

class StartingDataset(torch.utils.data.Dataset):
    """
    Dataset that contains 100000 3x224x224 black images (all zeros).
    """

    def __init__(self, file):
        # read the file into a pandas dataframe
        self.file = file
        self.dataset = pd.read_csv(file)
        # define a transform from PIL image to Torch tensor
        self.transform = transforms.Compose([
            transforms.CenterCrop(600),
            transforms.PILToTensor(),
            transforms.ConvertImageDtype(torch.float)
            ])
        pass

    def __getitem__(self, index):
        if index < 0 or index > self.__len__():
            return

        image = self.dataset["image_id"][index]
        pil_image = Image.open("./dataset/train_images/" + image)
        inputs = self.transform(pil_image)
        label = self.dataset["label"][index]
        return inputs, label

    def __len__(self):
        return 1000
        # return len(self.dataset)
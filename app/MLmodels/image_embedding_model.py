from transformers import ResNetForImageClassification, AutoImageProcessor
import torch
torch.backends.nnpack.enabled = False

model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

processor_model =  AutoImageProcessor.from_pretrained("microsoft/resnet-50")
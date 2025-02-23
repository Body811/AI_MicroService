from transformers import ResNetForImageClassification, AutoImageProcessor


model = ResNetForImageClassification.from_pretrained("microsoft/resnet-50")

processor_model =  AutoImageProcessor.from_pretrained("microsoft/resnet-50")
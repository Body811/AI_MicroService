from typing import List
from io import BytesIO
from PIL import Image
from MLmodels.image_embedding_model import model, processor_model



async def download_image(session, url):
    async with session.get(url) as response:
        return Image.open(BytesIO(await response.read())).convert("RGB")


def preprocess_image(images):
    
    
    inputs = processor_model(
        images,
        return_tensors="pt",
    )
    
    return inputs


def get_image_embedding(inputs):
    
    outputs= model(**inputs)
    embeddings = outputs.logits
    
    return embeddings

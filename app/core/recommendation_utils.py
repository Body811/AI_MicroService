import torch
import numpy as np
import re
from sklearn.preprocessing import MinMaxScaler
from MLmodels.product_recommendation_model import model, tokenizer
import torch
torch.backends.nnpack.enabled = False

def get_text_embedding(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()

def process_product_data(products):
    
    text_embeddings = []
    numerical_features = []
    
    price_list, rating_list = [], []
    
    for product in products:
        text = f"{product.name} {product.description} {' '.join(product.categories)} {product.handcrafter_name}"
        cleaned_text = re.sub(r"[^a-zA-Z\s]", "", text)
        text_embeddings.append(get_text_embedding(cleaned_text))
        print(text)

        price_list.append(product.price)
        rating_list.append(product.average_rating)
    
    scaler = MinMaxScaler()
    numerical_data = np.array([price_list, rating_list]).T
    numerical_data = scaler.fit_transform(numerical_data)

    for i in range(len(products)):
        numerical_features.append(numerical_data[i])
        print(numerical_data[i])
    return text_embeddings, numerical_features
from transformers import AutoTokenizer, AutoModel
import torch
torch.backends.nnpack.enabled = False

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
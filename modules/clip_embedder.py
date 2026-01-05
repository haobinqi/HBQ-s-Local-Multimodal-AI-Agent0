import torch
import clip
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"

clip_model, preprocess = clip.load("ViT-B/32", device=device)

def embed_image(image_path):
    image = preprocess(Image.open(image_path).convert("RGB")).unsqueeze(0).to(device)
    with torch.no_grad():
        return clip_model.encode_image(image)[0].cpu().numpy()

def embed_text_for_clip(text):
    text_tokens = clip.tokenize([text]).to(device)
    with torch.no_grad():
        return clip_model.encode_text(text_tokens)[0].cpu().numpy()

import streamlit as st
from pathlib import Path
import torch
from diffusers import StableDiffusionPipeline
from transformers import set_seed
import PIL

# Configuration
class CFG:
    device = "cuda"
    seed = 42
    generator = torch.Generator(device).manual_seed(seed)
    image_gen_steps = 35
    image_gen_model_id = "stabilityai/stable-diffusion-2"
    image_gen_size = (400, 400)
    image_gen_guidance_scale = 9

# Load the model
image_gen_model = StableDiffusionPipeline.from_pretrained(
    CFG.image_gen_model_id, torch_dtype=torch.float16,
    revision="fp16", use_auth_token='Your_API_key', guidance_scale=9
)
image_gen_model = image_gen_model.to(CFG.device)

def generate_image(prompt, model):
    image = model(
        prompt, num_inference_steps=CFG.image_gen_steps,
        generator=CFG.generator,
        guidance_scale=CFG.image_gen_guidance_scale
    ).images[0]

    image = image.resize(CFG.image_gen_size)
    return image

# Streamlit app
st.title('Stable Diffusion Image Generator')

st.sidebar.header('Settings')
prompt = st.text_input("Enter your prompt here:", value="A beautiful landscape")
steps = st.slider("Number of Inference Steps:", min_value=10, max_value=100, value=CFG.image_gen_steps, step=5)
guidance_scale = st.slider("Guidance Scale:", min_value=1.0, max_value=20.0, value=CFG.image_gen_guidance_scale, step=0.5)

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        CFG.image_gen_steps = steps
        CFG.image_gen_guidance_scale = guidance_scale

        generated_image = generate_image(prompt, image_gen_model)
        st.image(generated_image, caption="Generated Image", use_column_width=True)
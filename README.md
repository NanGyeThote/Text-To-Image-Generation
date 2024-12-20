# Stable Diffusion Image Generator

This project is a Streamlit-based web application that generates images using the Stable Diffusion model. It allows users to input a text prompt and configure model parameters to generate stunning images.

## Features

- **Prompt-Based Image Generation**: Enter a text prompt to generate images.
- **Customizable Parameters**:
  - Number of inference steps.
  - Guidance scale for image generation.
- **Streamlit Interface**: Interactive and user-friendly GUI.

## Requirements

The project requires the following Python packages:

- `streamlit`
- `torch`
- `diffusers`
- `transformers`
- `Pillow`

Ensure you have Python 3.8 or later installed.

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have access to the Stable Diffusion model. Obtain an API key from Hugging Face and replace 'Your_API_key' in the script.

4. If you're using a GPU, ensure PyTorch is installed with the appropriate CUDA version. Check PyTorch installation instructions.

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open the app in your web browser at http://localhost:8501.

3. Enter a text prompt in the input field and configure the inference steps and guidance scale using the sliders.

4. Click Generate Image to create and view the generated image.

## Configuration

- **Device**: The application defaults to GPU (cuda). Update the CFG.device parameter in the script to cpu if GPU is unavailable.
- **Model**: The app uses the stabilityai/stable-diffusion-2 model by default. Update CFG.image_gen_model_id to use a different model.
- **Image Settings**: Adjust CFG.image_gen_size, CFG.image_gen_steps, and CFG.image_gen_guidance_scale for custom outputs.

## Troubleshooting

- If the app fails to start or generate images:
    - Ensure your Hugging Face API key is valid.
    - Verify that your GPU drivers and CUDA toolkit are installed correctly.
    - Check package versions for compatibility.

## Acknowledgments

- **Hugging Face** for providing pre-trained models and the diffusers library.
-- **Streamlit** for the interactive web app framework.

## License

This project is licensed under the MIT License. See the LICENSE file for more details. (Not Yet)

## Contact

For questions or feedback, feel free to open an issue or contact the repository owner.

    ```bash
    You can copy and paste this into a `README.md` file for your project. Let me know if you need further adjustments!
    ```

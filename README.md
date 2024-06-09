## ICG final project: Image Harmonization

1. Task inroduction
    - A zero-shot image harmonization method that avoids extensive training on synthetic images.

    - Using off-the-shelf vision-language models and text-to-image generation for guided harmonization without the need for extensive composite image collections.

## Requirements

1. Hardware Requirements
    - GPU: 1x high-end NVIDIA GPU with at least 20GB memory

2. Software Requirements
    - Python: 3.9 or above
    - CUDA: 11.3
    - cuDNN: 8.4.1

   To install other requirements, please check [requirements.txt](requirements.txt), or directly run the following command:

   ```
   pip install -r requirements.txt
   ```

3. Pre-trained Models
   - We adopt `Stable Diffusion 2.0` as our diffusion model, you can load the pretrained weight by setting `pretrained_diffusion_path="stabilityai/stable-diffusion-2-base"` in [main.py](main.py).

## Data preparation

1. For foreground object, using segmentation model (like Segment Anything Model) to obtain the foreground mask `mask image`.

2. Paste foreground object on background image directly, which result a unharmization image `composite image`.

3. Preparation foreground_prompt and background_prompt like "girl autumn", "girl winter", which will be the prompt description of harmazition image. And if you want to generate image in batch, store all prompt in a caption file following the format : {foreground_prompt},{background_prompt}

- There have been demo data in [demo](demo), you can directly run the code below to see the results.

- If you want to test your own data, please follow the format of the demo data. Specifically, you need to prepare `composite image` and `mask image`, and `caption`.

## Harmonizing

The code supports either harmonize a single image, or harmonize a bunch of images. When the harmonization loop is finished, you can manually select the best one among a number of harmonized results, or directly use the result named `final_output` which is automatically selected. 

(**Note:** Since Diff-Harmonization is a Zero-Shot method, the results are not always good. If generating bad results, we recommend you to try different initial environmental text to get the best results.)

### Harmonize a single image

```bash
python main.py --harmonize_iterations 10 --save_dir "./output" --is_single_image --image_path "./demo/girl_comp.jpg" --mask_path "./demo/girl_mask.jpg" --foreground_prompt "girl autumn" --background_prompt "girl winter" --pretrained_diffusion_path "stabilityai/stable-diffusion-2-base" --use_edge_map
```

- `--harmonize_iterations`: the iterations' number of harmonization loop. This will be aligned with the results' number saved in the output directory.
- `--save_dir`: the directory to save the harmonized image.
- `--is_single_image`: harmonize a single image.
- `--image_path`: the path of the composite image.
- `--mask_path`: the path of the mask image.
- `--foreground_prompt`: the prompt describing foreground environment.
- `--background_prompt`: the prompt describing background environment.
- `--pretrained_diffusion_path`: the path of the pretrained diffusion model.
- `--use_edge_map`: whether to use edge maps to preserve structure.
- (optional) `--use_evaluator`: whether automatically select image.
- ... (Please refer to [main.py](main.py) for more options.)

### Harmonize a bunch of images

```bash
python main.py --harmonize_iterations 10 --save_dir "./output" --images_root "./demo/composite" --mask_path "./demo/mask" --caption_txt "./demo/caption.txt" --pretrained_diffusion_path "stabilityai/stable-diffusion-2-base" --use_edge_map
```

- `--harmonize_iterations`: the iterations' number of harmonization loop. This will be aligned with the results' number saved in the output directory.
- `--save_dir`: the directory to save the harmonized image.
- `--images_root`: the root directory of the composite images.
- `--mask_path`: the path of the mask image.
- `--caption_txt`: the path of the caption file.
- `--pretrained_diffusion_path`: the path of the pretrained diffusion model.
- `--use_edge_map`: whether to use edge maps to preserve structure.
- (optional) `--use_evaluator`: whether automatically select image.
- ... (Please refer to [main.py](main.py) for more options.)


## Reference

1. Zero-Shot Image Harmonization with Generative Model Prior
https://github.com/WindVChen/Diff-Harmonization

2. Segment-Anything
https://github.com/facebookresearch/segment-anything

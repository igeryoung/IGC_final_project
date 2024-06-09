python main.py --harmonize_iterations 10 --save_dir "/tmp2/kent/harm/Diff-Harmonization/Data/out" --is_single_image \
    --image_path "/tmp2/kent/harm/Diff-Harmonization/Data/out/63950/image.png" \
    --mask_path "/tmp2/kent/harm/Diff-Harmonization/Data/out/63950/mask.png" \
    --foreground_prompt "cat" --background_prompt "scream-style" \
    --pretrained_diffusion_path "stabilityai/stable-diffusion-2-base" \
    --use_edge_map
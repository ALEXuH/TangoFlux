
CUDA_VISISBLE_DEVICES=0,1 accelerate launch --config_file='configs/accelerator_config.yaml' src/train.py   --checkpointing_steps="best" --save_every=5 --config='configs/tangoflux_config.yaml' 
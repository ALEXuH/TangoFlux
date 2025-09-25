from setuptools import setup

setup(
    name="tangoflux",
    description="TangoFlux: Super Fast and Faithful Text to Audio Generation with Flow Matching",
    version="0.1.0",
    packages=["tangoflux"],
    install_requires=[
        "torch",
        "torchaudio",
        "torchlibrosa=",
        "torchvision",
        "transformers",
        "diffusers",
        "accelerate",
        "datasets",
        "librosa",
        "tqdm",
        "wandb",
        "click",
        "gradio",
        "torchaudio",
    ],
    entry_points={
        "console_scripts": [
            "tangoflux=tangoflux.cli:main",
            "tangoflux-demo=tangoflux.demo:main",
        ],
    },
)

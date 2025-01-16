from setuptools import setup, find_packages

setup(
    name="ai_model",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'autopep8==2.0.4',
        'dash==2.18.1',
        'flake8==7.1.1',
        'geopandas==1.0.1',
        'matplotlib==3.10.0',
        'pip-chill==1.0.3',
        'pydocstyle==6.3.0',
        'rope==1.13.0',
        'scikit-learn==1.6.1',
        'spyder==6.0.3',
        'tqdm==4.67.1',
        'wandb==0.19.2',
        'whatthepatch==1.0.7',
        'yapf==0.43.0',
        'torch==2.5.1 ',
        'torchvision==0.20.1',
        'torchaudio==2.5.1 ',
    ],
    entry_points={
        "console_scripts": [
            "ai_model=main:calculattion_data",
        ],
    },
)

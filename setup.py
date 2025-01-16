from setuptools import setup, find_packages

setup(
    name="ai_model",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        'filelock==3.13.1',
        'fsspec==2024.2.0',
        'Jinja2==3.1.3',
        'joblib==1.4.2',
        'MarkupSafe==2.1.5',
        'mpmath==1.3.0',
        'networkx==3.2.1',
        'numpy==1.26.3',
        'pandas==2.2.3',
        'pillow==10.2.0',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.2',
        'scikit-learn==1.6.1',
        'scipy==1.15.1',
        'setuptools==70.0.0',
        'six==1.17.0',
        'sympy==1.13.1',
        'threadpoolctl==3.5.0',
        'typing_extensions==4.9.0',
        'tzdata==2024.2',
    ],
    entry_points={
        "console_scripts": [
            "ai_model=main:calculattion_data",
        ],
    },
)

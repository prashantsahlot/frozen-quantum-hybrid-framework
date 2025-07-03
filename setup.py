from setuptools import setup, find_packages

setup(
    name="FrozenQuantumHybridFramework",
    version="0.1.0",
    description="Run future games and apps on quantum computers — by Frozen Bots.",
    author="Frozen Bots",
    packages=find_packages(),
    install_requires=["qiskit"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Creative Commons Attribution-NonCommercial 4.0 International License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)


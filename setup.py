from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="motor-auditoria-rupturas",
    version="1.0.0",
    author="edduchzsant21-prog",
    author_email="contact@example.com",
    description="Sistema avanzado de detección de anomalías en series financieras usando Entropía de Shannon y Entropía de Hugo (S_H)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/edduchzsant21-prog/motor-auditoria-rupturas",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Office/Business :: Financial :: Investment",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "scikit-learn>=0.24.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "plotly>=5.0.0",
        "yfinance>=0.1.70",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.12.0",
            "black>=21.0",
            "flake8>=3.9.0",
            "sphinx>=4.0",
        ],
    },
    keywords="finance anomaly-detection entropy hilbert-transform pca trading",
    project_urls={
        "Bug Reports": "https://github.com/edduchzsant21-prog/motor-auditoria-rupturas/issues",
        "Source": "https://github.com/edduchzsant21-prog/motor-auditoria-rupturas",
        "Documentation": "https://github.com/edduchzsant21-prog/motor-auditoria-rupturas#documentación-completa",
    },
)

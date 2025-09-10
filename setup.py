from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]

setup(
    name="enterprise-identity-lifecycle",
    version="2.1.0",
    author="Muhammad Hammad",
    author_email="your.email@example.com",
    description="Open-source identity management automation platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Muhammadhammad24/enterprise-identity-lifecycle",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "identity-manager=identity_guard.cli:main",
        ],
    },
)

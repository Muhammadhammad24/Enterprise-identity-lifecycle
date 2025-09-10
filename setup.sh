#!/usr/bin/env bash
set -euo pipefail

echo ">> Creating folders"
mkdir -p src/identity_guard src/{config,integrations,services,utils} \
         tests/{unit,integration,performance} \
         config scripts/migration docs/{examples,architecture} \
         examples/custom_workflows monitoring/{prometheus,grafana,health} \
         deployment/{kubernetes,terraform,helm/templates} \
         logs data/backups .github/workflows .github/ISSUE_TEMPLATE

echo ">> README.md"
cat > README.md <<'MD'
# Enterprise Identity Lifecycle
Open-source identity management automation platform.
MD

echo ">> requirements.txt"
cat > requirements.txt <<'REQ'
requests>=2.28.0
fastapi>=0.95.0
uvicorn>=0.21.0
redis>=4.0.0
psycopg2-binary>=2.9.0
sqlalchemy>=1.4.0
alembic>=1.7.0
click>=8.0.0
prometheus-client>=0.14.0
python-dotenv>=0.19.0
REQ

echo ">> src/identity_guard/cli.py"
cat > src/identity_guard/cli.py <<'PY'
import sys

def main():
    print("Identity Manager CLI is live.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
PY

echo ">> setup.py"
cat > setup.py <<'PY'
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
PY

echo "✅ All files created successfully!"

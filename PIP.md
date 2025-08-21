# PIP and Virtual envs

## PyPI and PIP in Python

### What is PyPI (Python Package Index)?

- PyPI (https://pypi.org/) is the official repository of Python packages.
- Think of it as a central “marketplace” where developers publish Python libraries and frameworks for others to use.
- Similar repositories in other ecosystems:
  - npm for JavaScript
  - Maven Central for Java
  - NuGet for .NET

#### Key Features:
- Hosts over 500,000 packages (as of 2025).
- Provides libraries for various domains: web development, data science, AI, automation, etc.
- Each package usually includes:
  - Documentation and description
  - Release history and versions
  - Dependencies
  - Installation instructions

### What is PIP?
- PIP = Package Installer for Python.
- It is the official tool for installing, upgrading, and managing packages from PyPI.
- Since Python 3.4, PIP has been included by default in most Python distributions.


#### Common PIP Commands:
##### Install a package (latest version) from PyPI
```
pip install requests
```

##### Install a specific version
```
pip install requests==2.31.0
```

##### Upgrade a package
```
pip install --upgrade requests
```

##### Uninstall a package
```
pip uninstall requests
```

##### List installed packages
```
pip list
```

##### Show detailed information about a package
```
pip show requests
```

### Best practices when using PIP
- Always use virtual environments (venv, virtualenv, poetry, pipenv) to avoid dependency conflicts across projects.
- Keep pip itself updated:
```
python -m pip install --upgrade pip
```
- Document your dependencies with a requirements.txt file.

### Current notes (2025)
- PIP remains the default package manager in Python.
- Alternative dependency managers (like Poetry, PDM, and Conda) are gaining popularity, especially for data science and large projects.
- Despite alternatives, PyPI + PIP is still the foundation of Python’s package ecosystem.


## Virtual environments in Python

### 1. What is a Virtual Environment?
A virtual environment is an isolated Python environment that allows you to install and manage packages independently from the global Python installation.

Each project can have its own dependencies and versions, preventing conflicts between projects.

👉 Without a virtual environment, all packages are installed system-wide, which can quickly lead to version conflicts.

### 2. Why Use Virtual Environments?

- ✅ Avoid dependency conflicts between projects.
- ✅ Reproduce environments easily (with requirements.txt).
- ✅ Keep your global Python installation clean.
- ✅ Work with different Python versions and package versions simultaneously.

### 3. Creating and Using Virtual Environments (Standard Library: venv)
Since Python 3.3, the built-in venv module is the recommended way to create virtual environments.

#### Create a new virtual environment in a folder called "venv"
```
python -m venv venv
```

This creates a venv/ directory containing a private Python interpreter and a copy of pip.

#### Activate the environment

##### Windows (PowerShell):

```
venv\Scripts\Activate
```

##### macOS/Linux (bash/zsh):

```
source venv/bin/activate
```

When activated, your terminal prompt changes, usually showing (venv) at the beginning.

#### Deactivate the environment:
```
deactivate
```

### 4. Installing packages inside a virtual environment
Once activated, you can install packages with PIP as usual:
```
pip install requests
```
Packages will be installed inside the venv folder, not globally.

### 5. Alternatives to venv
While venv is the standard and lightweight tool, other tools exist:

- **virtualenv** → older, more feature-rich than venv.
- **pipenv** → integrates virtual environments + dependency management.
- **Poetry** → modern tool for dependency management and packaging.
- **Conda** → popular in data science, manages both Python and non-Python dependencies.


## The requirements.txt file
### 1. What is a requirements.txt file?
A requirements.txt file is a plain text file that lists the dependencies (packages) your Python project needs to run.

It is commonly used with PIP to install all dependencies at once.

Each line in the file typically represents one package, optionally with a version specifier.

### 2. Why use requirements.txt?
- Ensures that your project can be recreated consistently on another system.
- Useful for collaboration (team members install the same packages).
- Makes deployment (e.g., to servers, Docker, CI/CD pipelines) predictable.
- Prevents the “it works on my machine” problem.

### 3. Creating a requirements.txt
If you already have a virtual environment with your installed packages:
```
pip freeze > requirements.txt
```
Example generated file:
```
matplotlib==3.9.2
numpy==2.1.1
pandas==2.2.2
```

### 4. Installing from requirements.txt
To install all packages listed in the file:
```
pip install -r requirements.txt
```

This will install exact versions if specified (e.g., matplotlib==3.9.2) or the latest version if no version is set.

### 5. Version Specifiers
You can control which versions of a package are installed:

#### Exact version

> numpy==2.1.1

#### Minimum version

> numpy>=2.0.0


#### Version range

> numpy>=1.25,<2.0


#### Any version (not recommended for production)

> numpy


### 6. Best practices
- Always use a virtual environment before generating a requirements.txt.
- Pin versions (==) in production for stability.
- For development projects, you can allow flexible versions (>=) but always test before deployment.
- Consider using requirements-dev.txt for development tools (linters, testing libraries).
- For larger projects, modern alternatives like Poetry or PDM can manage dependencies more elegantly — but requirements.txt is still the standard across most Python projects.


## Splitting requirements.txt into multiple files

### 1. Why split dependencies?
In real-world projects, not all dependencies are required for production. Some are only used during development, testing, or documentation. Example:
```
Production dependencies: Flask, NumPy, Pandas
Dev-only dependencies: Pytest, Black, Flake8
```

Keeping everything in a single requirements.txt makes deployments heavier and can introduce unnecessary dependencies into production.

### 2. Common files used

#### ✅ requirements.txt
Contains only the core dependencies needed to run the application in production.Example:
```
flask==3.0.3
numpy==2.1.1
pandas==2.2.2
```

#### ✅ requirements-dev.txt
Contains extra tools for development (testing, linting, formatting). Often includes -r requirements.txt so dev dependencies extend the main file. Example:
```
-r requirements.txt
pytest==8.3.2
black==24.8.0
flake8==7.1.1
```

#### ✅ requirements-test.txt (optional)
Specifically for CI/CD pipelines or test environments. Can also extend from requirements.txt. Example:
```
-r requirements.txt
pytest==8.3.2
coverage==7.6.1
```

### 3. Installing from Different Files

#### Production install:

> pip install -r requirements.txt


#### Development install:

> pip install -r requirements-dev.txt


#### Test install:

> pip install -r requirements-test.txt

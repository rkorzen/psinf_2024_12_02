import os

readme_content = """Oto zawartość pliku `README.md`, która zawiera instrukcje dotyczące budowy, instalacji oraz publikacji paczki w PyPI:

```markdown
# MyPackage

This is an example Python package demonstrating how to build, install, and publish Python packages.

## Building the Package

### Using `build`

You can build the package using the `build` tool. Ensure you have the `build` module installed:

```bash
pip install build
```

Then run the following command in the directory containing `setup.py`:

```bash
python -m build
```

This will create a `dist` directory containing `.whl` (wheel) and `.tar.gz` (source distribution) files.

### Using `sdist`

You can also build a source distribution manually using the following command:

```bash
python setup.py sdist
```

This will create a `.tar.gz` file in the `dist` directory.

## Installing the Package from GitHub

You can install the package directly from a GitHub repository using `pip`. Replace `<username>` and `<repository>` with the appropriate values:

```bash
pip install git+https://github.com/<username>/<repository>.git
```

For example:

```bash
pip install git+https://github.com/yourusername/mypackage.git
```

## Publishing the Package to PyPI

1. Install the tools required for publishing:

   ```bash
   pip install twine
   ```

2. Ensure your package is built and the files are located in the `dist` directory.

3. Test your package upload using the Test PyPI repository:

   ```bash
   twine upload --repository-url https://test.pypi.org/legacy/ dist/*
   ```

4. Once you confirm the upload to Test PyPI is successful, publish your package to the official PyPI repository:

   ```bash
   twine upload dist/*
   ```

5. Your package should now be available on PyPI. You can install it using:

   ```bash
   pip install mypackage
   ```

## Notes

- Replace `mypackage` with your actual package name.
- Use a `.pypirc` file for easier authentication when uploading to PyPI.
```

### Wyjaśnienia:

1. **Budowanie paczki**:
   - Sekcja pokazuje, jak zbudować paczkę zarówno za pomocą `build`, jak i `sdist`.

2. **Instalacja z GitHub**:
   - Komenda `pip install git+https://...` pozwala na instalację paczki bezpośrednio z repozytorium.

3. **Publikacja do PyPI**:
   - `twine` jest narzędziem używanym do wysyłania paczek na Test PyPI i PyPI.
   - `twine upload` obsługuje zarówno Test PyPI (do testów), jak i produkcyjny PyPI.
"""


def create_package_with_setup(base_dir, package_name):
    # Ścieżka do katalogu paczki
    package_path = os.path.join(base_dir, package_name)
    
    # Struktura paczki
    structure = {
        package_path: {},  # Katalog paczki
        os.path.join(base_dir, "setup.py"): f"""\
from setuptools import setup, find_packages

setup(
    name="{package_name}",
    version="0.1.0",
    packages=find_packages(),
    description="A Python package example",
    author="Your Name",
    author_email="your.email@example.com",
    python_requires=">=3.6",
)
""",
        os.path.join(base_dir, "README.md"): readme_content,
    }

    # Funkcja tworząca pliki i foldery
    def create_files(structure):
        for path, content in structure.items():
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)  # Tworzenie katalogu
            else:
                with open(path, "w") as file:  # Tworzenie pliku
                    file.write(content)

    # Tworzenie plików i folderów
    create_files(structure)
    print(f"Package '{package_name}' created successfully in '{base_dir}'!")

# Katalog główny dla struktury paczki
base_dir = "package_build_example"
os.makedirs(base_dir, exist_ok=True)

# Nazwa paczki
package_name = "mypackage"

# Generowanie struktury paczki
create_package_with_setup(base_dir, package_name)

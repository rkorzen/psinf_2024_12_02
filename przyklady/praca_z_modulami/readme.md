# praca z modulami

## modul 

to pojedynczy plik zawierający kod w pythonie

## package 

to kolekcja modułów zawartych w jednym katalogu

## struktura typowa

```
outer_package/
    package/
        __init__.py
        module_a.py
        module_b.py
    main.py
```

```
# main.py
from package.module_a import a
```
## dynamiczne importy

```
# main.py
import importlib
module = importlib.import_module("package.module_a")
```
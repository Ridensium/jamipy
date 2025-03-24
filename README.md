
UI widget library for building web apps with **PyScript**.

#### Emphasis on:

**speed**, especially in the *MicroPython* interpreter

**pythonic** usage

**small** package size

**no thirdparty** python or javascript libraries


#### Instalation

the easiest way is to provide the url to the `distro.zip` in to `config.toml` in pyscript

```toml
#config.toml

[files]
"https:.../distro.zip" = "./jamipy/*"

```

[pyscript user guide](https://docs.pyscript.net/2025.3.1/user-guide/configuration/#files)

The other way is to provide the package files one by one in same way, or make your own `.zip` or `.tar.gz` if self hosted. 

Apart of the source files in `/src` directory there are minified versions in `/dist/py`

#### Example

```python
from jamipy import Label, Container

label = Label('Hello World')

label.display()

container = Container()

label_2 = Label(text='Hello World', icon='sunny')

container += label_2

container.display()
```


#### Documentation

[Documentation index](/docs/docs/_jamipy_.md)


#### Roadmap

[ROADMAP](/docs/ROADMAP.md)



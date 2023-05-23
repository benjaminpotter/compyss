# compyss
A tool built for analysing skylight polarization patterns. It aims to provide
heading information from skylight angle of polarization images.

### Design philosophy
compyss is designed to be as flexible as possible. It's flexibility allows it to
support multiple cameras and decode methods. Once you write a decoder, it should
be available for all supported cameras. See the wiki for more information.

### Author
This package was written in conjuction with a study at [Queen's
University](https://queensu.ca/) at Kingston. If you use this code, please cite
our work. We have not published yet, but when we do I will link the citation
here.

<!--
## Contents

- [Features](#features)
- [Usage](#usage)
  - [Initial setup](#initial-setup)
- [FAQ](#faq)
- [Projects](#projects)
- [Contributing](#contributing)

-->

## Features
- Read heading from AoLP image
- Read angle to solar meridian from AoLP image

### Camera SDK support
- Lucid Vision Labs, Arena SDK

## Usage
Examples are provided in the source. The general flow is 

```
import compyss.core
from compyss.sources.file import FileSource

# create a new compass object
cmps = compyss.core.Compass(source=FileSource("path/to/file.png")

# use the compass object to extract data from the source
cmps.read()
```

### Initial setup
The package is not currently available on pypi. Download the source and install
as a local package using pip.

## FAQ
For questions, open an issue or send an email to ben [dot] potter [at] queensu
[dot] ca.

## Projects
If you use this code, open a PR and add your project to this list. We also ask
you cite our paper. See [author](#author).

## Contributing 
Contributions are welcome, mostly with respect to camera SDK support. If you need support for another camera SDK,
reach out to me ben [dot] potter [at] queensu [dot] ca.


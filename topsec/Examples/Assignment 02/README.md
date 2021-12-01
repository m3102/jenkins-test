[![Build Status][build-shield]][build-url]
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div>
  <div align="center">
    <h1 style="font-weight: bold">ICT 3x03</h1>
    <a href="https://github.com/SIT-ICT3x03/Team09-AY21">
        <img src="./resources/logo.png" alt="Logo">
    </a>
    <p align="center" style="margin-top: 30px">
        Minimum real-word Secure Web Application with User Login
        <br />
        <a href="https://t.me/teamsys_bot">View Demo</a>
        ·
        <a href="https://github.com/SIT-ICT3x03/Team09-AY21/issues">Report Bug</a>
        ·
        <a href="https://github.com/SIT-ICT3x03/Team09-AY21/issues">Request Feature</a>
    </p>
  </div>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [ENV File](#env-file)
- [License](#license)
- [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
<h2 align="center"><b>About The Project</b></h2>

Minimum real-word Secure Web Application with User Login

## Getting Started

This is an example of how you can set up your project locally. To get a local copy up and running follow these simple example steps.

### Installation

1. Clone the repo

```sh
git clone with HTTPS          https://github.com/SIT-ICT3x03/Team09-AY21.git
git clone with SSH            git@github.com:SIT-ICT3x03/Team09-AY21.git
git clone with Github CLI     gh repo clone SIT-ICT3x03/Team09-AY21
```

2. Starting Server

```sh
1. cd Server
2. python -m venv venv                              # Creates virtual environment locally
3. venv\Scripts\activate                            # Activates virtual environment
4. python -m pip install -r requirements.txt        # Installs all dependencies
5. $env:FLASK_APP="server.py"
6. $env:FLASK_ENV="development"
7. python -m flask run                              # Runs the python main file
```

3. Starting Client

```sh
1. cd ClientApp
2. npm install
3. npm run dev
```

### ENV File

```sh
1. Create a .env.local in ClientApp folder
2. Create a .env in Server folder
```

<!-- LICENSE -->
<br />

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- Acknowledgements -->
<br />

## Acknowledgements

- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)

<!-- Contributions -->
<br />

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

## Jenkins Usage
```sh
1. Access the dashboard through jenkins.rchan.sitict.net:8443
2. Ensure that port is specified to 8443
```


[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[build-url]: #
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[contributors-url]: https://github.com/SIT-ICT3x03/Team09-AY21/graphs/contributors
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit

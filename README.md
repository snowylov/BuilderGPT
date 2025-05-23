<div align="center">
<img src="https://github.com/Zhou-Shilin/picx-images-hosting/blob/master/buildergpt-logo.jpeg?raw=true"/> 
<img src="https://img.shields.io/badge/Builder-GPT-blue">
<a href="https://github.com/CyniaAI/BuilderGPT/pulls"><img src="https://img.shields.io/badge/PRs-welcome-20BF20"></a>
<img src="https://img.shields.io/badge/License-Apache-red">
<a href="https://discord.gg/kTZtXw8s7r"><img src="https://img.shields.io/discord/1212765516532289587
"></a>
<!-- <a href="https://crowdin.com/project/bukkitgpt"><img src="https://img.shields.io/badge/i18n-Crowdin-darkblue"></a> -->
<!-- <p>English | <a href="https://github.com/CyniaAI/BukkitGPT/blob/master/README-zh_cn.md">简体中文</a></p> -->
<br>
<a href="https://discord.gg/kTZtXw8s7r">Join our discord</a>
<br/>
</div>

> [!NOTE]
> Developers and translators are welcome to join the CyniaAI Team!

## Introduction
> Give GPT your idea, AI generates customized Minecraft structures.

BuilderGPT is an open source, free, AI-powered Minecraft structure generator. It was developed for minecraft map makers. It can generate structures in `*.schem` format and users can import them via worldedit, etc.

# Showcase
![](https://github.com/Zhou-Shilin/picx-images-hosting/blob/master/img-mUATep311QjghtgbcihXCJwZ.png?raw=true)
![](https://github.com/Zhou-Shilin/picx-images-hosting/blob/master/Snipaste_2024-05-12_21-11-55.png?raw=true)

## Features

- [x] Generate structures
- [x] Preview rendered schematic in-program
- [x] Export generated structures to `*.schem` files
- [x] Export generated structures to `*.mcfunction` files
- [x] **Advanced Mode** (Use Stable Diffusion/DALL-E to generate the design image and let `gpt-4-vision` generate the struture base on it.)
- [ ] Edit structures

### Other projects of CyniaAI Team
- [x] Bukkit plugin generator. {*.jar} ([BukkitGPT](https://github.com/CyniaAI/BukkitGPT))
- [x] Structure generator. {*.schem} ([BuilderGPT](https://github.com/CyniaAI/BuilderGPT))
- [ ] Serverpack generator. {*.zip} (ServerpackGPT or ServerGPT, or..?)
- [ ] Have ideas or want to join our team? Send [us](mailto:admin@baimoqilin.top) an email!


## Requirements

### Plan A. Windows/Linux (executable edition)

> [!WARNING]
> The version of the executable is still in the testing process. Plan B is recommended if possible.

Nothing. Just download the executable file and run it.

### Plan B. Python (Any operating systems; Recommend if possible)

You can use BukkitGPT on any device with [Python 3+](https://www.python.org/).  

And you need to install the depencies with this command:
```
pip install -r requirements.txt
```

## Quick Start

*(Make sure you have the [Python](https://www.python.org) environment installed on your computer)*

<!--
### Executable/UI
1. Download `windows-build.zip` or `linux-build.zip` from [the release page](https://https://github.com/CyniaAI/BuilderGPT/releases) and unzip it.
2. Edit `config.yaml`, fill in your OpenAI Apikey. If you don't know how, remember that [Google](https://www.google.com/) and [Bing](https://www.bing.com/) are always your best friends.
3. Run `ui.exe` (Windows) or `ui` (Linux), enter the description and let GPT generate the structure.
4. Find your structure in `/generated/<name>.schem`.
5. Import the file into the game via worldedit or other tools. (Google is your best friend~~)
-->

### Fabric Mod Builder

`fabric_mod_builder.py` scaffolds a Fabric mod project. Specify the project
directory and optional Minecraft version. If Gradle is installed, the script
sets up the wrapper, downloads Fabric Loader, Fabric API and Yarn mappings and
can launch a development client.

Usage:

```bash
python fabric_mod_builder.py MyMod --version 1.21.5 --run-client
```

The generated folder contains `src/main/java` and `src/main/resources`.


Moved to [Wiki](https://github.com/CyniaAI/BuilderGPT/wiki).

<!--
### Python/UI (RECOMMEND)
1. Download `Source Code.zip` from [the release page](https://https://github.com/CyniaAI/BuilderGPT/releases) and unzip it.
2. Edit `config.yaml`, fill in your OpenAI Apikey. If you don't know how, remember that [Google](https://www.google.com/) and [Bing](https://www.bing.com/) are always your best friends.
3. Run `ui.py` (bash `python ui.py`), enter the description and let GPT generate the structure.
4. Find your structure in `/generated/<name>.schem`.
5. Import the file into the game via worldedit or other tools. (Google is your best friend~~)

### Python/Console
1. Download `Source Code.zip` from [the release page]([https:///](https://github.com/CyniaAI/BuilderGPT/releases)) and unzip it.
2. Edit `config.yaml`, fill in your OpenAI Apikey. If you don't know how, remember that [Google](https://www.google.com/) and [Bing](https://www.bing.com/) are always your best friends.
3. Run `console.py` (bash `python console.py`), enter the description and let GPT generate the structure.
4. Find your structure in `/generated/<name>.schem`.
5. Import the file into the game via worldedit or other tools. (Google is your best friend~~)

-->



## Contributing
If you like the project, you can give the project a star, or [submit an issue](https://github.com/CyniaAI/BuilderGPT/issues) or [pull request](https://github.com/CyniaAI/BuilderGPT/pulls) to help make it better.

## License
```
Copyright [2024] [CyniaAI Team]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

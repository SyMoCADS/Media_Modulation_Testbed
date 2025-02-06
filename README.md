<img src="idc_bvt_logo.png" alt="IDC Logo" width="130" height="80"/>

# Media Modulation Testbed: Code Package

This repository contains parts of the code from the paper:

M. Scherer, L. Brand, L. Wolf, T. tom Dieck, M. Schäfer, S. Lotter, A. Burkovski, H. Sticht, R. Schober, and K. Castiglione, "Closed-Loop Long-Term Experimental Molecular Communication System," *arXiv version arXiv:2502.00831*, Feb. 2025. [Click here to view the paper](https://arxiv.org/pdf/2502.00831).

> [!NOTE]
> This repository includes only a subset of experimental data to keep it small and quick to download. To access the complete experimental dataset, download the [full database](https://zenodo.org/records/13898880/files/mmtb.db?download=1) from [Zenodo](https://zenodo.org/records/13898880) and place the `mmtb.db` file in the project directory or one of its subdirectories. 

## Module Structure & Documentation
The `mmtb`package is structured as followed:
* **mmtb**
    * [**evaluation**](./docs/evaluation.md)
      * [**synchronization**](./docs/evaluation/synchronization.md)
      * [**detection**](./docs/evaluation/detection.md)
      * [**filters**](./docs/evaluation/filters.md)
    * [**experiments**](./docs/experiments.md)
    * ([**dtypes**](./docs/dtypes.md))

> [!IMPORTANT]
> By clicking on the specific submodules, you can access the documentation and learn more about their classes and functions. Note also that all new data types/classes are collected in the `dtypes` submodule.

## Code Examples
Detailed list and description of all code examples: [Click here](./examples/examples.md).

The code examples refer to the examples in the `examples` folder. After the initial setup and installation of the `mmtb`package, you can run them yourself.
To run the code examples, we recommend to use [Installation Option 2](#Installation), once you finished the steps in [Prerequisites](#Prerequisites) and [Set Up](#Set-Up).

## Setup & Installation

### Prerequisites

+ [Git](https://git-scm.com/downloads)
+ [Python](https://www.python.org/downloads/)

> [!IMPORTANT]
> This package is compatible with Python 3.11, 3.12, and 3.13 (excluding [Python 3.13.0](https://github.com/python/cpython/issues/125179))

> [!CAUTION]
> This package relies on the `tkinter` package for the graphical user interface. However, some Python distributions for Unix/macOS operating systems do not include it out of the box. This means you have to install it yourself using your native package manager.
> + Debian/Ubuntu-based Linux:
>```shell
> sudo apt install python3-tk
>```
> + SUSE-based Linux:
>```shell
> sudo zypper in python3-tk
>```
> + macOS 
>```shell
> brew install python-tk@3.11
>```

> [!NOTE]
> Adapt @3.11 to the Python version you are using.

### Set Up

#### Windows
   
1. **Create a Project Folder and Navigate to it**
   - Create a new directory to store your project.
   - Navigate to the directory with:
      ```shell
      cd <path-to-directory>
      ```

2. **Create a Virtual Environment:**
   - To create a virtual environment enter:
      ```shell
      py -m venv .venv
      ```
> [!IMPORTANT]
> Other terminals than the Windows Command Prompt may require the command *python* instead of *py*

> [!TIP]
> To ensure you're using an suitable Python version in the virtual environment, specify the version in the Windows Command Prompt:
> ```shell
> py -3.11 -m venv .venv
> ```

> [!NOTE]
> Adapt -3.11 to the Python version you are using.

> [!TIP]
> You may want to [use globally installed Python packages](https://www.nithinbose.com/posts/make-virtualenv-use-packages-from-global-site-packages/):
> ```shell
> py -m venv .venv --system-site-packages
> ```

3. **Activate the Virtual Environment:**
   - Activate the environment with:
      ```shell
      .\.venv\Scripts\activate
      ```

> [!WARNING]
> If you encounter issues, run
> ```shell
>  Set-ExecutionPolicy Unrestricted -Scope Process
> ```
> and attempt to activate again. This command allows you to run all scripts, regardless of signature, within the current terminal, until you close the terminal. 

#### Unix/macOS
   
1. **Create a Project Folder and Navigate to it**
   - Create a new directory to store your project.
   - Navigate to the directory with:
      ```shell
      cd <path-to-directory>
      ```

2. **Create a Virtual Environment:**
   - To create a virtual environment enter:
     ```shell
     python3 -m venv .venv
     ```

> [!TIP]
> To ensure you're using the right Python version in the virtual environment, specify the version. E.g., for Python version 3.11, type:
> ```shell
> python3.11 -m venv .venv
> ```

> [!NOTE]
> Adapt 3.11 to the Python version you are using.

> [!TIP]
> You may want to [use globally installed Python packages](https://www.nithinbose.com/posts/make-virtualenv-use-packages-from-global-site-packages/):
> ```shell
> python3 -m venv .venv --system-site-packages
> ```

3. **Activate the Virtual Environment:**
   - Activate the environment with:
     ```shell
     source .venv/bin/activate
     ```

### Installation
You have two options to install this package:

- Option 1: Direct Installation via GitHub (recommended, when used in **existing project**):
   
    ```shell
    pip install git+https://github.com/SyMoCADS/Media_Modulation_Testbed.git
    ```

- Option 2: Download/Cloning & Local Installation (recommended to **test the provided code examples**):
    1. Clone repository by running:
       ```shell
       git clone https://github.com/SyMoCADS/Media_Modulation_Testbed.git
       ```

   2. Navigate to the repository with:
      ```shell
      cd <path-to-cloned-repository>
      ```
      
   3. Locally build and install package by entering:
       ```shell
       pip install .
       ```

   4. Now, everything is ready to test our [code examples](./examples/examples.md):
      > + Windows:
      >```shell
      > python .\examples\plotting_example.py
      >```
      > + Unix/macOS:
      >```shell
      > python ./examples/plotting_example.py
      >```
> [!TIP]
> Increasing the zoom level in the plot will make the gray bars that are present in the initial view disappear.

## Additional Experimental Data
   - The majority of our experimental results are provided via Zenodo under the CC BY licence.
   - To access data from all experiments presented in our [paper](https://arxiv.org/pdf/2502.00831), download the [full database](https://zenodo.org/records/13898880/files/mmtb.db?download=1) from [Zenodo](https://zenodo.org/records/13898880) and copy it (the `mmtb.db` file) into your project folder.



## Contact
If you have any question or suggestions for improvements, feel free to open an issue or contact us directly.

**Louis Wolf**:

- Email: louis.wolf@fau.de

**Maike Scherer**:

- Email: maike.scherer@fau.de

**Lukas Brand**:

- Email: lukas.brand@fau.de

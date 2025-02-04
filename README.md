<img src="idc_bvt_logo.png" alt="IDC Logo" width="130" height="80"/>

# Media Modulation Testbed: Code Package

This repository contains parts of the code used in the paper titled "Closed-Loop Long-Term Experimental Molecular Communication System". For the Arxiv version of the paper: [Click here](https://arxiv.org/pdf/2502.00831).

> [!NOTE]
> This repository includes only a subset of experimental data to keep it small and quick to download. To access the complete experimental dataset, download the [full database](https://zenodo.org/api/records/13898880/draft/files/mmtb.db/content) from [Zenodo](https://zenodo.org/uploads/13898880) and place the `mmtb.db` file in the project directory. The data will be accessible as long as this file is located in the current working directory or its subdirectories.

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
> This serves as the documentation for this package. By clicking on the specific submodules, you can learn more about their classes and functions. Note also that all new data types/classes are collected in the `dtypes` submodule.

## Code Examples
Detailed list and description of all code examples: [Click here](./examples/examples.md).

The code examples refer to the examples in the `examples` folder. After the initial setup and installation, you may download and run them yourself.
To run the code examples, we recommend to use [Installation Option 2](#Installation), once you finished the steps in [Prerequisites](#Prerequisites) and [Set Up](#Set-Up).

## Setup & Installation

### Prerequisites

+ [Git](https://git-scm.com/downloads)
+ [Python](https://www.python.org/downloads/) (3.11 or newer)

> [!CAUTION]
> This package relies on the `tkinter` package for the graphical user interface. However, the Python distributions for Unix/macOS operating systems do not include it out of the box. This means you have to install it yourself using your native package manager.
> + Debian/Ubuntu-based Linux:
>```shell
> sudo apt install python3-tk
>```
> + SUSE-based Linux:
>```shell
> sudo zypper in python3-tk
>```
> + macOS:
>```shell
> brew install python-tk@3.11
>```

### Set Up

#### Windows

1. **Create a Project Folder and Navigate to it**
   - Create a new directory to store your project.
   - Navigate to the directory with:
      ```shell
      cd <path-to-directory>
      ```

2. **Create and Activate a Virtual Environment:**
   - To create a virtual environment enter:
      ```shell
      py -m venv .venv
      ```

> [!TIP]
> To ensure you're using the right Python version in the virtual environment, specify the version in the Windows Command Prompt like this:
> ```shell
> py -3.11 -m venv .venv
> ```

> [!TIP]
> Other terminals than the Windows Command Prompt may require the command *python* instead of *py*

   - Activate the environment with:
      ```shell
      .\.venv\Scripts\activate
      ```

> [!WARNING]
> If you encounter issues, run `Set-ExecutionPolicy Unrestricted -Scope Process` and attempt to activate again.


#### Unix/macOS

1. **Create a Project Folder and Navigate to it**
   - Create a new directory to store your project.
   - Navigate to the directory with:
      ```shell
      cd <path-to-directory>
      ```

2. **Create and Activate a Virtual Environment:**
   - To create a virtual environment enter:
     ```shell
     python3 -m venv .venv
     ```

> [!TIP]
> To ensure you're using the right Python version in the virtual environment, specify the version like this:
> ```shell
> python3.11 -m venv .venv
> ```

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

- Option 2: Download/Cloning & Local Installation (recommended to **test our code examples**):
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
> Zoom into the plots so that the initial gray bars disappear and the curves look nice.

## Additional Experimental Data
   - The majority of our experimental results are provided via Zenodo under the CC BY licence.
   - To access data from all experiments presented in our [paper](https://arxiv.org/pdf/2502.00831), download the [full database](https://zenodo.org/api/records/13898880/draft/files/mmtb.db/content) from [Zenodo](https://zenodo.org/uploads/13898880) and copy it (the `mmtb.db` file) into your project folder.



## Contact
If you have any question or suggestions for improvements, feel free to open up issues or contact us directly.

**Louis Wolf**:

- Email: louis.wolf@fau.de

**Maike Scherer**:

- Email: maike.scherer@fau.de

**Lukas Brand**:

- Email: lukas.brand@fau.de

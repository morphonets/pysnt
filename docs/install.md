# <i class="fas fa-download"></i>&hairsp;Install

## Requirements


The stack of dependencies used by PySNT is rather complex and includes Python 3.8+, Java 21+, [SNTv5 pre-release](https://github.com/morphonets/SNT/releases), [imglyb](https://github.com/imglib/imglyb), [jgo](https://github.com/scijava/jgo), [numpy](https://github.com/numpy/numpy), [pyimagej][pyimagejdocs], [scyjava](https://github.com/scijava/scyjava), among others. Because of this complexity we recommend using a package manager. We endorse Mamba
since Conda can be painfully slow with complex environments. If you do not have Mamba installed you can do
so by [Installing Miniforge3](https://github.com/conda-forge/miniforge#miniforge3).

```{important}
In the future, PySNT will automatically download OpenJDK and SNT if they're not found. For now, you'll need to download them manually (see installation instructions below).
```

Here we only summarize the _easiest_ way to install pysnt. For other (advanced) install options (via pip, condacolab, dynamic install, etc.) you should be able to adapt the advanced install documentation of [pyimagej][pyimagejdocs].

## Setting Up

1. Assuming you have `mamba` installed, activate conda-forge:

   ```bash
   mamba config append channels conda-forge
   mamba config set channel_priority strict
   ```

2. [Clone](https://github.com/morphonets/pysnt.git) or [download](https://github.com/morphonets/pysnt/archive/refs/heads/main.zip) pysnt

   ```bash
   cd /path/to/hosting/directory
   git clone https://github.com/morphonets/pysnt.git
   ```

3. Create a new `pysnt` environment using the provided `environment.yml`. This will install all the key dependencies:

   ```bash
   cd ./pysnt # cd to pysnt root directory
   mamba env create -f environment.yml
   ```

4. Install pysnt in editable/development mode

   ```bash
   mamba activate pysnt # activate the newly created environment
   pip install -e .
   ```

5. Test that PySNT has been successfully installed, by displaying its version:

   ```bash
   mamba activate pysnt
   python -c 'import pysnt; print(f"Using PySNT version: {pysnt.version()}")'
   ```
   Which should print:
   ```bash
   0.0.1
   ```

6. At this point, it may be convenient to make the new `pysnt` environment available in the graphical 
   notebook interface (skip this step if you have no intention of using notebooks):

   ```bash
   mamba activate pysnt
   mamba install ipykernel
   python -m ipykernel install --user --name=pysnt
   ```

   Now, when you now start jupyter (or Jupyter lab), it will show `pysnt` in the list of registered
   kernels. Selecting it, makes all the packages installed in the `pysnt` environment available.


### Attaching to SNT

PySNT requires a connection to a local SNT installation. There are two options:

1. **Use an existing Fiji installation** (recommended): Point PySNT to a Fiji install that's subscribed to the [NeuroAnatomy update site](https://imagej.net/SNT#install)

2. **Automatic download**: PySNT will automatically download the SNT binary in the background the first time you import an SNT class. This initial download may take several minutes, but subsequent runs will start instantly.


```{important}
Currently the automatic option does not retrieve the latest version of SNT. Until SNTv5 is officially released,
it is best to point pyimagej to a SNT pre-release bundle:

1. Download a pre-release bundle from the [SNT Release Page](https://github.com/morphonets/SNT/releases).
   Unzip it to a local directory, e.g., `~/Downloads/`

2. Point pysnt to the bundle:

   ```python
   import pysnt
   pysnt.initialize_snt(fiji_path="~/Downloads/Fiji-SNTv5_pre-release_macOS") # Specify path directly
   ```

#### Interactive Setup
When you initialize pysnt using default options...

```python
import pysnt
pysnt.initialize_snt()
```
... The program will look for a Fiji install in common locations. If Fiji is not found, an interactive installer kicks in:

```terminaloutput
Fiji Installation Not Found
========================================
PySNT requires Fiji to be installed:

Common installation locations checked:
  - /Applications/Fiji.app
  - C:/Fiji.app
  - ~/Fiji.app
  - ~/Applications/Fiji.app
  - ~/Desktop/Fiji.app
  - ~/Downloads/Fiji.app

If Fiji is installed in a different location, please provide the path.
If Fiji is not installed, you can:
  1. Set FIJI_PATH environment variable
  2. Pass fiji_path parameter to initialize_snt()

📍Enter Fiji installation path (or 'skip' to continue without): /Users/user/Downloads/Fiji-SNTv5_pre-release_macOS
✅ Using Fiji installation: /Users/user/Downloads/Fiji-SNTv5_pre-release_macOS
❓Save this path to FIJI_PATH environment variable for future use? (y/N): y
✅ FIJI_PATH set for current session.
👉 To make permanent, add this to your shell profile:
   export FIJI_PATH='/Users/user/Downloads/Fiji-SNTv5_pre-release_macOS'
```

## Verify Installation

To check version and system info:

```python
import pysnt
print(f"PySNT version: {pysnt.version()}")
print("System info:")
pysnt.info()
```

```terminaloutput
PySNT version: 0.0.1
System info:
PySNT Version Information
===================================
PySNT version: 0.0.1
Author: SNT contributors

Python Environment:
Python version: 3.12.12
Python executable: /Users/ferreirat/miniforge3/envs/pysnt-dev/bin/python
Platform: macOS-26.0.1-arm64-arm-64bit
Architecture: arm64

📦 Core Dependencies:
  ✅ scyjava      1.12.1       (SciJava Python bridge)
  ✅ imagej       1.7.0        (PyImageJ)
  ✅ numpy        2.3.3        (NumPy)
  ✅ jdk          1.1.0        (install-jdk library (OpenJDK installer))

☕ Java Environment:
  ✅ Java version: 24 (OpenJDK)
  📍 Java executable: /Users/ferreirat/miniforge3/envs/pysnt-dev/lib/jvm/bin/java
  🏠 JAVA_HOME: /Users/ferreirat/miniforge3/envs/pysnt-dev/lib/jvm

🔬 SNT/Fiji Environment:
  ✅ PySNT initialized: Yes
  ℹ️ ImageJ version: 2.17.0/1.54p
  ℹ️ SNT version: 4.9.9-SNAPSHOT-4896c9da7f9ebc6db367ec4fd8c222232f00b2ed

📁 Installation:
  📍 PySNT location: /Users/ferreirat/code/pysnt/src/pysnt

💻 System Information:
  OS: Darwin 25.0.0
  CPU: arm
  Memory: 48 GB total, 22 GB available
```

Now you can test that SNT access is fully functional:

```python
import pysnt
from pysnt import SNTService, Tree
pysnt.initialize_snt('~/Downloads/Fiji-SNTv5_pre-release_macOS/') # or simply pysnt.initialize_snt() if FIJI_PATH is set

snt_service = SNTService() # SNT's Scijava service
tree = snt_service.demoTree('fractal') # retrieve a toy neuron
tree.show() # display reconstruction
```

Because SNT is running headless, the reconstruction is displayed as ascii art in the console:
```
################################################################################
###########################  ######  #######  ######  ##########################
#######################  ##  ######  ##   ##  ######  ##  ######################
#######################      ######  #        ######  #   ######################
#########################    ######     ##    ######     #######################
###############  ########    ######    ###    ######    #########  #############
###########  ##  ##########  ######   ######  ######   ##########  ##  #########
###########   #  ##########   #####  #######   #####  ###########      #########
############     ###########  #####  ########  #####  ###########     ##########
#############    ###########   ###   ########   ###   ###########    ###########
##############   ############  ##   ##########  ##   ############   ############
####  #########   ###########  ##  ###########  ##  ############   #########  ##
####   #########  ###########   #  ###########   #  ############  #########   ##
#####   ########  ############     ############     ###########   ########   ###
##       #######   ############   ##############   ############  ########       
##         ######  ############   ##############   ############  ######         
########      ###   ###########  ###############  ############   ###     #######
##########     ###  ###########  ###############  ############  ###     ########
############        ###########  ###############  ###########        ###########
###############      ##########  ###############  ###########      #############
##################   ##########  ###############  ##########    ################
####################   ########  ###############  #########   ##################
#####################  ########  ###############  ########   ###################
#####################    ######  ###############  #######   ####################
#######################   #####  ###############  ######   #####################
########################   ####  ###############  ####    ######################
#########################  ####  ###############  ####   #######################
#########################    ##  ###############  ###   ########################
###########################   #  ###############  ##   #########################
############################     ###############      ##########################
#############################    ###############    ############################
##############################   ###############    ############################
###############################   ##############  ##############################
################################  ##############  ##############################
################################   ############   ##############################
#################################  ############  ###############################
#################################  ###########   ###############################
#################################   ##########  ################################
##################################   ########   ################################
###################################  ########  #################################
###################################  #######   #################################
###################################   ######  ##################################
####################################  ######  ##################################
####################################   ####   ##################################
#####################################  ####  ###################################
#####################################  ###   ###################################
#####################################   ##  ####################################
######################################  #   ####################################
####################################### #  #####################################
#######################################    #####################################
#######################################   ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
########################################  ######################################
```

## Troubleshooting

PySNT includes some Java management capabilities:

```python
from pysnt.java_utils import print_java_status
print_java_status() # check Java installation status
```

```python
import pysnt
pysnt.initialize_snt() # check Java installation and install OpenJDK if needed
```

### Manual Java Setup

```python
from pysnt.java_utils import ensure_java_available

# Ensure Java 21 or newer is available
ensure_java_available(required_version=21)
```

```python
from pysnt.java_utils import setup_java_environment
setup_java_environment()  # Interactive wizard for jdk installation (experimental)
```

```{note}
Do [reach out](https://forum.image.sc/tag/snt) if you run into issues!
```


[snt]: https://imagej.net/SNT
[api]: https://morphonets.github.io/SNT
[pyimagej]: https://github.com/imagej/pyimagej
[pyimagejdocs]: https://pyimagej.readthedocs.io/en/latest/
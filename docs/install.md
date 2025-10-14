# Installation

## Requirements


The stack of dependencies used by PySNT is rather complex and includes Python 3.8+, Java 21, [SNTv5 pre-relase](https://github.com/morphonets/SNT/releases), [imglyb](https://github.com/imglib/imglyb), [jgo](https://github.com/scijava/jgo), [numpy](https://github.com/numpy/numpy), [pyimagej][pyimagejdocs], [scyjava](https://github.com/scijava/scyjava), among others. Because of this complexity we recommend using a package manager. We endorse Mamba
since Conda can be painfully slow with complex environments. If you do not have Mamba installed you can do
so by [Installing Miniforge3](https://github.com/conda-forge/miniforge#miniforge3).

```{important}
In the future PySNT should be able to download OpenJDK 21, and SNT if not found. For now, these may need to be dowloaded manualy.
```

Here we only summarize the _easiest_ way to install pysnt. For other (advanced) install options (via pip, condacolab, dynamic install, etc.) you should be able to adapt the advanced install documentation of [pyimagej][pyimagejdocs].

## Setting Up

1. Assuming you have `mamba` installed, activate conda-forge:

   ```bash
   mamba config append channels conda-forge
   mamba config set channel_priority strict
   ```

2. Install the provided `environment.yml`

   ```bash
   cd to/pysnt/root/directory/
   mamba env create -f environment.yml
   ```

   This will install all of the key dependencies in a new environment called pysnt.

3. Install pysnt in editable/development mode

   ```bash
   mamba activate pysnt # activate the newly created environment
   pip install -e .
   ```

4. Test that PySNT has been successfully installed, by displaying its version:

   ```bash
   mamba activate pysnt # activate the newly created environment
   python -c 'import pysnt; print(f"Using PySNT version: {pysnt.version()}")'
   ```
   Which should print:
   ```bash
   0.0.1
   ```

4. At this point, it may be convenient to make the new `pysnt` environment available in the graphical 
   notebook interface (skip this step if you have no intention of using notebooks):

   ```bash
   mamba activate pysnt
   mamba install ipykernel
   python -m ipykernel install --user --name=pysnt
   ```

   Now, when you now start jupyter (or Jupyter lab), it will show `pysnt` in the list of registered
   kernels. Selecting it, makes all the packages installed in the `pysnt` environment available.


### Attaching to SNT

PySNT needs to connect to a local SNT install. This can be done in two ways: 1) By specifying a local Fiji
install already subscribed to the [NeuroAnatomy update site](https://imagej.net/SNT#install) (recommended)
or 2) by dynamic loading of a SNT binary that is downloaded in the background. Dynamic loading is done the
first time a SNT class is imported. Note this may take quite a long time (several minutes). Subsequent
runs should run without any lag. 

```{important}
Currently the dynamic option does not retrieve the latest version of SNT. Until SNTv5 is officially released,
it is best to point pyimagej to a SNT pre-release bundle:

1. Download a pre-release bundle from the [SNT Release Page](https://github.com/morphonets/SNT/releases).
   Unzip it to a local directory, e.g., `~/Downloads/`.

2. Point pysnt to the bundle:

   ```python
   import pysnt
   pysnt.initialize_snt(fiji_path="~/Downloads/Fiji-SNTv5_pre-release_macOS") # Specify path directly
    ```

```


## Verify Installation

Test your installation is fully functional by running:

```python
import pysnt
from pysnt import SNTService, Tree
pysnt.initialize_snt('~/Downloads/Fiji-SNTv5_pre-release_macOS/')

snt_service = SNTService() # Scijava service associated with SNT
tree = snt_service.demoTree('fractal') # retrieve a toy neuron
tree.show() # display it
```

Because SNT is running headless, the tree is displayed as ascii art in the console:
```python
>>> tree.show()

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
pysnt.initialize_snt() # check Java installation and install OpenJDK 21 if needed
```

### Manual Java Setup

```python
from pysnt.java_utils import ensure_java_available

# Ensure Java 21 is available
ensure_java_available(required_version=21)
```

```python
from pysnt.java_utils import setup_java_environment
setup_java_environment()  # Interactive wizard for jdk installation (experimental)
```

```{warning}
Running SNT from python is pretty much a bleeding edge experience. Things are being actively developed and some things may break. That being said, it is certainly possible (hundreds of people use it frequently). Your feedback is key! Please do [reach out](https://forum.image.sc/) if you run into issues.
```


## Next Steps

- Check out the [Getting Started notebook](notebooks/1_overview.ipynb)
- Browse the [Notebooks Gallery](notebooks/index.md)
- Read the [SNT User Manual](https://imagej.net/plugins/snt/)


[snt]: https://imagej.net/SNT
[api]: https://morphonets.github.io/SNT
[pyimagej]: https://github.com/imagej/pyimagej
[pyimagejdocs]: https://pyimagej.readthedocs.io/en/latest/
[pyimagej_intro]: https://nbviewer.jupyter.org/github/imagej/tutorials/blob/master/notebooks/1-Using-ImageJ/6-ImageJ-with-Python-Kernel.ipynb

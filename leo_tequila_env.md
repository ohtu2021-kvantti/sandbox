# Setting up Leo's conda env for tequila
```shell
# Create enviroment
conda create --name tequila

# Move to enviroment
conda activate tequila

# Install psi
conda install psi4 -c psi4

# Install pip and git
conda install pip git

# Install tequila
pip install git+https://github.com/aspuru-guzik-group/tequila.git
```

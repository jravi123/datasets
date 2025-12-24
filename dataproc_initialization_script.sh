# Install Miniconda / conda
./dataproc-initialization-actions/conda/bootstrap-conda.sh
# Update conda root environment with specific packages in pip and conda
CONDA_PACKAGES='panda beautifulsoup4'
CONDA_PACKAGES=$CONDA_PACKAGES PIP_PACKAGES=$PIP_PACKAGES ./dataproc-initialization-actions/conda/install-conda-env.sh
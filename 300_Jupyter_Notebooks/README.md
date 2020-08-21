# Overview

Jupyter notebooks, pandas, numpy, matplotlib

# Instructions


Jupyter notebooks (formerly known as iPython Notebooks) allow you to execute Python code via an interactive web interface.

It's great for exploratory data science and visualization and presentations. For "production workloads" or anything that runs in a non-interactive fashion, 
you would probably use a script instead.

There are a number of options for running Jupyter notebooks:

 * [Binder](https://mybinder.org/) lets you launch Jupyter notebooks. You can do so by clicking this button: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/agussman/a_python_tutorial/master) (note: if you've cloned the repo, you'll be launching the "original" code, not yours)
 * [AI Platform Notebooks](https://cloud.google.com/ai-platform-notebooks) in Google Cloud are a managed service for launching Jupyter notebooks. It's not free, but a new GCP account comes with credits.
* [Colaboratory](https://colab.research.google.com/) notebooks are essentially Jupyter notebooks.
* Download and run [Jupyter](https://jupyter.org/) locally (I recommend checking out [Jupyter Lab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html) if you haven't already)



Jupyter notebooks are fairly synonmous with three packages:
 * [pandas](https://pandas.pydata.org/) for data manipulation
 * [numpy](https://numpy.org/) array math and scientific computing
 * [matplotlib](https://matplotlib.org/) for visualizations

 These (plus some other useful packages) can be installed from the included `requirements.txt`:
 ```
 pip install -r requirements.txt
 ```

If you're launching the notebook from Binder it will automatically install the contents of `requirements.txt`. Those packages will also be available by default in Colab.

Jupyter notebooks typically have the file extension `.ipynb`. Go ahead and view the included notebook(s) in Jupyter

 * `sample_visualizations.ipynb` - basic data ingest and visualization

If you look at the file directly, you'll see that it's not really human-readable. It's still a good idea to keep your notebooks versioned with git, but keep in mind that a) understanding changes (e.g., "diffs") won't really work without special tools and b) they can grow to be large in size.
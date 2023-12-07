# Instructions to RUN LM-SD and LM-Human on Local Machine

- Download and place the **config** folders, which are used by the Language Models For Training/Fine-tuning
- The fine-tuned models are too large to be uploaded here, so we are linking them in corresponding and **model** folders.

## Required Libraries:
```
conda create -n "myenv" python==3.9.16 ipython
conda activate myenv

pip install --upgrade pip
pip install --upgrade setuptools
pip install --upgrade wheel

pip install notebook
pip install ipywidgets
python -m ipykernel install --user --name=myvenv

pip install -U spaczz
pip install -U rdflib
pip install -U coreferee
pip install -U print-dict
pip install -U matplotlib
pip install -U pandas
pip install -U openpyxl
pip install -U nervaluate

pip install -U spacy==3.6.1
python -m spacy download en_core_web_lg
python -m spacy download en_core_web_trf
```
-----------------------------------------------------------------------------------------------------------------------
## Optional for using Google Colab Notebook with Local Runtime
```
pip install jupyter_http_over_ws
jupyter serverextension enable --py jupyter_http_over_ws
```
#### If the above installation does not work you should install them via conda-forge:
```
pip uninstall jupyter_http_over_ws
conda install -c conda-forge jupyter_http_over_ws
jupyter serverextension enable --py jupyter_http_over_ws
```
#### Follow this link to know more:
    `https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment`
-----------------------------------------------------------------------------------------------------------------------

## GPU Support - (Preferred Way)
```
conda install pytorch torchvision torchaudio pytorch-cuda=11.7 -c pytorch -c nvidia
conda install -c conda-forge spacy==3.5.0
conda install -c conda-forge cupy
```

#### OR use the one below if you are in a Colab environment - (Not Recommended)
```
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117
pip install -U spacy==3.5.0
pip install -U spacy[cuda-autodetect]
```

#### <ins>Note</ins>:
  - Make sure you have CUDA enabled on your computer.
  - Optional - For Windows, GPU support might also need to have cl.exe in the PATH of your Environment Variable
  - Instructions Below: <br>
      `https://stackoverflow.com/questions/8125826/error-compiling-cuda-from-command-prompt`
  - For example, if you have Microsoft Visual Studio 2019, the path to cl.exe would probably be in the: <br>
      `PATH="C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\bin\Hostx64\x64"`
-----------------------------------------------------------------------------------------------------------------------

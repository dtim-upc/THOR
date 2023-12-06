## <ins>T</ins>ext <ins>H</ins>omogenization from <ins>O</ins>blivion to <ins>R</ins>eality (**THOR**)
### Codebase for ICDE Paper:
#### "**Mitigating Data Sparsity in Integrated Data through Text Conceptualization**"
---
### <ins>How to Run THOR</ins>:
1) Open the [**THOR_Conceptualization.ipynb**](https://github.com/dtim-upc/THOR/blob/main/THOR_Conceptualization.ipynb) script and click on the **Open In Colab** Button.
2) Run the script from **Runtime ->  Run All**
3) It will automatically Download our Disease A-Z Dataset from the repository.
4) At the bottom of the notebook in the **Main Function** you will be asked which EVALUATION set you want to use OR if you want to do only INFERENCING.
      - **EVALUATION:** This will RUN the Evaluation for the selected split, and save the **RESULTS** (2 Excel Files) in the "**output**" Folder.
        - By **Default** the **Threshold** is set to **T=0.8** (80%). In order to change the threshold, please change this line in Main Function:<br>
                      `matcher = initiate_matcher(patterns=accu_data, threshold=80)`
      - **INFERENCING:** In order inference on your own text:
        - UPLOAD ONE TEXT (.txt) DOCUMENT (per-run) containing Disease and Condition related information (from your device) by clicking on **Choose Files** button.

**NOTE:** Running on the Colab might take up-to 3x inference time due to the slow I/O bandwidth of Colab.



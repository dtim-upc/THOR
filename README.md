## <ins>T</ins>ext <ins>H</ins>omogenization from <ins>O</ins>blivion to <ins>R</ins>eality (**THOR**)
### Codebase for ICDE 2024 Paper:
#### "**Mitigating Data Sparsity in Integrated Data through Text Conceptualization**"
---
### <ins>How to Run THOR</ins>:
1) Open the [**THOR_Conceptualization.ipynb**](https://github.com/dtim-upc/THOR/blob/main/THOR_Conceptualization.ipynb) script and click on the **Open In Colab** Button.
2) Run the script from **Runtime ->  Run All**
3) It will automatically Download our Disease A-Z Dataset from the repository.
4) At the bottom of the notebook, in the **Main Function**, you will be asked which EVALUATION set you want to use OR if you want to do only INFERENCING.
      - **EVALUATION:** This will RUN the Evaluation for the selected split, and save the **RESULTS** (2 Excel Files) in the "**output**" Folder.
        - By **Default** the **Threshold** is set to **T=0.7** (70%). In order to change the threshold, please change this line in Main Function:<br>
                      `matcher = initiate_matcher(patterns=accu_data, threshold=70)`
      - **INFERENCING:** In order inference on your own text:
        - UPLOAD ONE TEXT (.txt) DOCUMENT (per-run) containing Disease and Condition related information (from your device) by clicking on **Choose Files** button.

### <ins>How to Run Baseline</ins>:
  - Follow the same instructions as above to run the [**Baseline.ipynb**](https://github.com/dtim-upc/THOR/blob/main/Baseline.ipynb).

### <ins>How to Run LM-SD/LM-Human</ins>:
  - The [**LM-SD.ipynb**](https://github.com/dtim-upc/THOR/blob/main/LM-SD.ipynb) and [**LM-Human.ipynb**](https://github.com/dtim-upc/THOR/blob/main/LM-Human.ipynb) **NEEDS GPU** in order to run.
  - Colab Free offers a limited GPU option; thus, we assume you have access to either Colab Pro or a Local GPU (at least 6GB VRAM).
  - Please follow the **instructions** inside the [**model_config**](https://github.com/dtim-upc/THOR/tree/main/model_config) folder.

### <ins>How to Run UniversalNER</ins>:
  - The [**UniversalNER.ipynb**](https://github.com/dtim-upc/THOR/blob/main/UniversalNER.ipynb) also requires a **Big GPU** (**Minimum 40 GB VRAM**) with at least 32 GB of system RAM.
  - You need to UPLOAD the test data [**Masked_Text_Only_Test.json**](https://github.com/dtim-upc/THOR/blob/main/Dataset/Masked_Text_Only_Test.json) into the same directory as the code.
    - To run in **Colab**, upload it into the local cache directory: `'/content/Masked_Text_Only_Test.json'`

### <ins>GPT-4</ins>:
  - Please follow the content of the [**GPT-4**](https://github.com/dtim-upc/THOR/tree/main/GPT-4) folder in order to reproduce this experiment.

**NOTE:** Running on the Colab might take up-to 3x inference time due to the slow I/O bandwidth of Colab.

---
### <ins>EXPERIMENTAL RESULTS</ins>:
  - You can find all the evaluation scores (.xlsx) in the [**Results**](https://github.com/dtim-upc/THOR/tree/main/Results) folder.
  - We followed the [**Evaluation Scheme**](https://github.com/MantisAI/nervaluate) proposed in SemEval 2013 for the Entity Recognition Task (9.1)



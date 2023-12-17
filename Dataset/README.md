# Dataset: Disease/Conditions A-Z

## Evaluation Settings and Splits

For our comparative evaluation, we utilize the **test** portion of our annotated text dataset (refer to Table: Annotated Text Dataset Statistics). The task-specific fine-tuning employs the **structured data** for **LM-SD**, and the same data is used to build patterns for the **Baseline** and to fine-tune the embedding vector in our approach, **THOR**. The **LM-Human** is fine-tuned with a contextualized **training** set from the annotated text. For both language models, the **validation** data is used to learn optimal hyperparameters.

The text dataset is split based on the **Diseases** files, aiming to distribute the total number of entities into approximately 70% for training, 20% for validation, and 10% for testing. There are some deviations in the entity counts due to the difficulty in splitting them exactly into 70/20/10 percentages.

### Annotated Text Dataset (Disease A-Z) Statistics

| \#          | Training | Validation | Test | Total  |
|-------------|----------|------------|------|--------|
| Disease     | 240      | 61         | 13   | 314    |
| Documents   | 1438     | 366        | 90   | 1894   |
| Entities    | 18539    | 3989       | 2222 | 24750  |
| Relations   | 10269    | 2145       | 867  | 13281  |
| Tokens      | 168816   | 38722      | 19237| 226775 |

### Statistics of Structured Data

| Sources | Concepts | Instances | Tokens |
|---------|----------|-----------|--------|
| 10      | 11       | 4706      | 14010  |

## Disease/Conditions A-Z Dataset Description

We consider a health-related data scenario containing **Disease A-Z** information with **Conditions**. The following sections describe the data sources and schema used.

### Structured Data Sources and Integrated Schema

Our structured data sources contain disease and condition information in tabular format (CSVs), following the integrated schema (Fig. Schema). Each structured data source contains two columns relating concepts such as **Disease** and **Anatomy** or **Surgery** and **Anatomy**. We have 10 structured sources containing instances of 11 concepts.

![The Integrated Schema for our Use Case Datasets](images/disease_schema.png)

---

### Text Data Sources

To address data sparsity via enrichment during data integration, our intrinsic evaluation accounts for a wide variety of entity types and a complex schema. We annotated a text dataset with concepts and relations shown in our schema (Fig. Schema). The dataset aggregates **Disease/Conditions A-Z** information from major health portals like WHO, NHS, and CDC. We manually collected texts about 314 diseases, organized into up to eight different text documents per condition.

#### <ins>Text Data Annotation Guidelines</ins>

The following guidelines pertain specifically to the Text Data Annotation portion of our dataset. Each text file has been named according to the corresponding ICD11 disease code, adhering to the International Classification of Diseases 11th edition, which can be found at [ICD-11](https://icd.who.int/ct11/icd11_mms/en/release).

To facilitate Named Entity Recognition and Relation Extraction, we have compiled a comprehensive health dataset encompassing detailed information on individual diseases. From an initial compilation of information on approximately 1100 diseases, a total of 314 diseases have been meticulously annotated. Our annotation efforts have been focused on ensuring the highest quality of data by incorporating punctuation corrections, integration of abbreviations, processing of bullet points, and integration of disease codes. The guidelines adhered to in the annotation process are as follows:

- Initialization of entity labels and relation labels to set the foundation for the annotation framework.
- Development of a specialized schema tailored for the annotation task, serving as a structured guideline.
- Marking of words followed by the selection of appropriate labels from the predefined set.
- Identification and establishment of dependencies between entities, followed by the addition of these into a corresponding relation, chosen from a list of available relation labels.
- Rigorous validation of chosen relations against the schema to ensure consistency and accuracy.

By strictly following these guidelines, we aim to create a dataset that is not only precise but also aligns with the intended use-case scenarios.

#### Annotation Tool and Sample

We utilized the open-source tool [doccano](https://doccano.github.io/doccano/) to annotate our dataset. The annotation process involves identifying and labeling entities such as diseases, symptoms, and anatomy, as well as the relations between them, such as causality and symptoms association.

The following image represents a snippet of our annotated text, showcasing how entities and relations are structured within the dataset:

![Annotated Text Sample](images/annotated_text.png)

*Figure: A snippet of the annotated text showing entities and relations for Tuberculosis.*

Entities are denoted with suffix `_E` and relations with `_R`, allowing for a clear and concise representation of complex medical information. This structured annotation facilitates the training of models for Named Entity Recognition and Relation Extraction tasks.

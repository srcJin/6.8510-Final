# SentiScribe: Multimodal Fusion for Sentiment Analysis

SentiScribe is a comprehensive toolset for analyzing sentiment and emotion from multimodal data sources such as MELD datasets and Zoom recordings. This project integrates various data processing, visualization, and machine learning techniques to provide a robust analysis of conversational dynamics.


Jin Gao, Selena Zhang

Note: for the sake of size, we don't include the dataset video files in this reposotory. 

You can download the video files from https://affective-meld.github.io/

## File structure

Project Root
│
├── archive
│
├── data  -  processed files for zoom recordings
│   └── outputs
│       ├── dataframe
│       ├── gpt
│       ├── hume
│       ├── zoom
│       └── zoom_clipped
│           ├── processed_results.csv
│           └── processed_results.json
│
└── dataset  -  processed files for MELD Dataset
    └── outputs
        ├── dev_result - dev dataset outputs
        ├── hume - original outputs from hume api call 
        ├── merged_all - processed and merged files for further prediction
        ├── dev_sent_emo.csv - metadata for MELD dev datasets
        └── train_sent_emo.csv - metadata for MELD test datasets
│
├── HTML_UI
│   ├── .vscode
│   ├── UI_Dataset - HTML UI for Dataset visualization
│   └── UI_Zoom - HTML UI for Zoom visualization
│
└── Root Directory Files
    ├── .env - configure your API keys
    ├── .env_template

    Step 1: Dataset Preparation

    ├── API_Workflow_1_dataset_preparation.ipynb -- slice and process MELD Datasets
    ├── API_Workflow_1_dataset_preparation_reversed.ipynb  -- slice and process MELD Datasets reversly, can be used together with the non-reversed notebook for parallel processing.
    ├── Product_Workflow_Zoom_Processing.ipynb  -- slice and process zoom recordings


    Step 1.5: Visualize the dataset, and Test using ChatGPT

    ├── API_Workflow_1.5_Test_on_ChatGPT_API.ipynb - Test for MVP using ChatGPT to process conversation level sentiments
    ├── API_Workflow_1.5_Visualization.ipynb - Visualize porosody to see the dynamic of changing sentiments
    ├── visualization_dataset.png - visualization result on MELD dataset
    ├── visualization_zoom.png - visualization result on Zoom recordings

    Step 2: Merge the data for prediction

    ├── API_Workflow_2_merge_modalities.ipynb

    Step 3: Prediction emotions using different methods

    ├── API_Workflow_3_performance_experiments_traindataset.ipynb
    ├── API_Workflow_3_performance_experiments.ipynb
    ├── emotion_mappings.ipynb


    Presentation Movie:
    ├── presentation_movie.mp4

    Others:
    ├── .gitignore
    ├── README.md
    ├── requirements.txt
    └── LICENSE


## Getting Started

1. **Environment Setup**:
   - Begin by cloning the repository and navigating into the project directory.
   - Set up your Python environment using the provided `.env_template`. Rename this file to `.env` and configure it with your local settings or API keys as needed.

    ```
    OPENAI_API_KEY=
    HUME_API_KEY=
    ```

   - Install all required dependencies listed in `requirements.txt` by running:
     ```bash
     pip install -r requirements.txt
     ```

   We recommend python 3.10+ for running this project.

2. **Data Preparation**:
   - Use the `API_Workflow_1_dataset_preparation.ipynb` to prepare your dataset. This notebook likely contains scripts to fetch, clean, and structure the data needed for sentiment analysis.
   - The `API_Workflow_1_dataset_preparation_reversed.ipynb` might be used for a similar purpose but perhaps processes the data in a different order or method.

3. **Testing and Visualization**:
   - Execute `API_Workflow_1.5_Test_on_ChatGPT_API.ipynb` to test how the ChatGPT API responds to your dataset, which can be crucial for understanding model interactions.
   - Visualize your data or model outputs with `API_Workflow_1.5_Visualization.ipynb` to inspect distributions, patterns, or anomalies.

4. **Merging Modalities**:
   - The `API_Workflow_2_merge_modalities.ipynb` is used for combining different types of data (like text, audio, or video) that are relevant for your multimodal sentiment analysis.

5. **Performance Experiments**:
   - Conduct performance experiments using `API_Workflow_3_performance_experiments.ipynb` to evaluate the effectiveness of your sentiment analysis model across different settings or parameters.
   - The `API_Workflow_3_performance_experiments_traindataset.ipynb` might focus specifically on training dataset configurations and their impact on model performance.


## Project Structure

The project is organized into several directories:

- **archive**: Stores archived files.
- **data**: Contains processed files for Zoom recordings.
  - **outputs**: Includes subdirectories for each processing stage (`dataframe`, `gpt`, `hume`, `zoom`, `zoom_clipped`).
- **dataset**: Holds processed files for MELD Dataset.
  - **outputs**: Contains specific outputs like development and test dataset results.
- **HTML_UI**: Contains HTML interfaces for data visualization.
- **Root Directory Files**: Includes configuration files, notebooks for various workflows, and other necessary files.

#### MELD Datasets

- `API_Workflow_1_dataset_preparation.ipynb`: Processes the MELD datasets.
- `API_Workflow_1_dataset_preparation_reversed.ipynb`: Processes the MELD datasets in reverse order; useful for parallel processing.

#### Zoom Recordings

- `Product_Workflow_Zoom_Processing.ipynb`: Processes Zoom recordings to extract relevant data.

### Visualization and Testing

- `API_Workflow_1.5_Test_on_ChatGPT_API.ipynb`: Tests the processed data using the ChatGPT API to simulate conversation-level sentiment analysis.
- `API_Workflow_1.5_Visualization.ipynb`: Visualizes the dynamics of sentiment changes within the conversations.
- **Visualizations**:
  - `visualization_dataset.png`
  - `visualization_zoom.png`

### Data Merging

- `API_Workflow_2_merge_modalities.ipynb`: Merges different modalities prepared in earlier steps for comprehensive analysis.

### Emotion Prediction

- `API_Workflow_3_performance_experiments.ipynb`: Conducts performance experiments on the train dataset.
- `emotion_mappings.ipynb`: Maps detected emotions to predefined categories.


## HTML_UI

- You can navigate to the HTML_UI folder, use VS Code plugin including Live Server or Five Server, to browse the HTML pages as a website.

## Presentation

- **Movie**: Watch `presentation_movie.mp4` for a visual explanation of the project and its findings.


## Contributing

Feel free to fork the repository, make changes, and submit pull requests. Contributions to extend the functionality or improve the project are welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Generate requirements.txt

```
pip install pipreqs --user
python -m  pipreqs.pipreqs ./
```

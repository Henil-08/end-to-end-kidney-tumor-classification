# End-to-End Kidney Tumor Classification Project

## Overview

This project aims to develop an end-to-end machine learning pipeline for classifying kidney tumors. It involves data ingestion, model preparation, training, evaluation, and deployment using various tools and technologies such as MLflow, DVC, Docker, AWS ECR, and EC2. The final model is deployed as an HTML-based website for easy access and interaction.


## Project Structure
'''
├── artifacts
│   ├── data_ingestion
│   ├── prepared_base_model
│   └── training
├── model
├── research
├── pipeline
│   ├── data_ingestion.py
│   ├── prepare_base_model.py
│   ├── train_model.py
│   ├── evaluate_model.py
├── app.py
├── main.py
├── Dockerfile
├── dvc.yaml
├── params.yaml
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
'''


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py


## Pipeline DAG
'''
+----------------+            +--------------------+ 
| data_ingestion |            | prepare_base_model | 
+----------------+*****       +--------------------+ 
         *             *****             *
         *                  ******       *
         *                        ***    *
         **                        +----------+      
           **                      | training |      
             ***                   +----------+
                ***             ***
                   **         **
                     **     **
                  +------------+
                  | evaluation |
                  +------------+
'''




## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.


## License
This project is licensed under the MIT License.


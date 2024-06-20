# House-Price-Prediction-Model

In this repository, you will find a simple machine-learning model built and deployed to predict house prices based on the data it is trained on.

## Data Frame

The data frame used to train this model contains the following features for each house:
- **Area**
- **Number of Bedrooms**
- **Age** 
- **Price**

## Model

For this model, a multiple linear regression algorithm was implemented using supervised machine learning. The model can predict house prices once trained on the provided data frame.

## Steps to Run the Model

### 1. Analyze and Visualize Data

- Open the `Project_2.ipynb` Jupyter notebook file.
- This file contains code to analyze and visualize the data.
- Run all cells in the notebook to see the data analysis and visualization results.

### 2. Train the Model and Create a Pickle File

- In the latter part of the `Project_2.ipynb` notebook, the `pickle` module is imported.
- The model is trained, and a pickle file `house.pkl` is created, which converts the model object into a byte stream. This file is essential for displaying the model on a GUI.

### 3. Run the Model with GUI

- Use the `myfile.py` script to run the `house.pkl` file and interact with the model through a graphical user interface (GUI).
- Ensure you have all the required dependencies installed. You can install them using the following command:
  ```bash
  pip install -r requirements.txt
  ```
- Execute the Python script:
  ```bash
  python myfile.py
  ```

By following these steps, you will be able to visualize the data, train the model, and interact with it through a GUI to predict house prices.

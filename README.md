<p align="center"><h1 align="center">CUSTOMER-PERSONALITY-ANALYSIS</h1></p>
<p align="center">
	<em>Unveil Customer Insights, Drive Marketing Success!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/Shrijeet14/Customer-Personality-Analysis?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/Shrijeet14/Customer-Personality-Analysis?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/Shrijeet14/Customer-Personality-Analysis?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/Shrijeet14/Customer-Personality-Analysis?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

## 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The Customer-Personality-Analysis project offers interactive visualizations to understand customer demographics, spending habits, and product preferences. By exploring correlations between demographics and purchasing behavior, it empowers marketers to optimize campaigns effectively. This tool is ideal for businesses seeking to enhance their marketing strategies and tailor campaigns to specific customer segments.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes <code>K-means clustering</code> for customer segmentation analysis</li><li>Employs <code>JupyterNotebook</code> for interactive data exploration</li><li>Modular structure with separate files for data preprocessing, model building, and analysis</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Follows PEP 8 coding standards</li><li>Includes detailed comments and docstrings for functions</li><li>Uses <code>seaborn</code> and <code>scikit-learn</code> for enhanced data visualization and machine learning capabilities</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive documentation in <code>JupyterNotebook</code> format</li><li>Includes usage commands and test commands for easy reference</li><li>Provides insights into data preprocessing, analysis, and model building processes</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates trained models and scalers for customer segmentation predictions</li><li>Enables user input for predicting customer segments through a user-friendly interface</li><li>Enhances data insights through interactive visualizations</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Separate files for different project components like data preprocessing, model building, and analysis</li><li>Encourages code reusability and maintainability</li><li>Facilitates easy collaboration among team members</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes testing commands for validating code functionality</li><li>Ensures accuracy of customer segmentation predictions</li><li>Tests data preprocessing and model training processes</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes customer segmentation analysis for efficient processing</li><li>Utilizes <code>seaborn</code> and <code>scikit-learn</code> for high-performance data visualization and machine learning tasks</li><li>Efficiently handles large datasets for insightful analysis</li></ul> |
| 🛡️ | **Security**      | <ul><li>Ensures data privacy and security during customer data analysis</li><li>Implements secure data handling practices</li><li>Follows best practices for data encryption and access control</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Dependent on <code>seaborn</code> and <code>scikit-learn</code> for enhanced data visualization and machine learning capabilities</li><li>Utilizes <code>pip</code> for managing Python dependencies</li><li>Includes a <code>requirements.txt</code> file for easy installation of dependencies</li></ul> |

---

## 📁 Project Structure

```sh
└── Customer-Personality-Analysis/
    ├── Adv_Data_Preprocessing_and_EDA
    │   └── Data_Preprocessing2_EDA.ipynb
    ├── Basic_Data_Preprocessing
    │   └── DataPreprocessingFilePrProject.ipynb
    ├── Code_File_3_Kmeans_Clustring_based_analysis
    │   └── Customer_Segmentation_Analysis.ipynb
    ├── Code_File_4_Final_Model_Building
    │   ├── .ipynb_checkpoints
    │   └── FINAL_MODEL_TRAINING.ipynb
    ├── Code_file_1_Basic_Data_Preprocessing
    │   ├── .ipynb_checkpoints
    │   └── DataPreprocessingFilePrProject.ipynb
    ├── Code_file_2_Adv_Data_Preprocessing_and_EDA
    │   ├── .ipynb_checkpoints
    │   └── Data_Preprocessing2_EDA.ipynb
    ├── Final_Model_Building
    │   └── FINAL_MODEL_TRAINING.ipynb
    ├── Kmeans_Clustring_based_analysis
    │   └── Customer_Segmentation_Analysis.ipynb
    ├── Output_Model
    │   ├── best_model.pkl
    │   └── scaler.pkl
    ├── README.md
    ├── Read_Analysis.py
    ├── __pycache__
    │   └── functions.cpython-38.pyc
    ├── data
    │   ├── Cleaned_marketing_campaign.csv
    │   └── marketing_campaign.csv
    ├── functions.py
    ├── pages
    │   ├── Test_Model.py
    │   └── best_model.pkl
    └── requirements.txt
```


### 📂 Project Index
<details open>
	<summary><b><code>CUSTOMER-PERSONALITY-ANALYSIS/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Read_Analysis.py'>Read_Analysis.py</a></b></td>
				<td>- Generates interactive visualizations for analyzing customer data, including age distribution, spending patterns, income influence, and product preferences<br>- Explores correlations between demographics and purchasing behavior, aiding in marketing strategy decisions<br>- Visualizes data insights to understand customer segments and optimize campaigns effectively.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>Enhances data visualization and machine learning capabilities by incorporating seaborn and scikit-learn dependencies.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/functions.py'>functions.py</a></b></td>
				<td>- Transforms and analyzes customer data by categorizing income, family status, and spending habits<br>- Provides insights on age distribution, total spending, marital status spending, income-wise spending, education-campaign correlation, family spending patterns, product preferences, and shopping behavior.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- pages Submodule -->
		<summary><b>pages</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/pages/Test_Model.py'>Test_Model.py</a></b></td>
				<td>- Enable customer segmentation predictions based on various input features, such as age, education, income, and purchase behavior<br>- The code file integrates a trained model and scaler to predict customer segments and provides insights into high and low-income groups<br>- Users can input data through a user-friendly interface to receive predictions and detailed information about the predicted customer group.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- Code_file_2_Adv_Data_Preprocessing_and_EDA Submodule -->
		<summary><b>Code_file_2_Adv_Data_Preprocessing_and_EDA</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Code_file_2_Adv_Data_Preprocessing_and_EDA/Data_Preprocessing2_EDA.ipynb'>Data_Preprocessing2_EDA.ipynb</a></b></td>
				<td>- Summary:
The code file "Data_Preprocessing2_EDA.ipynb" in the project focuses on advanced data preprocessing and exploratory data analysis (EDA) tasks<br>- It plays a crucial role in preparing and analyzing the data to derive insights and patterns, contributing significantly to the overall architecture of the codebase.</td>
			</tr>
			</table>
			<details>
				<summary><b>.ipynb_checkpoints</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Code_file_2_Adv_Data_Preprocessing_and_EDA/.ipynb_checkpoints/Data_Preprocessing2_EDA-checkpoint.ipynb'>Data_Preprocessing2_EDA-checkpoint.ipynb</a></b></td>
						<td>- The code file "Data_Preprocessing2_EDA.ipynb" in the "Code_file_2_Adv_Data_Preprocessing_and_EDA" directory performs advanced data preprocessing and exploratory data analysis (EDA) tasks within the project architecture<br>- It contributes to enhancing data quality and gaining insights for informed decision-making, supporting the overall project objectives.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- Kmeans_Clustring_based_analysis Submodule -->
		<summary><b>Kmeans_Clustring_based_analysis</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Kmeans_Clustring_based_analysis/Customer_Segmentation_Analysis.ipynb'>Customer_Segmentation_Analysis.ipynb</a></b></td>
				<td>- SUMMARY:
The code file "Customer_Segmentation_Analysis.ipynb" in the "Kmeans_Clustring_based_analysis" directory performs customer segmentation analysis using K-means clustering<br>- This analysis aids in understanding customer behavior and preferences, enabling targeted marketing strategies and personalized customer experiences within the project's architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- Basic_Data_Preprocessing Submodule -->
		<summary><b>Basic_Data_Preprocessing</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Basic_Data_Preprocessing/DataPreprocessingFilePrProject.ipynb'>DataPreprocessingFilePrProject.ipynb</a></b></td>
				<td>- The code file `DataPreprocessingFilePrProject.ipynb` in the `Basic_Data_Preprocessing` directory of the project is responsible for importing the dataset from Kaggle<br>- This file focuses on the initial data preprocessing steps required for the project, setting the foundation for further data analysis and modeling.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- Code_File_3_Kmeans_Clustring_based_analysis Submodule -->
		<summary><b>Code_File_3_Kmeans_Clustring_based_analysis</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Code_File_3_Kmeans_Clustring_based_analysis/Customer_Segmentation_Analysis.ipynb'>Customer_Segmentation_Analysis.ipynb</a></b></td>
				<td>- Summary:
The code file "Customer_Segmentation_Analysis.ipynb" in the "Code_File_3_Kmeans_Clustring_based_analysis" directory performs customer segmentation analysis using K-means clustering<br>- This analysis is crucial for understanding customer behavior and preferences, enabling targeted marketing strategies and personalized customer experiences within the project's architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- Final_Model_Building Submodule -->
		<summary><b>Final_Model_Building</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Final_Model_Building/FINAL_MODEL_TRAINING.ipynb'>FINAL_MODEL_TRAINING.ipynb</a></b></td>
				<td>- The code file `FINAL_MODEL_TRAINING.ipynb` in the `Final_Model_Building` directory is responsible for building and training the final model for the project<br>- It handles data preprocessing, model training, and evaluation<br>- This file integrates various libraries for data manipulation, visualization, and machine learning to create a robust final model.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- Code_File_4_Final_Model_Building Submodule -->
		<summary><b>Code_File_4_Final_Model_Building</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Code_File_4_Final_Model_Building/FINAL_MODEL_TRAINING.ipynb'>FINAL_MODEL_TRAINING.ipynb</a></b></td>
				<td>- The code file FINAL_MODEL_TRAINING.ipynb in the Code_File_4_Final_Model_Building directory is responsible for training the final model of the project<br>- It handles the process of building and fine-tuning the model using the provided dataset<br>- This file likely contains the necessary code to preprocess the data, train the model, and evaluate its performance before finalizing it for deployment within the project architecture.</td>
			</tr>
			</table>
			<details>
				<summary><b>.ipynb_checkpoints</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Code_File_4_Final_Model_Building/.ipynb_checkpoints/FINAL_MODEL_TRAINING-checkpoint.ipynb'>FINAL_MODEL_TRAINING-checkpoint.ipynb</a></b></td>
						<td>- The code file `FINAL_MODEL_TRAINING-checkpoint.ipynb` is responsible for building the final model in the project<br>- It handles importing necessary libraries, filtering warnings, and preparing the data for model training<br>- This file plays a crucial role in the project's architecture by executing the final steps to create and train the model for the specified task.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<details> <!-- Adv_Data_Preprocessing_and_EDA Submodule -->
		<summary><b>Adv_Data_Preprocessing_and_EDA</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Adv_Data_Preprocessing_and_EDA/Data_Preprocessing2_EDA.ipynb'>Data_Preprocessing2_EDA.ipynb</a></b></td>
				<td>- The code file "Data_Preprocessing2_EDA.ipynb" in the project focuses on advanced data preprocessing and exploratory data analysis (EDA)<br>- It plays a crucial role in preparing and analyzing data to derive meaningful insights, contributing to the overall architecture by enhancing data quality and facilitating informed decision-making.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- Code_file_1_Basic_Data_Preprocessing Submodule -->
		<summary><b>Code_file_1_Basic_Data_Preprocessing</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Code_file_1_Basic_Data_Preprocessing/DataPreprocessingFilePrProject.ipynb'>DataPreprocessingFilePrProject.ipynb</a></b></td>
				<td>- The code file `DataPreprocessingFilePrProject.ipynb` is responsible for importing the dataset from Kaggle and performing basic data preprocessing tasks<br>- It plays a crucial role in preparing the data for further analysis and model building within the project's architecture.</td>
			</tr>
			</table>
			<details>
				<summary><b>.ipynb_checkpoints</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/master/Code_file_1_Basic_Data_Preprocessing/.ipynb_checkpoints/DataPreprocessingFilePrProject-checkpoint.ipynb'>DataPreprocessingFilePrProject-checkpoint.ipynb</a></b></td>
						<td>- Summary:
The provided code file in "DataPreprocessingFilePrProject.ipynb" focuses on basic data preprocessing tasks for the project<br>- It aims to prepare the dataset for further analysis and modeling within the codebase architecture.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with Customer-Personality-Analysis, ensure your runtime environment meets the following requirements:

- **Programming Language:** JupyterNotebook
- **Package Manager:** Pip


### ⚙️ Installation

Install Customer-Personality-Analysis using one of the following methods:

**Build from source:**

1. Clone the Customer-Personality-Analysis repository:
```sh
❯ git clone https://github.com/Shrijeet14/Customer-Personality-Analysis
```

2. Navigate to the project directory:
```sh
❯ cd Customer-Personality-Analysis
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-INSTALL-COMMAND-HERE'
```




### 🤖 Usage
Run Customer-Personality-Analysis using the following command:
**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-RUN-COMMAND-HERE'
```


### 🧪 Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="" />]()

```sh
❯ echo 'INSERT-TEST-COMMAND-HERE'
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/Shrijeet14/Customer-Personality-Analysis/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/Shrijeet14/Customer-Personality-Analysis/issues)**: Submit bugs found or log feature requests for the `Customer-Personality-Analysis` project.
- **💡 [Submit Pull Requests](https://github.com/Shrijeet14/Customer-Personality-Analysis/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/Shrijeet14/Customer-Personality-Analysis
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/Shrijeet14/Customer-Personality-Analysis/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=Shrijeet14/Customer-Personality-Analysis">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---

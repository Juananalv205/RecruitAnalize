# Readme.md

This project focuses on the analysis of 50,000 applications in various work areas, with the objective of understanding the recruitment process in companies.

The following is a description of the structure of the branches used, the tools employed, the installation processes of libraries and other components, as well as the analysis of the dashboard necessary for this project, ensuring compliance with the established requirements.

---

## Technologies used

The technologies used for the creation of this project are listed below:

- **Python** 🐍
    - Libraries:
        - `Tabulate` 📊: For formatting data in tables.
        - `Pandas` 🐼: For data manipulation and analysis.
        - Numpy` 🔢: For efficient numerical operations.
        - `sys` ⚙️: For interacting with the system and manipulating environment variables.
        - os` 🖥️: To interact with the operating system.
        - `mysql.connector` 🗄️: To connect and execute MySQL queries.
        - `dotenv` 🔐: To load environment variables from an `.env` file.
- **Jupyter Notebooks** 📓: For developing and executing scripts in an interactive and controlled environment.
- **Clever Cloud** ☁️: For database management in the cloud.
- **Looker Studio** 📊: For data visualization and dashboard creation.
- **SQL** 🗃️: As a relational database management system.
- **Git** 🔧: For project version control.
- **GitHub** 🐙: To host the project repository and facilitate collaboration.
- Notion** 📝: For task management and project documentation.

---

## Explanation of the project structure:

```bash
This project is organized into several folders and files, each fulfilling a specific role in the workflow. The structure of the project is described below:
├───data.
│ └└───raw.
│       └└────candidates (1).csv #Dirty dataset.
├────docs.
│     └└───Workshop -001 Data engineer.pdf #Requirements.
├────notebooks.
│    └└───000_data_load.ipynb #Data_load.
│    └└───001_data_exploration.ipynb #Exploratory data analysis.
│    └└───002_data_cleaning.ipynb #Data cleaning and loading.
├────reports.
│    └└────Candidates dashboard.pdf #Dashboard on candidates.
├────sql.
│ └────queries.
│      └└───count_data.sql #SQL query to count records in a table.
│      └└───delete_data.sql #SQL query to delete all records in a table.
│      └└───drop_table.sql #Sql query to delete table.
│      └└───get_rows.sql #SQL query to get all rows.
│      └└───insert_data.sql #Sql query to insert data.
│      └└───schema.sql #Database schema.
└└───src
│    └└───data.
│    └└───load_data.py #Functions for uploading data to Clever Cloud.
│    └└───database.py #Functions to perform database connection and queries.
└└───requirements.txt # Project requirements.
```

---

## Structure of the project branches

![Sin título-2024-08-27-1144.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/6afc3ed2-036b-4c6e-9c9e-8825242df6e9/e780338f-7768-44f6-b5c8-b275dfce7247/Sin_ttulo-2024-08-27-1144.png)

## Branch 'data_load' 📥

This branch handles the process of creating the `load_data.py` and `database.py` functions, as well as converting the Excel file to a DataFrame using the **Pandas** library. After this process, the data is batch loaded into the Clever Cloud database. At this point in the data ingestion, the following steps were performed:

1. **Record insertion:** The first 10 records were inserted.
2. **Batch upload:** The upload was continued in batches of 1000 records each. In the event of a problem occurring during loading, the process would be cancelled and the exact point at which data ingestion stopped would be returned, thus avoiding loss of progress. This is possible thanks to the use of a unique identifier.

## Branch 'eda' 📊

- The The dataset contains the following columns:
    - 'First Name'
    - 'Last Name'
    - 'Email'
    - 'Country'
    - 'Application Date
    - 'Yoe (years of experience)' 'Seniority
    - Seniority
    - Technology
    - Code Challenge Score
    - Technical Interview

This branch is responsible for exploratory data analysis (EDA), specifically examining each column to determine the type of data and its respective information.

### Key findings:

- ❌ There are no records for the entire year 2022, as the data goes up to a certain point in the year.
- 📊 The dataset contains a total of 50,000 records.
- ✅ The dataset contains no null values.
- 🆔 The main identifier of the dataset is 'id'.
- 📋 The dataset contains 3 categorical columns: 'Country', 'Seniority' and 'Technology'.
- 🔢 The dataset contains 3 discrete columns: 'Yoe', 'Code' 'Challenge Score' and 'Technical Interview Score'.
- ⚠️ The dataset contains 1 erroneous column, 'Application Date'.
- 🛠️ For the cleanup process, it was found necessary to group the data in the 'Technology' column, as there are several redundant roles that can be simplified.
- ✏️ It is recommended to rename the 'Yoe' column to 'Years_of_Experience' for better understanding.
- 📉 The minimum score received for the code test is 0 and the maximum score is 10.
- ⚖️ The mean of the results in the code test is 4.9964 and the median is 5.0, indicating that more than half of the applicants did not pass, as the minimum grade required was 7.
- 📉 The minimum grade received for the technical test is 0 and the maximum grade is 10.
- ⚖️ The mean of the results of the technical test is 5.00388 and the median is 5.0, which indicates that more than half of the applicants did not pass, since the minimum grade required was 7.

## Branch 'ETL' 🛠️

- The categories in the 'Technology' column were grouped as follows:
    
    ```python
    mapping_dict = {
        'Game Development': 'Desarrollo de Software',
        'Development - Backend': 'Desarrollo de Software',
        'Development - FullStack': 'Desarrollo de Software',
        'Development - Frontend': 'Desarrollo de Software',
        'Development - CMS Backend': 'Desarrollo de Software',
        'Development - CMS Frontend': 'Desarrollo de Software',
        'Mulesoft': 'Desarrollo de Software',
        'Adobe Experience Manager': 'Desarrollo de Software',
        'System Administration': 'Administración y Gestión',
        'Database Administration': 'Administración y Gestión',
        'Business Analytics / Project Management': 'Administración y Gestión',
        'Sales': 'Administración y Gestión',
        'Data Engineer': 'Ingeniería de Datos',
        'Security': 'Seguridad',
        'Security Compliance': 'Seguridad',
        'Design': 'Diseño y Experiencia de Usuario',
        'QA Manual': 'Diseño y Experiencia de Usuario',
        'QA Automation': 'Diseño y Experiencia de Usuario',
        'Technical Writing': 'Diseño y Experiencia de Usuario',
        'Social Media Community Management': 'Marketing y Gestión de Redes Sociales',
        'DevOps': 'Otras Tecnologías y Habilidades',
        'Client Success': 'Otras Tecnologías y Habilidades',
        'Salesforce': 'Otras Tecnologías y Habilidades',
        'Business Intelligence': 'Otras Tecnologías y Habilidades'
    }
    ```
    

- Changed the data type of the 'Application Date' column to date format 📅.
- Renamed the 'Yoe' column to 'Years_of_Experience' for better understanding.
- After completing these changes, the cleaned data is sent back to the 'Candidates' table, where it will soon be connected to the dashboard using Looker Studio 📊.

---

## Dashboard analysis 📊

After this process, a connection is made to Looker Studio, the result of which can be found in the file named 'Candidates_dashboard.pdf', located in the 'report' folder.

Several things can be concluded from this analysis:

1. 🧪 **Data distribution:** The data, being artificially generated, present a normal distribution.
2. 📉 **Decline in 2022:** It is observed that the number of applications in the year 2022 decreases drastically, but this is because there are no records for that entire year.
3. 🔍 **Distribution close to normal:** Being a distribution very close to normal and not having outliers, not many significant differences between the data can be observed.
4. 💻 **Most popular category:** The category with the most applications is “Software Development” with 34.7% (173,503 applications). The category with the least applications is “Data Engineering” with 3.9% (1,950 requests).
5. 🇨🇴 **Trend in Colombia:** Colombians' applications requests were steadily increasing from 2018 to 2020, when they ranked first. Subsequently, they began to decrease until 2022, when they share the same position as Brazil.
6. 🇧🇷 **Brazilian trend:** Brazilian applications were the highest from 2018 to 2019, then declined, but managed to regain the top spot in 2021. However, in 2022 they declined again, occupying the same position as Colombia.
7. 🇪🇨 **Trend in Ecuador:** Ecuadorians' application requests presented a large increase between 2018 and 2019, reaching the first position in applications. However, from 2019 to 2020, they had a big drop, managing to partially recover between 2020 and 2021, and ending 2021 sharing the position with the United States.
8. 🇺🇸 **U.S. trend:** U.S. applications showed a slight drop from 2018 to 2019. However, from 2019 to 2021, they managed to increase applications, peaking in 2020, ranking second.

---

## How to Clone and Use the Repository? 🛠️

For a correct use it is necessary to follow the following steps:

1. Clone the repository📁 2.
    
    First, clone the repository and navigate to the project directory:
    
    ```bash
    git clone https://github.com/Juananalv205/Workshop--001-Data-engineer.git
    cd Workshop--001-Data-engineer
    
    ```
    
2. **Create a virtual environment 🐍**
    
    Next, create a virtual environment to install the project dependencies:
    
    ```bash
    python -m venv .venv
    source venv/bin/activate # On Windows use ``venv/scripts/activate`.
    ```
    
3. *Install the requirements 📦 **.
    
    Install the required libraries and dependencies from the 'requirements.txt' file:
    
    ```bash
    pip install -r requirements.txt
    ```
    
4. Add environment variables:🔐
    
    Set the environment variables required for the database connection in a `.env` file:
    
    ```bash
    # Database
    DatabaseHost=“***-mysql.services.clever-cloud.com” # The *** must be changed to the respective identifier.
    DatabaseName=“” #Add the database name, not the table name
    DatabaseUser=“” #Add the used user name
    DatabasePassword=“” #Add the password
    DatabasePort=“3306” #This port will always remain while using Mysql
    ```
    

This set of instructions will guide you through the configuration and preparation of the working environment for this project. By following these steps, you will be able to clone, configure and run the code on your local machine.

---

This translation includes all relevant sections from your original document, structured and formatted appropriately for a GitHub `README.md` file. Let me know if you need any further modifications!
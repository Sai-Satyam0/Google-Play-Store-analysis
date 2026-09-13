# Google Play Store Analysis

A data analysis project based on Google Play Store application data and user reviews. The project covers data cleaning, preprocessing, exploratory data analysis, comparative analysis, and sentiment analysis, with the final results presented through an interactive Streamlit dashboard.

## Project Overview

The raw Google Play Store dataset contains information about applications, including ratings, reviews, installs, categories, pricing, size, and update information. The user reviews dataset contains review text along with sentiment and sentiment scores.

The purpose of this project is to clean and analyze these datasets to identify patterns in application performance and understand user opinions.

The project follows the complete data analysis workflow:

```text
Raw Data
   |
   v
Data Cleaning
   |
   v
Data Preprocessing
   |
   v
Exploratory Data Analysis
   |
   v
Comparative Analysis
   |
   v
Sentiment Analysis
   |
   v
Interactive Dashboard
```

## Dashboard

The analysis is presented through a Streamlit application with separate sections for dataset exploration, preprocessing, descriptive analysis, visualizations, and sentiment analysis.

### Home

![Dashboard Home](assets/home.png)

## Datasets

Two datasets are used in this project.

### Google Play Store Dataset

The main dataset contains information about Google Play Store applications.

Important columns include:

* `App`
* `Category`
* `Rating`
* `Reviews`
* `Size`
* `Installs`
* `Type`
* `Price`
* `Content Rating`
* `Genres`
* `Last Updated`
* `Current Ver`
* `Android Ver`

The original dataset contains 10,841 records and 13 columns.

![Dataset Overview](assets/Dataset1.png)

![Dataset Summary](assets/Dataset2.png)

### User Reviews Dataset

The second dataset contains user reviews and sentiment information.

Important columns include:

* `App`
* `Translated_Review`
* `Sentiment`
* `Sentiment_Polarity`
* `Sentiment_Subjectivity`

![User Reviews Dataset](assets/Dataset6.png)

## Data Cleaning and Preprocessing

The raw dataset contains missing values, inconsistent formats, duplicate records, and values that cannot be used directly for analysis.

The preprocessing process includes:

* removing invalid values from the `Reviews` column
* converting reviews to numeric values
* cleaning the `Installs` column
* converting installs to numeric values
* cleaning the `Price` column
* converting prices to numeric values
* converting application size into MB
* converting `Last Updated` into datetime format
* removing duplicate records
* handling missing numerical values
* handling missing categorical values
* removing extreme values
* creating additional variables required for analysis

Additional variables are created during preprocessing, including:

* update year
* installation category
* estimated revenue

### Missing Values

![Missing Values](assets/Dataset3.png)

### Data Types

![Data Types](assets/Dataset4.png)

### Preprocessed Dataset

![Preprocessed Dataset](assets/Dataset%205.png)

## Descriptive Analysis

The descriptive analysis provides an overview of the dataset before performing comparisons and deeper analysis.

The analysis examines:

* app ratings
* number of reviews
* number of installs
* application categories
* application types
* prices
* application sizes
* numerical feature distributions

![Descriptive Analysis](assets/Description1.png)

![Preprocessing Analysis](assets/Description2.png)

## Exploratory Data Analysis

The exploratory analysis is used to identify patterns and relationships between different variables in the Play Store dataset.

The analysis includes:

* distribution of application ratings
* distribution of numerical variables
* number of applications by category
* reviews versus installs
* free versus paid applications
* installs by application type
* top genres by installs
* rating trends by update year

![Visualization Dashboard](assets/VIzualitaion_main.png)

![Exploratory Analysis](assets/Visulaization1-1.png)

## Comparative Analysis

Different application groups are compared to understand how performance varies across the Play Store.

The analysis includes:

* free applications versus paid applications
* highest-rated paid applications
* highest-rated free applications
* most-reviewed free applications
* average revenue by category
* revenue versus installs
* installs by application type
* top genres based on installs
* rating trends across update years

![Comparative Analysis](assets/Visulaizationn1-2.png)

![Comparative Analysis](assets/VIsulizationn1-3.png)

## Sentiment Analysis

The user reviews dataset is used to analyze the opinions expressed by users.

The analysis is based on:

* sentiment
* sentiment polarity
* sentiment subjectivity

The sentiment analysis explores:

* distribution of positive, neutral, and negative reviews
* sentiment polarity
* sentiment by application category
* relationship between polarity and subjectivity
* sentiment patterns across different applications

### Sentiment Polarity

![Sentiment Polarity](assets/VIsulaization2-1.png)

### Sentiment by Category

![Sentiment by Category](assets/Visualization2-2.png)

### Sentiment Subjectivity

![Sentiment Subjectivity](assets/Visulaizationn2-3.png)

## Technology Stack

| Technology            | Purpose                        |
| --------------------- | ------------------------------ |
| Python                | Data processing and analysis   |
| Pandas                | Data cleaning and manipulation |
| Matplotlib            | Data visualization             |
| Seaborn               | Statistical visualization      |
| Plotly                | Interactive visualizations     |
| Streamlit             | Interactive dashboard          |
| Streamlit Option Menu | Dashboard navigation           |
| Streamlit Lottie      | Dashboard interface            |
| Jupyter Notebook      | Exploratory analysis           |

## Project Structure

```text
Play store project/
│
├── prac.py
├── app.ipynb
│
├── googleplaystore.csv
├── googleplaystore_user_reviews.csv
├── preprocessed_GPS.csv
│
├── README.md
│
└── assets/
    ├── home.png
    ├── Dataset1.png
    ├── Dataset2.png
    ├── Dataset3.png
    ├── Dataset4.png
    ├── Dataset 5.png
    ├── Dataset6.png
    ├── Description1.png
    ├── Description2.png
    ├── VIzualitaion_main.png
    ├── Visulaization1-1.png
    ├── Visulaizationn1-2.png
    ├── VIsulizationn1-3.png
    ├── VIsulaization2-1.png
    ├── Visualization2-2.png
    └── Visulaizationn2-3.png
```

## Running the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd "Play store project"
```

### 2. Install dependencies

```bash
pip install pandas matplotlib seaborn plotly streamlit streamlit-option-menu streamlit-lottie statsmodels
```

### 3. Run the Streamlit application

```bash
streamlit run prac.py
```

The dashboard will be available at the local URL provided by Streamlit.

## Analysis Workflow

The project was developed in the following stages:

### 1. Data Exploration

The original datasets were inspected to understand their structure, columns, data types, and missing values.

### 2. Data Preprocessing

The raw data was cleaned and transformed into a format suitable for analysis.

### 3. Exploratory Analysis

Individual variables and their distributions were analyzed to understand the overall Play Store dataset.

### 4. Comparative Analysis

Different application categories, types, ratings, installs, reviews, and revenue were compared to identify relationships and differences.

### 5. Sentiment Analysis

User reviews were analyzed using sentiment, polarity, and subjectivity to understand user feedback.

### 6. Dashboard Development

The analysis was integrated into a Streamlit dashboard so that the datasets and visualizations could be explored interactively.

## Implementation

The project includes both the analysis code and the Streamlit application.

### Data Preprocessing

![Preprocessing Code](assets/Codingpart1.png)

### Analysis

![Analysis Code](assets/Coding%20%20part%202.png)

### Visualization

![Visualization Code](assets/Coding%20part3.png)

### Chart Generation

![Chart Code](assets/Coding%20part4.png)

## Key Areas of Analysis

The project focuses on the following areas:

* Application popularity
* User ratings
* User reviews
* Installation patterns
* Application categories
* Application genres
* Free and paid applications
* Application pricing
* Estimated revenue
* User sentiment
* Sentiment polarity
* Sentiment subjectivity
* Relationships between application metrics

## Future Improvements

Possible extensions to the project include:

* deploying the Streamlit dashboard publicly
* adding more interactive filters
* adding KPI cards for important metrics
* improving the sentiment analysis with more advanced NLP techniques
* building an application recommendation system
* adding more detailed revenue analysis
* adding automated data updates

## Author

**Sai Satyam Biswal**

Data Analytics | Python | Streamlit | Data Visualization

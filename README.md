# School Enrollment Comparison App

This Streamlit app allows users to compare the enrollment data of elementary schools, with a focus on the breakdown of ethnicities across various campuses. Users can select multiple schools, view their enrollment figures, and analyze the distribution of students by ethnicity. The app also provides visualizations to help users better understand the data through bar charts and pie charts.

## Features

- **School Selection**: Users can select multiple schools from a list to compare.
- **Enrollment Visualization**: Bar chart showing the enrollment numbers for each selected school.
- **Ethnicity Breakdown**: Pie charts displaying the distribution of ethnicities for each selected school.
- **Ethnicity by Grade**: A comparative bar chart showing the breakdown of ethnicities by grade across selected schools.

## Dataset

The app uses a dataset that includes enrollment data for multiple elementary schools within a district. The data includes the following columns:

- **CAMPUS NAME**: The name of the school (campus).
- **ENROLLMENT**: The number of enrolled students at the school.
- **GRADE**: The grade levels for the students.
- **ETHNICITY**: The ethnicity of the students.

The dataset is pre-processed to handle missing or ambiguous values (e.g., replacing values like "<10" with a midpoint value).

### Dataset Source

The dataset used in this app is called `Enrollment Report_District_220905_Campuses_Grade_Ethnicity_2023-2024.csv`, and it contains detailed enrollment information for the 2023-2024 academic year.

## Installation

To run this app locally, follow these steps:

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/school-enrollment-comparison.git
cd school-enrollment-comparison
```

### 2. Install dependencies
Ensure you have Python 3.7 or higher installed, then create a virtual environment and install the required libraries:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```
After running the above command, you can access the app in your browser at http://localhost:8501.

## Usage

- **Select Schools**: Use the sidebar to select one or more schools to compare.
- **View Data**: The app displays detailed enrollment data in a table.
- **Visualize**: The app automatically generates the following visualizations:
    - **Enrollment by School**: A bar chart showing the number of students at each selected school.
    - **Ethnicity Breakdown**: Pie charts for each selected school displaying the distribution of students by ethnicity.
    - **Ethnicity Breakdown by Grade**: A grouped bar chart showing how the ethnicities are distributed across different grade levels.

## Example

Here’s an example of what the app looks like after selecting a few schools and viewing the visualizations:

- Bar chart showing enrollment by school.
- Pie charts showing the ethnic breakdown for each selected school.
- Group bar chart showing the ethnicity distribution across different grades.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Feel free to fork the repository and submit issues or pull requests if you'd like to contribute to the app.


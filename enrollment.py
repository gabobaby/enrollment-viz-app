import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
@st.cache_data
def load_data():
    file_path = "Enrollment Report_District_220905_Campuses_Grade_Ethnicity_2023-2024.csv"
    df = pd.read_csv(file_path, skiprows=4, nrows=3248, encoding="utf-8")

    # Clean Enrollment Column (replace "<10" with midpoint values)
    def replace_less_than(value):
        if isinstance(value, str) and value.startswith("<"):
            return int(value[1:]) // 2  # Replace "<x" with x/2
        return value

    df["ENROLLMENT"] = df["ENROLLMENT"].apply(replace_less_than).astype(float)

    return df

df = load_data()

# Sidebar for user input
st.sidebar.title("School Comparison")
selected_schools = st.sidebar.multiselect("Select Schools to Compare", df["CAMPUS NAME"].unique())

# Filter dataset based on user selection
filtered_df = df[df["CAMPUS NAME"].isin(selected_schools)]

# Display summary statistics
st.title("Elementary School Comparison")
st.write(f"Comparing {len(selected_schools)} schools.")

if not filtered_df.empty:
    st.dataframe(filtered_df[["CAMPUS NAME", "ENROLLMENT", "GRADE", "ETHNICITY"]])

    # Bar Chart: Enrollment by School
    fig = px.bar(filtered_df, x="CAMPUS NAME", y="ENROLLMENT", title="Enrollment by School")
    st.plotly_chart(fig)

    # Pie Chart: Ethnicity Breakdown
    if "ETHNICITY" in filtered_df.columns:
        ethnicity_counts = filtered_df.groupby("ETHNICITY")["ENROLLMENT"].sum().reset_index()
        fig_pie = px.pie(ethnicity_counts, values="ENROLLMENT", names="ETHNICITY", title="Ethnicity Distribution")
        st.plotly_chart(fig_pie)

    # New Comparative Bar Chart: Ethnicity Breakdown by Grade across Schools
    st.subheader("Ethnicity Breakdown by Grade Across Schools")

    fig_ethnicity_grade = px.bar(
        filtered_df,
        x="GRADE",
        y="ENROLLMENT",
        color="CAMPUS NAME",
        barmode="group",
        facet_row="ETHNICITY",
        title="Enrollment Breakdown by Grade and Ethnicity Across Schools"
    )

    # Rotate ethnicity labels for readability
    fig_ethnicity_grade.update_yaxes(tickangle=0)  # Keep vertical Y labels
    fig_ethnicity_grade.update_xaxes(tickangle=-45)  # Rotate X-axis (Grade) labels

    st.plotly_chart(fig_ethnicity_grade)

else:
    st.write("Please select at least one school to compare.")


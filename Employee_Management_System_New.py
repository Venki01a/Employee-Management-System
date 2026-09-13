# ============================================================
# Employee Management System (EMS)
# Streamlit Web Application
# ============================================================

import streamlit as st
import pandas as pd


# ============================================================
# PAGE CONFIGURATION
# ============================================================
# This section sets the title, icon and layout of the Streamlit
# application.

st.set_page_config(
    page_title="Employee Management System",
    page_icon="👨‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================
# This CSS makes the application more attractive by adding:
# - Background color
# - Cards
# - Buttons
# - Headings
# - Rounded corners
# - Better spacing

st.markdown("""
<style>

    /* Main application background */
    .stApp {
        background: linear-gradient(
            135deg,
            black 0%,
            black 50%,
            black 100%
        );
    }

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #1e293b;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #1e293b;
        margin-bottom: 30px;
    }

    /* Dashboard cards */
    .dashboard-card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
    }

    .card-icon {
        font-size: 30px;
    }

    .card-title {
        font-size: 16px;
        color: black;
        margin-top: 5px;
    }

    .card-value {
        font-size: 28px;
        font-weight: bold;
        color: #1e293b;
    }

    /* Information box */
    .info-box {
        background: black;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #2563eb;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.06);
        margin-bottom: 20px;
    }

    /* Section heading */
    .section-heading {
        color: black;
        font-size: 28px;
        font-weight: 700;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: white;
        padding: 30px;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# STEP 1: EMPLOYEE DATA STORAGE
# ============================================================
# A dictionary is used to store employee information.
#
# Employee ID is the key.
# The value is another dictionary containing:
# - Name
# - Age
# - Department
# - Salary
#
# st.session_state is used so that employee data remains available
# when Streamlit refreshes the page.

if "employees" not in st.session_state:

    st.session_state.employees = {
        101: {
            "name": "Satya",
            "age": 27,
            "department": "HR",
            "salary": 50000
        },

        102: {
            "name": "Rahul",
            "age": 30,
            "department": "IT",
            "salary": 60000
        },

        103: {
            "name": "Priya",
            "age": 26,
            "department": "Finance",
            "salary": 55000
        }
    }


# ============================================================
# FUNCTION: add_employee()
# ============================================================
# Purpose:
# This function displays a form where the user can enter
# information about a new employee.
#
# It validates:
# - Employee ID
# - Name
# - Age
# - Department
# - Salary
#
# It also checks whether the Employee ID already exists.

def add_employee():

    st.markdown(
        '<div class="section-heading">➕ Add New Employee</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter the employee's information below and click "
        "**Add Employee**."
    )

    # Create an input form.
    with st.form("add_employee_form"):

        # Employee ID
        emp_id = st.number_input(
            "🆔 Employee ID",
            min_value=1,
            step=1,
            help="Enter a unique ID for the employee."
        )

        # Employee Name
        name = st.text_input(
            "👤 Employee Name",
            placeholder="Example: Amit Sharma"
        )

        # Age
        age = st.number_input(
            "🎂 Age",
            min_value=1,
            max_value=100,
            step=1
        )

        # Department
        department = st.selectbox(
            "🏢 Department",
            [
                "HR",
                "IT",
                "Finance",
                "Marketing",
                "Sales",
                "Operations",
                "Administration",
                "Other"
            ]
        )

        # Salary
        salary = st.number_input(
            "💰 Monthly Salary (₹)",
            min_value=0.0,
            step=1000.0
        )

        # Submit button
        submitted = st.form_submit_button(
            "➕ Add Employee",
            use_container_width=True
        )

        # Process the form after clicking the button.
        if submitted:

            # Check whether Employee ID already exists.
            if int(emp_id) in st.session_state.employees:

                st.error(
                    "❌ This Employee ID already exists. "
                    "Please enter a different ID."
                )

            # Check whether the name is empty.
            elif not name.strip():

                st.warning(
                    "⚠️ Please enter the employee's name."
                )

            # Check whether the salary is valid.
            elif salary < 0:

                st.warning(
                    "⚠️ Salary cannot be negative."
                )

            else:

                # Add employee to the dictionary.
                st.session_state.employees[int(emp_id)] = {
                    "name": name.strip(),
                    "age": int(age),
                    "department": department,
                    "salary": float(salary)
                }

                # Display success message.
                st.success(
                    f"✅ Employee **{name}** was added successfully!"
                )


# ============================================================
# FUNCTION: view_employees()
# ============================================================
# Purpose:
# This function displays all employees in a clean table.
#
# If there are no employees, it displays an appropriate message.

def view_employees():

    st.markdown(
        '<div class="section-heading">👥 All Employees</div>',
        unsafe_allow_html=True
    )

    employees = st.session_state.employees

    # Check whether employee data is available.
    if not employees:

        st.info("📭 No employees available.")

        return

    # Convert dictionary data into a list.
    employee_list = []

    for emp_id, details in employees.items():

        employee_list.append({
            "Employee ID": emp_id,
            "Name": details["name"],
            "Age": details["age"],
            "Department": details["department"],
            "Monthly Salary": details["salary"]
        })

    # Convert the list into a Pandas DataFrame.
    df = pd.DataFrame(employee_list)

    # Format salary as Indian currency.
    df["Monthly Salary"] = df["Monthly Salary"].apply(
        lambda x: f"₹{x:,.2f}"
    )

    # Display the table.
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FUNCTION: search_employee()
# ============================================================
# Purpose:
# This function allows the user to search for an employee
# using their Employee ID.
#
# If the employee exists, all details are displayed.
# Otherwise, an "Employee not found" message is displayed.

def search_employee():

    st.markdown(
        '<div class="section-heading">🔍 Search Employee</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Enter an Employee ID to view the employee's details."
    )

    # Employee ID input.
    emp_id = st.number_input(
        "🆔 Enter Employee ID",
        min_value=1,
        step=1,
        key="search_employee_id"
    )

    # Search button.
    if st.button(
        "🔍 Search Employee",
        use_container_width=True
    ):

        emp_id = int(emp_id)

        # Check whether the ID exists.
        if emp_id in st.session_state.employees:

            employee = st.session_state.employees[emp_id]

            st.success("✅ Employee Found!")

            # Display employee information in columns.
            col1, col2 = st.columns(2)

            with col1:

                st.info(
                    f"""
                    👤 **Name**

                    {employee["name"]}
                    """
                )

                st.info(
                    f"""
                    🎂 **Age**

                    {employee["age"]} years
                    """
                )

            with col2:

                st.info(
                    f"""
                    🏢 **Department**

                    {employee["department"]}
                    """
                )

                st.info(
                    f"""
                    💰 **Monthly Salary**

                    ₹{employee["salary"]:,.2f}
                    """
                )

        else:

            st.error(
                "❌ Employee not found. "
                "Please check the Employee ID."
            )


# ============================================================
# FUNCTION: dashboard()
# ============================================================
# Purpose:
# This function displays useful summary information about
# the employees in the system.
#
# It shows:
# - Total employees
# - Total departments
# - Average salary
# - Highest salary

def dashboard():

    employees = st.session_state.employees

    # Calculate basic statistics.
    total_employees = len(employees)

    departments = set()

    salaries = []

    for employee in employees.values():

        departments.add(employee["department"])

        salaries.append(employee["salary"])

    total_departments = len(departments)

    if salaries:

        average_salary = sum(salaries) / len(salaries)

        highest_salary = max(salaries)

    else:

        average_salary = 0

        highest_salary = 0

    # Create four dashboard columns.
    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="card-icon">👥</div>
                <div class="card-title">Total Employees</div>
                <div class="card-value">{total_employees}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="card-icon">🏢</div>
                <div class="card-title">Departments</div>
                <div class="card-value">{total_departments}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="card-icon">💰</div>
                <div class="card-title">Average Salary</div>
                <div class="card-value">
                    ₹{average_salary:,.0f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:

        st.markdown(
            f"""
            <div class="dashboard-card">
                <div class="card-icon">🏆</div>
                <div class="card-title">Highest Salary</div>
                <div class="card-value">
                    ₹{highest_salary:,.0f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# MAIN APPLICATION
# ============================================================

# Application title.
st.markdown(
    '<div class="main-title">👨‍💼 Employee Management System</div>',
    unsafe_allow_html=True
)

# Application subtitle.
st.markdown(
    '<div class="subtitle">'
    'Simple and easy employee management dashboard'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR MENU
# ============================================================
# The sidebar acts as the main navigation menu.
# Users can select what they want to do without knowing
# anything about programming.

st.sidebar.title("📋 EMS Menu")

st.sidebar.write(
    "Choose an option to manage employee information."
)

menu = st.sidebar.radio(
    "Select an option:",
    [
        "🏠 Dashboard",
        "➕ Add Employee",
        "👥 View All Employees",
        "🔍 Search Employee"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    "💡 **Tip:** Use the menu above to add, view, "
    "or search employee information."
)


# ============================================================
# DISPLAY SELECTED SECTION
# ============================================================

if menu == "🏠 Dashboard":

    # Display dashboard.
    dashboard()

    st.markdown("---")

    st.markdown(
        '<div class="info-box">'
        '<h3>👋 Welcome to the Employee Management System!</h3>'
        '<p>'
        'This simple application helps you manage employee '
        'information easily. Use the menu on the left to '
        'add employees, view employee records, or search '
        'for a specific employee.'
        '</p>'
        '</div>',
        unsafe_allow_html=True
    )


elif menu == "➕ Add Employee":

    # Display Add Employee section.
    add_employee()


elif menu == "👥 View All Employees":

    # Display all employees.
    view_employees()


elif menu == "🔍 Search Employee":

    # Display search section.
    search_employee()


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    '<div class="footer">'
    '👨‍💼 Employee Management System | '
    'Built with Python & Streamlit'
    '</div>',
    unsafe_allow_html=True
)
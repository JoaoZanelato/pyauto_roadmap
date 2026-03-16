# PYTHON AUTOMATION ROADMAP
### My path to mastering Python for Automation Services

This repository contains scripts and mini-projects developed to practice Python, focusing on automating repetitive tasks, data manipulation, and system integrations to complement my backend development skills.

---

## Study Roadmap

### 1. Python Language Fundamentals
- [x] **Basic Syntax & Data Structures:** Variables, Lists, Dictionaries, Tuples, and String manipulation.
- [x] **Control Flow:** `if/elif/else` conditional statements and `for` loops.
- [ ] **Functions & OOP:** Creating modular code, classes, and objects in Python.
- [ ] **Exception Handling:** Managing runtime errors using `try/except` blocks.

### 2. File & System Manipulation
- [x] **OS Module:** Navigating directories, renaming, and moving files (`os.listdir`, `os.rename`).
- [x] **Shutil Module:** Copying and managing files systematically (`shutil.copy2`).
- [ ] **Pathlib:** Advanced, object-oriented file path manipulation.

### 3. Data Analysis & Manipulation
- [x] **Pandas Basics:** Reading datasets (Excel/CSV) and manipulating DataFrames (`pd.read_excel`).
- [x] **Data Aggregation:** Grouping data and calculating metrics (`groupby`, `sum`).
- [ ] **Data Cleaning:** Handling missing values and formatting data types.

### 4. Integration & Communication Automation
- [x] **Email Automation:** Sending automated HTML emails and reports using Outlook (`win32com.client`).
- [ ] **Web Scraping & Browser Automation:** Interacting with web elements using Selenium or BeautifulSoup.
- [ ] **API Consumption:** Making HTTP requests with the `requests` library to integrate with external services.
- [ ] **GUI Automation:** Controlling mouse and keyboard events using PyAutoGUI.

---

## 🛠️ Practical Projects Developed

#### CopyMove
A local file management script designed to automatically organize scattered Excel files into specific folders based on their naming conventions.

**Core Concepts Applied:**
- **File System Interaction:** Utilizing the `os` library to list directory contents and map current working paths.
- **String Matching & Logic:** Applying `if/elif` conditions to filter files containing specific keywords (like "Compras" or "Vendas") and routing them to their respective directories.
- **Automation of OS Tasks:** Programmatically renaming and moving files (`os.rename`) to eliminate manual drag-and-drop operations and organize the workspace instantly.

---

#### MiniCurso
A data analysis and reporting automation script that processes a raw sales dataset and autonomously emails a formatted performance report.

**Core Concepts Applied:**
- **Data Processing (Pandas):** Importing `.xlsx` data into DataFrames to analyze structural store performance.
- **Data Aggregation & Math:** Using `.groupby()` to calculate total revenue ("Valor Final") and total products sold ("Quantidade") per store, as well as mathematically deriving the average ticket ("Ticket Médio").
- **Email Automation (win32com):** Integrating directly with the local Windows Outlook application to dispatch automated emails (`win32.Dispatch`).
- **HTML Formatting & String Interpolation:** Embedding Pandas DataFrames directly into an HTML email body (using f-strings) with custom currency formatters (`formatters={'Valor Final': 'R${:,.2f}'.format}`) to generate a professional, presentation-ready report.

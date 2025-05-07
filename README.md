# 🧾 JIRA Issue Extractor

This Python script connects to your JIRA Cloud instance, fetches issue data using the JIRA REST API, and exports it into a clean Excel spreadsheet.

---

## 📦 Features

- ✅ Authenticates with JIRA using API token
- 📊 Extracts issues from a specific project
- 📁 Exports data to `jira_issues_export.xlsx`
- 🔐 Uses `.env` file to keep credentials safe

---

## 🛠 Requirements

Install dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### `requirements.txt` includes:

```
pandas
openpyxl
jira
python-dotenv
```

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/jira-extractor.git
cd jira-extractor
```

### 2. Create a `.env` file in the root directory

```
JIRA_SERVER=https://your-domain.atlassian.net
JIRA_EMAIL=your-email@example.com
JIRA_API_TOKEN=your-api-token
```

---

## 🔐 How to get JIRA credentials

### 🔹 `JIRA_SERVER`
This is your JIRA Cloud base URL (no trailing paths):
```
https://yourcompany.atlassian.net
```

### 🔹 `JIRA_EMAIL`
The Atlassian email you use to log in (must match the API token's creator).

### 🔹 `JIRA_API_TOKEN`

1. Go to https://id.atlassian.com/manage/api-tokens
2. Click **Create API token**
3. Give it a label like `JIRA extractor`
4. Click **Create**, then **Copy**
5. Paste it in your `.env` as `JIRA_API_TOKEN=yourtoken`

> 💡 Make sure your user account has permission to access the JIRA project and issues.

---

## ▶️ Run the Script

```bash
python extractor.py
```

This will connect to your JIRA instance, fetch issue data, and create:

```
jira_issues_export.xlsx
```

---

## 📁 Output Example

The exported Excel file contains:
- Issue key
- Summary
- Status
- Assignee
- Created/Updated dates (and other fields you define)

---


## 👨‍💻 Author

Built by Thomas James 
PRs and improvements are welcome!

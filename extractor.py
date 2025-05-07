import os
from jira import JIRA
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

jira_server = os.getenv('JIRA_SERVER')
jira_user = os.getenv('JIRA_EMAIL')
jira_api_token = os.getenv('JIRA_API_TOKEN')

jira = JIRA(server=jira_server, basic_auth=(jira_user, jira_api_token))
# JQL to search issues
jql = 'ORDER BY created DESC'
max_issues = 10  # Adjust based on need

# Fetch issues
issues = jira.search_issues(jql, maxResults=max_issues)

# Extract desired fields
data = []
for issue in issues:
    fields = issue.fields
    data.append({
        'Key': issue.key,
        'Summary': fields.summary,
        'Status': fields.status.name,
        'Assignee': fields.assignee.displayName if fields.assignee else 'Unassigned',
        'Reporter': fields.reporter.displayName,
        'Created': fields.created,
        'Resolved': fields.resolutiondate,
        'Priority': fields.priority.name if fields.priority else 'None',
        'Description': fields.description,
        'Labels': ', '.join(fields.labels),
    })

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('jira_issues_export.xlsx', index=False)

print("✅ Export completed: jira_issues_export.xlsx")
import os
from jira import JIRA
from dotenv import load_dotenv

# Load environment variables from .env
jira = None

def load_env():
    load_dotenv()
    jira_server = os.getenv("JIRA_SERVER")
    jira_username = os.getenv("JIRA_USERNAME")
    jira_password = os.getenv("JIRA_PASSWORD")
    load_jira(jira_server, jira_username, jira_password)

def load_jira(jira_server, jira_username, jira_password):
    global jira
    jira = JIRA(server=jira_server, basic_auth=(jira_username, jira_password))

def get_issues(jql_str):
    issues = jira.search_issues(jql_str)
    for issue in issues:
        yield issue

def get_existing_ticket(event):
    jql_str = 'project=YOUR_PROJECT AND summary ~ "{}"'.format(event.get("content"))
    issues = get_issues(jql_str)
    return next(issues, None)

def create_new_ticket(event):
    issue_dict = {
        'project': {'key': 'YOUR_PROJECT'},
        'summary': 'New issue from jira-python',
        'description': event.get("content"),
        'issuetype': {'name': 'Bug'},
    }
    return jira.create_issue(fields=issue_dict)

def create_new_comment(ticket, event):
    return ticket.add_comment(event.get("content"))
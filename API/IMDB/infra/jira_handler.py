from jira import JIRA
from API.IMDB.infra.config_provider import ConfigProvider


class JiraHandler:
    config = ConfigProvider().load_from_file(
        "C:\\Users\\ananh\\OneDrive\\Desktop\\QA Course\\Automation\\Automation_GIT\\API\\IMDB\\config.json")
    secret_file = ConfigProvider().load_from_file(
        "C:\\Users\\ananh\\OneDrive\\Desktop\\QA Course\\Automation\\Automation_GIT\\API\\IMDB\\secret.json")

    def __init__(self):
        self._jira_url = self.config['jira_url']
        self._auth_jira = JIRA(
            basic_auth=(self.config['email'], self.secret_file['token']),
            options={'server': self._jira_url}
        )

    def create_issue(self, project_key, summary, description, issue_type='Bug'):
        issue_dict = {
            'project': {'key': project_key},
            'summary': summary,
            'description': description,
            'issue_type': issue_type
        }
        return self._auth_jira.create_issue(fields=issue_dict)

import requests
import pytest

def test_github_status():
    response = requests.get("https://api.github.com/")
    assert response.status_code == 200
    assert "current_user_url" in response.json()

def test_repo_info():
    # Проверяем, что твой репозиторий существует
    url = "https://api.github.com/repos/ps3segovia/qa_project_1"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["name"] == "qa_project_1"

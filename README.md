# QA Automation Project

## О проекте
Этот проект создан для тренировки навыков автоматизации тестирования на Python.

## Что здесь есть
- `src/` — вспомогательные скрипты (например, hello_qa.py)
- `tests/` — автотесты с использованием PyTest
  - `test_github_api.py` — тесты для GitHub API
  - `test_jsonplaceholder.py` — тесты для JSONPlaceholder API

## Технологии
- Python 3.12
- PyTest
- Requests
- Git + GitHub (SSH)

## Как запустить тесты
1. Активируй виртуальное окружение: `source venv/bin/activate`
2. Запусти тесты: `pytest tests/ -v`
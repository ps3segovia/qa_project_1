import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_all_posts():
    """Проверяем, что можно получить список всех постов"""
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200, "Статус не 200"
    posts = response.json()
    assert isinstance(posts, list), "Ответ должен быть списком"
    assert len(posts) == 100, "Должно быть 100 постов"

def test_get_single_post():
    """Проверяем, что можно получить конкретный пост по ID"""
    post_id = 1
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == post_id, "ID в ответе не совпадает"
    assert "title" in post, "В ответе нет поля 'title'"
    assert "body" in post, "В ответе нет поля 'body'"

def test_create_new_post():
    """Проверяем, что можно создать новый пост (метод POST)"""
    new_post = {
        "title": "Мой первый тестовый пост",
        "body": "Это тело поста",
        "userId": 1
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201, "При создании статус должен быть 201"
    created = response.json()
    assert created["title"] == new_post["title"], "Заголовок не совпадает"
    assert created["body"] == new_post["body"], "Тело не совпадает"
    assert "id" in created, "В ответе нет ID созданного поста"
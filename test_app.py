import pytest
import json
from app import app, db, Todo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # In-memory DB for tests
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_index_empty(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"No todos" not in rv.data  # You can adjust based on your template output

def test_add_todo_and_index(client):
    rv = client.post('/add', data={'title': 'Test todo'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test todo' in rv.data

def test_complete_incomplete(client):
    # Add todo first
    with app.app_context():
        todo = Todo(title='Incomplete test')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    rv = client.get(f'/complete/{todo_id}', follow_redirects=True)
    assert rv.status_code == 200
    with app.app_context():
        assert Todo.query.get(todo_id).complete is True

    rv = client.get(f'/incomplete/{todo_id}', follow_redirects=True)
    assert rv.status_code == 200
    with app.app_context():
        assert Todo.query.get(todo_id).complete is False

def test_delete(client):
    with app.app_context():
        todo = Todo(title='To delete')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    rv = client.get(f'/delete/{todo_id}', follow_redirects=True)
    assert rv.status_code == 200
    with app.app_context():
        assert Todo.query.get(todo_id) is None

def test_edit(client):
    with app.app_context():
        todo = Todo(title='Old Title')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    rv = client.post(f'/edit/{todo_id}', data={'title': 'New Title'}, follow_redirects=True)
    assert rv.status_code == 200
    with app.app_context():
        assert Todo.query.get(todo_id).title == 'New Title'

# API tests

def test_api_get_todos_empty(client):
    rv = client.get('/api/todos')
    assert rv.status_code == 200
    data = rv.get_json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_api_create_todo_success(client):
    rv = client.post('/api/todos', json={'title': 'API Task'})
    assert rv.status_code == 201
    data = rv.get_json()
    assert data['title'] == 'API Task'
    assert data['complete'] is False

def test_api_create_todo_missing_json(client):
    rv = client.post('/api/todos', data='not json')
    assert rv.status_code == 400
    assert 'Missing JSON' in rv.get_json().get('error')

def test_api_create_todo_missing_title(client):
    rv = client.post('/api/todos', json={})
    assert rv.status_code == 400
    assert 'Title is required' in rv.get_json().get('error')

def test_api_get_todo(client):
    with app.app_context():
        todo = Todo(title='Get me')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    rv = client.get(f'/api/todos/{todo_id}')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['title'] == 'Get me'

def test_api_get_todo_404(client):
    rv = client.get('/api/todos/9999')
    assert rv.status_code == 404

def test_api_update_todo_success(client):
    with app.app_context():
        todo = Todo(title='Old API Title')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    rv = client.put(f'/api/todos/{todo_id}', json={'title': 'Updated Title', 'complete': True})
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['title'] == 'Updated Title'
    assert data['complete'] is True

def test_api_update_todo_missing_json(client):
    with app.app_context():
        todo = Todo(title='Test')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    rv = client.put(f'/api/todos/{todo_id}', data='not json')
    assert rv.status_code == 400
    assert 'Missing JSON' in rv.get_json().get('error')

def test_api_update_todo_missing_title(client):
    with app.app_context():
        todo = Todo(title='Test')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    rv = client.put(f'/api/todos/{todo_id}', json={'complete': True})
    assert rv.status_code == 400
    assert 'Title is required' in rv.get_json().get('error')

def test_api_update_todo_404(client):
    rv = client.put('/api/todos/9999', json={'title': 'Does not exist', 'complete': True})
    assert rv.status_code == 404

def test_api_delete_todo_success(client):
    with app.app_context():
        todo = Todo(title='Delete me')
        db.session.add(todo)
        db.session.commit()
        todo_id = todo.id

    rv = client.delete(f'/api/todos/{todo_id}')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['result'] is True

def test_api_delete_todo_404(client):
    rv = client.delete('/api/todos/9999')
    assert rv.status_code == 404

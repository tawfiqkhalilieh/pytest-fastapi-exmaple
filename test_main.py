import json
import pytest
from main import app
from fastapi.testclient import TestClient
# get test example

client = TestClient(app)
def test_read_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'massage': 'Hi'}


@pytest.mark.parametrize(
    ('url','expected'),
    (
        ("/id/1",200),
        ("/id/2",200),
        ("/2",404),
        ("/",200),
        ('/e/1',200),
        ('/e/e',422)
    )
)
def test_gets(url,expected):
    assert client.get(url).status_code == expected


@pytest.mark.parametrize(
    ('url','expected','detail','data'),
    (
        ("/add",200,'"ok"',{'id':'hi'}),
        ("/add", 401 ,'{"detail":"number"}',{'id':1}),
    )
)
def test_add(url: str,expected: int,detail: str,data: dict):
    response = client.post(
        url,
        data=json.dumps(data),
        headers={"Content-Type": "application/json"},
    )
    #assert response.status_code == expected
    assert response.text == detail
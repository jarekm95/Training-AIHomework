import requests


def test_ping_receiverservice():
    headers = {'Content-Type': 'application/json'}
    data = '{"url":"http://ReceiverService:8080/api/v1/info"}'
    resp = requests.post("http://localhost:8080/api/v1/ping", headers=headers, data=data)
    assert resp.json().get("Receiver") == "Cisco is the best!"

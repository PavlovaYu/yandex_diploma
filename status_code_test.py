import sender_stand_request

# Юлия Павлова, 13-я когорта — Финальный проект. Инженер по тестированию плюс

def test_status_get_new_order_info():
    response = sender_stand_request.get_new_order_info()
    assert response.status_code == 200
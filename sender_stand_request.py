import configuration
import requests
import data

# Запрос на создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
#response = post_new_order(data.order_body)
#print(response.status_code)
#print(response.text)

# Функция для получения трэка заказа
def get_new_order_track():
    order_body = data.order_body
    resp_order = post_new_order(order_body)
    return resp_order.json()["track"]

def get_new_order_info():
    current_params = data.params.copy()
    current_params["t"] = get_new_order_track()
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_INFO_PATH,
                         params=current_params, headers=data.headers)
#response = get_new_order_info()
#print(response.text)
#print(response.status_code)

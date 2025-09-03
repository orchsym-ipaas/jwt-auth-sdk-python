import requests
from JwtGenerator import JwtGenerator


def test_HS256_request():
    """
    测试JWT认证请求
    """
    # 配置参数
    app_code = "b3JjaHN5bS1qd3QtYXV0aDM5MjU0"
    client_id = "38e935c4-666a-48ba-8c64-7c0e21ff6b4f"
    secret_code = "fadwsfteawsfd"
    token_period = 250
    algorithm = "HS256"
    url = "http://orchsym-gateway.baishancloud.com/env-101/por-17834/propath/bsy/get"

    try:
        # 生成JWT token
        jwt_generator = JwtGenerator(secret_code, client_id, token_period, algorithm)
        token = jwt_generator.get_token()
        
        print(f"Generated Token: {token}")
        
        # 设置请求头
        headers = {
            "orchsym-app-code": app_code,
            "Authorization": f"bearer {token}"
        }
        print(f"headers: {headers}")
        
        # 发送GET请求
        response = requests.get(url, headers=headers)
        
        # 输出结果
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        return response
        
    except Exception as e:
        print(f"Request failed: {e}")
        return None



test_HS256_request()
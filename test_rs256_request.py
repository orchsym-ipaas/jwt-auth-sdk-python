import requests
from JwtGenerator import JwtGenerator



def test_RS256_request():
    """
    RS256算法测试函数
    """
    # 配置参数
    app_code = "b3JjaHN5bS1qd3QtYXV0aDM5MjMz"
    client_id = "fb7cc604-3732-446c-b2bc-4f92c414eba2"
    private_key = "MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDViFrSfCpARiwkj4YFSIEqNv7OuYPNhM1E+qPVwYpb8eviEctR1/KzO0DHcAH/UTuoFOJK1/f6BeMU8ExEC3g/EGubKe3d+WUZXyoA0JDRkKKOjZW0Ad7s5ZVOYYjpc8sw6KuO0G5UNRoU7XP9t1BpUpcxuNfu5XdboF1GPHDZNrzACB7AU0wyt8FQMTXQvosJ4ofUVWZSd4tW8eGSYLYDBdqe7uocByAOg2fJg+62558fGhvh82SW3rVfcQO3o4JKS3J+pKjGywBa7x+JzfMpIryEYGjoh5pbogMdveuAX+457kiTy+XyjO0il+4Hke6B0gQiA4p3sT1CpSM1evPrAgMBAAECggEASsR9ZLE0TCAmCcE1gLkT/ReXngPoSjijdXE7l7e2fh5V5Wkso6I1KZvoQU0PbfpgJKj3WZSIkEOqcST412SavJ4/x2tljjFqvHkNaI6e/rohqT+bORXknFeBMZpGSdQRRDVcCNwjnZmgYc6JLEAZSF+ycCcUeOJhKjSbJGI6c1uq/Lm8DzKCeeKtkdmplejTqMzqQc86ZueGEwNS1o5QVKzq+3aWGZxI6DC6cZ7uT/oTaUn2t6nSoZZItn9cO2MIERcCs2+2X+IH6NsFoJnqsf5UVFuwp1kyQ/p1YrGwnGOCTzA3r3yBrwUgFhF9LLP8bSHLRv+w/EluGeUOKiLinQKBgQDpM2jYvE/boKC9L8PoUdMBE2HTzU6LN7rL9mG+rgojzjFMOVY+ihyIvvO9jP/zswBwkASXiQHNyqhZVhFIvFzqQTa6uo44mWQYPo+mYq2WokTzLf1WXgmjGRTWO8oow1XrRHKjzWSX37A7hpDIx5Fu+Xs2Aw23LNkyhX93pv2PVwKBgQDqaK/AzzY4LcNgEVSX1oAcx1iO3sbGJvWcAzkG8TMAddJhCzuZ9UzL1q99w9w9vV2Up1Ux3WiNYhTmTiY1QMYpgGAsT+7yy4389PcqcOZeqJn9DGxU6Z69mUfPOLjQqmsnqN0s7jSk5lXfoYhSkZa9IlaWsIiv96qdytP/RLFnjQKBgQCz778OvP7BcIeWcqyvLbOqONJbIydftHiluE5jWtboGclgDz3Es7ygpvZbY9h6qbvFHtrsMgL6T0zm4cokXXM0LW2VVy017uWU73DX6XwXps2c9fdsFNNKzaeORkQOf+pjxkTOr0TXCvpoc8Rzp8lH36h6XJDQrgJJQUjBglBTsQKBgQCG48EnkdYgk+0XDkIAsjW82dYTOQ1nn6m8onohjZEM1cA/ieg9W1RbBGquU5QcjykXzwcOj9uHaIagVR5VjLW70h0FwuW9H/fQNeM5sAhRNnKOlKSOZHWto1QYYgqwQTEyfFDydw0iS03lR54b7Z2xrt3nDyVJJZsv/DTsc0onTQKBgQCPRZcrFLHH6DegCmkyD2Q3AMWLz92Eg5EoDDC6YMkU6T6NE8UJy1FEECKZIno6FowxCmV6tHFltICJ43aqLnxoEL9hCyniuiEyPmmxeFIxc4rhPW54+mmfZbNAJZ1zdF6xKwT1oiTA8XLu3motwORVZQ5w8gr2Gx+L/Khr4/2nOg=="
    token_period = 250
    algorithm = "RS256"
    url = "http://orchsym-gateway.baishancloud.com/env-101/por-17834/propath/bsy/get"

    try:
        # 生成JWT token
        jwt_generator = JwtGenerator(private_key, client_id, token_period, algorithm)
        token = jwt_generator.get_token()
        
        print(f"Generated Token: {token}")
        
        # 设置请求头
        headers = {
            "orchsym-app-code": app_code,
            "Authorization": f"bearer {token}"
        }
        
        print(f"Request headers: {headers}")
        
        # 发送GET请求
        response = requests.get(url, headers=headers, timeout=30)
        
        # 输出结果
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        
        return response
        
    except Exception as e:
        print(f"Request failed: {e}")
        import traceback
        traceback.print_exc()
        return None


test_RS256_request()
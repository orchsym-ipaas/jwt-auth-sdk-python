import base64
from datetime import datetime, timedelta
from typing import Optional

# pip3 install PyJWT==1.6.4
import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class JwtGenerator:
    """
    JWT Token生成类
    """
    
    def __init__(self, key_str: str, client_id: str, token_period: int, algorithm: Optional[str]):
        """
        生成token
        
        Args:
            key_str: 使用RS256算法时为privateKey, 使用HS256算法时为secretCode
            client_id: 签发人
            token_period: token过期时间 单位秒
            algorithm: 算法类型 'RS256' 或 'HS256'
        """
        if algorithm is None:
            self.token = None
            return
            
        # 计算过期时间
        expires_time = datetime.utcnow() + timedelta(seconds=token_period)
        
        if algorithm == "RS256":
            # 处理RSA私钥
            try:
                # 解码base64并加载私钥
                private_key_bytes = base64.b64decode(key_str)
                
                # 从PKCS8格式加载私钥
                private_key = serialization.load_der_private_key(
                    private_key_bytes,
                    password=None,
                    backend=default_backend()
                )
                
                # 生成JWT token
                token_bytes = jwt.encode(
                    {
                        'iss': client_id,
                        'exp': expires_time
                    },
                    private_key,
                    algorithm='RS256'
                )
                
                # 确保返回的是字符串
                if isinstance(token_bytes, bytes):
                    self.token = token_bytes.decode('utf-8')
                else:
                    self.token = token_bytes
                
            except Exception as e:
                raise ValueError(f"Failed to process RSA private key: {str(e)}")
                
        elif algorithm == "HS256":
            # 使用HMAC SHA256算法
            token_bytes = jwt.encode(
                {
                    'iss': client_id,
                    'exp': expires_time
                },
                key_str,
                algorithm='HS256'
            )
            
            # 确保返回的是字符串
            if isinstance(token_bytes, bytes):
                self.token = token_bytes.decode('utf-8')
            else:
                self.token = token_bytes
            
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}. Only 'RS256' and 'HS256' are supported.")
    
    def get_token(self) -> Optional[str]:
        """获取生成的token"""
        return self.token
    
    def __str__(self) -> str:
        """字符串表示"""
        return f"token = \n{self.token}"

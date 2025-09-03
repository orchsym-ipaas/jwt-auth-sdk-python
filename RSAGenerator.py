from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import base64

class OrchsymRSA256KeyGenerator:
    """秘钥对生成类,使用构造方法传入私钥长度生成或将生成的秘钥对传入构造方法生成"""
    
    def __init__(self, key_size=2048):
        # 生成RSA密钥对
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
        )
        
        self.private_key = private_key
        self.public_key = private_key.public_key()
    
    def get_public_key(self):
        """获取公钥"""
        return self.public_key
    
    def get_private_key(self):
        """获取私钥"""
        return self.private_key
    
    def __str__(self):
        """转换为字符串表示形式"""
        # 序列化公钥为PEM格式然后Base64编码
        public_key_bytes = self.public_key.public_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        public_key_b64 = base64.b64encode(public_key_bytes).decode('utf-8')
        
        # 序列化私钥为PEM格式然后Base64编码
        private_key_bytes = self.private_key.private_bytes(
            encoding=serialization.Encoding.DER,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        private_key_b64 = base64.b64encode(private_key_bytes).decode('utf-8')
        
        return f"publicKey = \n{public_key_b64}\nprivateKey = \n{private_key_b64}"

# 使用示例
if __name__ == "__main__":
    try:
        # 创建2048位RSA密钥对生成器
        key_generator = OrchsymRSA256KeyGenerator(2048)
        
        # 获取密钥
        public_key = key_generator.get_public_key()
        private_key = key_generator.get_private_key()
        
        # 打印密钥
        print(key_generator)
        
        # 如果需要PEM格式的密钥
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')
        
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ).decode('utf-8')
        
        print("\nPEM格式公钥:")
        print(public_pem)
        
        print("PEM格式私钥:")
        print(private_pem)
        
    except Exception as e:
        print(f"生成密钥时出错: {e}")
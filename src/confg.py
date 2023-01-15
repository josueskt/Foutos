from decouple import config



class Config:
    secret_key=config("secret_key")
    
class debelop(Config):
    DEBUG =True
    
config={
    'development':debelop
 
    
    
} 

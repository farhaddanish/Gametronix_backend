from django.contrib.auth.tokens import default_token_generator

def token (user):
    return default_token_generator.make_token(user)
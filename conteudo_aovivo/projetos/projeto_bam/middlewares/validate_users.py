import re

def validar_nome(nome):
    if not nome:
        return {"error": True, "mensagem": "Nome não pode ser vazio"}
    
    if not isinstance(nome, str):
        return {"error": True, "mensagem": "Nome deve ser uma string"}
    
    if nome.isnumeric():
        return {"error": True, "mensagem": "Nome não pode conter apenas números"}
    
    return {"error": False}

def validar_email(email):
    if not email:
        return False, "Email não pode ser vazio"
    
    if not isinstance(email, str):
        return False, "Email deve ser uma string"
    
    # Regex para validar o formato do email
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(regex, email):
        return {"error": True, "mensagem": "Formato de email inválido"}
    
    return {"error": False}

def validar_senha(senha):
    if not senha:
        return {"error": True, "mensagem": "Senha não pode ser vazia"}
    
    if not isinstance(senha, str):
        return {"error": True, "mensagem": "Senha deve ser uma string"}
    
    if len(senha) < 6:
        return {"error": True, "mensagem": "Senha deve ter pelo menos 6 caracteres"}

    if not re.search(r'[A-Z]', senha):
        return {"error": True, "mensagem": "Senha deve conter pelo menos uma letra maiúscula"}
    
    if not re.search(r'[a-z]', senha):
        return {"error": True, "mensagem": "Senha deve conter pelo menos uma letra minúscula"}
    
    if not re.search(r'\d', senha):
        return {"error": True, "mensagem": "Senha deve conter pelo menos um número"}
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return {"error": True, "mensagem": "Senha deve conter pelo menos um caractere especial"}

    return {"error": False}

def validar_usuario(usuario):
    nome_valido, erro_nome = validar_nome(usuario.get("name"))
    if not nome_valido:
        return {"error": True, "mensagem": "Este não é um nome válido"}
    
    email_valido, erro_email = validar_email(usuario.get("email"))
    if not email_valido:
        return {"error": True, "mensagem": "Email inválido"}
    
    senha_valida, erro_senha = validar_senha(usuario.get("password"))
    if not senha_valida:
        return {"error": True, "mensagem": "Senha inválida"}
    
    return {"error": False}

def validar_telefone(telefone):
    if not telefone:
        return {"error": True, "mensagem": "Telefone não pode ser vazio"}
    
    if not isinstance(telefone, str):
        return {"error": True, "mensagem": "Telefone deve ser uma string"}
    
    # Remove espaços, parênteses, traços, etc.
    telefone = re.sub(r'\D', '', telefone)
    
    if len(telefone) < 10 or len(telefone) > 11:
        return {"error": True, "mensagem": "Telefone deve ter entre 10 e 11 dígitos (DDD + número)"}

    if not telefone.isdigit():
        return {"error": True, "mensagem": "Telefone deve conter apenas dígitos"}

    return {"error": False}
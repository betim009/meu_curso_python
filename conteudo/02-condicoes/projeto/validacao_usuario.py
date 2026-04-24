idade = 25
usuario_ativo = True
senha_digitada = "python123"
senha_cadastrada = "python123"
tentativas = 1

if tentativas >= 3:
    print("Usuário bloqueado por tentativas.")
elif idade < 18:
    print("Acesso bloqueado. Idade mínima não atingida.")
elif not usuario_ativo:
    print("Acesso bloqueado. Usuário inativo.")
elif senha_digitada != senha_cadastrada:
    print("Acesso negado. Senha incorreta.")
else:
    print("Acesso liberado.")

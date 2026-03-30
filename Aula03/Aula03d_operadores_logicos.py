#Logica e (and)

verifique_email = True
verifique_senha = False

verifique_login = verifique_email and verifique_senha
print(verifique_login)

if verifique_login:
    print("entrar no programa")

#logica ou (or)
logica_ou = False or False or False
print(logica_ou)

if not verifique_login:
    print("loga ai ...")
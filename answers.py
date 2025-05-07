from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Usuario, Produto, Pedido, Avaliacao

engine = create_engine('sqlite:///exercicios.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Liste todos os produtos cadastrados no sistema.
def q01():
    return session.query(Produto).all()

# 2. Recupere todos os usuários ativos com mais de 18 anos.
def q02():
    return [u for u in session.query(Usuario).all() if u.idade >= 18 and u.ativo]

# 3. Obtenha todos os pedidos feitos depois de 01/03/2025 com quantidade superior a 5.
def q03():
    data_selecionada = '01/03/2025'
    return [p for p in session.query(Pedido).all()
            if p.data_pedido > datetime.strptime(data_selecionada, '%d/%m/%Y') and p.quantidade > 5]

# 4. Encontre o primeiro usuário cadastrado no sistema.
def q04():
    return session.query(Usuario).first()

# 5. Verifique qual é o produto mais barato da categoria "eletrônicos".
def q05():
    return session.query(Produto).filter(Produto.categoria == 'eletrônicos').order_by(Produto.preco).first()

# 6. Determine o último pedido realizado por qualquer usuário.
def q06(usuario_id):
    return session.query(Pedido).filter(Pedido.usuario_id == usuario_id).order_by(Pedido.data_pedido.desc()).first()

# 7. Recupere os dados completos do usuário com ID 7.
def q07():
    return session.get(Usuario, 7)

# 8. Verifique se existe um produto com ID 5 e estoque positivo.
def q08():
    produto = session.get(Produto, 5)
    return produto.estoque > 0 if produto else False

# 9. Obtenha o pedido de ID 3 junto com os dados do usuário associado.
def q09():
    pedido = session.get(Pedido, 3)
    usuario = session.get(Usuario, pedido.usuario_id) if pedido else None
    return pedido, usuario

# 10. Encontre usuários com idade entre 25 e 35 anos.
def q10():
    return session.query(Usuario).filter((Usuario.idade >= 25) & (Usuario.idade <= 35)).all()

# 11. Liste pedidos com status "cancelado" ou "pendente" feitos depois de 2024.
def q11():
    return session.query(Pedido).filter(
        ((Pedido.status == 'cancelado') | (Pedido.status == 'pendente')) &
        (Pedido.data_pedido > datetime.strptime('01/01/2025', '%d/%m/%Y'))
    ).all()

# 12. Selecione produtos com preço acima de R$ 500 que tiveram pelo menos 1 pedido.
def q12():
    return session.query(Produto, Pedido).join(Produto, Pedido.produto_id == Produto.id).filter(Produto.preco > 500).all()

# 13. Busque todos os usuários com status inativo.
def q13():
    return session.query(Usuario).filter_by(ativo=False).all()

# 14. Encontre produtos da categoria "livros" com preço inferior a R$ 100.
def q14():
    return session.query(Produto).filter((Produto.categoria == 'livros') & (Produto.preco < 100)).all()

# 15. Obtenha os 3 produtos mais caros com estoque disponível.
def q15():
    return session.query(Produto).order_by(Produto.preco.desc()).filter(Produto.estoque > 0).limit(3).all()

# 16. Liste todos os usuários em ordem alfabética de nome.
def q16():
    return session.query(Usuario).order_by(Usuario.nome).all()

# 17. Ordene os produtos do mais caro para o mais barato.
def q17():
    return session.query(Produto).order_by(Produto.preco.desc()).all()

# 18. Organize os pedidos por data de criação (mais recentes primeiro) e depois por status.
def q18():
    return session.query(Pedido).order_by(Pedido.data_pedido.desc(), Pedido.status).all()

# 19. Liste os 10 primeiros usuários cadastrados no sistema.
def q19():
    return session.query(Usuario).limit(10).all()

# 20. Obtenha os 5 produtos mais baratos disponíveis no estoque.
def q20():
    return session.query(Produto).filter(Produto.estoque > 0).order_by(Produto.preco).limit(5).all()

# 21. Selecione os 3 pedidos mais recentes feitos por usuários com idade maior que 30 anos.
def q21():
    return session.query(Pedido, Usuario).join(Pedido, Usuario.id == Pedido.usuario_id).filter(Usuario.idade > 30).order_by(Pedido.data_pedido.desc()).limit(3).all()

# 22. Liste os usuários cadastrados, ignorando os 5 primeiros resultados.

def q22():
    return session.query(Usuario).offset(5).all()

# 23. Obtenha os produtos mais caros, pulando os 3 primeiros resultados na ordenação por preço.

def q23():
    return session.query(Produto).order_by(Produto.preco.desc()).offset(3).all()

# 24. Liste os pedidos realizados, ignorando os 8 primeiros, mas ordenados pela data de criação de forma decrescente.

def q24():
    return session.query(Pedido).order_by(Pedido.data_pedido.desc()).offset(8).all()

# 25. Conte quantos usuários estão cadastrados no sistema.
# (pendente de implementação)
def q25():
    pass

# 26. Determine o número de pedidos realizados com status "entregue".
# (pendente de implementação)
def q26():
    pass

# 27. Conte quantos produtos existem na categoria "eletrônicos" com estoque maior que 0 e preço acima de R$ 100,00.
# (pendente de implementação)
def q27():
    pass

# 28. Liste todas as categorias únicas de produtos disponíveis no sistema.
# (pendente de implementação)
def q28():
    pass

# 29. Identifique as idades únicas dos usuários cadastrados no banco de dados.
# (pendente de implementação)
def q29():
    pass

# 30. Obtenha todos os status únicos dos pedidos realizados por usuários ativos com mais de 25 anos de idade.
# (pendente de implementação)
def q30():
    pass

# 31. Liste o nome dos usuários e os IDs dos pedidos que eles realizaram.
# (pendente de implementação)
def q31():
    pass

# 32. Obtenha o nome dos produtos e a quantidade comprada em cada pedido realizado por um usuário específico chamado "João".
# (pendente de implementação)
def q32():
    pass

# 33. Liste todos os usuários que fizeram pedidos de produtos da categoria "livros", incluindo o nome do produto e a quantidade comprada em cada pedido.
# (pendente de implementação)
def q33():
    pass

# 34. Verifique se existe algum usuário chamado "Maria" cadastrado no sistema.
# (pendente de implementação)
def q34():
    pass

# 35. Confirme se há algum pedido realizado para um produto com estoque igual a 0.
# (pendente de implementação)
def q35():
    pass

# 36. Determine se existe algum pedido feito por um usuário inativo com status "pendente".
# (pendente de implementação)
def q36():
    pass

# 37. Retorne o nome e a idade de todos os usuários cadastrados no sistema.
# (pendente de implementação)
def q37():
    pass

# 38. Liste o nome dos produtos e seus preços para todos os itens cadastrados no banco de dados.
# (pendente de implementação)
def q38():
    pass

# 39. Obtenha o nome dos usuários, o ID dos pedidos e a quantidade comprada em cada pedido realizado por eles.
# (pendente de implementação)
def q39():
    pass

# 40. Agrupe os pedidos pelo status e conte quantos pedidos existem para cada status diferente no banco de dados.
# (pendente de implementação)
def q40():
    pass

# 41. Agrupe os produtos pela categoria e calcule o preço médio dos produtos em cada categoria disponível no sistema.
# (pendente de implementação)
def q41():
    pass

# 42. Agrupe os pedidos por usuário e calcule a soma total das quantidades compradas por cada usuário ativo com mais de 30 anos de idade.
# (pendente de implementação)
def q42():
    pass

# 43. Agrupe os pedidos pelo status e filtre apenas aqueles com mais de 3 registros em um único status usando having().
# (pendente de implementação)
def q43():
    pass

# 44. Agrupe os produtos pela categoria e filtre as categorias cujo preço médio seja maior que R$ 200,00 utilizando having().
# (pendente de implementação)
def q44():
    pass

# 45. Agrupe os pedidos por usuário, calcule a soma total das quantidades compradas e filtre apenas aqueles usuários cuja soma total seja maior que 10 usando having().
# (pendente de implementação)
def q45():
    pass


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Base, Usuario, Produto, Pedido, Avaliacao
engine = create_engine('sqlite:///exercicios.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


produtos = session.query(Produto).all()

#all()
# for produto in produtos:
#     print(produto)


usuarios = session.query(Usuario).all()
usuarios18 = []

pedidos = session.query(Pedido).all()

# 2
for usuario in usuarios:
    if usuario.idade >= 18:
        usuarios18.append(usuario)

# 3
pedidosMaiores = []
data_selecionada = '01/03/2025'
for pedido in pedidos:
    if pedido.data_pedido > datetime.strptime(data_selecionada, '%d/%m/%Y') and pedido.quantidade > 5:
        pedidosMaiores.append(pedido)


# 4
primeiro_usuario = session.query(Usuario).first()

# 5
eletronicos_por_preco = session.query(Produto).filter(Produto.categoria == 'eletrônicos').order_by(Produto.preco)
eletronico_barato = eletronicos_por_preco.first()

# 6
def UltimoPedido(id):
    ultimo_pedido = session.query(Pedido).filter(Pedido.usuario_id == id).order_by(Pedido.data_pedido.desc()).first()
    return ultimo_pedido

# 7
usuario7 = session.get(Usuario, 7)

# 8
def verificar_produto(id):
    produto = session.get(Produto, id)
    if produto.estoque > 0:
        return True
    else:
        return False
    
# 9
def pedido_e_usuario(id):
    pedido = session.get(Pedido, id)
    usuario = session.get(Usuario, pedido.usuario_id)

    return pedido, usuario

# 10

usuarios_entre_idade = session.query(Usuario).filter((Usuario.idade >= 25) & (Usuario.idade <= 35)).all()


# 11

pedidos_depois_2024 = session.query(Pedido).filter(((Pedido.status == 'cancelado') or (Pedido.status == 'pendente')) & Pedido.data_pedido > datetime.strptime('01/01/2025', '%d/%m/%Y')).all()

# 12

pedidos_acima_500 = session.query(Produto).filter(Produto.preco > 500).all()

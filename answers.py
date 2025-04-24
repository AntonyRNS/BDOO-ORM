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


for usuario in usuarios:
    if usuario.idade >= 18:
        usuarios18.append(usuario)


# for i in usuarios18:
#     print(i.nome)

pedidosMaiores = []
data_selecionada = '01/03/2025'
for pedido in pedidos:
    if pedido.data_pedido > datetime.strptime(data_selecionada, '%d/%m/%Y') and pedido.quantidade > 5:
        pedidosMaiores.append(pedido)


for i in pedidosMaiores:
    print(i.status)


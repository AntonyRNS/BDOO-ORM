from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from random import randint
from models import (
    Base, Usuario, Produto, Pedido, Avaliacao,
    Autor, Livro, Grupo, Medico, Paciente, Consulta
)

engine = create_engine('sqlite:///exercicios.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Usuários
usuarios = [
    Usuario(nome='Carlos', email='carlos@exemplo.com', idade=25, ativo=True),
    Usuario(nome='Maria', email='maria@exemplo.com', idade=30, ativo=True),
    Usuario(nome='João', email='joao@exemplo.com', idade=35, ativo=False),
    Usuario(nome='Ana', email='ana@exemplo.com', idade=28, ativo=True),
    Usuario(nome='Pedro', email='pedro@exemplo.com', idade=42, ativo=True),
    Usuario(nome='Julia', email='julia@exemplo.com', idade=19, ativo=False),
    Usuario(nome='Lucas', email='lucas@exemplo.com', idade=31, ativo=True),
    Usuario(nome='Fernanda', email='fernanda@exemplo.com', idade=27, ativo=True),
]
session.add_all(usuarios)
session.commit()

# Produtos
produtos = [
    Produto(nome='Livro Python', preco=80.0, categoria='livros', estoque=15),
    Produto(nome='Monitor 24"', preco=700.0, categoria='eletrônicos', estoque=5),
    Produto(nome='Cadeira Gamer', preco=1200.0, categoria='móveis', estoque=2),
    Produto(nome='Smartphone', preco=1500.0, categoria='eletrônicos', estoque=10),
    Produto(nome='Mesa Escritório', preco=450.0, categoria='móveis', estoque=0),
    Produto(nome='Caneta Esferográfica', preco=2.5, categoria='papelaria', estoque=100),
    Produto(nome='Notebook', preco=3500.0, categoria='eletrônicos', estoque=3),
    Produto(nome='Livro SQL', preco=95.0, categoria='livros', estoque=8),
]
session.add_all(produtos)
session.commit()

# Pedidos
pedidos = [
    Pedido(usuario_id=usuarios[0].id, produto_id=produtos[0].id, quantidade=2, status='entregue', data_pedido=datetime(2024, 12, 15)),
    Pedido(usuario_id=usuarios[1].id, produto_id=produtos[1].id, quantidade=1, status='pendente', data_pedido=datetime(2025, 1, 10)),
    Pedido(usuario_id=usuarios[2].id, produto_id=produtos[2].id, quantidade=1, status='cancelado', data_pedido=datetime(2025, 2, 20)),
    Pedido(usuario_id=usuarios[3].id, produto_id=produtos[3].id, quantidade=3, status='entregue', data_pedido=datetime(2025, 3, 5)),
    Pedido(usuario_id=usuarios[4].id, produto_id=produtos[4].id, quantidade=1, status='pendente', data_pedido=datetime(2025, 4, 1)),
    Pedido(usuario_id=usuarios[0].id, produto_id=produtos[5].id, quantidade=10, status='entregue', data_pedido=datetime(2025, 3, 10)),
    Pedido(usuario_id=usuarios[0].id, produto_id=produtos[6].id, quantidade=2, status='entregue', data_pedido=datetime(2025, 3, 12)),
    Pedido(usuario_id=usuarios[1].id, produto_id=produtos[7].id, quantidade=5, status='entregue', data_pedido=datetime(2025, 3, 15)),
    Pedido(usuario_id=usuarios[1].id, produto_id=produtos[0].id, quantidade=3, status='entregue', data_pedido=datetime(2025, 3, 18)),
    Pedido(usuario_id=usuarios[2].id, produto_id=produtos[1].id, quantidade=1, status='cancelado', data_pedido=datetime(2025, 3, 20)),
]
session.add_all(pedidos)
session.commit()

# Avaliações
avaliacoes = [
    Avaliacao(usuario_id=usuarios[0].id, nota=5, comentario='Ótimo produto'),
    Avaliacao(usuario_id=usuarios[1].id, nota=4, comentario='Boa qualidade'),
    Avaliacao(usuario_id=usuarios[2].id, nota=3, comentario='Regular'),
    Avaliacao(usuario_id=usuarios[3].id, nota=2, comentario='Não recomendo'),
    Avaliacao(usuario_id=usuarios[4].id, nota=5, comentario='Excelente'),
    Avaliacao(usuario_id=usuarios[5].id, nota=1, comentario='Péssimo atendimento'),
    Avaliacao(usuario_id=usuarios[6].id, nota=4, comentario='Atendimento rápido'),
    Avaliacao(usuario_id=usuarios[7].id, nota=5, comentario='Superou expectativas'),
]
session.add_all(avaliacoes)
session.commit()

# Autores
autores = [
    Autor(nome="Machado de Assis", nacionalidade="Brasileira"),
    Autor(nome="Jane Austen", nacionalidade="Britânica"),
    Autor(nome="George Orwell", nacionalidade="Britânica"),
    Autor(nome="Gabriel García Márquez", nacionalidade="Colombiana"),
    Autor(nome="J.K. Rowling", nacionalidade="Britânica"),
    Autor(nome="Franz Kafka", nacionalidade="Alemã"),
    Autor(nome="Ernest Hemingway", nacionalidade="Americana"),
    Autor(nome="Clarice Lispector", nacionalidade="Brasileira"),
    Autor(nome="Haruki Murakami", nacionalidade="Japonesa"),
    Autor(nome="Chinua Achebe", nacionalidade="Nigeriana"),
]
session.add_all(autores)
session.commit()

# Livros
livros = [
    Livro(titulo="Dom Casmurro", ano_publicacao=datetime(1899, 1, 1), autor=autores[0]),
    Livro(titulo="Orgulho e Preconceito", ano_publicacao=datetime(1813, 1, 1), autor=autores[1]),
    Livro(titulo="1984", ano_publicacao=datetime(1949, 1, 1), autor=autores[2]),
    Livro(titulo="Cem Anos de Solidão", ano_publicacao=datetime(1967, 1, 1), autor=autores[3]),
    Livro(titulo="Harry Potter e a Pedra Filosofal", ano_publicacao=datetime(1997, 6, 26), autor=autores[4]),
    Livro(titulo="A Metamorfose", ano_publicacao=datetime(1915, 1, 1), autor=autores[5]),
    Livro(titulo="O Velho e o Mar", ano_publicacao=datetime(1952, 1, 1), autor=autores[6]),
    Livro(titulo="A Hora da Estrela", ano_publicacao=datetime(1977, 1, 1), autor=autores[7]),
    Livro(titulo="Kafka à Beira-Mar", ano_publicacao=datetime(2002, 1, 1), autor=autores[8]),
    Livro(titulo="O Mundo se Despedaça", ano_publicacao=datetime(1958, 1, 1), autor=autores[9]),
]
session.add_all(livros)
session.commit()

# Grupos
grupos = [
    Grupo(nome="Admin", descricao="Administradores do sistema"),
    Grupo(nome="Editores", descricao="Usuários que podem editar conteúdos"),
    Grupo(nome="Visitantes", descricao="Acesso somente leitura"),
    Grupo(nome="Autores", descricao="Usuários que escrevem artigos"),
    Grupo(nome="Leitores", descricao="Público geral"),
    Grupo(nome="Moderadores", descricao="Moderação de conteúdo"),
    Grupo(nome="TI", descricao="Equipe de tecnologia"),
    Grupo(nome="RH", descricao="Recursos Humanos"),
    Grupo(nome="Financeiro", descricao="Gestão financeira"),
    Grupo(nome="Marketing", descricao="Equipe de marketing"),
]
session.add_all(grupos)
session.commit()

# Associação usuários e grupos
usuarios[0].grupos.extend([grupos[0], grupos[1]])
usuarios[1].grupos.extend([grupos[2], grupos[4]])
usuarios[2].grupos.extend([grupos[1], grupos[3]])
usuarios[3].grupos.extend([grupos[0], grupos[5]])
usuarios[4].grupos.append(grupos[6])
usuarios[5].grupos.extend([grupos[4], grupos[7]])
usuarios[6].grupos.append(grupos[8])
usuarios[7].grupos.extend([grupos[1], grupos[9]])
session.commit()

# Médicos
medicos = [
    Medico(nome="Dr. Ana", especialidade="Cardiologia"),
    Medico(nome="Dr. Bruno", especialidade="Neurologia"),
    Medico(nome="Dr. Carla", especialidade="Dermatologia"),
    Medico(nome="Dr. Daniel", especialidade="Pediatria"),
    Medico(nome="Dr. Elisa", especialidade="Ortopedia"),
    Medico(nome="Dr. Fabio", especialidade="Psiquiatria"),
    Medico(nome="Dr. Gisele", especialidade="Ginecologia"),
    Medico(nome="Dr. Henrique", especialidade="Urologia"),
    Medico(nome="Dr. Isabel", especialidade="Endocrinologia"),
    Medico(nome="Dr. João", especialidade="Oftalmologia"),
]
session.add_all(medicos)

# Pacientes
pacientes = [
    Paciente(nome="Patrícia", data_nascimento=datetime(1980, 5, 20)),
    Paciente(nome="Ricardo", data_nascimento=datetime(1975, 3, 10)),
    Paciente(nome="Sandra", data_nascimento=datetime(1990, 7, 25)),
    Paciente(nome="Thiago", data_nascimento=datetime(1988, 11, 5)),
    Paciente(nome="Úrsula", data_nascimento=datetime(1995, 9, 12)),
    Paciente(nome="Valter", data_nascimento=datetime(1960, 1, 30)),
    Paciente(nome="Wanda", data_nascimento=datetime(2000, 2, 14)),
    Paciente(nome="Xavier", data_nascimento=datetime(1983, 6, 8)),
    Paciente(nome="Yasmin", data_nascimento=datetime(1998, 4, 22)),
    Paciente(nome="Zeca", data_nascimento=datetime(1970, 12, 18)),
]
session.add_all(pacientes)
session.commit()

# Consultas
consultas = [
    Consulta(
        data_hora=datetime(2025, 5, i + 1, 9),
        medico_id=medicos[i].id,
        paciente_id=pacientes[i].id,
        duracao_minutos=randint(20, 60)
    ) for i in range(10)
]
session.add_all(consultas)
session.commit()

print("População concluída com sucesso!")

session.close()

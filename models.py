from sqlalchemy import (
    Column, Integer, String, ForeignKey, Float,
    DateTime, Boolean, func, UniqueConstraint, Table
)
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime, timedelta
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()

# Associação para muitos-para-muitos entre Usuario e Grupo
usuario_grupo = Table(
    'usuario_grupo', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id'), primary_key=True),
    Column('grupo_id', Integer, ForeignKey('grupos.id'), primary_key=True)
)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    idade = Column(Integer)
    ativo = Column(Boolean, default=True)

    pedidos = relationship('Pedido', back_populates='usuario')
    grupos = relationship("Grupo", secondary=usuario_grupo, back_populates="usuarios")

class Produto(Base):
    __tablename__ = 'produtos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    categoria = Column(String(50))
    estoque = Column(Integer, default=0)
    criado_em = Column(DateTime, default=datetime.now)

    @hybrid_property
    def valor_estoque(self):
        return self.estoque * self.preco

class Pedido(Base):
    __tablename__ = 'pedidos'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    quantidade = Column(Integer, nullable=False)
    status = Column(String(20), default='pendente')
    data_pedido = Column(DateTime, default=datetime.now)

    usuario = relationship('Usuario', back_populates='pedidos')
    produto = relationship('Produto')

    __table_args__ = (
        UniqueConstraint('usuario_id', 'produto_id', name='uq_usuario_produto'),
    )

class Avaliacao(Base):
    __tablename__ = 'avaliacoes'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    nota = Column(Integer, nullable=False)
    comentario = Column(String(300))

    usuario = relationship('Usuario')

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    nacionalidade = Column(String(100))

    livros = relationship("Livro", back_populates="autor")

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True)
    titulo = Column(String(100), nullable=False)
    ano_publicacao = Column(DateTime, default=datetime.now)
    autor_id = Column(Integer, ForeignKey('autores.id'))

    autor = relationship("Autor", back_populates="livros")

class Grupo(Base):
    __tablename__ = 'grupos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(100), nullable=False)

    usuarios = relationship("Usuario", secondary=usuario_grupo, back_populates="grupos")

class Medico(Base):
    __tablename__ = 'medicos'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    especialidade = Column(String(100), nullable=False)

    consultas = relationship('Consulta', back_populates='medico')

class Paciente(Base):
    __tablename__ = 'pacientes'
    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    data_nascimento = Column(DateTime, default=datetime.now)

class Consulta(Base):
    __tablename__ = 'consultas'
    id = Column(Integer, primary_key=True)
    data_hora = Column(DateTime, default=datetime.now)
    medico_id = Column(Integer, ForeignKey('medicos.id'))
    paciente_id = Column(Integer, ForeignKey('pacientes.id'))
    duracao_minutos = Column(Integer, default=30)

    medico = relationship('Medico', back_populates='consultas')

    @hybrid_property
    def calcular_termino(self):
        return self.data_hora + timedelta(minutes=self.duracao_minutos)

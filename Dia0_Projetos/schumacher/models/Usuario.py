from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from schumacher.database.database import db

#    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
#     nome VARCHAR(100) NOT NULL,
#     sobrenome VARCHAR(100) NOT NULL,
#     data_nascimento DATE NOT NULL,
#     cpf VARCHAR(11) UNIQUE NOT NULL

class Usuario(db.Base):
    __tablename__ =  "usuarios"

    id  = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    sobrenome = Column(String, nullable=False)
    data_nascimento = Column(Da)
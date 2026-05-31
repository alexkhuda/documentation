from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from data_access_layer.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    full_name = Column(String)
    email = Column(String, unique=True)

    cards = relationship("PaymentCard", back_populates="user")


class IssuerCountry(Base):

    __tablename__ = "issuer_countries"

    id = Column(Integer, primary_key=True)

    country_name = Column(String)
    currency = Column(String)

    cards = relationship("PaymentCard", back_populates="country")


class PaymentCard(Base):

    __tablename__ = "payment_cards"

    id = Column(Integer, primary_key=True)

    card_number = Column(String)
    balance = Column(Float)

    user_id = Column(Integer, ForeignKey("users.id"))
    country_id = Column(Integer, ForeignKey("issuer_countries.id"))

    user = relationship("User", back_populates="cards")
    country = relationship("IssuerCountry", back_populates="cards")
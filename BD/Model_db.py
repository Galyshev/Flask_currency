from sqlalchemy import Column, Integer, String, Float
from BD.alchemy import Base


class Currency(Base):
    __tablename__ = "curr_history"

    id = Column(Integer, primary_key=True)
    bank = Column(String)
    date = Column(String)
    currency = Column(String)
    buy_value = Column(Float)
    sell_value = Column(Float)

    def __init__(self, id, bank, date, currency, buy_value, sell_value):
        self.id = id
        self.bank = bank
        self.date = date
        self.currency = currency
        self.buy_value = buy_value
        self.sell_value = sell_value

    # def __repr__(self):
    #     return f"Currency(id={self.id!r}, bank={self.bank!r}, date={self.date!r}, currency={self.currency!r}, " \
    #            f"buy_value={self.buy_value!r},sell_value={self.sell_value!r})"
from sqlalchemy import Column, BigInteger, String
from sqlalchemy.ext.hybrid import hybrid_property

from model.base import Base


class Cname(Base):
    __tablename__ = 'cname'
    __id = Column('id', BigInteger, primary_key=True)
    __http_requests_id = Column('http_requests_id', BigInteger)
    __cname = Column('cname', String)
    __ip = Column('ip', String)

    def __init__(self,
                 http_requests_id: int,
                 cname: str,
                 ip: str):
        self.__http_requests_id = http_requests_id
        self.__cname = cname
        self.__ip = ip

    @hybrid_property
    def id(self):
        return self.__id

    @hybrid_property
    def http_requests_id(self):
        return self.__http_requests_id

    @hybrid_property
    def cname(self):
        return self.__cname

    @hybrid_property
    def ip(self):
        return self.__ip

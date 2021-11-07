from __future__ import annotations

from datetime import date as dt
from typing import List, Optional, Tuple, Union

from pydantic import BaseModel
from pydantic.class_validators import validator


class Record(BaseModel):
    account: str
    value: float


class Transaction(BaseModel):
    date: dt
    description: Optional[str]
    records: List[Record]

    def detailed(self) -> Transaction:
        return self


class ShortTransaction(BaseModel):
    date: dt
    description: Optional[str]
    accounts: Tuple[str, str]
    value: float

    def detailed(self) -> Transaction:
        r1 = Record(account=self.accounts[0], value=self.value)
        r2 = Record(account=self.accounts[1], value=-self.value)
        return Transaction(
            date=self.date,
            description=self.description,
            records=[r1, r2]
        )


class Book(BaseModel):
    name: Optional[str]
    transactions: List[Transaction]


class ParsedBook(BaseModel):
    version: str
    name: Optional[str]
    transactions: List[Union[ShortTransaction, Transaction]]

    @validator('version')
    def version_must_be_v1(cls, v: str) -> str:
        if '1.0' not in v:
            raise ValueError('must contain one of the valid versions: ["1.0"]')
        return v.title()

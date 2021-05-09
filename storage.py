from redis import Redis as PyRedis
from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def set(self, key, value):
        pass


class InMemory(Storage):
    def __init__(self):
        self.data = dict()

    def get(self, key):
        return self.data.get(key, None)

    def set(self, key, value):
        self.data[key] = value


class Redis(Storage):
    def __init__(self):
        self.data = PyRedis()

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data.set(key, value)


class Store:
    store = Storage()

    @classmethod
    def __init__(cls, t):
        if t == 'redis':
            cls.store = Redis()
        else:
            cls.store = InMemory()

    @classmethod
    def get(cls, key):
        return cls.store.get(key)

    @classmethod
    def set(cls, key, value):
        cls.store.set(key, value)

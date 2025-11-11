from abc import ABC, abstractmethod

#===============Questão 1===============
class ConfigServiceSingleton():
    """Classe que representa a configuração do programa. Ela é implementada com
    o padrão de projeto singleton, o que significa que apenas uma instância dela
    pode existir. O acesso a ela é feito usando o método de classe `get_instance`.
    (implementado com a opção 2 do enunciado)"""
    _inst = None

    # Em uma linguagem que permite métodos protegidos/privados, o construtor não deve ser
    # mantido público. Em Python não há essa opção, então o que previne a criação da classe
    # pelo construtor é sobreescrever o método new.
    def __new__(cls) -> None:
        return None

    @classmethod
    def get_instance(cls) -> "ConfigServiceSingleton":
        """Retorna a única instância existente da classe.
        
        Returns
        -------
            ConfigServicesSingleton: a instância."""
        if cls._inst is None:
            print("[ConfigServiceSingleton] Criando nova instância.")
            cls._inst = super().__new__(cls)
        else:
            print("[ConfigServiceSingleton] Usando instância existente.")
        return cls._inst

    @classmethod
    def _reset_for_tests(cls) -> None:
        """Método para testes que desfaz a instância existente."""
        cls._inst = None
        print("[ConfigServiceSingleton] Apagando a instância existente para testes.")

#===============Questão 2===============

# Interfaces dos produtos
class Repository(ABC):
    @abstractmethod
    def start_connection(self, db_name: str) -> None: ...

class CacheClient(ABC):
    @abstractmethod
    def add_to_cache(self, query: str) -> None: ...

# Produtos concretos para SQLite e Postgres
class RepositorySQLite(Repository):
    def start_connection(self, db_name: str) -> None:
        print("[Repository] Criando conexão para SQLite")
    
class CacheClientSQLite(CacheClient):
    def add_to_cache(self, query: str) -> None:
        print("[CacheClient] Adicionando query no cache para SQLite")
        
class RepositoryPostgres(Repository):
    def start_connection(self, db_name: str) -> None:
        print("[Repository] Criando conexão para Postgres")
    
class CacheClientPostgres(CacheClient):
    def add_to_cache(self, query: str) -> None:
        print("[CacheClient] Adicionando query no cache para Postgres")

# Interface da abstract factory
class DatabaseFactory(ABC):
    @abstractmethod
    def create_repository(self) -> Repository: ...
    
    @abstractmethod
    def create_cache_client(self) -> CacheClient: ...

# Subclasses para famílias de produtos específicas
class SQLiteFactory(DatabaseFactory):
    def create_repository(self) -> RepositorySQLite:
        return RepositorySQLite()
    
    def create_cache_client(self) -> CacheClientSQLite:
        return CacheClientSQLite()
    
class PostgresFactory(DatabaseFactory):
    def create_repository(self) -> RepositoryPostgres:
        return RepositoryPostgres()
    
    def create_cache_client(self) -> CacheClientPostgres:
        return CacheClientPostgres()
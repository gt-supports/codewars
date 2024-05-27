from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session)

class DatabaseHelper:
    def __init__(self, url: str, echo:bool = False):
        self.engine = create_async_engine(
            url = url,
            echo = echo,
        )
        self.session_factory = async_sessionmaker(
            bind = self.engine,
            autoflush = False,
            autocommit = False,
            expire_on_commit = False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            sesssion_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self):
        async with self.get_scoped_session() as session:
            yield session
            await session.remove()



db_helper = DatabaseHelper(
    url = settings.db_url,
    echo=settings.dbecho,
)
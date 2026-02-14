from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select, desc
from .models import Book
from .schemas import BookCreateModel, BookUpdateModel
from datetime import datetime
import uuid

class BookService:
    async def get_all_books(self, session: AsyncSession):
        statement = select(Book).order_by(desc(Book.created_at))
        result = await session.execute(statement)
        return result.scalars().all()

    async def get_book(self, book_uid: str, session: AsyncSession):  # Changed to str
        statement = select(Book).where(Book.uid == book_uid)
        result = await session.execute(statement)
        return result.scalar_one_or_none()

    async def create_book(self, book_data: BookCreateModel, session: AsyncSession):
        book_data_dict = book_data.model_dump()
        # Generate UUID as string
        book_data_dict["uid"] = str(uuid.uuid4())
        new_book = Book(**book_data_dict)
        
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        
        return new_book

    async def update_book(self, book_uid: str, update_data: BookUpdateModel, session: AsyncSession):  # Changed to str
        book_to_update = await self.get_book(book_uid, session)
        
        if book_to_update is not None:
            update_data_dict = update_data.model_dump(exclude_unset=True)
            
            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)
            
            book_to_update.updated_at = datetime.now()
            
            await session.commit()
            await session.refresh(book_to_update)
            
            return book_to_update
        else:
            return None

    async def delete_book(self, book_uid: str, session: AsyncSession):  # Changed to str
        book_to_delete = await self.get_book(book_uid, session)
        
        if book_to_delete is not None:
            await session.delete(book_to_delete)
            await session.commit()
            return True
        else:
            return False
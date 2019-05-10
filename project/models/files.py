from sqlalchemy import Column, String, Table, MetaData
from sqlalchemy.dialects.postgresql import UUID
import uuid

metadata = MetaData()
Files = Table(
    'files',
    metadata,
    Column('file_uuid', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()),
    Column('dist', String(1024), nullable=False),
    Column('mimetype', String(50), nullable=False)
)
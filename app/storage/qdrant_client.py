import asyncio
from qdrant_client import AsyncQdrantClient
from qdrant_client.http.models import Distance, VectorParams
from app.config.settings import settings


class QdrantHandler:
    def __init__(self):
        self.client = AsyncQdrantClient(
            host=settings.QDRANT_HOST,
            port=settings.QDRANT_PORT,
        )

    async def init_collection(self):
        """Initialize CV collection if not exists."""
        try:
            collections = await self.client.get_collections()
            if settings.CV_COLLECTION not in [c.name for c in collections.collections]:
                await self.client.create_collection(
                    collection_name=settings.CV_COLLECTION,
                    vectors_config=VectorParams(
                        size=768, distance=Distance.COSINE  # embedding vector size
                    ),
                )
                print(f"✅ Created collection: {settings.CV_COLLECTION}")
            else:
                print(f"ℹ️ Collection already exists: {settings.CV_COLLECTION}")
        except Exception as e:
            print(f"❌ Error creating collection: {e}")
            raise

    async def upsert_cv(self, cv_id: str, vector: list[float], metadata: dict):
        """Insert or update a CV vector with metadata."""
        try:
            await self.client.upsert(
                collection_name=settings.CV_COLLECTION,
                points=[{"id": cv_id, "vector": vector, "payload": metadata}],
            )
            print(f"✅ Upserted CV: {cv_id}")
        except Exception as e:
            print(f"❌ Failed to upsert CV {cv_id}: {e}")

    async def search_cv(self, query_vector: list[float], top_k: int = 5, filters=None):
        """Search CVs based on query vector."""
        try:
            results = await self.client.search(
                collection_name=settings.CV_COLLECTION,
                query_vector=query_vector,
                limit=top_k,
                query_filter=filters,
            )
            return results
        except Exception as e:
            print(f"❌ Search failed: {e}")
            return []


# Quick test run
if __name__ == "__main__":

    async def main():
        handler = QdrantHandler()
        await handler.init_collection()

    asyncio.run(main())

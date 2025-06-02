"""
MongoDB connection and utility functions
"""
import pymongo
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

class MongoDBConnection:
    _instance = None
    _client = None
    _db = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoDBConnection, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._client is None:
            try:
                self._client = pymongo.MongoClient(settings.MONGODB_URI)
                self._db = self._client[settings.MONGODB_DB_NAME]
                # Test connection
                self._client.admin.command('ping')
                logger.info("MongoDB connection established successfully")
            except Exception as e:
                logger.error(f"MongoDB connection failed: {e}")
                # Fallback to local MongoDB for demo
                try:
                    self._client = pymongo.MongoClient('mongodb://localhost:27017/')
                    self._db = self._client[settings.MONGODB_DB_NAME]
                    logger.info("Connected to local MongoDB")
                except Exception as local_e:
                    logger.error(f"Local MongoDB connection also failed: {local_e}")
                    self._client = None
                    self._db = None
    
    @property
    def client(self):
        return self._client
    
    @property
    def db(self):
        return self._db
    
    def get_collection(self, collection_name):
        if self._db is not None:
            return self._db[collection_name]
        return None

# Global MongoDB instance
mongodb = MongoDBConnection()

def get_db():
    """Get MongoDB database instance"""
    return mongodb.db

def get_collection(collection_name):
    """Get MongoDB collection"""
    return mongodb.get_collection(collection_name)

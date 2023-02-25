import os

MONGODB_HOST = os.getenv("MONGODB_HOSTNAME", "0.0.0.0")
MONGODB_DBNAME = os.getenv("MONGODB_DATABASE", "helloworld")
MONGODB_USER_COLLECTION_NAME = os.getenv("MONGODB_COLLECTION", "users")
MONGODB_USER = os.getenv("MONGODB_USERNAME", "user")
MONGODB_PW = os.getenv("MONGODB_PASSWORD", "secret_password")
MONGODB_PORT = 27017
MONGO_AUTH_SOURCE = "admin"
MONGO_READ_PREFERENCE = "secondaryPreferred"
MONGO_REPLICA_SET = ""  # depends on mongo is cluster

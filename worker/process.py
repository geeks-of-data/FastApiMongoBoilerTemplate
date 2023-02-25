from worker.helpers.mongo import get_mongo_collection
from worker.conf import *


def get_user_collection():
    collection = get_mongo_collection(
        mongodb_hosts=MONGODB_HOST,
        read_preference=MONGO_READ_PREFERENCE,
        username=MONGODB_USER,
        mongodb_auth_source=MONGO_AUTH_SOURCE,
        password=MONGODB_PW,
        replica_set=MONGO_REPLICA_SET,
        db_name=MONGODB_NAME,
        collection_name=MONGODB_USER_COLLECTION_NAME
    )
    return collection


def _get_users():
    col = get_user_collection()
    result = list(col.find({}))
    return result


def _get_user(username):
    col = get_user_collection()
    result = list(col.find({"username": username}))
    return result

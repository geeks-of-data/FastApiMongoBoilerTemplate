import logging

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


def _get_users(skip, limit):
    col = get_user_collection()
    result = list(col.find({}, {"_id": 0}).skip(skip).limit(limit))
    return result


def _get_user(username):
    col = get_user_collection()
    result = list(col.find({"username": username}, {"_id": 0}))
    return result


def _create_user(data):
    col = get_user_collection()
    doc_id = col.insert_one(data)
    logging.info(doc_id)
    return doc_id


def _update_user(data):
    col = get_user_collection()
    data_filter = {"username": data['username']}
    query = {"$set": data}
    col.update_one(data_filter, query)


def _delete_user(data):
    pass

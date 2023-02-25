import logging

from worker.helpers.mongo import get_mongo_collection, get_data, insert_data, update_data
from worker.conf import *


def get_user_collection():
    return get_mongo_collection(
        mongodb_hosts=MONGODB_HOST,
        read_preference=MONGO_READ_PREFERENCE,
        username=MONGODB_USER,
        mongodb_auth_source=MONGO_AUTH_SOURCE,
        password=MONGODB_PW,
        replica_set=MONGO_REPLICA_SET,
        db_name=MONGODB_NAME,
        collection_name=MONGODB_USER_COLLECTION_NAME
    )


def _get_users(skip, limit):
    col = get_user_collection()
    return get_data(
        col=col,
        data_filter={},
        skip=skip,
        limit=limit
    )


def _get_user(username):
    col = get_user_collection()
    return get_data(
        col=col,
        data_filter={"username": username}
    )


def _create_user(data):
    col = get_user_collection()
    return insert_data(col, data)


def _update_user(data, username):
    col = get_user_collection()
    query = {"username": username}
    new_values = {"$set": data}
    return update_data(col, query, new_values)


def _delete_user(data):
    pass

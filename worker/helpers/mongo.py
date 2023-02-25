import logging

from pymongo import MongoClient


def get_mongo_client(mongodb_hosts, read_preference, replica_set, password, username, mongodb_auth_source):
    if replica_set == "":
        logging.info("Standalone Mongo")
        if username == "":
            logging.info("No username, no password for mongo")
            client = MongoClient(
                host=mongodb_hosts,
                readPreference=read_preference,
                authSource=mongodb_auth_source,
                connectTimeoutMS=None
            )
        else:
            client = MongoClient(
                host=mongodb_hosts,
                username=username,
                password=password,
                authSource=mongodb_auth_source,
                connectTimeoutMS=None
            )
    else:
        logging.info("Replica Mongo")
        client = MongoClient(
            host=mongodb_hosts,
            readPreference=read_preference,
            replicaSet=replica_set,
            password=password,
            username=username,
            authSource=mongodb_auth_source,
            connectTimeoutMS=None
        )
    logging.info("mongo health check")
    try:
        logging.info(client.server_info())
    except Exception as ex:
        logging.info(str(ex))
        raise Exception(ex)
    return client


def get_mongo_collection(mongodb_hosts, read_preference, replica_set, password, username, mongodb_auth_source, db_name,
                         collection_name):
    try:
        client = get_mongo_client(mongodb_hosts, read_preference, replica_set, password, username, mongodb_auth_source)
        return client.get_database(db_name).get_collection(collection_name)
    except Exception as ex:
        raise Exception(ex)

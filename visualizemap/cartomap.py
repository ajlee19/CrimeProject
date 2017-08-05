# #https://github.com/CartoDB/carto-python

# from carto.auth import NoAuthClient
# from carto.auth import APIKeyAuthClient
# from carto.sql import SQLClient
# from carto.sql import BatchSQLClient
# from carto.datasets import DatasetManager
# from carto.sync_tables import SyncTableJobManager
# from carto.file_import import FileImportJobManager
# from carto.datasets import DatasetManager
# from carto.visualizations import VisualizationManager
# from carto.maps import NamedMapManager, NamedMap
# import json
# from carto.maps import AnonymousMap

# # write here the path to a local file or remote URL
# LOCAL_FILE = "policeData2018.csv"

# dataset_manager = DatasetManager(auth_client)
# dataset = dataset_manager.create(LOCAL_FILE)

# # # how often to sync the dataset (in seconds)
# # SYNC_TIME = 900
# # URL_TO_DATASET = ""

# # dataset_manager = DatasetManager(auth_client)
# # dataset = dataset_manager.create(URL_TO_DATASET, SYNC_TIME)

# # syncTableManager = SyncTableJobManager(auth_client)
# # syncTable = syncTableManager.create(URL_TO_DATASET, SYNC_TIME)

# # # return the id of the sync
# # sync_id = syncTable.get_id()

# # while(syncTable.state != 'success'):
# #     time.sleep(5)
# #     syncTable.refresh()
# #     if (syncTable.state == 'failure'):
# #         print('The error code is: ' + str(syncTable.error_code))
# #         print('The error message is: ' + str(syncTable.error_message))
# #         break

# # # force sync
# # syncTable.refresh()
# # syncTable.force_sync()



# USERNAME="alee19"
# USR_BASE_URL = "https://alee19.carto.com/".format(user=USERNAME)
# auth_client = NoAuthClient(base_url=USR_BASE_URL)
# # auth_client = APIKeyAuthClient(api_key="myapikey", base_url=USR_BASE_URL)

# file_import_manager = FileImportJobManager(auth_client)
# file_imports = file_import_manager.all()

# # write here the ID of the dataset to retrieve
# DATASET_ID = ""

# dataset_manager = DatasetManager(auth_client)
# dataset = dataset_manager.get(DATASET_ID)

# sql = SQLClient(auth_client)

# LIST_OF_SQL_QUERIES = []

# batchSQLClient = BatchSQLClient(auth_client)
# createJob = batchSQLClient.create(LIST_OF_SQL_QUERIES)

# print(createJob['job_id'])

# # check the status of a job after it has been created and you have the job_id
# readJob = batchSQLClient.read(job_id)

# # update the query of a batch job
# updateJob = batchSQLClient.update(job_id, NEW_QUERY)

# # cancel a job given its job_id
# cancelJob = batchSQLClient.cancel(job_id)

# # try:
# #     data = sql.send('select * from mytable') #MUST SPECIFY ROW AND COL
# # except CartoException as e:
# #     print("some error ocurred", e)
# # print data['rows']

# # write here the name of the map to export
# MAP_NAME = ""

# visualization_manager = VisualizationManager(auth_client)
# visualization = visualization_manager.get(MAP_NAME)

# url = visualization.export()

# # the URL points to a .carto file
# print(url)

# # write the path to a local file with a JSON named map template
# JSON_TEMPLATE = ""

# named_map_manager = NamedMapManager(auth_client)
# named_map = NamedMap(named_map_manager.client)

# with open(JSON_TEMPLATE) as named_map_json:
#     template = json.load(named_map_json)

# # Create named map
# named = named_map_manager.create(template=template)

# # write the path to a local file with a JSON named map template
# JSON_TEMPLATE = ""

# anonymous = AnonymousMap(auth_client)
# with open(JSON_TEMPLATE) as anonymous_map_json:
#     template = json.load(anonymous_map_json)

# # Create anonymous map
# anonymous.instantiate(template)

# # write the path to a local file with a JSON named map template
# JSON_TEMPLATE = ""

# # write here the ID of the named map
# NAMED_MAP_ID = ""

# # write here the token you set to the named map when created
# NAMED_MAP_TOKEN = ""

# named_map_manager = NamedMapManager(auth_client)
# named_map = named_map_manager.get(NAMED_MAP_ID)

# with open(JSON_TEMPLATE) as template_json:
#     template = json.load(template_json)

# named_map.instantiate(template, NAMED_MAP_TOKEN)

# from carto.maps import NamedMapManager, NamedMap

# # write here the ID of the named map
# NAMED_MAP_ID = ""

# # get the named map created
# named_map = named_map_manager.get(NAMED_MAP_ID)

# # update named map
# named_map.view = None
# named_map.save()

# # delete named map
# named_map.delete()

# # list all named maps
# named_maps = named_map_manager.all()


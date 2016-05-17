'''
 - create prod_config dictionary, where dict keys are connection properties names and dict values are appropriate
values from the input tuple;
 - create staging_config dictionary with the same keys and values as prod_config;
 - in staging_config change host to 'semantic.amazonaws-staging.com' and password to 'root';
 - for prod_config and staging_config print connection strings in the following format
{dialect}://{user name}:{password}@{host}:{port}/{database name}
'''

keys = 'semantic','semantic.amazonaws-prod.com','admin','123456','5432','postgresql','root'
#    str = "{dialect}://{user name}:{password}@{host}:{port}/{database name}"
prod_con_str = '{0}://{1}:{2}@{3}:{4}/{5}'.format(keys[5],keys[2],keys[3],keys[1],keys[4],keys[0])
print (prod_con_str)




'''
 - create prod_config dictionary, where dict keys are connection properties names and dict values are appropriate
values from the input tuple;
 - create staging_config dictionary with the same keys and values as prod_config;
 - in staging_config change host to 'semantic.amazonaws-staging.com' and password to 'root';
 - for prod_config and staging_config print connection strings in the following format
{dialect}://{user name}:{password}@{host}:{port}/{database name}
'''

q =  5432,'postgresql'
env = ('staging', 'prod')
prod_cred = 'admin', '12345'
hosts = 'semantic', 'semantic.amazonaws-prod.com'
#    str = "{dialect}://{user name}:{password}@{host}:{port}/{database name}"
print "prod_config connection string : ", '{}://{}:{}@{}:{}/{}'.format('D',prod_cred[0],prod_cred[1],q[0],hosts[0],q[1])
print "stg_config connection string : ", '{}://{}:{}@{}:{}/{}'.format('D',prod_cred[0],'root',q[0],hosts[1],q[1])




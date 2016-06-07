'''
 - create prod_config dictionary, where dict keys are connection properties names and dict values are appropriate
values from the input tuple;
 - create staging_config dictionary with the same keys and values as prod_config;
 - in staging_config change host to 'semantic.amazonaws-staging.com' and password to 'root';
 - for prod_config and staging_config print connection strings in the following format
{dialect}://{user name}:{password}@{host}:{port}/{database name}
'''
values = {
        'dialect':'dialect',
        'host':'semantic.amazonaws-prod.com',
        'port':5432,
        'database name':'postgresql',
        'user name':'admin',
        'password':'12345'}

prod_con_str = '{0}://{1}:{2}@{3}:{4}/{5}'.format(values['dialect'], values['user name'], values['password'],values['host'], values['port'], values['database name'])
print "Prod str :", prod_con_str
values['host2'] = 'semantic'
values['password2'] = 'root'
prod_con_str = '{0}://{1}:{2}@{3}:{4}/{5}'.format(values['dialect'], values['user name'], values['password2'],values['host2'], values['port'], values['database name'])
print "Stg str :", prod_con_str

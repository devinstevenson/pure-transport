from sqlalchemy import create_engine
import puretransport

transport = puretransport.transport_factory(host='host',
                                            port=10000,
                                            username='username',
                                            password='secret')

# connection string pattern hive://username@/database_name
engine = create_engine('hive://username@/default',
                       connect_args={'thrift_transport': transport})
result = engine.execute("select * from table limit 1")

print result.fetchall()

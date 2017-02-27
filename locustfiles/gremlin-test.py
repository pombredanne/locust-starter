from locust import HttpLocust, TaskSet
import json, random

class UserBehavior(TaskSet):
    def fetch(self):
        package_list = ['io.vertx:vertx-web','io.vertx:vertx-mongo-client','io.vertx:vertx-core',
                        'io.vertx:vertx-hazelcast','io.vertx:vertx-jdbc-client']
        str_gremlin = "g.V().has('pecosystem', 'npm').has('pname', '"+str(random.choice(package_list))+"')" \
                      ".has('version', '3.3.3').toList();"
        payload = {'gremlin': str_gremlin}
        self.client.post("/", data=json.dumps(payload))

    tasks = {fetch : 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100
    max_wait = 100
from locust import HttpLocust, TaskSet, task
import os


class UserTasks(TaskSet):

    @task
    def version(self):
        """ Test version endpoint """
        self.client.get("/forge/version")

    @task
    def validate(self):
        """ Test validation endpoint """
        data = {
            "state": {},
            "stepIndex": 1,
            "inputs": [
                {
                    "name": "type",
                    "value": "Vert.x"
                },
                {
                    "name": "named",
                    "value": "demo"
                },
                {
                    "name": "topLevelPackage",
                    "value": "com.example"
                },
                {
                    "name": "version",
                    "value": "1.0.0-SNAPSHOT"
                },
                {
                    "name": "vertxVersion",
                    "value": "3.4.0.Beta1"
                },
                {
                    "name": "dependencies",
                    "value": [
                        "Vert.x Web",
                        "Vert.x Mongo Client"
                    ]
                }
            ]
        }

        self.client.post(
            "/forge/commands/obsidian-new-quickstart/validate", json=data)

    @task
    def execute(self):
        """Test zip file generation and download"""
        data = {"stepIndex": "1", "type": "Vert.x", "named": "demo", "topLevelPackage": "com.example", "version": "1.0.0-SNAPSHOT",
                "vertxVersion": "3.4.0.Beta1", "dependencies": ["Vert.x Mongo Client", "Vert.x (async) JDBC Client", "Vert.x Redis Client", "Vert.x Web Template Engine based on Thymeleaf", "Vert.x (async) RPC service proxies"]}
        self.client.post("/forge/commands/obsidian-new-project/execute", data)


class WebsiteUser(HttpLocust):
    """
    Locust user class that does requests to the locust web server running on localhost
    """

    host = os.environ.get("HOST").rstrip("/") + ":" + os.environ.get("PORT", "80")
    min_wait = 2000
    max_wait = 5000
    task_set = UserTasks

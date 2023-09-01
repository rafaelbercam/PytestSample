import requests

import setup.setup

ENDPOINT = setup.setup.SetupClass.base_url()


class TodoRequest:

    def create_task(self):
        return requests.put(ENDPOINT + "/create-task", json=self)

    def update_task(self):
        return requests.put(ENDPOINT + "/update-task", json=self)

    def get_task_by_id(self):
        return requests.get(ENDPOINT + f"/get-task/{self}")

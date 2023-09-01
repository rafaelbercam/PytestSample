class TodoData:

    def new_task_payload(self):
        return {
            "content": "my test content",
            "user_id": "my test user_id",
            "is_done": self
        }

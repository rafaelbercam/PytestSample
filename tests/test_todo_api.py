from services import todo_requests
from data import todo_data

call = todo_requests.TodoRequest
data_payload = todo_data.TodoData


class TestClassTodo:

    def test_can_create_task(self):
        payload = data_payload.new_task_payload(False)
        response_create = call.create_task(payload)
        assert response_create.status_code == 200
        data = response_create.json()
        task_id = data["task"]["task_id"]
        response_get_task = call.get_task_by_id(task_id)
        assert response_get_task.status_code == 200
        get_task_data = response_get_task.json()
        assert get_task_data["content"] == payload["content"]
        assert get_task_data["user_id"] == payload["user_id"]
        print(get_task_data)

    def test_update_task(self):
        payload = data_payload.new_task_payload(False)
        create_response = call.create_task(payload)
        task_id = create_response.json()["task"]["task_id"]
        assert create_response.status_code == 200

        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "my updated content",
            "is_done": True
        }

        updated_task_response = call.update_task(new_payload)
        assert updated_task_response.status_code == 200

        get_task_response = call.get_task_by_id(task_id)
        assert get_task_response.status_code == 200
        get_task_data = get_task_response.json()
        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["is_done"] == new_payload["is_done"]

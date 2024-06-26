{
	"info": {
		"_postman_id": "d335c57a-a4c2-42d9-9dc8-cd636e055d5f",
		"name": "project_management",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "25281354"
	},
	"item": [
		{
			"name": "user login",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"username\": \"newuser3\",\r\n    \"password\": \"password123\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/users/login/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"users",
						"login",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "user register",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"username\": \"newuser2\",\r\n    \"password\": \"password123\",\r\n    \"email\": \"newuser2@example.com\",\r\n    \"first_name\": \"newuser2\",\r\n    \"last_name\": \"LastName\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/users/register/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"users",
						"register",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "user details",
			"request": {
				"method": "GET",
				"header": []
			},
			"response": []
		},
		{
			"name": "Delete user",
			"request": {
				"method": "DELETE",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzcxNjk0LCJpYXQiOjE3MTkzNjk4OTQsImp0aSI6IjQ0YjkxZDMxMDUzOTQ1ZGJiOWM4ZDgyYTcwMzI2MGE3IiwidXNlcl9pZCI6ImY5ODYzMjA4LTgzMTAtNGM3MC1iYzAwLTYyYTIyYWE4ODdlNiJ9.VuATWwMjPKbUa12gqfBrqDVJD8onJsTLjhdt3wldNYM",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/users/f9863208-8310-4c70-bc00-62a22aa887e6/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"users",
						"f9863208-8310-4c70-bc00-62a22aa887e6",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Partial update user profile",
			"request": {
				"method": "PATCH",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzcxNjk0LCJpYXQiOjE3MTkzNjk4OTQsImp0aSI6IjQ0YjkxZDMxMDUzOTQ1ZGJiOWM4ZDgyYTcwMzI2MGE3IiwidXNlcl9pZCI6ImY5ODYzMjA4LTgzMTAtNGM3MC1iYzAwLTYyYTIyYWE4ODdlNiJ9.VuATWwMjPKbUa12gqfBrqDVJD8onJsTLjhdt3wldNYM",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"first_name\": \"UpdatedFirstName\",\r\n  \"last_name\": \"UpdatedLastName\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/users/f9863208-8310-4c70-bc00-62a22aa887e6/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"users",
						"f9863208-8310-4c70-bc00-62a22aa887e6",
						""
					],
					"query": [
						{
							"key": "first_name",
							"value": "changefirstname",
							"disabled": true
						}
					]
				}
			},
			"response": []
		},
		{
			"name": "User full details update",
			"request": {
				"method": "PUT",
				"header": [
					{
						"key": "",
						"value": "",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/users/f9863208-8310-4c70-bc00-62a22aa887e6/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"users",
						"f9863208-8310-4c70-bc00-62a22aa887e6",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Create a project",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5Mzc1OTE4LCJpYXQiOjE3MTkzNzQxMTgsImp0aSI6IjAwZjNhMzIwZTAyMjQ4NDg5OTI1OTc3NDA3ODVhNzU2IiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.K5fU62FtVPMd92x2wFet0K3Q8zbux0L2tgp3IWiZI_0",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"name\": \"Project universe\",\r\n    \"description\": \"This is a unique project.\"\r\n    \r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/projects/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"projects",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Project List view",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzgxMzY1LCJpYXQiOjE3MTkzNzk1NjUsImp0aSI6IjdiMWRmY2FiOTA0YTQ1ODVhYjY2M2Q2ZmU0ZmE4ZjkyIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.PBfdgokRMo9cFjqywY0_Vk10QXIoboQPxvSGGweAQ-s",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/projects/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"projects",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": " Retrieve details of a specific project",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzgxMzY1LCJpYXQiOjE3MTkzNzk1NjUsImp0aSI6IjdiMWRmY2FiOTA0YTQ1ODVhYjY2M2Q2ZmU0ZmE4ZjkyIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.PBfdgokRMo9cFjqywY0_Vk10QXIoboQPxvSGGweAQ-s",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/projects/9ffaaed7-3a69-4750-ac7e-48f1a4362d8e",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"projects",
						"9ffaaed7-3a69-4750-ac7e-48f1a4362d8e"
					]
				}
			},
			"response": []
		},
		{
			"name": " Update project details.",
			"request": {
				"method": "PATCH",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzgxMzY1LCJpYXQiOjE3MTkzNzk1NjUsImp0aSI6IjdiMWRmY2FiOTA0YTQ1ODVhYjY2M2Q2ZmU0ZmE4ZjkyIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.PBfdgokRMo9cFjqywY0_Vk10QXIoboQPxvSGGweAQ-s",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"name\": \"The univerversal project\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/projects/9ffaaed7-3a69-4750-ac7e-48f1a4362d8e/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"projects",
						"9ffaaed7-3a69-4750-ac7e-48f1a4362d8e",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": " Delete a project.",
			"request": {
				"method": "DELETE",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5MzgxMzY1LCJpYXQiOjE3MTkzNzk1NjUsImp0aSI6IjdiMWRmY2FiOTA0YTQ1ODVhYjY2M2Q2ZmU0ZmE4ZjkyIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.PBfdgokRMo9cFjqywY0_Vk10QXIoboQPxvSGGweAQ-s",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/projects/9ffaaed7-3a69-4750-ac7e-48f1a4362d8e/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"projects",
						"9ffaaed7-3a69-4750-ac7e-48f1a4362d8e",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Create a new task in a project",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5Mzk4MjgxLCJpYXQiOjE3MTkzOTY0ODEsImp0aSI6IjJkMzkzODk2NTYyODQzODFiMGI3OTkwY2I2OGJhZGZkIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.dIMCRGnIL0X8XBSi03M3D4Rj2J9Db0MCbTF49BNv0CQ",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"title\": \"New Task\",\r\n    \"description\": \"This is a new task description.\",\r\n    \"status\": \"To Do\",\r\n    \"priority\": \"High\",\r\n    \"assigned_to\": \"f9b5b4de-a9e1-4eb4-9e34-e543bd2eb7c1\",\r\n    \"project\": \"486eb5a2-f109-4e64-a4ae-5803fecde9b0\",\r\n    \"due_date\": \"2024-12-31T23:59:59Z\"\r\n}\r\n",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/projects/486eb5a2-f109-4e64-a4ae-5803fecde9b0/tasks/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"projects",
						"486eb5a2-f109-4e64-a4ae-5803fecde9b0",
						"tasks",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Retrieve a list of all tasks in a project.",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5Mzk4MjgxLCJpYXQiOjE3MTkzOTY0ODEsImp0aSI6IjJkMzkzODk2NTYyODQzODFiMGI3OTkwY2I2OGJhZGZkIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.dIMCRGnIL0X8XBSi03M3D4Rj2J9Db0MCbTF49BNv0CQ",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/projects/486eb5a2-f109-4e64-a4ae-5803fecde9b0/tasks/?",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"projects",
						"486eb5a2-f109-4e64-a4ae-5803fecde9b0",
						"tasks",
						""
					],
					"query": [
						{
							"key": "",
							"value": null
						}
					]
				}
			},
			"response": []
		},
		{
			"name": ": Retrieve details of a specific task.",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5Mzk4MjgxLCJpYXQiOjE3MTkzOTY0ODEsImp0aSI6IjJkMzkzODk2NTYyODQzODFiMGI3OTkwY2I2OGJhZGZkIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.dIMCRGnIL0X8XBSi03M3D4Rj2J9Db0MCbTF49BNv0CQ",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/tasks/531200a0-5c6b-40f5-9470-767767a4e575",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"tasks",
						"531200a0-5c6b-40f5-9470-767767a4e575"
					]
				}
			},
			"response": []
		},
		{
			"name": "Update task details.",
			"request": {
				"method": "PATCH",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5Mzk4MjgxLCJpYXQiOjE3MTkzOTY0ODEsImp0aSI6IjJkMzkzODk2NTYyODQzODFiMGI3OTkwY2I2OGJhZGZkIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.dIMCRGnIL0X8XBSi03M3D4Rj2J9Db0MCbTF49BNv0CQ",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"title\":\"titlle name changed\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/tasks/531200a0-5c6b-40f5-9470-767767a4e575/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"tasks",
						"531200a0-5c6b-40f5-9470-767767a4e575",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Delete a task",
			"request": {
				"method": "DELETE",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5Mzk4MjgxLCJpYXQiOjE3MTkzOTY0ODEsImp0aSI6IjJkMzkzODk2NTYyODQzODFiMGI3OTkwY2I2OGJhZGZkIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.dIMCRGnIL0X8XBSi03M3D4Rj2J9Db0MCbTF49BNv0CQ",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/tasks/531200a0-5c6b-40f5-9470-767767a4e575/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"tasks",
						"531200a0-5c6b-40f5-9470-767767a4e575",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Create a new comment on a task.",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5Mzk4MjgxLCJpYXQiOjE3MTkzOTY0ODEsImp0aSI6IjJkMzkzODk2NTYyODQzODFiMGI3OTkwY2I2OGJhZGZkIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.dIMCRGnIL0X8XBSi03M3D4Rj2J9Db0MCbTF49BNv0CQ",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"content\": \"This is content field\",\r\n    \"user\": \"f9b5b4de-a9e1-4eb4-9e34-e543bd2eb7c1\",\r\n    \"task\":\"531200a0-5c6b-40f5-9470-767767a4e575\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/tasks/531200a0-5c6b-40f5-9470-767767a4e575/comments/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"tasks",
						"531200a0-5c6b-40f5-9470-767767a4e575",
						"comments",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Retrieve a list of all comments on a task.",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5Mzk4MjgxLCJpYXQiOjE3MTkzOTY0ODEsImp0aSI6IjJkMzkzODk2NTYyODQzODFiMGI3OTkwY2I2OGJhZGZkIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.dIMCRGnIL0X8XBSi03M3D4Rj2J9Db0MCbTF49BNv0CQ",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/tasks/531200a0-5c6b-40f5-9470-767767a4e575/comments/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"tasks",
						"531200a0-5c6b-40f5-9470-767767a4e575",
						"comments",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Retrieve details of a specific comment.",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5Mzk4MjgxLCJpYXQiOjE3MTkzOTY0ODEsImp0aSI6IjJkMzkzODk2NTYyODQzODFiMGI3OTkwY2I2OGJhZGZkIiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.dIMCRGnIL0X8XBSi03M3D4Rj2J9Db0MCbTF49BNv0CQ",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/comments/f3cf15fa-4e1b-4b25-b61f-4dbc210c7195/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"comments",
						"f3cf15fa-4e1b-4b25-b61f-4dbc210c7195",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Update comment details.",
			"request": {
				"method": "PATCH",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NDAwMTc0LCJpYXQiOjE3MTkzOTgzNzQsImp0aSI6ImJhMDVhZjQ4MTk3ZjQ4NGI4Y2FhMjdkOGRiYTUwMmM5IiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.g09YQ_ZykF0FYqryYzVUnq6Tj8TzzDm4Z9aRAb_PdxU",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"content\": \"The content Field has changed\"\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/comments/f3cf15fa-4e1b-4b25-b61f-4dbc210c7195/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"comments",
						"f3cf15fa-4e1b-4b25-b61f-4dbc210c7195",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Delete a comment",
			"request": {
				"method": "DELETE",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE5NDAwMTc0LCJpYXQiOjE3MTkzOTgzNzQsImp0aSI6ImJhMDVhZjQ4MTk3ZjQ4NGI4Y2FhMjdkOGRiYTUwMmM5IiwidXNlcl9pZCI6ImY5YjViNGRlLWE5ZTEtNGViNC05ZTM0LWU1NDNiZDJlYjdjMSJ9.g09YQ_ZykF0FYqryYzVUnq6Tj8TzzDm4Z9aRAb_PdxU",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/comments/f3cf15fa-4e1b-4b25-b61f-4dbc210c7195/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"comments",
						"f3cf15fa-4e1b-4b25-b61f-4dbc210c7195",
						""
					]
				}
			},
			"response": []
		}
	]
}

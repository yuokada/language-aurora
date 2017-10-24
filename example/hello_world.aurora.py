import os
hello_world_process = Process(name = 'hello_world', cmdline = 'echo hello world')

hello_world_task = Task(
  resources = Resources(cpu = 0.1, ram = 16 * MB, disk = 16 * MB),
  processes = [hello_world_process])

hello_world_job = Job(
  cluster = 'cluster1',
  role = os.getenv('USER'),
  task = hello_world_task)

jobs = [hello_world_job]

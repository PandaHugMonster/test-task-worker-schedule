# Test Task Worker Schedule (test-task-worker-schedule)
 * Minimal code implementation (prototype) took from 2 to 3 hours in a relax-paced mode 
   with occasional coffee-breaks
 * The polishing and improving/documenting/bug-fixing/tests were done within 3 - 4 hours in total in the same
   relax-paced mode
 * In total the task was completed within ~6 hours
 * The code was written from scratch
 * Unfinished todo `app/time_management/serializers/ShiftSerializer.py:28`: Fix non-strict 2-days shift

## Quick start

 1. Getting code with `git clone https://github.com/PandaHugMonster/test-task-worker-schedule.git`
 2. To start docker-compose services run in the git-root folder 
    this command `docker-compose up -d` (docker and docker-compose software must be installed).
 3. Then to install basic data (1 worker + 4 shifts for one week) run the following command
    `docker exec -ti test-task-worker-schedule_app_1 bash /app/shell/defaults.sh`
 4. At this point you can use curl or any other tool to do REST API requests.


### Tests
 * To run tests please run 
   the following command `docker exec -ti test-task-worker-schedule_app_1 /app/manage.py test`

## Some settings
The basic used settings you can find in the end of `/app/schedule/settings.py` file.

Example:
```python

TIME_MANAGEMENT_APP = {
    # IMP   Strict time slots limit "target td" time to only 0-8, 8-16, 16-24
    #       And in this case 00:00, 08:00 and 16:00 accordingly
    'STRICT_TIME_SLOTS': True,

    # IMP   If set to True, will limit to maximum shifts per week to the value
    #       specified for each Worker (max_shifts_per_week property of class Worker)
    'LIMIT_WEEKLY_SHIFTS': True,
}

```

## Some REST API request commands

### Create
```shell
curl -H 'Accept: application/json; indent=4' -u root:root \
	http://localhost:8005/workers/ \
	-X POST \
	-d 'name=JJane Doe&birthdate=1020-01-01'
```


### Partial Update
```shell
curl -H 'Accept: application/json; indent=4' -u root:root \
	http://localhost:8005/workers/3/ \
	-X PATCH \
	-d 'name=Jane Doe&birthdate=2021-01-01'
```


### View
```shell
curl -H 'Accept: application/json; indent=4' -u root:root \
	http://localhost:8005/workers/3/ \
	-X GET
```

Bash code examples could be found in `/app/bash/defaults.sh`;


## Default credentials and security
**Important:** This application/code is a simple test-task/example-task. 
Please be careful using it for production without revision of code. The code is purely 
for demonstrative (and maybe snippets) purposes.

**Important:** Please make sure you do not expose any of the secret keys (Like it's done for this test task) 
and using proper security practices (with strong passwords).

----

Default credentials for development purposes only!:

 * Auth user: root
 * Auth pass: root


#!/usr/bin/python

import requests
import config

# response = requests.request("GET", url, headers=headers)
runner_info: list = []

# Get runners from Gitlab project
def get_runners(url, headers, project_id):

    response = requests.get('{}/api/v4/projects/{}/runners/'.format(url,project_id), headers=headers)
    data: dict = response.json()
    for i in data:
        runner_info.append((i['id'], i['description'], i['ip_address']))


# Get every active running job on Gitlab project
def check_runner_jobs(url, headers):

    for sublist in runner_info:
        response = requests.get('{}/api/v4/runners/{}/jobs?status=running'.format(url, sublist[0]), headers=headers)
        runner_job_info: list = response.json()
        if runner_job_info:
            print("{}(id={}) {}:\n".format(sublist[1],sublist[0],sublist[2]))
            for i in runner_job_info:
                print("Job: "+i['name'])
            print("-------------------------------------------------------")
    if not runner_job_info:
        print("There are no jobs at the moment")

# run
get_runners(config.url, config.headers, 9)
check_runner_jobs(config.url, runner_info, config.headers)

# I did not get any good looking output.. just got lazy. But i did something though!

import requests, datetime

from tasks.models        import Task, Department, Institute, Type, TrialStage, Scope
from humanscape.settings import OPEN_API_SERVICE_KEY

OPEN_API_URL         = 'http://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887'
OPEN_API_SERVICE_KEY = OPEN_API_SERVICE_KEY

def get_total_count():
    params = {'serviceKey' : OPEN_API_SERVICE_KEY}
    response = requests.get(OPEN_API_URL, params=params).json()
    return response['totalCount']

def daily_batch_task():
    params = {
    'page'       : 1,
    'perPage'    : get_total_count(),
    'serviceKey' : OPEN_API_SERVICE_KEY
    }
    response = requests.get(OPEN_API_URL, params=params).json()
    
    print(datetime.datetime.now(), response) #TODO:
    for task in response['data']:
        department, created  = Department.objects.get_or_create(name=task['진료과']) if task['진료과'] else (None, False)
        institute, created   = Institute.objects.get_or_create(name=task['연구책임기관']) if task['연구책임기관'] else (None, False)
        type, created        = Type.objects.get_or_create(name=task['연구종류']) if task['연구종류'] else (None, False)
        trial_stage, created = TrialStage.objects.get_or_create(name=task['임상시험단계(연구모형)']) if task['임상시험단계(연구모형)'] else (None, False)
        scope, created       = Scope.objects.get_or_create(name=task['연구범위']) if task['연구범위'] else (None, False)

        if Task.objects.filter(number=task['과제번호']).exists():
            Task.objects.filter(number=task['과제번호']).update(
                number           = task['과제번호'],
                title            = task['과제명'],
                duration         = task['연구기간'],
                number_of_target = task['전체목표연구대상자수'],
                department       = department,
                institute        = institute,
                type             = type,
                trial_stage      = trial_stage,
                scope            = scope
            )
        else:
            Task.objects.create(
                number           = task['과제번호'],
                title            = task['과제명'],
                duration         = task['연구기간'],
                number_of_target = task['전체목표연구대상자수'],
                department       = department,
                institute        = institute,
                type             = type,
                trial_stage      = trial_stage,
                scope            = scope
            )
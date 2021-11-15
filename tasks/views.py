from datetime     import datetime, timedelta

from json.decoder import JSONDecodeError

from django.db.models       import Q
from django.views           import View 
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from .models          import *

class SearchView(View):
    def get(self, request):
        try:
            offset = request.GET.get('offset', 0)
            limit  = request.GET.get('limit', 30)

            title       = request.GET.get('title', None)
            department  = request.GET.get('department', None)
            institute   = request.GET.get('institute', None)
            type        = request.GET.get('type', None)
            trial_stage = request.GET.get('trial_stage', None)
            scope       = request.GET.get('scope', None)

            q = Q()

            if title:
                q.add(Q(title__icontains=title), q.AND)
            
            if department:
                q.add(Q(department__name__iexact=department), q.AND)
            
            if institute:
                q.add(Q(institute__name__contains=institute), q.AND)
            
            if type:
                q.add(Q(type__name=type), q.AND)
            
            if trial_stage:
                q.add(Q(trialstage__name__iexact=trial_stage), q.AND)
            
            if scope:
                q.add(Q(scope__name=scope), q.AND)

            tasks = Task.objects.filter(q)\
                                .select_related('department', 'institute', 'type', 'trial_stage', 'scope')\
                                .order_by('updated_at')[offset:offset+limit]

            result = {
                'count' : len(tasks),
                'data'  : [{
                    'number'           : task.number,
                    'title'            : task.title,
                    'department'       : task.department.name,
                    'institute'        : task.institute.name,
                    'number_of_target' : task.number_of_target,
                    'duration'         : task.duration,
                    'type'             : task.type.name,
                    'trial_stage'      : task.trial_stage.name,
                    'scope'            : task.scope.name
                } for task in tasks]
            }
            
            return JsonResponse(result, status=200)
        
        except TypeError:
            return JsonResponse({'messsage' : 'TYPE_ERROR'}, status=400)
        
class TaskDetailView(View):
    def get(self, request, task_id):
        try:
            task = Task.objects.select_related(
                'type',
                'institute', 
                'department', 
                'trial_stage',
                'scope'
                ).get(id=task_id)
            
            task_info = {
                "number"           : task.number,
                "title"            : task.title,
                "duration"         : task.duration,
                "scope"            : task.scope.name,
                "type"             : task.type.name,
                "institute"        : task.institute.name,
                "trial_stages"     : task.trial_stage.name,
                "number_of_target" : task.number_of_target,
                "department"       : task.department.name,
                "created_at"       : task.created_at,
                "updated_at"       : task.updated_at
            }

            return JsonResponse({'message' : 'SUCCESS', 'task_info' : task_info}, status = 200)
        
        except Task.DoesNotExist:
            return JsonResponse({'message' : 'TASK_DOES_NOT_EXIST'}, status = 400)

class TaskList(View):
  def get(self, request):
    try:
      offset = int(request.GET.get('offset', 0))
      limit  = int(request.GET.get('limit', 10))
      now    = datetime.now()

      one_week_list = Task.objects.select_related(
        'trial_stage', 
        'department', 
        'institute', 
        'scope',
        'type'
        ).filter(updated_at__range=[now - timedelta(days=7), now])[offset:offset+limit]
      
      data = [{
        'title' : value.title,
        'number' : value.number,
        'duration' : value.duration,
        'number_of_target' : value.number_of_target,
        'trial_stage' : value.trial_stage.name,
        'department' : value.department.name,
        'institute' : value.institute.name,
        'scope' : value.scope.name,
        'type' : value.type.name
      } for value in one_week_list]

      return JsonResponse({'data' : data }, status=201)

    except KeyError :
      return JsonResponse({'message' : 'KEY_ERROR'}, status=400)

    except JSONDecodeError:
      return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status = 400)
      
    except ValidationError as e:
      return JsonResponse({'message' : (e.message)}, status = 400)

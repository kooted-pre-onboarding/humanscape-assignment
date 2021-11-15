from django.test  import TestCase, Client

from tasks.models import *

class TasksTest(TestCase):
    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_search_test(self):
        client = Client()
        response = client.get("/tasks/search?title=한국인&department=cardiology")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 
        {
            "count": 2,
            "data": [
                {
                "number": "C130012",
                "title": "한국인 유전성(가족성) 부정맥 질환 임상연구 네트워크 구축",
                "department": "Cardiology",
                "institute": "고려대안암병원",
                "number_of_target": "250",
                "duration": "8년",
                "type": "관찰연구",
                "trial_stage": "코호트",
                "scope": "국내다기관"
                },
                {
                "number": "C130002",
                "title": "한국인 유전성(가족성) 심근병증 유전자 발굴을 위한 임상자료 및 유전체자원 수집",
                "department": "Cardiology",
                "institute": "세브란스병원",
                "number_of_target": "250",
                "duration": "7개월",
                "type": "관찰연구",
                "trial_stage": "코호트",
                "scope": "국내다기관"
                }
            ]
            })
        
        # 알맞지 않은 값을 보낸 경우 400을 리턴합니다.
        response = client.get("/tasks/search?limit=xxx")
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(), {'messsage' : 'TYPE_ERROR'})
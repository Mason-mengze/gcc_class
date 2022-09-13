
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse


allow_url = ["/login", "/"]
class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path_info in allow_url:
            return
            
        info_dict = request.session.get("info")
        if info_dict:
            if info_dict['studentid'] and info_dict['name']:
                return
            return JsonResponse({"message":"数据异常请重新登录"})
            
        return JsonResponse({"message":"无权访问"}, json_dumps_params={'ensure_ascii': False})
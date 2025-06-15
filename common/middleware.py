# common/middleware.py
import datetime
import re

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ignored_paths = [
            '/request-info/',
        ]
        # Chrome DevTools 자동 요청 패턴 필터
        if (
            request.path not in ignored_paths
            and not re.match(r'^/\.well-known/appspecific/', request.path)
        ):
            log = request.session.get('request_log', [])
            log.append({
                'method': request.method,
                'path': request.path,
                'get': dict(request.GET),
                'post': dict(request.POST),
                'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'user': request.user.username if request.user.is_authenticated else '익명',
            })
            request.session['request_log'] = log[-100:]
            request.session.modified = True

        return self.get_response(request)

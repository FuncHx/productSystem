from rest_framework.pagination import PageNumberPagination

class PaginationUtil(PageNumberPagination):
    page_size = 10  # 默认每页显示数量
    page_size_query_param = 'page_size'  # 允许通过请求参数控制每页显示数量
    max_page_size = 50  # 每页显示数量的最大值

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)
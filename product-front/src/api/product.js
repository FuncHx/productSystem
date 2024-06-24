import request from '@/utils/request'

export function getProduct(page, searchForm) {
    return request({
        url: `/product/search/?pageSize=${page.pageSize}&currentPage=${page.currentPage}`,
        method: 'post',
        data: searchForm
    })
}


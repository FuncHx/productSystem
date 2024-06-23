import request from '@/utils/request'

export function updateUserInfo(form) {
    return request({
        method: "put",
        data: form,
        url: "/updateUserInfo/"
    })
}

export function editPassword(form) {
    return request({
        method: "post",
        data: form,
        url: "/editPassword/"
    })
}

export function editAvatar(imgUrl) {
    return request({
        method: "post",
        data: {
            avatar: imgUrl
        },
        url: "/adminUser/editAvatar/"
    })
}
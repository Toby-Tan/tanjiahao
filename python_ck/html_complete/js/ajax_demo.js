$(function () {
    // 获取密码
    var user = $('#username').val()
    var pwd = $('#password').val()
    // 相关加密处理
    //发送ajax请求  方式一
    // $.ajax({
    //     method: "POST",
    //     url: '/login',
    //     data: {
    //         "user": user,
    //         "pwd": pwd,
    //     },
    //     dataType: 'json',
    //     // 请求成功回调
    //     success: function (data) {
    //         if (data.code === '1') {
    //             alert(data.msg);
    //         } else {
    //             alert(data.msg)
    //         }
    //     },
    //     // 请求失败回调
    //     error:function (data){
    //         alert('服务开小差了')
    //     },
    // })
    // 方式二
    $.ajax({
        method: "POST",
        url: '/login',
        data: {
            "user": user,
            "pwd": pwd,
        },
        dataType: 'json',
    }).done(function (data) {
        if (data.code === '1') {
            alert(data.msg);
        } else {
            alert(data.msg)
        }
    }).fail(function () {
        alert('服务开小差了')
    })

    // 获取项目列表，添加到页面
    var pro = $('#pro');
    $.ajax({
        url: '/pro_list',
        method: 'GET',
        dataType: 'json',
    }).done(function (data) {
        var res = data.data;
        for (i in res) {
            var option = '<option value=' + res[i].id + '>' + res[i].title + '</option>'
            pro.append(option)
        }
    })

    // change事件：检测元素是否发生变化
    pro.change(function () {
        var pro_id = pro.val()
        $.ajax({
            url: '/interface',
            method: 'POST',
            dataType: 'json',
            data: {"pro_id": pro_id}
        }).done(function (data) {
            var inter = $('#interface');
            if (data.code === '1') {
                // 状态码为’1‘时调用回调函数，清空之前联动的值
                inter.empty()
                var res = data.data;
                //循环插入option
                for (var i = 0; i < res.length; i++) {
                    var option = '<option value="">' + res[i].name + '</option>>'
                    inter.append(option)
                }
            }
        })

    })


})

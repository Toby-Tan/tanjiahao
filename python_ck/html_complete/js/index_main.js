// js语法
// alert('hello')
// var name;
// name = "tanjiahao";
// console.log(name);

// var a = 10;
// if else 语句
// function test(a){
//     console.log('tanjiahao')
//     if(a>0){
//         console.log('输入的值>0');
//     }else if(a===0){
//         console.log('输入的值=0');
//     }else {
//         console.log('输入的值<0');
//     }
//     return a
// }

// var b=10;
// var c=15;
//

// switch 语句
// function test1(b,c){
//     switch (c-b){
//         case 4:
//             console.log('错误');
//             break;
//         case 55:
//             console.log('正确 ')
//             break;
//         default:
//             console.log('默认执行')
//     }
//     return b
// }
//
// test1(b,c)

// for()循环
// for (var i = 1; i < 11; i++) {
//     console.log(i)
// }

// for in 循环
// var li = Array(11,22,33,44)
//
// for (i in li){
//     console.log(li[i])
// }

// while ()循环
// var a = 1
// while (a<11){
//     console.log(a);
//     a++;
// }
$(function () {
    // 弹出/关闭添加项目弹窗
    $('#proAdd').click(function () {
        $('.pro_back').show();
    });
    $('.pro_alert_quit').click(function () {
        $('.pro_back').hide();
    });
    $('.tj').click(function () {
        $('.pro_back').hide();
    });
    // 展开侧边栏 方式一
    // $('.left_menu_list h3').click(function (){
    //     $(this).next().toggle()
    //         .parent().siblings().children('ul').hide()
    // });
    // 展开侧边栏 方式二
    $('.left_menu_list h3').click(function () {
        $(this).next().slideToggle(10)
            .parent().siblings().children('ul').slideUp();
    });

})

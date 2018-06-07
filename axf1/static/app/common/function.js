

function addCart(goods_id){
    // $.get('/app1/addCart/?goods_id=' + goods_id, function (msg) {
    //     alert(msg)
    //     if(msg.code == 200) {
    //         $('#num_' + goods_id).text(msg.c_num)
    //     }else{
    //         alert(msg)
    //     }
    // })
    var csrf=$('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app1/addCart/',
        type: 'POST',
        data: {'goods_id': goods_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if(msg.code == 200){
                $('#num_' + goods_id).text(msg.c_num)
                count_all()
            }else{
                alert(msg)
            }
        },
        error: function (msg) {
            alert('1')
        }
    })
}


function subCart(goods_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app1/subCart/',
        type: 'POST',
        data: {'goods_id': goods_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if(msg.code == '200'){
                 $('#num_' + goods_id).text(msg.c_num)
                 count_all()
            }else{
                alert(data.msg)
            }
            if(msg.c_num == 0){
                $('#myCart').parent.remove()
            }
        },
        error: function (msg) {
            alert('请求失败')
        }

    })
}

function changeSelectStatus(cart_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app1/changeSelectStatus/',
        type: 'POST',
        data: {'cart_id': cart_id},
        dataType: 'json',
        headers:{'X-CSRFToken': csrf},
        success: function (data) {
            if(data.code == 200){
                if(data.is_select){
                    $('#cart_id_' + cart_id).html('√')
                    count_all()
                }else{
                    $('#cart_id_' + cart_id).html('×')
                    count_all()
                }
            }
        },
        error: function (data) {
            alert('请求失败')
        }

    })
}

function checkAll(cart_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: 'app1/changeSelectStatus/',
        type: 'POST',
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        data: {'cart_id': cart_id},
        success: function (msg) {
            alert('请求成功')
            if(data.is_select){
                $('#cart_id_' + cart_id).html('√')
            }

        },
        error: function (msg) {
            alert('请求失败')
        }
    })
}

function change_order(order_id){
    var csrf = $('input[name="csrfmiddlewaretoken"]').val()
    $.ajax({
        url: '/app1/changeOrderStatus/',
        type: 'POST',
        data: {'order_id': order_id},
        dataType: 'json',
        headers: {'X-CSRFToken': csrf},
        success: function (msg) {
            if(msg.code == 200){
                location.href = '/app1/mine/'
            }
        },
        error: function (msg) {
            alert('请求失败')
        }

    })
}

count_all()
function count_all(){
    $.ajax({
        url: '/app1/allPrice/',
        type: 'GET',
        dataType: 'json',
        success: function (msg) {
            $('#allPrice').html('总价: '+ msg.t_price)
        },
        error: function (msg) {
            alert('请求失败')
        }
    })
}

// $.get('/app1/allPrice/', function (data) {
//     if(data.code == '200'){
//         $('#allPrice').html('总价: ' + data.t_price)
//     }
// })
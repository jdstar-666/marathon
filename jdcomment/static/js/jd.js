/**
* @Author: lisnb
* @Date:   2016-07-28T00:03:04+08:00
* @Email:  lisnb.h@hotmail.com
* @Last modified by:   lisnb
* @Last modified time: 2016-07-28T04:25:53+08:00
*/

$(document).ready(function(){
  var user = null;//{'user_name': '张龙', 'user_id':'1000001' }
  //sessionStorage.setItem('user', JSON.stringify(user))
  var orders = null
  function init_profile(){
    $('#username').text(user.user_name);
  }
  var ordertemplate = $.templates('#order-template');
  console.log(ordertemplate)
  var item_in_order_template = $.templates('#item-in-order-template');
  function init_orders(){
    var user_id = user.user_id;
    var url = '/jdorder/orders/';
    var params = {
      'user_id': user_id
    }
    $.get(url, params, function(data){
      // console.log(data);

      var response = JSON.parse(data);
      console.log(response);
      var orders = []
      for (var i = 0; i < response.orders.length; i++) {
        response.orders[i]['order_items'] = item_in_order_template.render(response.orders[i]['items'])
      }
      console.log(response.orders)
      var orders_html = ordertemplate.render(response.orders)
      console.log(orders_html)
      $('#main').html(orders_html)

    })
  }

  function init_user(){
    init_profile()
    init_orders()
  }

  (function(){
    var s_original_user = sessionStorage.getItem('user');
    if (s_original_user){
      user = JSON.parse(s_original_user);
      init_user();
    }
  })()

  // $('.comment-order').click(function())

  $('#login-button').click(function(){
    var original_user = sessionStorage.getItem('user')
    if(original_user){
      alert('已经登录！')
      return ;
    }
    // console.log('login')
    user_name = $('#user_name').val()
    user_passwd = $('#user_passwd').val()
    if(!user_name){
      alert('请输入用户名！');
    }
    if(!user_passwd){
      alert('请输入密码！');
    }
    params = {
      'user_name': user_name,
      'user_passwd': user_passwd
    }
    url = '/jduser/login/'
    $.post(url, params, function(data){
      console.log(data);
      response = JSON.parse(data);
      console.log(response);
      console.log(response.msg);
      if(response.code < 0){
        alert(response.msg);
      }else{
        $('#close-login-modal').click()
        user = response.user;
        sessionStorage.setItem('user', JSON.stringify(user))
        init_user()
      }
    })
  })
})

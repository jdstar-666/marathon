/**
* @Author: lisnb
* @Date:   2016-07-28T09:59:02+08:00
* @Email:  lisnb.h@hotmail.com
* @Last modified by:   lisnb
* @Last modified time: 2016-07-28T11:42:45+08:00
*/

$(document).ready(function(){
  var user = null;//{'user_name': '张龙', 'user_id':'1000001' }
  //sessionStorage.setItem('user', JSON.stringify(user))
  function init_profile(){
    $('#username').text(user.user_name);
  }
  (function(){
    var s_original_user = sessionStorage.getItem('user');
    if (s_original_user){
      user = JSON.parse(s_original_user);
      init_profile();
    }
  })()



  var hash = location.hash;
  var item_id = hash.split('=')[1]
  $.get('/jditem/detail/', {'item_id': item_id}, function(data){
    var response = JSON.parse(data)
    var detail_html = $('#detail-template').render(response.item)
    $('#detail-wrapper').html(detail_html)
    $('#detail-picture').animate({'margin-top':'0',opacity:1.0},1500);
    $.get('/jditem/comments/', {'item_id': item_id}, function(inner_data){

      var picture_template = $.templates('#picture-template')
      var inner_response = JSON.parse(inner_data);
      console.log(inner_response)
      for (var i = 0; i < inner_response.comments.length; i++) {
        var pics = inner_response.comments[i].evaluation_pic.split(';')
        var pics_d = []
        for (var j=0; j< pics.length; j++){
          if(pics[j])
            pics_d.push({'pic_path': pics[j]})
        }
        console.log(pics_d)
        inner_response.comments[i]['pictures'] = picture_template.render(pics_d)

      }
      var comments_html = $('#comment-template').render(inner_response.comments)
      console.log(comments_html)
      $('#comment-wrapper').html(comments_html)
      $('.rating').rating({
        defaultCaption: '{rating} 分',
        readonly: true
      })
    })

  })
})

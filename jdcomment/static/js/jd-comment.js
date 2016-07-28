/**
* @Author: lisnb
* @Date:   2016-07-28T04:30:28+08:00
* @Email:  lisnb.h@hotmail.com
* @Last modified by:   lisnb
* @Last modified time: 2016-07-28T13:21:34+08:00
*/


$(document).ready(function(){

  var user = JSON.parse(sessionStorage.getItem('user'))
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
  var hash = location.hash
  var order_id = hash.split('=')[1]
  var pictures = {}
  var itemids = []
  function get_order(){
    var url = '/jdorder/order/'
    var params = {
      'order_id': order_id
    }
    $.get(url, params, function(data){
      // console.log(data);
      var response = JSON.parse(data)
      var items = response.items;

      for (var i = 0; i < items.length; i++) {
        itemids.push(items[i].item_id)
      }
      var items_html = $('#item-template').render(items);
      $('#items-panel').html(items_html);
      $('.rating-loading').rating(
        {
          'languate':'zh',
          'step':1,
          'starCaptions': {1: '1分', 2: '2分', 3: '3分', 4: '4分', 5: '5分'},
          'clearCaption': '0分'
        }
      )
      for (var i = 0; i < itemids.length; i++) {
        var itemid = itemids[i];
        console.log(itemid);
        new AjaxUpload($('#i-'+itemid.toString()+'-pic'), {
          // data: {'item_id': $(this)[0]._button.id},
          // data: {
          //   'item_id': itemid
          // },
          action: '/comment/upload/',
          responseType: 'json',
          name: 'picture',
          onComplete: function(file, uploadResult){
            console.log(itemid)
            console.log(file)
            console.log(uploadResult)
            var aitemid = $(this)[0]._button.id
            if(!pictures.hasOwnProperty(aitemid)){
              pictures[aitemid] = []
            }
            pictures[aitemid].push(uploadResult.name)
            console.log(pictures)
            var thumb = '<span class="comment-image-thumb"><img src="/media/upload/'+uploadResult.name+'"></span>';
            $('#thumb-wall-'+aitemid).append(thumb);
          }
        })
      }


    })
  }
  get_order();
  console.log('bar')
  $(document).on('click', '.ajaxsubmitcomment', function(e){
    console.log('foo')
    var item_id = $(this).data('itemid');
    var user_id = user.user_id
    var content = $('#i-'+item_id.toString()+'-content').val();

    if(!content){
      alert('评论内容不能为空！')
      return ;
    }
    var index = $('#i-'+item_id.toString()+'-index').val();
    console.log(index)
    console.log(content)
    if(!index){
      alert('评分不能为空！')
      return ;
    }
    var params = {
      'item_id': item_id,
      'user_id': user_id,
      'comment': content,
      'score': index,
      'pictures': pictures['i-'+item_id+'-pic']
    }
    console.log(params)
    $.post('/comment/post/', params, function(data){
      console.log(data);
      var response = JSON.parse(data)
      if(response.code===0){
        $('#hint-'+item_id).show();
        // console.log($(this))
        // console.log($(this).find('.ajaxsubmitcomment'))
        // $('#')
        // console.log($(this))
        // $(this).attr('value', '评价成功')
        // console.log($(this).siblings())
        setTimeout(function(){
          window.close();
        }, 3000)
      }else{
        alert(response.msg);
      }
    })
  })

  // new AjaxUpload($('.ajaxpostcomment'), {
  //   data: $(this).data('itemid'),
  //   action: '/jdcomment/upload/',
  //   responseType: 'json',
  //   name: 'picture',
  //   onComplete: function(file, uploadResult){
  //     console.log(file);
  //     console.log(uploadResult)
  //   }
  // })

  /*
  $(document).on('submit', 'form', function(e){
    console.log('foo')
    e.preventDefault()
    // console.log(e)
    // console.log(this)
    // var item_id = $(this).data('itemid')
    // var formdata = new FormData($('#form-'+item_id.toString())[0]);
    var formdata = new FormData(this);
    console.log(formdata)
    $.ajax({
      url: '/comment/post/',
      method: 'POST',
      data: formdata,
      mimeTypes:"multipart/form-data",
      contentType: false,
      cache: false,
      processData: false,
      success: function(){
          alert("file successfully submitted");
      },error: function(){
          alert("okey");
      }
    })
  })*/

})

/* 
* @Author: lisnb
* @Date:   2015-01-20 18:47:22
* @Last Modified by:   LiSnB
* @Last Modified time: 2015-02-03 21:26:38
*/

$(document).ready(function(){
    'use strict';
    pageit(1);
    $('.ajaxpagination').click(function(e){
        e.preventDefault();
        $('.ajaxpagination').parent().removeClass('active');
        $(e.currentTarget).parent().addClass('active');
        var page = $(e.currentTarget).data('page');
        pageit(page);
        return false;
    });
    var aqsize = 0
    function pageit(page){
        $.get('./ajaxindex/',{'page':page},function(data){
            var jdata = JSON.parse(data);
            var html = $('#newstemplate').render(jdata['newslist']);
            $('#newsitemspanel').html(html);

            $('.addtoqueue').click(function(e){
                // console.log($(e.currentTarget));
                var button = $(e.currentTarget)
                var newsid = button.data('newsid');
                var title = button.data('title');
                var tnews = $('<div class="col-md-3 aqitem" data-newsid='+newsid+'><span class="label label-success"><span class="glyphicon glyphicon-remove-sign aqitemdel"></span> '+title+'</span></div>');
                $('#aq').append(tnews);
                tnews.click(function(e){
                    tnews.remove();
                    $('body').css({'padding-bottom':$('#aqnav').height()+20})
                })
                $('body').css({'padding-bottom':$('#aqnav').height()+20})
                return false;
            });
        })
    }

    $('#gotoanalysis').click(function(e){
        var news = $('#aq').children();
        var newsid = [];
        [].forEach.call(news,function(item){
            newsid.push($(item).data('newsid'));
        });
        window.open('/analysis/newslist/#'+newsid.join(','));
        return false;

    })

    $('#emptyaq').click(function(e){
        $('.aqitem').remove()
        $('body').css({'padding-bottom':70})
    })
    
})

/* 
* @Author: LiSnB
* @Date:   2016-01-15 11:00:13
* @Last Modified by:   LiSnB
* @Last Modified time: 2016-01-22 10:32:06
*/

'use strict';

$(document).ready(function(){
    var lastappitem = null;
    var currentappitem = null;
    var currentchannels = null;
    var cache = {}

    function setchannelcollect(cid, collect){
        if(!cid){
            $.bs_alert('Invalid cid')
            return false;
        }
        var query = {
            'collect':collect
        };
        $.post('./channels/'+cid+'/', query, function(data){
            if(!data){
                $.bs_alert('No data');
                return;
            }
            data = JSON.parse(data);
            if(data && data.code!==undefined){
                if(data.code===0){
                    $.bs_alert('Success!', 'Yes!', 'info');
                }else{
                    $.bs_alert(data.msg);
                }
            }else{
                $.bs_alert('Parse data failed or no code');
            }
        });
    }

    function channelitemchanged(e){
        // var collect = e.currentTarget.checked;
        var channel = $(e.currentTarget);
        var collect = $(channel).prop('checked');
        // console.log('collect', collect)

        var cid = channel.data('id');
        setchannelcollect(cid, collect);
    }

    function fetchchannelsbyapp(app, kw){
        if (!app){
            $.bs_alert('Invalide app');
            return
        }
        var query = {'app':app, 'kw':kw};
        $.get('./'+app+'/', function(data){
            if(!data){
                $.bs_alert('No data');
                return false;
            }
            var channels = JSON.parse(data);
            if(channels && channels.code!==undefined){
                if(channels.code!==0){
                    $.bs_alert(channels.msg);
                    return false;
                }
                channels = channels.channels;
                if(!channels){
                    $.bs_alert('No channels in this app', 'Warning!', 'warning');
                    $('#channellist').html('');
                    return false;
                }
                var channels_html = $('#channeltemplate').render(channels);
                $('#channellist').html(channels_html)
            }else{
                $.bs_alert('Parse data failed or no code');
            }
        })
    }

    function appitemclicked(e){
        e.preventDefault();
        currentappitem = $(e.currentTarget);
        var app = currentappitem.data('appename');
        fetchchannelsbyapp(app);
        currentappitem.parent().addClass('active');
        if(lastappitem!==null)
            lastappitem.parent().removeClass('active');
        lastappitem = currentappitem;
    }

    function fetchallapps(){
        $.get('/common/apps/', function(data){
            if(!data){
                $.bs_alert('No data');
                return false;
            }
            var apps = JSON.parse(data);
            if(apps && apps.code!==undefined){
                if(apps.code!==0){
                    $.bs_alert(apps.msg)
                    return false;
                }
                var apps_html = $('#apptemplate').render(apps.apps);
                $('#applist').html(apps_html);
            }else{
                $.bs_alert('Parse data failed or no code');
            }
        })
    }
    fetchallapps();
    $(document).on('click', '.appitem', appitemclicked);
    $(document).on('change', '[name="channels[]"]', channelitemchanged);
})

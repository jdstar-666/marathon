/*
* @Author: LiSnB
* @Date:   2016-01-21 15:33:21
* @Last Modified by:   LiSnB
* @Last Modified time: 2016-01-21 21:03:57
*/

'use strict';

$(document).ready(function(){
    $.bs_alert = function (body, title, type, fade){
        var message = {
            'title': title || 'Error!',
            'body': body || "Unknown error",
            'type': type || 'danger'
        };
        var alert_html = $('#alerttemplate').render(message);
        $('#bs-alert-panel').html(alert_html);
        var current_alert = $('#bs-alert-panel').children()[0];
        if (fade===undefined || fade!==false)
            $(current_alert).fadeOut(2000);
        // setTimeout(function(){
        //     $(current_alert).fadeOut();
        // }, 2000);
    }
})


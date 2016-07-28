/*
* @Author: LiSnB
* @Date:   2016-01-22 15:50:17
* @Last Modified by:   LiSnB
* @Last Modified time: 2016-01-22 19:14:12
*/

'use strict';

$(document).ready(function(){
    function setcaptcha(){
        $('#captcha').val(Math.random().toString(36).substr(2, 6));
    }
    setcaptcha();
    $('#refresh-captcha').click(setcaptcha);
    function deletecheckdup(e){
        e.preventDefault();
        var rcaptcha = $('#rcaptcha').val();
        var captcha = $('#captcha').val();
        if(rcaptcha!==captcha){
            $.bs_alert('字符串未输入正确，请确认，避免误操作', '错误！', 'danger', false);
            return false;
        }
        var time_nolimit = $('#time-nolimit').prop('checked');
        var time_before = $('#time-before').prop('checked');
        if((!time_nolimit)&&(!time_before)){
            $.bs_alert('至少应该提供一个时间选项', '错误！', 'danger', false);
            return false;
        }
        var query = {'nolimit': true, 'app': null};
        if(time_before){
            var before = $('#before').val();
            if(!before){
                $.bs_alert('无效的时间', '错误', 'danger', false);
                return false;
            }
            query['before'] = before;
            query['nolimit'] = false;
        }

        $.ajax({
            url: './dups/',
            type: 'POST',
            data: query,
            error:function(a, status, error){
                $.bs_alert(error, status, 'danger', false);
                return false;
            },
            success: function(data){
                if(data){
                    var response = JSON.parse(data);
                    if(!response){
                        $.bs_alert('解析返回数据错误', '错误！', 'danger', false);
                        return false;
                    }
                    if(response.code!==0){
                        $.bs_alert(response.msg, '错误！', 'danger', false);
                        return false;
                    }
                    $.bs_alert('删除成功,共删除记录'+response.count+'条，3秒后将跳转到“采集状态”页面... ', '成功', 'info', false);
                    setTimeout(function(){
                        window.location='/status/'
                    }, 3000);
                }else{
                    $.bs_alert('服务器返回的数据为空', '错误！', 'danger', false);
                    return false;
                }
            }
        });

    }
    $('#btn-delete-checkdup').click(deletecheckdup);
});
/* 
* @Author: LiSnB
* @Date:   2015-01-16 21:40:06
* @Last Modified by:   LiSnB
* @Last Modified time: 2015-01-17 16:45:37
*/

$(document).ready(function(){
    $('#query').focus()
    var lastquery='';
    var currentquery = '';
    function fetchnews(tquery){
        $.get('/search/searchahead/',{query:tquery},function(data){
            // console.log(data)
            var jdata = JSON.parse(data)
            var rdata = $('#sartemplate').render(jdata)
            // console.log(rdata)
            $('#searchahead-result').html(rdata)
        })
    }

    $('#query').keyup(function(event){
        var e = window.event || event
        var key = e.keyCode || e.which
        if ( key == 13 ) {
           $('$btn-search').click();
        }
        if (key == 32||key == 8||key == 0){
            currentquery = $('#query').val().trim()
            if ( currentquery!= lastquery && currentquery){
                lastquery = currentquery
                fetchnews(currentquery);    
            }
        }
    })
});
/* 
* @Author: LiSnB
* @Date:   2015-01-19 15:46:02
* @Last Modified by:   LiSnB
* @Last Modified time: 2015-01-22 15:26:57
*/

$(document).ready(function(){
    $('.toggleicon').click(function(e){
        $(e.currentTarget).children('span').toggle();
    })
    var newslist=window.location.hash.substr(1).trim()||'';
    // #TEC2015012001701403,TEC2015012001810103,TEC2015012001916600,TEC2015012001299301
    

    var province_distribution = false;
    var get_province_distribution_url = './provincedistribution/';
    $('#province-distribution').on('show.bs.collapse',function(){
        if(newslist===''){
            $('#province-distribution-map').text('没有新闻可以分析');
                return ;
        }
        if (province_distribution)
            return ;
        $.get(get_province_distribution_url,{'newslist':newslist},function(data){
            var jdata = JSON.parse(data);
            var error = jdata['error']||false;
            if(error){
                $('#province-distribution-map').text(jdata['message']||'未知错误');
                return ;
            }
            chart_province_distribution(jdata['newslist']);
            $("#province-distribution-panel").scrollTop(0);
        })
    })
    function chart_province_distribution(data){
        console.log('highmap')
        $('#province-distribution-map').highcharts('Map', {
            chart: {
                spacingBottom: 15,
                spacingTop: 10,
                spacingLeft: 10,
                spacingRight: 10,
                width: null,
                height: 650
            },
            credits:{
                enabled:false
                // href:'http://lixipeng.me'
            },
            title : {
                text : '评论数目按省份分布图'
            },
            subtitle : {
                text : '只统计有地址信息的评论'
            },
            mapNavigation: {
                enabled: true,
                buttonOptions: {
                    verticalAlign: 'bottom'
                }
            },
            colorAxis: {
                min: 0
            },
            series : [{
                data : data,
                mapData: Highcharts.maps['countries/cn/cn-all'],
                joinBy: 'hc-key',
                name: '评论数',
                states: {
                    hover: {
                        color: '#BADA55'
                    }
                },
                dataLabels: {
                    enabled: true,
                    format: '{point.name}'
                }
            }]
        });
        province_distribution = true;
    }

    var title_url = './titles/';
    var newsmeta = null;
    gettitles();
    function gettitles(){
        if(newslist===''){
            $('#titles').html('没有选择任何新闻,请到<a href="/newslist/" alt="新闻列表">这里</a>选择新闻以分析')
            return ;
        }
        $.get(title_url,{'newslist':newslist},function(data){
            newsmeta = JSON.parse(data);
            var error = newsmeta['error']||false;
            if(error){
                $('#titles').text(newsmeta['message']||'未知错误')
            }
            newsmeta = newsmeta['newsmeta'];
            var titlelist = $('#titlelist')
            // jdata['titles'].forEach(function(title){
            //     var tli = '<li>'+title+'</li>'
            //     titlelist.append(tli)
            // })
            for(var tn in newsmeta){
                var tli = '<li>'+newsmeta[tn]['title']+'</li>';
                titlelist.append(tli)
            }
        })
    }

    var commentrank=false;
    $('#commentrank').on('shown.bs.collapse',function(){
        if(commentrank)
            return ;
        if(!newsmeta){
            gettitles();
        }
        var titles = [];
        var ccnt = [];
        for(var tn in newsmeta){
            titles.push(newsmeta[tn]['title']);
            ccnt.push(newsmeta[tn]['commentcount']);
        }
        chart_commentrank(titles,ccnt);
    })

    function chart_commentrank(titles,ccnt){
        $('#commentrank-chart').highcharts({
            chart: {
                type: 'bar',
                // width:null,
            },
            title: {
                text: '新闻评论统计信息'
            },
            subtitle: {
                text: '只统计数据库中当前的信息'
            },
            xAxis: {
                categories: titles,
                title: {
                    text: null
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: '评论数 (条)',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                }
            },
            tooltip: {
                valueSuffix: ' 条'
            },
            plotOptions: {
                bar: {
                    dataLabels: {
                        enabled: true
                    }
                }
            },
            legend: {
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'top',
                // x: -40,
                // y: 100,
                floating: true,
                borderWidth: 1,
                backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
                shadow: true
            },
            credits: {
                enabled: false
            },
            series: [{
                name: '评论数目',
                data: ccnt
            }]
        });
        commentrank = true;
    }

    var commenttag=false;
    $('#comment-tag').on('shown.bs.collapse',function(){
        if(commenttag)
            return ;
        if(!newsmeta){
            gettitles()
        }
        chart_comment_tag();
    })

    function chart_comment_tag(){
        var tags = []
        for(var tn in newsmeta){
            newsmeta[tn]['tag'].forEach(function(tag){
                var t = '<div class="col-md-2  tagclouditem"><span class="label label-danger">'+tag+'</span></div>'
                tags.push(t)
            })
        }
        $('#comment-tag-cloud').html(tags.join(''));
        commenttag = true;
    }
});
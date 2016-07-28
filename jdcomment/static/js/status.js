/* 
* @Author: lisnb
* @Date:   2016-01-18 14:26:51
* @Last Modified by:   LiSnB
* @Last Modified time: 2016-01-27 16:02:15
*/

'use strict';

$(document).ready(function(){

    function chart_allapps(apps, newscnts){
        $('#chart-allapps').highcharts({
            chart: {
                type: 'bar',
            },
            // title: {
            //     text: '采集新闻数'
            // },
            // subtitle: {
            //     text: '只统计数据库中当前的信息'
            // },
            title: {
                text: '只统计数据库中当前的信息'
            },
            xAxis: {
                categories: apps,
                title: {
                    text: null
                }
            },
            yAxis: {
                min: 0,
                title: {
                    text: '新闻 (条)',
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
                name: '新闻数目',
                data: newscnts
            }]
        });
    }

    function index(){
        $.get('/status/all/', function(data){
            if(!data){
                $.bs_alert('No data');
                return;
            }
			data = JSON.parse(data);
            if(data && data.code!==undefined){
                if(data.code!==0){
                    $.bs_alert(data.msg);
                    return;
                }
                var apps = []
                var newscnts = []
                var counts = data['counts'];
                counts.forEach(function(app){
                    apps.push(app[1]);
                    newscnts.push(app[2]);
                });
                chart_allapps(apps, newscnts)
            }else{
                $.bs_alert('Parse data failed or no code.');
            }
        })
    }
    $('#refresh-counts').click(index);
    index();

    function fetchallapps(){
        $.get('/common/apps/', function(data){
            if(!data){
                $.bs_alert('No data');
                return;
            }
            data = JSON.parse(data);
            if(data && data.code!==undefined){
                if(data.code!==0){
                    $.bs_alert(data.msg );
                    return;
                }
                var apps = data.apps;
                if (!apps){
                    $.bs_alert('No apps');
                    return ;
                }
                var apps_html = $('#apptemplate').render(apps);
                $('#applist').html(apps_html);
            }else{
                $.bs_alert('Parse data failed or no code.');
            }
        })
    }
    fetchallapps();

    function fetchcollectorsstatus(){
        $('#collectors-loading').show();
        $.get('./collectors/', function(data){
            if(!data){
                $.bs_alert('No data');
                return;
            }
            data = JSON.parse(data);
            if(data && data.code!==undefined){
                if(data.code!==0){
                    if(data.code===1)
                        $.bs_alert(data.msg, 'Warning!', 'warning', false);
                    else
                        $.bs_alert(data.msg );
                    return;
                }
                // var tablehead = '<tr><th>采集器</th><th>进程ID</th><th>进程启动时间</th><th>运行时间</th><th>运行状态</th></tr>';
                var collectors_html = $('#collectortemplatetr').render(data['collectors']);
                // var tablehtml = tablehead + collectors_html;
                $('#collectortable').html(collectors_html)
                $('#collectors-loading').hide();
            }else{
                $.bs_alert('Parse data failed or no code.');
            }
        })
    }
    fetchcollectorsstatus();
    $('#refresh-status').click(fetchcollectorsstatus);
})

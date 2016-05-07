$(function(){
/*widgest 中卷起的js
    $('.panel-close').click(function(){
        $(this).parent().parent().parent().hide(300);
    });

    $('.collapse').on('hide.bs.collapse',function(){
        $(this).prev().find(".panel-collapse").removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
    });

    $('.collapse').on('show.bs.collapse',function(){
        $(this).prev().find(".panel-collapse").removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
    });
*/

});

/*提示的js
$(function () { $("[data-toggle='tooltip']").tooltip(); });
$('#nav-login').tooltip('hide');
*/

/*load included_monioring_count_year_chart_panel */
var myChart = echarts.init(document.getElementById('included_monitoring_count_chart_panel'));
var option = {
    title : [{
      text: '矫正对象纳入电子监控情况',
      //subtext: '12个月数据变化情况',
      textStyle: {
        fontSize: 14,
        fontWeight:"normal"
      }
    }],
    tooltip : {
        trigger: 'axis'
    },
    grid:[{
      top: 40,
      bottom: 30,
      left: "5%",
      right: "1%" 
    }],
    legend: {
        data:['预购','成交']
    },
    xAxis : [
        {
            type : 'category',
            boundaryGap : false,
            data : ['201505','201506','201507','201508','201509','201510','201511','201512','201601','201602','201603','201604']
        }
    ],
    yAxis : [
        {
            type : 'value',
        }
    ],
    series : [
      {
       name:'成交',
       type:'line',
       smooth:true,
       itemStyle: {normal: {areaStyle: {type: 'default'}}},
       data:[10, 12, 21, 54, 260, 830, 710]

      },
      {
       name:'预购',
       type:'line',
       smooth:true,
       itemStyle: {normal: {areaStyle: {type: 'default'}}},
       data:[30, 182, 434, 791, 390, 30, 10]

      }
    ] 

};
myChart.setOption(option);

option = myChart.getOption();


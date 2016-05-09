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

//option = myChart.getOption();


/* load included_monioring_count_area_chart_panel */
var included_monioring_count_area_chart = echarts.init(document.getElementById('included_monitoring_count_area_chart_panel'));
var included_monioring_count_area_chart_option = {
  title :[{
      text: '温度计式图表',
      //subtext: 'From ExcelHome',
      //sublink: 'http://e.weibo.com/1341556070/AizJXrAEa'
      textStyle: {
        fontSize: 14,
        fontWeight:"normal"
      }

  }],
  tooltip : {
      trigger: 'axis',
      axisPointer : {            // 坐标轴指示器，坐标轴触发有效
        type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
      },
      formatter: function (params){
        return params[0].name + '<br/>'
          + params[0].seriesName + ' : ' + params[0].value + '<br/>'
          + params[1].seriesName + ' : ' + (params[1].value + params[0].value);
      }
  },
  grid:[{
      top: 40,
      bottom: 30,
      left: "5%",
      right: "1%" 
  }],
  legend: {
      selectedMode:false,
      data:['Acutal', 'Forecast']
  },
  //toolbox: {
  //    show : true,
  //    feature : {
  //      mark : {show: true},
  //      dataView : {show: true, readOnly: false},
  //      restore : {show: true},
  //      saveAsImage : {show: true}
  //    }
  //},
  calculable : true,
  xAxis : [
    {
       type : 'category',
       data : ['Cosco','CMA','APL','OOCL','Wanhai','Zim']
    }
  ],
  yAxis : [
   {
      type : 'value',
      boundaryGap: [0, 0.1]
   }
  ],
  series : [
    {
      name:'Acutal',
      type:'bar',
      stack: 'sum',
      barCategoryGap: '50%',
      itemStyle: {
        normal: {
          color: 'tomato',
          barBorderColor: 'tomato',
          barBorderWidth: 6,
          barBorderRadius:0,
          label : {
            show: true, position: 'insideTop'
          }
       }
      },
      data:[260, 200, 220, 120, 100, 80]
    },
    {
      name:'Forecast',
      type:'bar',
      stack: 'sum',
      itemStyle: {
        normal: {
          color: '#fff',
          barBorderColor: 'tomato',
          barBorderWidth: 6,
          barBorderRadius:0,
          label : {
            show: true, 
            position: 'top',
            formatter: function (params) {
              for (var i = 0, l = option.xAxis[0].data.length; i < l; i++) {
                if (option.xAxis[0].data[i] == params.name) {
                   return option.series[0].data[i] + params.value;
                }
              }
            },
          textStyle: {
            color: 'tomato'
          }
        }
      }
   },
   data:[40, 80, 50, 80,80, 70]
   }
   ]
};
included_monioring_count_area_chart.setOption(included_monioring_count_area_chart_option);  



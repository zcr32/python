/**
 * Created by admin on 2023/5/13.
 */
  // 基于准备好的dom，初始化echarts实例
      var myChart1 = echarts.init(document.getElementById('main1'));
option1 = {
  xAxis: {
    type: 'category',
    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: [150, 230, 224, 218, 135, 147, 260],
      type: 'line'
    }
  ]
};


      // 使用刚指定的配置项和数据显示图表。
      myChart1.setOption(option1);

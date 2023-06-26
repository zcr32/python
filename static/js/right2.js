var ec_right2 = echarts.init(document.getElementById('right2'), "dark");
option = {
    title: {
        text: '全国新增趋势'
    },
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'cross',
            label: {
                backgroundColor: '#6a7985'
            }
        }
    },
    legend: {
        data: ['新增确诊', '新增疑似']
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    xAxis: [
        {
            type: 'category',
            boundaryGap: false,
            data: []
        }
    ],
    yAxis: [
        {
            type: 'value'
        }
    ],
    series: [
        {
            name: '新增确诊',
            type: 'line',
            stack: '总量',
            areaStyle: {},
            data: []
        },
        {
            name: '新增疑似',
            type: 'line',
            stack: '总量',
            areaStyle: {},
            data: []
        }
    ]
};
ec_right2.setOption(option)


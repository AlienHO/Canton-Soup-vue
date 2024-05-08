<template>
    <div id="app">
      <div ref="main" style="width: 600px; height: 400px;"></div>
    </div>
  </template>
  
  <script>
  import * as echarts from 'echarts';
  
  export default {
    name: 'App',
    mounted() {
      this.$nextTick(() => {
        this.initChart();
      });
    },
    methods: {
      initChart() {
        const myChart = echarts.init(this.$refs.main);
  
        // 异步获取数据
        fetch('/chart_data.json')
          .then(response => response.json())
          .then(data => {
            // 定义四性和五味的文字映射
            const fourXingMapping = {
              0: '寒', 1: '凉', 2: '平', 3: '温', 4: '热'
            };
            const fiveWeiMapping = {
              0: '咸', 1: '酸', 2: '甘', 3: '辛', 4: '苦'
            };
  
            // 将数据按大小排序，小点在上大点在下
            const formattedData = data.x.map((x, index) => {
              const fourXingValue = Math.floor(x);
              const fiveWeiValue = Math.floor(data.y[index]);
  
              return {
                value: [x, data.y[index], data.size[index]],
                itemStyle: { color: data.color[index] },
                name: data.name[index],
                description: data.description[index],
                fourXing: fourXingMapping[fourXingValue] || '未知',
                fiveWei: fiveWeiMapping[fiveWeiValue] || '未知',
                citationCount: data.size[index]
              };
            }).sort((a, b) => b.value[2] - a.value[2]);
  
            myChart.setOption({
              title: {
                text: '广式煲汤材料四性与五味分析',
                subtext: '基于汤方数据整合',
                left: 'center'
              },
              tooltip: {
                trigger: 'item',
                formatter: function (params) {
                  // 使用项目点颜色动态调整名称颜色
                  const nameStyle = `color:${params.data.itemStyle.color}`;
                  const xingWei = `性${params.data.fourXing}味${params.data.fiveWei}`;
  
                  return `
                    <strong style="${nameStyle}">${params.data.name}</strong><br>
                    ${xingWei}<br>
                    引用次数：${params.data.citationCount}<br>
                    ${params.data.description}
                  `;
                }
              },
              xAxis: {
                type: 'value',
                axisLabel: {
                  formatter: function (value) {
                    const categories = {
                      1: '寒',
                      2: '凉',
                      3: '平',
                      4: '温',
                      5: '热'
                    };
                    return categories[Math.floor(value)] || '四性';
                  }
                }
              },
              yAxis: {
                type: 'value',
                axisLabel: {
                  formatter: function (value) {
                    const tastes = {
                      1: '咸',
                      2: '酸',
                      3: '甘',
                      4: '辛',
                      5: '苦',
                    };
                    return tastes[Math.floor(value)] || '五味';
                  }
                }
              },
              series: [{
                name: '数据点',
                type: 'scatter',
                symbolSize: function (data) {
                  return data[2];  // 使用 size 数值作为符号大小
                },
                data: formattedData
              }]
            });
          })
          .catch(error => console.error('Error loading the chart data:', error));
      }
    }
  };
  </script>
  
  <style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  </style>
  
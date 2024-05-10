<template>
  <div id="app" ref="chartContainer" style="width: 100%; height: 100%;">
    <button @click="toggleLabels">Toggle Labels</button> <!-- 新增切换显示标签按钮 -->
    <button @click="downloadSVG">Download SVG</button> <!-- 下载 SVG 按钮 -->
    <div ref="main" style="width: 100%; height: 100%;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'MaterialChartComponent',
  data() {
    return {
      myChart: null,
      showLabels: true // 是否显示标签的状态
    };
  },
  mounted() {
    this.myChart = echarts.init(this.$refs.main, null, {renderer: 'svg'});
    this.initChart(this.myChart);
    window.addEventListener('resize', this.onResize);
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize);
    if (this.myChart) {
      this.myChart.dispose();
    }
  },
  methods: {
    onResize() {
      if (this.myChart) {
        this.myChart.resize();
      }
    },
    initChart(myChart) {
      fetch('/chart_data.json')
        .then(response => response.json())
        .then(data => {
          const formattedData = this.formatData(data);
          myChart.setOption(this.getChartOption(formattedData));
        })
        .catch(error => console.error('Error loading the chart data:', error));
    },
    formatData(data) {
      const fourXingMapping = {0: '寒', 1: '凉', 2: '平', 3: '温', 4: '热'};
      const fiveWeiMapping = {0: '咸', 1: '酸', 2: '甘', 3: '辛', 4: '苦'};

      return data.x.map((x, index) => ({
        value: [x, data.y[index], data.size[index]],
        itemStyle: { 
          color: data.color[index],
          borderColor: this.getHighSaturationColor(data.color[index]), // 边框颜色
          borderWidth: 2 // 边框宽度
        },
        name: data.name[index],
        description: data.description[index],
        fourXing: fourXingMapping[Math.floor(x)] || '未知',
        fiveWei: fiveWeiMapping[Math.floor(data.y[index])] || '未知',
        citationCount: data.size[index]
      })).sort((a, b) => b.value[2] - a.value[2]);
    },
    getHighSaturationColor(color) {
      // 使用简单的方法将颜色转换为较高饱和度的颜色
      const colorObject = echarts.color.parse(color);
      colorObject.s *= 1.3; // 增加饱和度
      return echarts.color.stringify(colorObject, 'rgba');
    },
    getChartOption(data) {
      // 定义数据范围和目标范围
      const minSize = 1;
      const maxSize = 200;
      const minMappedSize = 10;
      const maxMappedSize = 100;

      // 将数据范围映射到目标范围
      const mappedSize = size => (size - minSize) / (maxSize - minSize) * (maxMappedSize - minMappedSize) + minMappedSize;

      return {
        title: {
          text: '广式煲汤材料四性与五味分析',
          subtext: '基于汤方数据整合',
          left: 'center'
        },
        tooltip: {
          trigger: 'item',
          formatter: params => {
            const nameStyle = `color:${params.data.itemStyle.color}`;
            const xingWei = `性${params.data.fourXing}味${params.data.fiveWei}`;
            return `<strong style="${nameStyle}">${params.data.name}</strong><br>${xingWei}<br>引用次数：${params.data.citationCount}<br>${params.data.description}`;
          }
        },
        xAxis: {
          type: 'value',
          axisLabel: {
            formatter: value => ['寒', '凉', '平', '温', '热'][Math.floor(value) - 1] || '四性'
          }
        },
        yAxis: {
          type: 'value',
          axisLabel: {
            formatter: value => ['咸', '酸', '甘', '辛', '苦'][Math.floor(value) - 1] || '五味'
          }
        },
        series: [{
          name: '数据点',
          type: 'scatter',
          symbolSize: data => mappedSize(data[2]), // 使用映射后的大小作为符号大小
          data,
          label: {
            show: this.showLabels, // 动态显示或隐藏标签
            position: 'top', // 标签位置
            formatter: params => params.data.name // 显示材料的名字
          }
        }]
      };
    },

    toggleLabels() {
      // 切换标签显示状态
      this.showLabels = !this.showLabels;
      // 重新设置图表选项
      const currentOption = this.myChart.getOption();
      currentOption.series[0].label.show = this.showLabels;
      this.myChart.setOption(currentOption);
    },

    downloadSVG() {
      const svgDataURL = this.myChart.getDataURL({type: 'svg'});
      const downloadLink = document.createElement('a');
      downloadLink.href = svgDataURL;
      downloadLink.download = "chart.svg";
      document.body.appendChild(downloadLink);
      downloadLink.click();
      document.body.removeChild(downloadLink);
    }
  }
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  background-color: transparent;
}
button {
  margin: 5px;
}
</style>

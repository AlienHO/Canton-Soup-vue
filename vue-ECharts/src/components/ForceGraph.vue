<template>
  <div ref="chartContainer" style="width: 100%; height: 100%;"></div>
</template>

<script>
import * as echarts from 'echarts';
import Papa from 'papaparse';

export default {
  data() {
    return {
      chartInstance: null,
      chartData: [],
    };
  },
  mounted() {
    this.initChart();
    this.loadData();
  },
  methods: {
    initChart() {
      this.chartInstance = echarts.init(this.$refs.chartContainer);
    },
    loadData() {
      fetch('/public/Force_date.csv')
        .then(response => response.text())
        .then(csvData => {
          this.chartData = this.parseCSV(csvData);
          this.updateChart();
        });
    },
    parseCSV(csvData) {
      const results = Papa.parse(csvData, { header: false });
      const chartData = [];
      results.data.forEach((row, index) => {
        if (index === 0 || row[1] === '') return; // 跳过第一行和空行
        const nodes = row.slice(1).filter(ingredient => ingredient.trim() !== '').map((ingredient, idx) => ({ id: String(idx), name: ingredient }));
        const edges = [];
        if (nodes.length > 1) {
          nodes.forEach((node, idx) => {
            if (idx < nodes.length - 1) {
              edges.push({ source: String(idx), target: String(idx + 1) });
            }
          });
          // 首尾相连
          edges.push({ source: String(nodes.length - 1), target: '0' });
        }

        chartData.push({
          name: row[0],
          nodes,
          edges
        });
      });
      return chartData;
    },
    updateChart() {
  const columns = 8; // 横向排列的图表数
  const rows = Math.ceil(this.chartData.length / columns); // 纵向排列的图表数
  const options = {
    series: this.chartData.map((item, idx) => ({
      type: 'graph',
      layout: 'force',
      animation: false,
      name: item.name,
      data: item.nodes.map(n => ({
        ...n,
        symbolSize: 20,
        label: {
          show: true,
          formatter: '{b}', // 显示节点名称
          color: '#FFF', // 将文本设置为白色
          textBorderColor: '#BBBBBB', // 使用节点当前颜色进行描边
          textBorderWidth: 2 // 边框宽度
        }
      })),
      edges: item.edges.map(e => ({ source: e.source, target: e.target })),
      force: {
        repulsion: 60, // 排斥力
        edgeLength: 2 // 边长度
      },
      label: {
        show: true,
        position: 'inside',
        formatter: '{b}', // 显示节点名称
        color: '#FFF', // 设置为白色
        textBorderWidth: 2, // 设置描边宽度
      },
      left: `${(idx % columns) * (100 / columns)}%`,
      top: `${Math.floor(idx / columns) * (100 / rows)}%`,
      width: `${100 / columns}%`,
      height: `${100 / rows}%`,
    })),
    graphic: this.chartData.map((item, idx) => ({
      type: 'text',
      left: `${(idx % columns) * (100 / columns) + 3}%`, // 居中调整
      top: `${Math.floor(idx / columns) * (100 / rows) + 20}%`, // 底部调整
      style: {
        text: item.name,
        fill: '#333',
        font: '14px Arial',
        textAlign: 'center'
      }
    }))
  };

  this.chartInstance.setOption(options);
}



  }
};
</script>


<style>
/* CSS 样式保持适应性布局 */
body, html {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}
</style>

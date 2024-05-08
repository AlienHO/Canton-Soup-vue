

<script setup>
import { ref, onMounted } from 'vue'
import * as echarts from 'echarts'

// 使用和模板中一致的 ref 名称
const chart = ref(null);

onMounted(() => {
  // 确保 DOM 已经加载并且 ref 已经绑定
  if (chart.value) {
    // 基于准备好的 dom，初始化 echarts 实例
    var myChart = echarts.init(chart.value);

    // 指定图表的配置项和数据
    var option = {
      title: {
        text: 'ECharts 入门示例'
      },
      tooltip: {},
      legend: {
        data: ['销量']
      },
      xAxis: {
        data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
      },
      yAxis: {},
      series: [
        {
          name: '销量',
          type: 'bar',
          data: [5, 20, 36, 10, 10, 20]
        }
      ]
    };

    // 应用图表配置
    myChart.setOption(option);
  }
});
</script>

<template>
  <div>
    <!-- 确保 ref 名称和脚本中的相匹配 -->
    <div ref="chart" style="width: 1000px; height: 400px;"></div>
  </div>
</template>

<style scoped>
</style>

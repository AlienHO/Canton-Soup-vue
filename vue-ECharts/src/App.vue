<template>
  <div class="common-layout">
    <el-container style="width: 100vw;height: 100vh;">
      <!-- 调整 Header 的高度为总高度的 2/5 -->
      <el-header style="height: 40vh;">
        <material-chart-component></material-chart-component>
      </el-header>
      <!-- Main 占据剩余的 3/5 -->
      <el-main style="height: 60vh;">
        <force-graph></force-graph>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import MaterialChartComponent from './components/MaterialChartComponent.vue';
import ForceGraph from './components/ForceGraph.vue';

export default {
  name: 'App',
  components: {
    MaterialChartComponent,
    ForceGraph
  }
};
</script>

<style>
/* 使用 @font-face 规则定义方正楷体_GBK */
@font-face {
  font-family: 'FZKaiTi';
  src: url('/fonts/FZKTK--GBK1-0.ttf') format('truetype');
  font-weight: normal;
  font-style: normal;
}

/* 这将确保 #app 元素和所有的容器元素占满整个可用屏幕 */
html, body, #app {
  height: 100%;
  margin: 0;
  font-family: 'FZKaiTi', sans-serif; /* 应用方正楷体_GBK 作为默认字体 */
}

.common-layout {
  height: 100%;
  background-image: url('/01.jpg'); /* 设置背景图片 */
  background-size: cover; /* 覆盖整个容器 */
  background-position: center; /* 图片居中显示 */
}
</style>


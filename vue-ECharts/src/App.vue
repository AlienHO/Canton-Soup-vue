<template>
  <div class="common-layout">
    <el-container style="height: 100vh;">
      <el-header style="height: 10vh;">Header</el-header> <!-- 使用 vh 单位 -->
      <el-container>
        <el-aside width="60vw" style="height: 90vh;"> <!-- 容器高度调整为视口高度减去 header 高度 -->
          <material-chart-component></material-chart-component>
        </el-aside>
        <el-container style="height: 90vh;">
          <el-main>Main</el-main>
          <el-footer style="height: 10vh;">Footer</el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>


<script>
import MaterialChartComponent from './components/MaterialChartComponent.vue';

export default {
  name: 'App',
  components: {
    MaterialChartComponent
  }
};
</script>

<style>
/* 这将确保 #app 元素和所有的容器元素占满整个可用屏幕 */
html, body, #app {
  height: 100%;
  margin: 0;
}
.common-layout {
  height: 100%;
}
</style>

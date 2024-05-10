<template>
  <div class="common-layout">
    <el-container style="height: 100vh;">
      <el-header style="height: 10vh;">Header</el-header>
      <el-container>
        <el-aside width="60vw" style="height: 90vh;">
          <material-chart-component></material-chart-component>
        </el-aside>
        <el-container style="width: 40vw;">
          <!-- 调整 Main 和 Footer 的宽度比例 -->
          <el-main style="height: 21vh;">Main</el-main> <!-- 高度为 21vh，占剩余高度的 3/10 -->
          <el-footer style="height: 49vh;"> <!-- 高度为 49vh，占剩余高度的 7/10 -->
            <force-graph></force-graph> <!-- 引入 ForceGraph 组件 -->
          </el-footer>
        </el-container>
      </el-container>
    </el-container>
  </div>
</template>

<script>
import MaterialChartComponent from './components/MaterialChartComponent.vue';
import ForceGraph from './components/ForceGraph.vue'; // 引入 ForceGraph 组件

export default {
  name: 'App',
  components: {
    MaterialChartComponent,
    ForceGraph // 注册组件
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
footer {
  padding: 20px;
  background-color: #f9f9f9;
}
</style>

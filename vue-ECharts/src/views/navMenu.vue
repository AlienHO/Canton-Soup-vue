<script setup>
import { ref, onMounted } from 'vue'

import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'

</script>

<template>

    <el-aside width="200px" class="aside">
        <el-menu
            default-active="2"
            class="el-menu-vertical-demo"
            @open="handleOpen"
            @close="handleClose"
        >
            <el-menu-item index="1">
            <el-icon><icon-menu /></el-icon>
            <span>Navigator 1111</span>
            </el-menu-item>

            <el-menu-item index="2">
            <el-icon><icon-menu /></el-icon>
            <span>Navigator 2222</span>
            </el-menu-item>

            <el-menu-item index="3">
            <el-icon><icon-menu /></el-icon>
            <span>Navigator 3333</span>
            </el-menu-item>
        </el-menu>
        
    </el-aside>

</template>



<style scoped>
</style>

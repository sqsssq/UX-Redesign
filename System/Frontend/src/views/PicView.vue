<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2022-09-17 23:36:36
 * @LastEditTime: 2023-02-13 11:02:16
-->
<template>
    <div class="common-layout" style="width: 100%; height: 100vh; background-color: #FFF;" v-loading="!initSign" :element-loading-text="loadingText" element-loading-background="rgba(0, 0, 0, 0.8)">
        <!-- #e6e6e6 -->
        <div>
            计数器{{ cnt }}
        </div>
    </div>
</template>
  
<script>
import Main from '../components/Main.vue';
import { useDataStore } from "../stores/counter";

import GoEasy from 'goeasy';

export default {
    name: "home_view",
    data() {
        return {
            msgH: null,
            cnt: 0
        };
    },
    computed: {
        initSign() {
            return 1;
        },
        loadingText() {
            return "Loading"
        }
    },

    mounted() {
        this.msgH = 1;
        let goEasy = GoEasy.getInstance({
    host:'hangzhou.goeasy.io', //新加坡host：singapore.goeasy.io
    appkey: "BS-bb5385b44cf84e7aa10529360a06b6bc", //替换为您的应用appkey
    modules: ['pubsub']
});
 //建立连接
goEasy.connect({
    onSuccess: function () { //连接成功
        console.log("GoEasy connect successfully.") //连接成功
    },
    onFailed: function (error) { //连接失败
        console.log("Failed to connect GoEasy, code:"+error.code+ ",error:"+error.content);
    }
});

let counter = 0;
const vm = this;
//订阅消息
goEasy.pubsub.subscribe({
    channel: "test",//替换为您自己的channel
    onMessage: function (message) { //收到消息
        console.log("Channel:" + message.channel + " content:" + message.content);
        // counter += 1;
        // document.getElementById('counter').innerHTML = counter;
        vm.cnt += 1;
    },
    onSuccess: function () {
        console.log("Channel订阅成功。");
    },
    onFailed: function (error) {
        console.log("Channel订阅失败, 错误编码：" + error.code + " 错误信息：" + error.content)
    }
});
    },
    methods: {
        fetchData() {}
    },
    components: { Main }
};
</script>

<style scoped>
.boundary {
    /*border-style: dashed;*/
    border-style: solid;
    border-color: #d3dce6;
    border-width: 0.5px;
    border-radius: 3px;
}
</style>
  
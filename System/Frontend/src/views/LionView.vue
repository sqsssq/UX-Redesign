<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2022-09-17 23:36:36
 * @LastEditTime: 2023-02-13 11:02:16
-->
<template>
    <div class="common-layout content" style="width: 100%; height: 100vh; background-color: #dbcfa6;" v-loading="!initSign" :element-loading-text="loadingText" element-loading-background="rgba(0, 0, 0, 0.8)">
        <!-- <Main :msgH="msgH"/> -->
        <!-- #e6e6e6 -->
    
        <button @click="addLion()" class="addButton" style="background-color: transparent; color: #886e56; font-size: 20px; border: 1px solid #886e56;">
                    
                    狮子 +1
                    <div class="logo">
                        <img src="../assets/lion.png" alt="" srcset="" style="width: 200px;">
                    </div>
                </button>
    </div>
</template>

<script>
import Main from '../components/Main.vue';
import { useDataStore } from "../stores/counter";
import GoEasy from 'goeasy';
import { ElMessage } from 'element-plus';

export default {
    name: "home_view",

    data() {
        return {
            msgH: null,
            goEasy: null,
            pubsub: null
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
        this.goEasy = GoEasy.getInstance({
            host: 'hangzhou.goeasy.io', //新加坡host：singapore.goeasy.io
            appkey: "BC-263fff6acdbe4b41938ae0a266882820", //替换为您的应用appkey
            modules: ['pubsub']
        });
        // this.goEasy = goEasy;
        // 建议在main.js里初始化全局的GoEasy对象
        // Vue.prototype.goEasy = goEasy;
        //建立连接
        this.goEasy.connect({
            onSuccess: function() { //连接成功
                console.log("GoEasy connect successfully.") //连接成功
            },
            onFailed: function(error) { //连接失败
                console.log("Failed to connect GoEasy, code:" + error.code + ",error:" + error.content);
            }
        });
        this.pubsub = this.goEasy.pubsub;
    },
    methods: {
        fetchData() {},
        addLion() {
            console.log(111);
            this.pubsub.publish({
                channel: "test", //替换为您自己的channel
                message: "Hello, GoEasy!", //替换为您想要发送的消息内容
                onSuccess: function() {
                    console.log("消息发布成功。");
                    ElMessage({
                        message: "添加成功！",
                        type: "success"
                    })
                },
                onFailed: function(error) {
                    console.log("消息发送失败，错误编码：" + error.code + " 错误信息：" + error.content);
                    ElMessage({
                    message: "出了问题，再来一次吧",
                    type: "error"
                    })
                }
            });
        }
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

.addButton {
    color: rgb(86, 55, 33);
    width: auto;
    background-color: rgba(0, 0, 0, 0);
    font-size: 20px;
    /* color: #886e56; */
}

.content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background-color: rgb(225, 212, 173);
    width: 100%;
    height: 100%;
}

.logo {
    width: 100%;
    display: flex;
    align-items: center;
    /* height: 200rpx; 
		width: 200rpx;
		margin-top: 200rpx;
		margin-left: auto;
		margin-right: auto;
		margin-bottom: 50rpx; */
}

.text-area {
    display: flex;
    justify-content: center;
}

.title {
    font-size: 36rpx;
    color: #8f8f94;
}
</style>

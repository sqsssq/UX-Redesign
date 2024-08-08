<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-02-01 19:32:17
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-08-04 22:36:43
-->
<template>
    <div style="width: 100%; height: 100%;">
        
        <div id="navBar" style="display: flex; justify-content: space-between;">
            <div style="font-weight: 800; padding-left: 0px;position: absolute;">
                    UX Redesign
                    <!-- <span id="version">
                    <a id="version" style="font-size: 16px; font-style: italic;">
                        <router-link to="/baseline">Full Version</router-link>
                    </a>
                </span> -->
            </div>

            <div style="position: absolute; right: 10px;"><el-button text bg type="primary" @click="startStudy()">开始</el-button> <el-button text bg type="success" @click="saveData()">保存</el-button> <el-button text bg type="danger" @click="endStudy()">结束</el-button></div>
        </div>
        <div style="height: calc(100vh - 40px); width: calc(100% - 0px);">
            <div class="framework" id="videoView" style="position: absolute; left: calc(5px); top: calc(5px); height: calc(100% - 10px); width: calc(70vw - 0px);">
                <div class="frameworkTitle">
                    <div class="title">
                        <div style="margin-top: -3px;">Ideation</div>
                        
                    </div>
                    <div class="titleTriangle"></div>
                </div>
                <div class="frameworkBody">
                    <MainView :startTag="startTag" />
                </div>
            </div>
            <div class="framework" id="controlView" style="position: absolute; right: calc(5px); top: calc(5px); height: calc(60% - 5px); width: calc(30vw - 15px);">
                
                <div class="frameworkTitle" style="display: flex;">
                    <div class="title"> 
                        <div style="margin-top: -3px;">Chatbot</div>
                        
                    </div>
                    <div class="titleTriangle"></div>
                    
                </div>
                <div class="frameworkBody">
                    <DesignView />
                </div>
            </div>
            <div class="framework" id="controlView" style="position: absolute; right: calc(5px); top: calc(5px + 60%); height: calc(40% - 10px); width: calc(30vw - 15px);">
                
                <div class="frameworkTitle">
                    <div class="title">
                        <div style="margin-top: -3px;">Design</div>
                    </div>
                    <div class="titleTriangle"></div>
                </div>
                <div class="frameworkBody">
                    <!-- <DesignView /> -->
                    <ResultView />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useDataStore } from "@/stores/counter";
import { Fireworks } from 'fireworks-js';
import MainView from './MainView.vue';
import DesignView from './DesignView.vue';
import ResultView from "./ResultView.vue";
import axios from 'axios';
export default {
    name: "APP",
    props: ["msgH"],
    data() {
        return {
            msg1: "Hello, main!",
            intervalID: null,
            startTag: false
        };
    },
    methods: {
        generalChat() {
            const dataStore = useDataStore();
            dataStore.chatData = dataStore.generalChatData;
        },
        sendData(data) {
            // https://formspree.io/f/mnnavdze
            axios.post('https://formspree.io/f/xrgnoavv', {
                data: JSON.stringify(data),
                dataType: 'json'
            }).then((res) => {
                console.log(res);
            }).catch(err => {
                console.log(err);
            })
        },
        saveData() {
            const dataStore = useDataStore();
            const data = dataStore.saveData();
            console.log(data);
            this.sendData(data);
        },
        startStudy() {
            this.startTag = true;
            const vm = this;
            this.intervalID = setInterval(() => {
                vm.saveData();
            }, 600000);
        },
        endStudy() {
            clearInterval(this.intervalID);
            this.saveData();
        }
    },
    created() {},
    mounted() {
        // let dataStore = useDataStore();
        // dataStore.$subscribe(() => {
        //     this.leftShow = dataStore.leftShow;
        //     this.video_select = dataStore.select_video;
        // })
    },
    watch: {
        
    },
    components: { MainView, DesignView, ResultView }
}
</script>

<style>
#version {
    position: relative;
    padding-bottom: 0px;
    /* 控制线的位置 */
}

#version::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    border-bottom: 1px solid #00bd7e;
}

#version::before {
    content: '';
    position: absolute;
    bottom: -5px;
    right: -15px;
    /* 控制线的位置 */
    width: 10px;
    height: 18px;
    border-left: 1px solid #00bd7e;
    /* 右侧的线 */
    transform: rotate(45deg);
    /* 旋转45度 */
}

.el-select-dropdown__item {
    color: white;
}

.framework {
    border: 0px solid rgb(105, 119, 122);
    background-color: white;
    border-radius: 3px;
}

.framework .frameworkTitle {
    height: 32px;
}

.framework .frameworkBody {
    height: calc(100% - 32px);
    padding: 5px 10px 5px 10px;
}

.framework .frameworkTitle .title {
    float: left;
    width: fit-content;
    background-color: rgba(255, 159, 49, 1);
    /* background-color: black; */
    height: 32px;
    font-weight: 600;
    font-size: 24px;
    color: white;
    padding-left: 10px;
    padding-right: 3px;
    padding-top: 0px;
    font-family: 'KoHo';
    line-height: 35px;
}

.framework .frameworkTitle .titleTriangle {
    float: left;
    width: 0;
    height: 0;
    border-color: transparent rgba(255, 159, 49, 1);
    border-width: 0px 0px 32px 32px;
    border-style: solid;
}

#navBar {
    background-color: #FF9F31;
    text-align: left;
    font-weight: bold;
    color: white;
    font-size: 24px;
    height: calc(40px);
    /* padding-top: 0.2%; */
    /* padding-bottom: 0.5%; */
    padding-left: 10px;
    font-family: 'jejuHallasan', 'Avenir', Helvetica, Arial, sans-serif;
}
</style>

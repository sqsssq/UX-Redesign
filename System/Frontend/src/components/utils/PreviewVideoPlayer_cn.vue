<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-08-25 21:02:43
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-08-25 21:02:44
-->
<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-01-23 13:24:12
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-01-24 15:13:23
-->
<template>
    <el-dialog ref="videoDialog" v-model="visible" :title="'视频预览 ' + video_name" width="50%"  :class="'show_info_dialog_pre'">
        <div style="font-style: italic;font-size: 16px;">
            <span style="color: red; font-weight: bold;">问题：</span>
            <span>{{  info.text }}</span>
        </div>
        
        <div :style="{width: '100%', 'padding-left': (.5 * .05 * elWidth - 20) + 'px', height: '500px', overflowY: 'auto', textAlign: 'left'}">
            <h1>Video</h1>
            <video-player :src="video_url" playsinline controls :volume="0.2" :width=".5 * .9 * elWidth" :playback-rates="[0.7, 1.0, 1.5, 2.0]" @mounted="handleMounted" @ready="handleEvent($event)" @play="handleEvent($event)" @pause="handleEvent($event)"
                @ended="handleEvent($event)" @loadeddata="handleEvent($event)" @waiting="handleEvent($event)" @playing="handleEvent($event)" @canplay="handleEvent($event)" @canplaythrough="handleEvent($event)" @timeupdate="handleEvent(player?.currentTime())"
            />
            <h1>UI</h1>
            <img :src="img_url" alt="" :width=".5 * .9 * elWidth">

        </div>
        <template #footer>
            <span class="dialog-footer" style="display: flex; justify-content: center;">
                <!-- <el-button type="success" @click="analysisVideo">
                    分析
                </el-button> -->
                <el-button type="primary" @click="visible = false">
                    关闭
                </el-button>
            </span>
        </template>
    </el-dialog>
</template>

<script>
import { VideoPlayer } from '@videojs-player/vue'
import 'video.js/dist/video-js.css'
import videojs from 'video.js'
import 'video.js/dist/video-js.css'
import { useDataStore } from '../../stores/counter';

export default {
    name: "PCV",
    props: ['dialogVisible', 'config', 'info'],
    components: { VideoPlayer },
    data() {
        return {
            elHeight: 0,
            elWidth: 0,
            visible: false,
            player: {},
            video_url: '',
            img_url: '',
            video_name: ''
        };
    },
    methods: {
        translate(x, y, deg) {
            return `translate(${x}, ${y}) rotate(${deg})`;
        },
        analysisVideo() {
            this.visible = false;
            const dataStore = useDataStore();
            dataStore.select_video = this.config.video_id;
            dataStore.currentPlayTime = this.config.time;
            dataStore.previewSelect = 1;
            dataStore.leftShow = 1;
            console.log(dataStore.currentPlayTime)
        },
        handleEvent(log) {
            // console.log(log);
        },
        handleMounted(payload) {
            this.player = payload.player;
            // console.log(payload)
        }
    },
    created() {},
    mounted() {
        this.elWidth = document.body.clientWidth;
        this.elHeight = this.$refs.videoDialog.offsetHeight;
    },
    watch: {
        dialogVisible: {
            handler(newVal) {
                this.visible = newVal;
                // this.visible = false;
            }
        },
        visible: {
            handler(newVal) {
                // console.log(this.visible)
                if (!this.visible) this.player.pause()
                this.$emit("showDialog", newVal);
            }
        },
        config: {
            handler(newVal) {
                console.log(this.config)
                this.video_url = 'AI_Tool/P' + this.config.video_id + '/video.mp4';
                this.video_name = this.config.name;
                console.log(this.video_url);
                this.$nextTick(() => {
                    this.player.currentTime(this.config.time);
                })
            },
            deep: true
        },
        info: {
            handler() {
                this.img_url = 'Product UI/' + this.info.ui + '.png';
            },
            deep: true
        }
    },
};
</script>

<style scoped>
.show_info_dialog_pre {
    --el-dialog-bg-color: #454647AA;
    color: white;
    /* border-radius: 15px; */
}
:deep(.video-js .vjs-big-play-button .vjs-icon-placeholder:before) {
    position: relative;
}

:deep(.vjs-button > .vjs-icon-placeholder:before) {
    position: relative;
}
</style>

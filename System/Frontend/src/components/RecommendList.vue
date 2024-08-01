<!--
 * @Description: Prediction Comparator View
 * @Author: Qing Shi
 * @Date: 2023-06-29 10:17:17
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-02-07 19:44:21
-->
<template>
    <PreviewVideoPlayer :dialogVisible="dialogVisible" :config="config" @showDialog="showDialog" />
    <div class="frameworkBody">
        <div style=" height: 30px;text-align: left; font-size: 24px; color: white; font-weight: bold; justify-content: space-between; display: flex;">
            <span>视频推荐</span>
            <span style="font-size: 20px;">相似度：高 → 低</span>
        </div>
        <div style="height: calc(100% - 40px);">
            <div ref="recommendList" id="recommendList" style="height: calc(100% - 0px); margin-top: 10px; overflow-x: hidden; width: 100%; display: flex;">
                <div v-for="(d, i) in video_list" ref="video_element" :key="'video' + i" id="video_list" style="border: 0px solid white; height: 100%; color: white; font-size: 20px; padding: 3px 10px 5px 10px;">
                    <div style="height: 30px; display: flex; justify-content: space-between;">
                        <div>{{ d.id[0] == 'P' ? 'V' + d.id.substr(1) : d.id }}</div>
                        <div style="height: 100%; width: calc(100% - 40px); display: flex; align-items: center; justify-content: end; border-left: 1px solid white; border-right: 1px solid white;">
                            <div :style="{width: (100 * d.similarity / max_similarity) + '%', height: '50%', backgroundColor: 'white'}"></div>
                        </div>
                    </div>
                    <!-- <div style="width: 400px;"></div> -->
                    <!-- <div style="width: 00px;"></div> -->
                    <div style="height: calc(100% - 35px);">
                        <img :src="'AI_Tool/' + d.id + '/fig.png'" alt="" style="height: 100%;">
                        <div class="play_button align-class" @click="showPreview(d.id)">
                            <div style="background-color: white; border-radius: 80px; height: 80px;">
                                <svg t="1705932141588" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4359" width="80" height="80"><path d="M374.272 333.312v355.328c0 30.208 20.992 40.448 45.568 26.112l288.768-175.104c25.088-15.872 25.088-40.448 0-54.784L419.84 309.76c-7.68-5.12-14.336-6.656-20.992-6.656-14.336-2.56-24.576 9.216-24.576 30.208zM1024 512c0 282.624-229.376 512-512 512S0 794.624 0 512 229.376 0 512 0s512 229.376 512 512z" p-id="4360" fill="#8a8a8a"></path></svg>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
    
            <div style="position: absolute; top: calc(0px); left: 0px; width:50px; height: calc(100% - 0px); background-color: rgba(0, 0, 0, .7);  border-radius: 0px;" class="scroll-button" @click="scrollToLeft">
                <svg style="position: absolute; top: calc(50% - 25px); left: 10px;" t="1705561614491" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4198" width="25" height="50"><path fill="white" d="M609.408 149.376 277.76 489.6a32 32 0 0 0 0 44.672l331.648 340.352a29.12 29.12 0 0 0 41.728 0 30.592 30.592 0 0 0 0-42.752L339.264 511.936l311.872-319.872a30.592 30.592 0 0 0 0-42.688 29.12 29.12 0 0 0-41.728 0z"></path></svg>
            </div>
    
            <div style="position: absolute; top: calc(0px); right: 0px; width:50px; height: calc(100% - 0px); background-color: rgba(0, 0, 0, .7); border-radius: 0px;" class="scroll-button" @click="scrollToRight">
                <svg style="position: absolute; top: calc(50% - 25px); right: 10px;" t="1705561614491" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4198" width="25" height="50"><path fill="white" d="M340.864 149.312a30.592 30.592 0 0 0 0 42.752L652.736 512 340.864 831.872a30.592 30.592 0 0 0 0 42.752 29.12 29.12 0 0 0 41.728 0L714.24 534.336a32 32 0 0 0 0-44.672L382.592 149.376a29.12 29.12 0 0 0-41.728 0z"></path></svg>
            </div>
        </div>
    </div>
</template>

<script>
import { useDataStore } from "../stores/counter";
import PreviewVideoPlayer from './utils/PreviewVideoPlayer.vue';

export default {
    name: "PCV",
    props: [],
    components: { PreviewVideoPlayer },
    data() {
        return {
            video_cnt: 0,
            select_video: '',
            elHeight: 0,
            elWidth: 0,
            video_list: [],
            config: {},
            category: [],
            showTagList: [],
            dialogVisible: false,
            max_similarity: 1
        };
    },
    methods: {
        translate(x, y, deg) {
            return `translate(${x}, ${y}) rotate(${deg})`;
        },
        showPreview(id) {
            this.dialogVisible = true;
            this.config = {
                time: 0,
                video_id: id,
                name: id
            }
        },
        showDialog(data) {
            this.dialogVisible = data;
        },
        scrollToRight() {
            let video_width = document.getElementById('video_list').offsetWidth;
            let cnt = parseInt(video_width * (this.video_list.length) / (this.elWidth)) + 1;
            if (this.video_cnt < cnt) {
                this.video_cnt += 1;
                document.getElementById('recommendList').scrollTo({ top: 0, left: this.video_cnt * (this.elWidth / 2), behavior: 'smooth' });
            }
        },
        scrollToLeft() {
            let video_width = document.getElementById('video_list').offsetWidth;
            if (this.video_cnt > 0) {
                this.video_cnt -= 1;
                while (this.video_cnt * (this.elWidth / 2) >= (video_width * (this.video_list.length - 2)))
                    this.video_cnt--;
                if (this.video_cnt < 0) this.video_cnt = 0;
                document.getElementById('recommendList').scrollTo({ top: 0, left: this.video_cnt * (this.elWidth / 2), behavior: 'smooth' });
            }
        },
        jaccardSimilarity(set1, set2) {
            const intersectionSize = this.intersection(set1, set2).size;
            const unionSize = this.union(set1, set2).size;
            return intersectionSize / unionSize;
        },
        intersection(set1, set2) {
            let uni_set1 = new Set(set1.map(JSON.stringify));
            let uni_set2 = new Set(set2.map(JSON.stringify));
            return new Set([...uni_set2].filter(x => {
                return uni_set1.has(x)
            }));
        },
        union(set1, set2) {
            let uni_set1 = new Set(set1.map(JSON.stringify));
            let uni_set2 = new Set(set2.map(JSON.stringify))
            return new Set([...uni_set1, ...uni_set2]);
        },
        calcSimilarity(data) {
            let pre_data = new Array();
            let test_data = {};
            for (let i in data) {
                let tmp = new Array();
                for (let j in data[i].info) {
                    tmp.push(data[i].info[j].tag);
                }
                if (i == this.select_video) {
                    test_data = {
                        id: i,
                        data: tmp
                    };
                } else {
                    pre_data.push({
                        id: i,
                        data: tmp
                    });
                }
            }
            // console.log(this.showTagList);
            const dataStore = useDataStore();
            if ((this.showTagList.length == 0 || dataStore.select_all == 1)) {
                for (let i in pre_data) {
                    let similarity_data = this.jaccardSimilarity((test_data.data), (pre_data[i].data));
                    pre_data[i].similarity = similarity_data;
                }
            } else {
                for (let i in pre_data) {
                    let cnt = 0;
                    let tmp_data = pre_data[i].data;
                    for (let j in tmp_data) {
                        for (let k in tmp_data[j]) {
                            if (this.showTagList.indexOf(tmp_data[j][k]) != -1)
                                cnt++;
                        }
                    }
                    pre_data[i].similarity = cnt;
                }
            }
            pre_data.sort((a, b) => b.similarity - a.similarity);
            this.max_similarity = pre_data[0].similarity;
            return pre_data;
        }
    },
    created() {},
    mounted() {
        this.elWidth = this.$refs.recommendList.offsetWidth;

        const dataStore = useDataStore();
        let _this = this;

        /**
         * @description: watch the data changes in the store
         * @return {*}
         */

        dataStore.$subscribe((mutations) => {
            this.select_video = dataStore.select_video;
            this.category = dataStore.categorySource;
            this.showTagList = dataStore.showTagList;
            if (this.select_video != '') {
                this.video_list = this.calcSimilarity(dataStore.all_data);
            }
        });
    },
    watch: {},
};
</script>

<style scoped>
.align-class {
    display: flex;
    justify-content: center;
    align-items: center;
}
.scroll-button {
    opacity: .5;
    transition: .5s;
    cursor: pointer;
}

.scroll-button:hover {
    opacity: 1;
    cursor: pointer;
}

.play_button {
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0px;
    left: 0px;
    opacity: 0;
    transition: .5s;
    cursor: pointer;
}

.play_button:hover {
    opacity: 1;
}

/*chrome--------------------------------------------start*/

::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}

/* Track */

::-webkit-scrollbar-track {
    background: #ffffff;
    border-radius: 8px;
}

/* Handle */

::-webkit-scrollbar-thumb {
    background: rgb(201, 201, 202);
    border-radius: 8px;
}

/* Handle on hover */

::-webkit-scrollbar-thumb:hover {
    background: rgb(162, 162, 163);
}

.el-menu::-webkit-scrollbar,
.el-table__body-wrapper::-webkit-scrollbar {
    display: none;
}

.el-menu:hover::-webkit-scrollbar,
.el-table__body-wrapper:hover::-webkit-scrollbar {
    display: block;
}

/*chrome--------------------------------------------end*/
</style>

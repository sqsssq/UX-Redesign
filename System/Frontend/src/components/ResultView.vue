<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-01-24 17:02:12
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-08-04 22:41:27
-->
<template>
    <!-- <PreviewVideoPlayer :dialogVisible="dialogVisible" :config="config" @showDialog="showDialog" /> -->
    
    
    <div style="width: 100%; height: 100%; overflow-y: auto;">
        <el-dialog v-model="previewDialogTag" width="70%">
            <img w-full :src="previewUrl" alt="Preview Image" style="width: 100%;" />
        </el-dialog>
        <el-dialog v-model="uploadDialogTag" title="Design Upload" width="600">
            <div v-loading="loadingTag" element-loading-text="Loading...">
                <el-upload action="#" list-type="picture-card" :auto-upload="false" :on-change="handleSuccess">
                    <svg t="1722558768874" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="21906" width="20" height="20">
                            <path d="M474 152m8 0l60 0q8 0 8 8l0 704q0 8-8 8l-60 0q-8 0-8-8l0-704q0-8 8-8Z" fill="#000000"
                                p-id="21907"></path>
                            <path d="M168 474m8 0l672 0q8 0 8 8l0 60q0 8-8 8l-672 0q-8 0-8-8l0-60q0-8 8-8Z" fill="#000000"
                                p-id="21908"></path>
                        </svg>
    
                    <template #file="{ file }">
                            <div>
                                <img class="el-upload-list__item-thumbnail" :src="file.url" alt="" />
                                <span class="el-upload-list__item-actions">
                                    <span class="el-upload-list__item-preview" @click="showPreview(file.url)">
                                        <svg t="1722558737907" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                            xmlns="http://www.w3.org/2000/svg" p-id="20827" width="20" height="20">
                                            <path
                                                d="M637 443H519V309c0-4.4-3.6-8-8-8h-60c-4.4 0-8 3.6-8 8v134H325c-4.4 0-8 3.6-8 8v60c0 4.4 3.6 8 8 8h118v134c0 4.4 3.6 8 8 8h60c4.4 0 8-3.6 8-8V519h118c4.4 0 8-3.6 8-8v-60c0-4.4-3.6-8-8-8z"
                                                p-id="20828" fill="#fff"></path>
                                            <path
                                                d="M921 867L775 721c122.1-148.9 113.6-369.5-26-509-148-148.1-388.4-148.1-537 0-148.1 148.6-148.1 389 0 537 139.5 139.6 360.1 148.1 509 26l146 146c3.2 2.8 8.3 2.8 11 0l43-43c2.8-2.7 2.8-7.8 0-11zM696 696c-118.8 118.7-311.2 118.7-430 0-118.7-118.8-118.7-311.2 0-430 118.8-118.7 311.2-118.7 430 0 118.7 118.8 118.7 311.2 0 430z"
                                                p-id="20829" fill="#fff"></path>
                                        </svg>
                                    </span>
        
                                </span>
                            </div>
</template>
            </el-upload>
            <!-- <h3>笔记</h3>
            <el-input
                v-model="uploadData.note"
                style="width: 80%"
                :autosize="{ minRows: 4, maxRows: 8 }"
                type="textarea"
                placeholder="Please input"
            /> -->
            <div style="margin-top: 20px;">
                <el-button type="primary" @click="upload()">上传</el-button>
            </div>
            </div>
        </el-dialog>
        <span class="uxButton" @click="isUpload ? uploadDialogTag = true : uploadDialogTag = false"
            style="position: fixed; right: 20px; top: calc(30px + 60%)">
            <svg t="1722556775460" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                p-id="17628" width="20" height="20">
                <path
                    d="M1022.955204 556.24776c0 100.19191-81.516572 181.698249-181.718715 181.698249l-185.637977 0c-11.2973 0-20.466124-9.168824-20.466124-20.466124 0-11.307533 9.168824-20.466124 20.466124-20.466124l185.637977 0c77.628008 0 140.786467-63.148226 140.786467-140.766001 0-77.423347-62.841234-140.448776-140.203182-140.766001-0.419556 0.030699-0.828878 0.051165-1.248434 0.061398-5.935176 0.153496-11.665691-2.302439-15.666818-6.702656-4.001127-4.41045-5.884011-10.345626-5.157463-16.250102 1.330298-10.806113 1.944282-19.760043 1.944282-28.192086 0-60.763922-23.658839-117.874641-66.617234-160.833035-42.968627-42.958394-100.089579-66.617234-160.843268-66.617234-47.368844 0-92.742241 14.449084-131.208321 41.781592-37.616736 26.738991-65.952084 63.700811-81.925894 106.884332-2.425236 6.54916-8.012488 11.399631-14.827707 12.893658-6.815219 1.483794-13.927197-0.603751-18.859533-5.536087-19.289322-19.340487-44.943608-29.982872-72.245418-29.982872-56.322773 0-102.146425 45.813419-102.146425 102.125959 0 0.317225 0.040932 0.982374 0.092098 1.627057 0.061398 0.920976 0.122797 1.831718 0.153496 2.762927 0.337691 9.465582-5.863545 17.928325-15.001669 20.455891-32.356942 8.943696-61.541635 28.550243-82.181721 55.217602-21.305235 27.516704-32.571836 60.508096-32.571836 95.41307 0 86.244246 70.188572 156.422585 156.443052 156.422585l169.981393 0c11.2973 0 20.466124 9.15859 20.466124 20.466124 0 11.2973-9.168824 20.466124-20.466124 20.466124l-169.981393 0c-108.828614 0-197.3753-88.536452-197.3753-197.354833 0-44.053332 14.223956-85.712127 41.126676-120.473839 22.809495-29.450752 53.897537-52.086285 88.710414-64.816215 5.065366-74.322729 67.149353-133.2447 142.751215-133.2447 28.386514 0 55.504128 8.217149 78.651314 23.52581 19.657712-39.868009 48.842405-74.169233 85.497233-100.212376 45.434795-32.295544 99.004875-49.354058 154.918325-49.354058 71.692832 0 139.087778 27.915793 189.782368 78.600149 50.694589 50.694589 78.610382 118.089535 78.610382 189.782368 0 3.704368-0.102331 7.470135-0.296759 11.368932C952.633602 386.245901 1022.955204 463.188294 1022.955204 556.24776z"
                    p-id="17629" fill="#4c4c4c"></path>
                <path
                    d="M629.258611 589.106122c-3.990894 3.990894-9.230222 5.996574-14.46955 5.996574s-10.478655-2.00568-14.46955-5.996574l-67.087954-67.077721 0 358.689289c0 11.307533-9.15859 20.466124-20.466124 20.466124-11.307533 0-20.466124-9.15859-20.466124-20.466124l0-358.689289-67.087954 67.077721c-7.992021 7.992021-20.947078 7.992021-28.939099 0s-7.992021-20.957311 0-28.949332l102.023628-102.013395c7.992021-7.992021 20.947078-7.992021 28.939099 0l102.023628 102.013395C637.250632 568.148811 637.250632 581.114101 629.258611 589.106122z"
                    p-id="17630" fill="#4c4c4c"></path>
            </svg>
        </span>
        <div style="overflow-y: auto; height: calc(100% - 20px); width: 100%;">
            <div v-for="(design, design_i) in uploadData" :key="design_i" class="design" style="text-align: left;">
                <div v-if="design.length != 0">
                    <img class="uxButton" @click="showPreview(design.url)" :src="design.url" alt="" style="width: 100%;">
                    
                </div>
                <h3>修改</h3>
                <div>
                    <v-md-preview :text="design.info.change"></v-md-preview>
                </div>
                <h3>反思</h3>
                <div>
                    {{ design.info.reflection }}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useDataStore } from "../stores/counter";

import PreviewVideoPlayer from './utils/PreviewVideoPlayer.vue';

import * as d3 from 'd3';

export default {
    name: "PCV",
    props: [],
    data() {
        return {
            previewDialogTag: false,
            previewUrl: '',
            uploadDialogTag: false,
            uploadData: [],
            imgRes: '',
            imgUrl: '',
            loadingTag: false
        };
    },
    methods: {
        async upload() {
            // console.log(this.uploadData);
            this.loadingTag = true;
            const dataStore = useDataStore();
            const now = new Date();
            const timeTag = Math.floor(now.getTime() / 1000);
            dataStore.interactionList.push({
                time: timeTag,
                text: '上传设计'
            })
            console.log(this.imgRes)
            let info = [{
                "type": "text",
                "text": "问题: " + dataStore.selectProblem.Problem
            }, {
                "type": "image_url",
                "image_url": dataStore.selectProblem.ui
            }, {
                "type": "image_url",
                "image_url": this.imgRes
            }]
            console.log(info);
            try {

                let response = await dataStore.generatePoint({ 'info': info, 'tag': 2 });
                console.log(response)
                for (let i in dataStore.solutionList) {
                    if (dataStore.solutionList[i].pid == dataStore.selectProblem.pid) {
                        dataStore.solutionList[i].designPath.push({
                            url: this.imgUrl,
                            // note: this.uploadData.note
                            info: JSON.parse(response.data.response),
                            time: timeTag
                        });
                        this.uploadData = dataStore.solutionList[i].designPath;
                    }
                    this.uploadDialogTag = false;
                }
            } catch (error) {

                ElMessage({
                    message: "Oops, 上传失败，请重新上传",
                    type: "warning"
                })
            }
            this.loadingTag = false;
        },
        showPreview(url) {
            this.previewDialogTag = !this.previewDialogTag;
            this.previewUrl = url;
        },

        handleSuccess(response, file) {
            // console.log(file)
            const fileUrl = URL.createObjectURL(file[0].raw);
            // file.url = fileUrl;
            const reader = new FileReader();
            reader.readAsDataURL(file[0].raw);
            let vm = this;
            reader.onloadend = () => {
                vm.imgRes = reader.result;
            }
            this.imgUrl = fileUrl;
        },
    },
    components: { PreviewVideoPlayer },
    created() {},
    computed: {
        isUpload() {
            const dataStore = useDataStore();
            for (let i in dataStore.solutionList) {
                if (dataStore.solutionList[i].pid == dataStore.selectProblem.pid) {
                    return true;
                }
            }
            return false;
        }
    },
    mounted() {
        const dataStore = useDataStore();

        dataStore.$subscribe((mutations, states) => {
            this.uploadData = [];

            for (let i in dataStore.solutionList) {
                if (dataStore.solutionList[i].pid == dataStore.selectProblem.pid) {
                    this.uploadData = dataStore.solutionList[i].designPath;
                }
            }
        });
    },
    watch: {

    },
};
</script>

<style>
.v-md-editor-preview .github-markdown-body {
    padding: 10px 20px 0px 20px;
    /* padding-left: 0px; */
}

.chatContent {
    height: calc(100% - 60px);
    overflow-y: auto;
    overflow-x: inherit;
}

.userBox {
    display: flex;
    justify-content: end;
    /* align-items: center; */
    margin-top: 10px;
}

.robotBox {
    display: flex;
    justify-content: left;
    /* align-items: center; */
    margin-top: 10px;
}

.userContent {
    text-align: left;
    max-width: 70%;
    border: 1px solid #ccc;
    padding: 10px 20px;
    border-radius: 10px;
    margin-right: 10px;
    font-size: 16px;
    line-height: 1.2;
}

.robotIcon {
    padding-top: 5px;
}

.robotContent {
    text-align: left;
    min-height: 50px;
    /* width: 60%; */
    /* border: 1px solid #ccc; */
    /* padding: 5px; */
    /* border-radius: 10px; */
    margin-left: 0px;
}
</style>

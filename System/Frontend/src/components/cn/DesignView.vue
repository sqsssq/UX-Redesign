<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-08-25 20:50:00
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-08-25 20:50:01
-->
<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-01-24 17:02:12
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-08-04 22:41:27
-->
<template>
    <!-- <PreviewVideoPlayer :dialogVisible="dialogVisible" :config="config" @showDialog="showDialog" /> -->
        <el-dialog v-model="previewDialogTag" width="70%">
            <img w-full :src="previewUrl" alt="Preview Image" style="width: 100%;" />
        </el-dialog>
    <div style="position: absolute; right: 10px; top: -25px; display: flex; cursor: pointer;" @click="useGeneralChat">
        <div style="color: blue;" v-if="chatID == -1">通用 &nbsp;</div>
        <div style="color: blue;" v-else>解决方案 &nbsp;</div>
        <svg t="1722930017689" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5328" width="20" height="20"><path d="M928 736c-4 0-8.032-0.736-11.904-2.272-58.528-23.424-115.072-61.056-168.032-111.808a32 32 0 1 1 44.32-46.176c26.048 24.96 52.928 46.304 80.384 63.808a1113.728 1113.728 0 0 1-28.416-121.92 32.032 32.032 0 0 1 10.016-29.152C901.856 445.44 928 391.328 928 336 928 203.648 784.448 96 608 96S288 203.648 288 336c0 3.904 0.128 7.744 0.384 11.584a32 32 0 0 1-29.856 34.016c-17.824 0.512-32.864-12.224-34.016-29.856A233.088 233.088 0 0 1 224 336C224 168.384 396.256 32 608 32s384 136.384 384 304c0 68.16-28.832 134.08-81.568 187.392 18.048 94.624 47.008 168 47.296 168.736a31.936 31.936 0 0 1-7.136 34.496A31.936 31.936 0 0 1 928 736z" p-id="5329" fill="#4c4c4c" stroke="#4c4c4c"></path><path d="M96 992a32 32 0 0 1-29.76-43.84c0.32-0.736 29.248-74.112 47.296-168.736C60.832 726.048 32 660.16 32 592 32 424.384 204.256 288 416 288s384 136.384 384 304S627.744 896 416 896c-47.296 0-93.504-6.848-137.76-20.352-53.664 51.936-110.88 90.272-170.368 114.048A31.36 31.36 0 0 1 96 992z m320-640c-176.448 0-320 107.648-320 240 0 55.296 26.144 109.44 73.632 152.48 8.096 7.36 11.904 18.336 10.016 29.152a1108.832 1108.832 0 0 1-28.416 121.952c32.768-20.896 64.672-47.264 95.456-78.784a32 32 0 0 1 33.6-7.808c43.136 15.264 88.8 23.008 135.712 23.008 176.448 0 320-107.648 320-240S592.448 352 416 352z" p-id="5330" fill="#4c4c4c" stroke="#4c4c4c"></path><path d="M192 624a32 32 0 0 1-32-32c0-84.992 102.88-176 256-176a32 32 0 1 1 0 64c-117.216 0-192 66.336-192 112a32 32 0 0 1-32 32z" p-id="5331" fill="#4c4c4c" stroke="#4c4c4c"></path></svg>
    </div>
    <div style="width: 100%; height: 100%; overflow-y: auto;">
        <div class="chatContent" ref="chatContent">
            <div v-for="(d, i) in chatHistory" :key="'chat_history' + i" style="width: 100%;">
                <div v-if="d.role == 'user'" class="userBox">
                    <div class="userContent">
                        <div v-if="d.content.length > 1" style="margin-bottom: 10px; cursor: pointer;" @click="showPreview('./Product UI/' + d.content[1].image_url + '.png')">
                            <img :src="'./Product UI/' + d.content[1].image_url + '.png'" alt="" style="width: 100%;">
                        </div>
                        {{ d.content[0].text }}
                    </div>
                    <div class="userIcon">
                        <el-avatar style="width: 30px; height: 30px">
                            <svg t="1722321771335" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5261" width="20" height="20"><path d="M1024.016 959.888s0-174.928-127.792-238.496c-80.88-40.24-49.712-9.456-149.008-50.624-99.28-41.104-122.8-54.544-122.8-54.544l-0.88-94.288s37.184-28.224 48.784-117.392c23.216 6.72 31.072-27.216 32.336-48.896 1.376-20.944 13.728-86.224-14.672-80.4 5.808-43.584 10.368-82.992 8.32-103.856-7.104-73.216-57.728-149.68-185.52-155.264-108.64 5.584-179.168 82.096-186.288 155.312-2.048 20.864 2.128 60.24 7.936 103.904-28.384-5.904-16.16 59.504-14.912 80.432 1.376 21.68 9.056 55.712 32.32 48.992 11.552 89.184 48.736 117.616 48.736 117.616l-0.928 94.8s-23.52 14.352-122.8 55.456c-99.28 41.184-68.144 8.528-149.024 48.752C0 784.992 0 959.888 0 959.888h0.032A48 48 0 0 0 48 1008h928a48 48 0 0 0 48-48l-0.016-0.112h0.032z" fill="#ffffff" p-id="5262"></path></svg>
                        </el-avatar>
                    </div>
                </div>
                <div v-else class="robotBox">
                    <div class="robotIcon">
                        <el-avatar style="width: 30px; height: 30px">
                            <svg width="20" height="20" viewBox="0 0 41 41" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-md" role="img"><text x="-9999" y="-9999">ChatGPT</text><path d="M37.5324 16.8707C37.9808 15.5241 38.1363 14.0974 37.9886 12.6859C37.8409 11.2744 37.3934 9.91076 36.676 8.68622C35.6126 6.83404 33.9882 5.3676 32.0373 4.4985C30.0864 3.62941 27.9098 3.40259 25.8215 3.85078C24.8796 2.7893 23.7219 1.94125 22.4257 1.36341C21.1295 0.785575 19.7249 0.491269 18.3058 0.500197C16.1708 0.495044 14.0893 1.16803 12.3614 2.42214C10.6335 3.67624 9.34853 5.44666 8.6917 7.47815C7.30085 7.76286 5.98686 8.3414 4.8377 9.17505C3.68854 10.0087 2.73073 11.0782 2.02839 12.312C0.956464 14.1591 0.498905 16.2988 0.721698 18.4228C0.944492 20.5467 1.83612 22.5449 3.268 24.1293C2.81966 25.4759 2.66413 26.9026 2.81182 28.3141C2.95951 29.7256 3.40701 31.0892 4.12437 32.3138C5.18791 34.1659 6.8123 35.6322 8.76321 36.5013C10.7141 37.3704 12.8907 37.5973 14.9789 37.1492C15.9208 38.2107 17.0786 39.0587 18.3747 39.6366C19.6709 40.2144 21.0755 40.5087 22.4946 40.4998C24.6307 40.5054 26.7133 39.8321 28.4418 38.5772C30.1704 37.3223 31.4556 35.5506 32.1119 33.5179C33.5027 33.2332 34.8167 32.6547 35.9659 31.821C37.115 30.9874 38.0728 29.9178 38.7752 28.684C39.8458 26.8371 40.3023 24.6979 40.0789 22.5748C39.8556 20.4517 38.9639 18.4544 37.5324 16.8707ZM22.4978 37.8849C20.7443 37.8874 19.0459 37.2733 17.6994 36.1501C17.7601 36.117 17.8666 36.0586 17.936 36.0161L25.9004 31.4156C26.1003 31.3019 26.2663 31.137 26.3813 30.9378C26.4964 30.7386 26.5563 30.5124 26.5549 30.2825V19.0542L29.9213 20.998C29.9389 21.0068 29.9541 21.0198 29.9656 21.0359C29.977 21.052 29.9842 21.0707 29.9867 21.0902V30.3889C29.9842 32.375 29.1946 34.2791 27.7909 35.6841C26.3872 37.0892 24.4838 37.8806 22.4978 37.8849ZM6.39227 31.0064C5.51397 29.4888 5.19742 27.7107 5.49804 25.9832C5.55718 26.0187 5.66048 26.0818 5.73461 26.1244L13.699 30.7248C13.8975 30.8408 14.1233 30.902 14.3532 30.902C14.583 30.902 14.8088 30.8408 15.0073 30.7248L24.731 25.1103V28.9979C24.7321 29.0177 24.7283 29.0376 24.7199 29.0556C24.7115 29.0736 24.6988 29.0893 24.6829 29.1012L16.6317 33.7497C14.9096 34.7416 12.8643 35.0097 10.9447 34.4954C9.02506 33.9811 7.38785 32.7263 6.39227 31.0064ZM4.29707 13.6194C5.17156 12.0998 6.55279 10.9364 8.19885 10.3327C8.19885 10.4013 8.19491 10.5228 8.19491 10.6071V19.808C8.19351 20.0378 8.25334 20.2638 8.36823 20.4629C8.48312 20.6619 8.64893 20.8267 8.84863 20.9404L18.5723 26.5542L15.206 28.4979C15.1894 28.5089 15.1703 28.5155 15.1505 28.5173C15.1307 28.5191 15.1107 28.516 15.0924 28.5082L7.04046 23.8557C5.32135 22.8601 4.06716 21.2235 3.55289 19.3046C3.03862 17.3858 3.30624 15.3413 4.29707 13.6194ZM31.955 20.0556L22.2312 14.4411L25.5976 12.4981C25.6142 12.4872 25.6333 12.4805 25.6531 12.4787C25.6729 12.4769 25.6928 12.4801 25.7111 12.4879L33.7631 17.1364C34.9967 17.849 36.0017 18.8982 36.6606 20.1613C37.3194 21.4244 37.6047 22.849 37.4832 24.2684C37.3617 25.6878 36.8382 27.0432 35.9743 28.1759C35.1103 29.3086 33.9415 30.1717 32.6047 30.6641C32.6047 30.5947 32.6047 30.4733 32.6047 30.3889V21.188C32.6066 20.9586 32.5474 20.7328 32.4332 20.5338C32.319 20.3348 32.154 20.1698 31.955 20.0556ZM35.3055 15.0128C35.2464 14.9765 35.1431 14.9142 35.069 14.8717L27.1045 10.2712C26.906 10.1554 26.6803 10.0943 26.4504 10.0943C26.2206 10.0943 25.9948 10.1554 25.7963 10.2712L16.0726 15.8858V11.9982C16.0715 11.9783 16.0753 11.9585 16.0837 11.9405C16.0921 11.9225 16.1048 11.9068 16.1207 11.8949L24.1719 7.25025C25.4053 6.53903 26.8158 6.19376 28.2383 6.25482C29.6608 6.31589 31.0364 6.78077 32.2044 7.59508C33.3723 8.40939 34.2842 9.53945 34.8334 10.8531C35.3826 12.1667 35.5464 13.6095 35.3055 15.0128ZM14.2424 21.9419L10.8752 19.9981C10.8576 19.9893 10.8423 19.9763 10.8309 19.9602C10.8195 19.9441 10.8122 19.9254 10.8098 19.9058V10.6071C10.8107 9.18295 11.2173 7.78848 11.9819 6.58696C12.7466 5.38544 13.8377 4.42659 15.1275 3.82264C16.4173 3.21869 17.8524 2.99464 19.2649 3.1767C20.6775 3.35876 22.0089 3.93941 23.1034 4.85067C23.0427 4.88379 22.937 4.94215 22.8668 4.98473L14.9024 9.58517C14.7025 9.69878 14.5366 9.86356 14.4215 10.0626C14.3065 10.2616 14.2466 10.4877 14.2479 10.7175L14.2424 21.9419ZM16.071 17.9991L20.4018 15.4978L24.7325 17.9975V22.9985L20.4018 25.4983L16.071 22.9985V17.9991Z" fill="currentColor"></path></svg>
                        </el-avatar>
                        <div class="uxButton" @click="copyToClipboard(d.content[0].text)" style="margin-top: 10px;">
                            <svg t="1723120233317" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4309" width="20" height="20"><path d="M394.666667 106.666667h448a74.666667 74.666667 0 0 1 74.666666 74.666666v448a74.666667 74.666667 0 0 1-74.666666 74.666667H394.666667a74.666667 74.666667 0 0 1-74.666667-74.666667V181.333333a74.666667 74.666667 0 0 1 74.666667-74.666666z m0 64a10.666667 10.666667 0 0 0-10.666667 10.666666v448a10.666667 10.666667 0 0 0 10.666667 10.666667h448a10.666667 10.666667 0 0 0 10.666666-10.666667V181.333333a10.666667 10.666667 0 0 0-10.666666-10.666666H394.666667z m245.333333 597.333333a32 32 0 0 1 64 0v74.666667a74.666667 74.666667 0 0 1-74.666667 74.666666H181.333333a74.666667 74.666667 0 0 1-74.666666-74.666666V394.666667a74.666667 74.666667 0 0 1 74.666666-74.666667h74.666667a32 32 0 0 1 0 64h-74.666667a10.666667 10.666667 0 0 0-10.666666 10.666667v448a10.666667 10.666667 0 0 0 10.666666 10.666666h448a10.666667 10.666667 0 0 0 10.666667-10.666666v-74.666667z" fill="#000000" p-id="4310"></path></svg>
                        </div>
                    </div>
                    <div class="robotContent"  v-loading="d.loadingTag" style="width: 100%;">
                        <v-md-preview :text="d.content[0].text"></v-md-preview>
                    </div>
                </div>
            </div>
        </div>
        <div style="display: flex; position: absolute; bottom: 10px; width: 100%; justify-content: space-between;">
            <el-input v-model="askArea" style="width: calc(100% - 60px)" :autosize="{ minRows: 1, maxRows: 4 }" type="textarea" @keyup.enter.native="submitConversation" placeholder="Please input" />
            <el-button type="primary" plain @click="submitConversation">
                <svg t="1722321124129" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4262" width="20" height="20"><path d="M954.51508497 69.46550967A25.37960888 25.37960888 0 0 0 929.02614893 63.14013037L79.98843448 324.3861081A25.5045542 25.5045542 0 0 0 62.4804084 343.83079268 25.89501006 25.89501006 0 0 0 69.82097276 367.14879599L252.91337363 550.22557959l60.34880479 243.45682471a17.61735323 17.61735323 0 0 0 2.2958789 5.31019511 18.10151807 18.10151807 0 0 0 18.9292834 9.37093184c8.27765683-1.39002187 14.05639864-7.80911016 15.21214717-16.75835068l1.45249453-6.82516231 26.14490156-104.92320674L657.22225362 954.51884141a25.19219003 25.19219003 0 0 0 17.9609537 7.48112695 25.86377373 25.86377373 0 0 0 6.16919678-0.76529268 25.27028086 25.27028086 0 0 0 18.21084609-17.18004287l261.29283223-849.08456895a25.42646338 25.42646338 0 0 0-6.34099745-25.50455419zM352.51076709 622.56917832l-3.95140957 3.77960889-18.53882841 87.08719922-40.85726485-164.81908389 373.49412978-223.34055556z m317.95573799 295.0594251L387.49558203 638.31234482l446.68111201-428.2516125a12.49457695 12.49457695 0 0 0-15.10281914-19.80390409L271.0148917 518.05204472 106.47693652 353.48285323 921.2482751 102.7479377z" fill="#515151" p-id="4263"></path></svg>
            </el-button>
        </div>
    </div>
</template>

<script>
import { useDataStore } from "../stores/counter";

import PreviewVideoPlayer from './utils/PreviewVideoPlayer.vue';
import useClipboard from "vue-clipboard3";
import { ElMessage } from 'element-plus';

export default {
    name: "PCV",
    props: [],
    data() {
        return {
            askArea: '',
            showChatbot: false,
            chatHistory: [],
            chatID: -1,
            previewDialogTag: false,
            previewUrl: ''
        };
    },
    methods: {
        showPreview(url) {
            this.previewDialogTag = !this.previewDialogTag;
            this.previewUrl = url;
        },
        useGeneralChat() {
            const dataStore = useDataStore();

            // this.chatHistory = dataStore.generalChatData;
            dataStore.chatTag = -1;
        },
        async copyToClipboard(data) {
            
            try {
                await useClipboard().toClipboard(data);
                ElMessage({
                    message: "复制成功",
                    type: "success"
                })
            } catch (error) {
                ElMessage({
                    message: "复制失败",
                    type: "error"
                })
            }
        },
        async submitConversation() {
            console.log(this.askArea);
            let now = new Date();
            let timeTag = Math.floor(now.getTime() / 1000);
            this.chatHistory.push({
                role: "user",
                content: [{type: "text", text: this.askArea}],
                loadingTag: false,
                time: timeTag
            });
            this.chatHistory.push({
                role: "assistant",
                content: [{type: "text", text: ""}],
                loadingTag: true
            })
            this.askArea = "";
            let chatContent = this.$refs.chatContent;
            
            this.$nextTick(() => {
                chatContent.scrollTo({
                    top: chatContent.scrollHeight,
                    behavior: "smooth"
                })
            })
            const dataStore = useDataStore();
            let data;
            try {
                if (dataStore.chatTag == -1) {
                    data = await dataStore.getGeneralChat({
                        content: this.askArea,
                        history: this.chatHistory
                    });
                } else {
                    data = await dataStore.solutionChat({
                        history: this.chatHistory
                    })
                }
                timeTag = Math.floor(now.getTime() / 1000);
                this.chatHistory[this.chatHistory.length - 1] = {
                    role: "assistant",
                    content: [{type: "text", text: data.data.response}],
                    loadingTag: false,
                    time: timeTag,
                    editTag: false
                };
                if (dataStore.chatTag == -1) {
                    dataStore.generalChatData = this.chatHistory;
                }
            } catch (error) {
                console.error(error);
                this.chatHistory.slice(0, -2);

                ElMessage({
                    message: "Oops，出错了，请重新输入",
                    type: "warning"
                })
            }
            this.$nextTick(() => {
                chatContent.scrollTo({
                    top: chatContent.scrollHeight,
                    behavior: "smooth"
                })
            })
            console.log(data);
        }
    },
    components: { PreviewVideoPlayer },
    created() {},
    computed: {},
    mounted() {
        const dataStore = useDataStore();

        dataStore.$subscribe((mutations, states) => {
            this.showChatbot = dataStore.showChatbot;
            // if (this.chatID == -1) {
            //     dataStore.generalChatData = this.chatHistory;
            // }
            if (this.chatID != dataStore.chatTag) {
                this.chatID = dataStore.chatTag;
                if (dataStore.chatTag == -1){
                    this.chatHistory = dataStore.generalChatData;
                } else {
                    this.chatHistory = dataStore.chatData
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

/*
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2022-09-17 23:36:36
 * @LastEditTime: 2023-02-02 15:02:39
 */
import {
    fetchAllData,
    fetchHello, uploadData, queryRecommendation, queryNewTag, saveData, tagOptimize
} from "../service/module/dataService";
import {
    ref,
    computed
} from "vue";
import {
    defineStore
} from "pinia";

// export const useCounterStore = defineStore("counter", {
//   const count = ref(0);
//   const doubleCount = computed(() => count.value * 2);
//   function increment() {
//     count.value++;
//   }

//   return { count, doubleCount, increment };
// });

export const useDataStore = defineStore("dataStore", {
    state: () => {
        return {
            msg: 'Hello, Vue SQ',
            categorySource: [],
            selectShowLevel: 1,
            noneDisabledTag: {},
            emptyTag: 0,
            showTagList: [],
            isShowTagList: false,
            select_video: '',
            select_dataset: '',
            noneDisabledTag: {},
            all_data: [],
            currentPlayTime: 0,
            leftShow: 1,
            video_list: [],
            time_list: [],
            reuse_list: [],
            changeTag_list: [],
            dataSelect: -1,
            previewSelect: 0,
            select_all: 1
        }
    },
    actions: {
        fetchHello() {
            const st = new Date();
            fetchHello({}, resp => {
                this.msg = resp;
                console.log("Fetch Hello Time: ", st - new Date());
            })
        },
        uploadData(param) {
            const st = new Date();
            uploadData(param, resp => {
                this.profileData = resp;
                console.log("Uploading File: ", new Date() - st);
            })
        },
        fetchAllData(param) {
            const st = new Date();
            fetchAllData(param, resp => {
                this.system_data = resp.data;
                console.log("Fetch Data: ", new Date() - st);
            });
        },
        async queryRecommendation(param) {
            const st = new Date();
            const data = await queryRecommendation(param);
            return data;
        },
        async queryNewTag(param) {
            const data = await queryNewTag(param);
            return data;
        },
        async saveData(param) {
            const data = await saveData(param);
            return data;
        },
        async tagOptimize(param) {
            const data = await tagOptimize(param);
            return data;
        }
    }
})
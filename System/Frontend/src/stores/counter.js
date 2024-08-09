/*
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2022-09-17 23:36:36
 * @LastEditTime: 2023-02-02 15:02:39
 */
import {
    fetchAllData,
    fetchHello, uploadData, generalChat,
    addMetric,
    solutionChat,
    generatePoint,
    evaluatePoint,
    save,
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
            showChatbot: false,
            generalChatData: [],
            chatData: [],
            chatTag: -1,
            selectProblem: [],
            problemList: [],
            startingPointList: [],
            solutionList: [],
            criterionList: [],
            interactionList: [],
            eyeTrackList: [],
        }
    },
    actions: {
        saveData() {
            const st = new Date();
            const data = {
                "time": st,
                "solutionList": this.solutionList,
                "startingPointList": this.startingPointList,
                // "criterionList": this.criterionList,
                "generalChatData": this.generalChatData,
                "interactionList": this.interactionList,
                "eyeTrackList": this.eyeTrackList
            }
            return data;
        },
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
        async getGeneralChat(param) {
            const data = await generalChat(param);
            return data;
        },
        async addMetric(param) {
            const data = await addMetric(param);
            return data;
        },
        async solutionChat(param) {
            const data = await solutionChat(param);
            return data;
        },
        async generatePoint(param) {
            const data = await generatePoint(param);
            return data;
        },
        async evaluatePoint(param) {
            const data = await evaluatePoint(param);
            return data;
        },
        async save(param) {
            const data = await save(param);
            return data;
        }
    }
})
<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-02-01 19:32:17
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-02-07 15:36:38
-->
<!--
 *                        _oo0oo_
 *                       o8888888o
 *                       88" . "88
 *                       (| -_- |)
 *                       0\  =  /0
 *                     ___/`---'\___
 *                   .' \\|     |// '.
 *                  / \\|||  :  |||// \
 *                 / _||||| -:- |||||- \
 *                |   | \\\  - /// |   |
 *                | \_|  ''\---/''  |_/ |
 *                \  .-\__  '-'  ___/-. /
 *              ___'. .'  /--.--\  `. .'___
 *           ."" '<  `.___\_<|>_/___.' >' "".
 *          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
 *          \  \ `_.   \_ __\ /__ _/   .-` /  /
 *      =====`-.____`.___ \_____/___.-`___.-'=====
 *                        `=---='
 * 
 * 
 *      ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 * 
 *            佛祖保佑     永不宕机     永无BUG
 -->

<template>
    <div class="frameworkBody">
        <div style="height: 80px;">
            <div style="text-align: left; font-size: 24px; color: white; font-weight: bold; justify-content: space-between; display: flex;">
                推荐设置
                <span>
                                                <el-button type="primary" @click="showProblem = !showProblem">
                                                    <svg t="1709214608225" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="15144" width="20" height="20" transform="rotate(180)"><path d="M117.418667 192a32 32 0 0 1 31.744 27.648l0.256 4.352L149.333333 778.837333a32 32 0 0 1-63.701333 4.352L85.333333 778.837333 85.418667 224a32 32 0 0 1 32-32z m550.186666 76.970667l3.114667-3.584a32 32 0 0 1 41.642667-3.114667l3.584 3.114667 213.205333 213.205333a32 32 0 0 1 3.114667 41.642667l-3.114667 3.626666-213.162667 213.461334a32 32 0 0 1-48.384-41.642667l3.072-3.584 158.336-158.592H245.461333a32 32 0 0 1-31.701333-27.605333l-0.298667-4.352a32 32 0 0 1 27.648-31.701334l4.352-0.298666 584.106667-0.042667L670.72 310.613333a32 32 0 0 1-3.114667-41.642666l3.114667-3.584-3.114667 3.584z" fill="#ffffff" p-id="15145"></path></svg>
                                                </el-button>
                                            </span>
            </div>
            <el-switch v-model="recommendTag" class="mb-2" style="--el-switch-on-color: #409eff; --el-switch-off-color: #409eff" active-text="二级标签推荐" inactive-text="一级标签推荐" />
        </div>
        <div ref="wholeWidth" id="problem_tag" style="height: calc(100% - 80px)">
            <el-dialog v-model="addPoint" :title="'添加' + add_tag_level + '级标签'" width="15%" height="100px" :append-to="'#problems_tag'" :modal="false" :class="'add_dialog'">
                <div v-loading="loadingTag" element-loading-background="#454647" style="width: 100%; height: 170px; margin-top: -10px;">
    
                    <h3 style="color: white; text-align: left;">标签名称</h3>
                    <span>
                                            <el-input v-model="tag_name" placeholder="Please input"  :input-style="{ 'font-size': '18px' }"/>
                                        </span>
                    <h3 style="color: white; text-align: left;">标签定义</h3>
                    <span>
                                            <el-input v-model="tag_description"  :autosize="{ minRows: 3, maxRows: 3 }" type="textarea" placeholder="Please input" />
                                        </span>
                </div>
                <div style="padding: 20px 0px 10px 0px;">
                    <el-button type="primary" @click="addTag()">确定</el-button>
                    <el-button @click="addPoint = false">取消</el-button>
                </div>
            </el-dialog>
            <el-dialog v-model="optimizeShowTag" :title="'标签优化'" width="22%" height="100px" :append-to="'#problems_tag'" :modal="false" :class="'optimize_dialog'">
                <div v-loading="optimizeLoading" element-loading-background="#454647" style="width: 100%; height: 400px; margin-top: -10px; overflow-y: auto;">
                    <div v-for="(d, i) in calcUnion" :keys="'union_tag_' + i" style="width: 100%; background-color: rgba(0, 0, 0, .3); padding: 10px 10px; border-radius: 5px; margin-top: 10px;">
                        <h2 style="color: white; text-align: left;">{{ '建议合并以下' + (d.level == 1 ? '一' : '二') + '级标签' }}</h2>
                        <h3 style="color: white; text-align: left;">原始标签</h3>
                        <div style="display: flex; flex-wrap: wrap;">
                            <div v-for="(dd, ii) in d.tag_detail" :key="'tag_detail_' + ii" class="align-class" :style="{ backgroundColor: colorMap[dd.id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px', cursor: 'pointer', 'color': 'white' }"
                                @click="selectTag(info_data.second_tag[d], dd.cnt, 0, dd.id)">
                                <div :style="{ backgroundColor: colorMap[dd.id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: dd.level == 1 ? '100px' : '0px' }">
    
                                </div>
                                <div>
                                    {{ dd.label }}
                                </div>
                            </div>
                        </div>
                        <h3 style="color: white; text-align: left; margin-top: 10px;">新标签名称</h3>
                        <span>
                                                            <el-input v-model="d.combined_name" placeholder="Please input" :input-style="{ 'font-size': '18px' }" />
                                                        </span>
                        <h3 style="color: white; text-align: left; margin-top: 10px;">新标签定义</h3>
                        <span>
                                                            <el-input v-model="d.combined_label" :autosize="{ minRows: 4, maxRows: 4 }" type="textarea"
                                                    placeholder="Please input" />
                                                        </span>
                        <div style="margin-top: 15px">
    
                            <el-button type="primary" @click="unionTag(d, 1)">确定</el-button>
                            <el-button type="danger" @click="unionTag(d, 0)">取消</el-button>
                        </div>
                    </div>
                </div>
                <!-- <div style="padding: 20px 0px 10px 0px;">
                                                <el-button @click="addPoint = false">取消</el-button>
                                                <el-button type="primary" @click="addTag()">确定</el-button>
                                            </div> -->
            </el-dialog>
            <div style="text-align: left; font-size: 24px; color: white; font-weight: bold; height: 40px; display: flex; justify-content: space-between;">
                <span style="display: flex;">
                                            <span>可用性问题标签</span> &nbsp;
                <!-- <span>
                                                    <el-popover
                                                        placement="bottom"
                                                        title="标签解释"
                                                        :width="elWidth * .8"
                                                        trigger="click"
                                                        :popper-class="'tag_description'"
                                                    >
                                                        <template #reference>
                                                        <a><svg t="1708679239889" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1495" width="30" height="35"><path d="M536 480v192a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16V480a16 16 0 0 1 16-16h16a16 16 0 0 1 16 16z m-32-128h16a16 16 0 0 1 16 16v32a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16v-32a16 16 0 0 1 16-16z m8 448c159.056 0 288-128.944 288-288s-128.944-288-288-288-288 128.944-288 288 128.944 288 288 288z m0 48c-185.568 0-336-150.432-336-336s150.432-336 336-336 336 150.432 336 336-150.432 336-336 336z" fill="#ffffff" p-id="1496"></path></svg></a>
</template>
                    <div :style="{ height: (elHeight * .8) + 'px', fontSize: '20px', lineHeight: 1.5}">
                        <div style="color: #777;">
                            灰色字体代表当前视频中未出现此标签
                        </div>
                        <div style="overflow: auto; height: calc(100% - 30px);">
                        <div v-for="(data, i) in dataSource" :key="'description_' + i" :style="{color: data.disabled == true ? '#777' : 'white'}">
                            <div :style="{ display: 'flex', alignItems: 'center'}"><div :style="{float: 'left', 'margin': '0px 10px 0px 0px', width: '20px', height: '20px', 'background-color': colorMap[data.id], 'borderRadius': data.level == 1 ? '20px' : '0px', }"></div> {{ (i + 1) + '   ' + data.label }}</div>
                            <div style="font-size: 18px; padding-right: 10px;">
                                {{ data.description }}
                            </div>
                            <div v-for="(child, j) in data.children" :style="{ color: child.disabled == true ? '#777' : 'white'}">
                                <div :style="{ display: 'flex', alignItems: 'center'}"><div :style="{float: 'left', 'margin': '0px 10px 0px 0px', width: '20px', height: '20px', 'background-color': colorMap[child.id], 'borderRadius': child.level == 1 ? '20px' : '0px',}"></div> {{ (i + 1) + '-' + (j + 1) +  '   ' + child.label }}</div>
                                <div style="font-size: 18px; padding-right: 10px;">
                                    {{ child.description }}
                                </div>

                            </div>
                        </div>
                    </div>
                    </div>
                </el-popover>
                </span> -->
            </span>
            <span>
                <el-button type="primary" @click="showOptimize()">标签优化</el-button>
            </span>
            </div>
            <div style="text-align: left; padding-left: 24px; height: 45px;width: 100%;">
                <span>
                        <el-checkbox label="全选" size="large" v-model="selectAll" />
                    </span>
                <span style=" position: absolute;top: 12px; right: 0px;">
                        <el-button style="margin-top: -10px;" type="primary" @click="showDialog(1, dataSource)">添加一级标签</el-button>
                    </span>
            </div>
            <div style="width: 100%; height: calc(100% - 85px); overflow-y: auto;">
                <el-tree ref="treeRef" v-if="showTree" :data="dataSource" show-checkbox node-key="id" :default-expand-all="expandTag" :expand-on-click-node="false" :props="defaultProps" @check="checkStatus">
<template #default="{ node, data }">
    <span class="custom-tree-node">
        <span :style="{color: data.disabled == true ? '#777' : 'white', display: 'flex', alignItems: 'center', paddingTop: '0px'}"> 
            <div :style="{'margin': '0px 10px 0px 0px', width: '20px', height: '20px', 'background-color': colorMap[data.id], 'borderRadius': node.level == 1 ? '20px' : '0px', }"></div> <div style="margin-top: 0px; margin-right: 10px;">{{ node.label }}</div>
            <div style="margin-top: 7px;">
            <el-tooltip
                class="box-item"
                effect="dark"
                placement="top"
            >
            <template #content> <div style="width: 150px; font-size: 16px;">{{ data.description }}</div> </template>
            <a><svg t="1708679239889" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1495" width="30" height="35"><path d="M536 480v192a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16V480a16 16 0 0 1 16-16h16a16 16 0 0 1 16 16z m-32-128h16a16 16 0 0 1 16 16v32a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16v-32a16 16 0 0 1 16-16z m8 448c159.056 0 288-128.944 288-288s-128.944-288-288-288-288 128.944-288 288 128.944 288 288 288z m0 48c-185.568 0-336-150.432-336-336s150.432-336 336-336 336 150.432 336 336-150.432 336-336 336z" fill="#ffffff" p-id="1496"></path></svg></a>
            </el-tooltip>
            </div>
        </span>
    <span style="padding-top: 5px;">
        <a v-if="node.level == 1" @click="showDialog(2, data)"> <svg t="1706082110613" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4198" width="20" height="20"><path d="M832 1024H192c-106.048 0-192-86.016-192-192V192a192 192 0 0 1 192-192h640a192 192 0 0 1 192 192v640c0 105.984-85.952 192-192 192z m64-832a64 64 0 0 0-64-64H192a64 64 0 0 0-64 64v640c0 35.392 28.608 64 64 64h640c35.392 0 64-28.608 64-64V192z m-192 384h-128v128c0 35.392-28.608 64-64 64s-64-28.608-64-64v-128h-128a64 64 0 1 1 0-128h128v-128a64 64 0 1 1 128 0v128h128a64 64 0 1 1 0 128z" fill="white" p-id="4199"></path></svg> </a>
    </span>
    </span>
</template>
                </el-tree>
            </div>
        </div>
    </div>
            <Transition name="el-fade-in-linear">
    <div v-show="showProblem" class="slide-out" style="height: 100%; width: 100%; position: absolute; top: 0px; background-color: #222c44; border-radius: 5px; z-index: 1000; padding: 10px 10px 5px 10px;">
        <div style="text-align: left; font-size: 24px; color: white; font-weight: bold; justify-content: space-between; display: flex; height: 40px;">
                可用性问题列表
                <span>
                    <el-button type="primary" @click="showProblem = !showProblem">
                        <svg t="1709214608225" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="15144" width="20" height="20" transform="rotate(0)"><path d="M117.418667 192a32 32 0 0 1 31.744 27.648l0.256 4.352L149.333333 778.837333a32 32 0 0 1-63.701333 4.352L85.333333 778.837333 85.418667 224a32 32 0 0 1 32-32z m550.186666 76.970667l3.114667-3.584a32 32 0 0 1 41.642667-3.114667l3.584 3.114667 213.205333 213.205333a32 32 0 0 1 3.114667 41.642667l-3.114667 3.626666-213.162667 213.461334a32 32 0 0 1-48.384-41.642667l3.072-3.584 158.336-158.592H245.461333a32 32 0 0 1-31.701333-27.605333l-0.298667-4.352a32 32 0 0 1 27.648-31.701334l4.352-0.298666 584.106667-0.042667L670.72 310.613333a32 32 0 0 1-3.114667-41.642666l3.114667-3.584-3.114667 3.584z" fill="#ffffff" p-id="15145"></path></svg>
                    </el-button>
                </span>
            </div>
        <!-- <div style="height: calc(100% - 50px); width: 100%; overflow-y: auto; padding-right: 8px; margin-top: 10px;">
            <div class="problem-card" v-for="(d, i) in calcInfoData" :key="'problem_card_' + i">
                <div class="problem-card-time">
                    {{ (parseInt(d.time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(d.time / 60).toString().padStart(2, '0')) + ':' + ((d.time % 60).toString().padStart(2, '0')) }}
                </div>
                <div class="problem-card-description">
                    {{ d.description }}
                </div>
            </div>
        </div> -->

        <div style="height: calc(100% - 50px); width: 100%; overflow-y: auto; padding-right: 8px; margin-top: 10px;">
            <div class="problem-card" v-for="(d, i) in calcInfoData" :key="'problem_card_' + i">
                <!-- <div class="problem-card-icon"><svg v-if="d.status == 2" t="1709486366176" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4381" width="20" height="20"><path d="M512 0C229.23 0 0 229.23 0 512s229.23 512 512 512 512-229.23 512-512S794.77 0 512 0z m80 768a80 80 0 0 1-160 0v-32a80 80 0 0 1 160 0v32z m0-256a80 80 0 0 1-160 0V256a80 80 0 0 1 160 0v256z" fill="#fda33e" p-id="4382"></path></svg>
                    <svg v-else-if="d.status == 1" t="1709486728584" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7086" width="20" height="20"><path d="M731.733333 294.4L450.133333 631.466667l-134.4-134.4-53.333333 53.333333 194.133333 194.133333L789.333333 345.6l-57.6-51.2zM512 992C247.466667 992 32 776.533333 32 512S247.466667 32 512 32 992 247.466667 992 512 776.533333 992 512 992z" p-id="7087" fill="#00FF7F"></path></svg></div> -->
                <div class="problem-card-time">
                    {{ (parseInt(d.time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(d.time / 60).toString().padStart(2, '0')) + ':' + ((d.time % 60).toString().padStart(2, '0')) }}
                </div>
                <div class="problem-card-description">
                    {{ d.description }}
                </div>
            </div>
        </div>
        
    </div>
            </Transition>
</template>

<script>
import { useDataStore } from "@/stores/counter";

export default {
    name: "PCV",
    props: [],
    data() {
        return {
            optimizeShowTag: false,
            optimizeLoading: false,
            showProblem: 0,
            showTable: 0,
            elHeight: 0,
            all_data: [],
            elWidth: 0,
            select_video: '',
            addPoint: false,
            expandTag: false,
            loadingTag: false,
            showTree: true,
            selectAll: true,
            tag_name: "",
            tag_description: "",
            add_tag_level: "",
            id_cnt: 12,
            selectData: [],
            colorMap: ['', '#F6D962', '#D5A138', '#EF753A', '#F08F70', '#EB7D81', '#B76E90', '#986EA4', '#9286B3', '#8796BC', '#A3BFCE', '#B4D3B4', '#D1EFFF', '#89D1FF', '#1B90FF', '#0057D2', '#002A86', '#E2D8FF', '#B894FF', '#7858FF', '#470CED', '#1C0C6E', '#FFDCF3', '#FF8AF0', '#F31DED', '#A100C2', '#510080', '#FFDCE8', '#FEADC8', '#FA4F96', '#BA066C', '#71014B', '#FFD5EA', '#FF8CB2', '#EE3939', '#AA0808', '#5A0404', '#FFF3B8', '#FFC933', '#E76500', '#A93E00', '#6D1900', '#EBF5CB', '#97DD40', '#36A41D', '#256F3A', '#164323', '#C2FCEE', '#2CE0BF', '#049F9A', '#046C7A', '#02414C', '#EAECEE', '#A9B4BE', '#5B738B', '#354A5F', '#1A2733'],
            dataSource: [],
            recommendTag: false,
            defaultProps: {
                children: 'children',
                label: 'label',
                disabled: 'is_dis'
            },
            showTagList: [],
            changeTag: false,
            noneDisabledTag: {},
            info_data: [],
            union_data: []
        };
    },
    computed: {
        calcInfoData() {
            this.info_data.sort((a, b) => a.time - b.time);
            return this.info_data.filter(d => d.status != 3 && d.status != 4 && d.repeat_status == 1)
        },
        calcUnion() {
            let union_data = [];
            for (let i in this.union_data) {
                // if (this.union_data[i].parent != "" && this.union_data[i].status == -1 && this.union_data[this.union_data[i].parent].status == 1) {
                //     this.union_data[i].status = 0;
                // }
                if (this.union_data[i].status == 0) {
                    union_data.push(this.union_data[i]);
                }
            }
            return union_data;
        }
    },
    methods: {
        unionTag(data, tag) {
            if (tag == 1) {
                data.status = 1;
                console.log(data);
                let union_tag = new Array();
                let union_data = data;
                // for (let i in union_data) {
                for (let j in union_data.tag_info) {
                    let t_tag = [];
                    let l_1_pos = -1;
                    let l_2_pos = -1;
                    let unique_id = union_data.tag_info[j].id;
                    for (let k in this.dataSource) {
                        if (this.dataSource[k].id == unique_id) {
                            t_tag = this.dataSource[k];
                            l_1_pos = k;
                        }
                        for (let kk in this.dataSource[k].children) {
                            if (this.dataSource[k].children[kk].id == unique_id) {
                                t_tag = this.dataSource[k].children[kk];
                                l_1_pos = parseInt(k);
                                l_2_pos = parseInt(kk);
                            }
                        }
                    }
                    union_tag.push({ tag: t_tag, level_1: parseInt(l_1_pos), level_2: parseInt(l_2_pos) });
                }
                // }
                let union_obj = new Object();
                // if (data.level == 1) {
                console.log(union_tag)
                let main_tag = union_tag[0];
                union_tag.splice(0, 1);
                console.log(main_tag)
                for (let i in union_tag) {
                    let tmp = union_tag[i].tag;
                    union_obj[tmp.id] = main_tag.tag.id;
                    for (let j in tmp.children) {
                        main_tag.tag.children.push(tmp.children[j]);
                    }
                    main_tag.tag.label = data.combined_name;
                    main_tag.tag.description = data.combined_label;
                    // console.log(tmp);
                    if (union_tag[i].level_2 == -1) {
                        this.dataSource.splice(union_tag[i].level_1, 1);
                    } else {
                        this.dataSource[union_tag[i].level_1].children.splice(union_tag[i].level_2, 1);
                    }
                }
                let tag_obj = new Object();
                for (let i in this.dataSource) {
                    if (typeof union_obj[this.dataSource[i].id] == 'undefined') {
                        tag_obj[this.dataSource[i].id] = {
                            level: 1,
                            tag: parseInt(i) + 1,
                            sec_tag: -1
                        };
                        this.dataSource[i].l_id = parseInt(i) + 1;
                        for (let j in this.dataSource[i].children) {
                            if (typeof union_obj[this.dataSource[i].children[j].id] == 'undefined') {
                                tag_obj[this.dataSource[i].children[j].id] = {
                                    level: 2,
                                    tag: parseInt(i) + 1,
                                    sec_tag: parseInt(j) + 1
                                };
                                this.dataSource[i].children[j].cnt = parseInt(j) + 1;
                            }
                        }
                    }
                }

                for (let p in this.all_data) {
                    for (let i in this.all_data[p].info) {
                        let tmp = this.all_data[p].info[i];
                        let tag_t = [];
                        let sec_tag_t = {};
                        for (let kk in tmp.unique_tag) {
                            let k = tmp.unique_tag[kk];
                            if (typeof union_obj[tmp.unique_tag[kk]] != 'undefined') {
                                k = union_obj[tmp.unique_tag[kk]];
                                let u_index = tmp.unique_tag.indexOf(union_obj[tmp.unique_tag[kk]]);
                                if (u_index != -1) {
                                    tmp.unique_tag.splice(kk, 1);
                                } else {
                                    tmp.unique_tag[kk] = union_obj[tmp.unique_tag[kk]];
                                }
                            }
                            if (tag_t.indexOf(tag_obj[k].tag) == -1) {
                                tag_t.push(tag_obj[k].tag);
                            }
                            if (typeof sec_tag_t[tag_obj[k].tag] == 'undefined') {
                                sec_tag_t[tag_obj[k].tag] = [];
                            }
                            if (tag_obj[k].sec_tag != -1) {
                                sec_tag_t[tag_obj[k].tag].push(tag_obj[k].sec_tag);
                            }
                        }
                        tmp.tag = tag_t;
                        tmp.second_tag = sec_tag_t;

                        let default_tag_t = [];
                        let default_sec_tag_t = {};
                        for (let kk in tmp.default.unique_tag) {
                            let k = tmp.default.unique_tag[kk];
                            if (typeof union_obj[tmp.default.unique_tag[kk]] != 'undefined') {
                                k = union_obj[tmp.default.unique_tag[kk]];
                                let u_index = tmp.default.unique_tag.indexOf(union_obj[tmp.unique_tag[kk]]);
                                if (u_index != -1) {
                                    tmp.default.unique_tag.splice(kk, 1);
                                } else {
                                    tmp.default.unique_tag[kk] = union_obj[tmp.unique_tag[kk]];
                                }
                            }
                            if (default_tag_t.indexOf(tag_obj[k].tag) == -1) {
                                default_tag_t.push(tag_obj[k].tag);
                            }
                            if (typeof default_sec_tag_t[tag_obj[k].tag] == 'undefined') {
                                default_sec_tag_t[tag_obj[k].tag] = [];
                            }
                            if (default_tag_obj[k].sec_tag != -1) {
                                default_sec_tag_t[tag_obj[k].tag].push(tag_obj[k].sec_tag);
                            }
                        }
                        tmp.default.tag = default_tag_t;
                        tmp.default.second_tag = default_sec_tag_t;
                    }
                }
                // }
            }
            if (tag == 0) {
                data.status = 2;
            }
            for (let i in this.union_data) {
                if (this.union_data[i].parent != "" && this.union_data[i].status == -1 && this.union_data[this.union_data[i].parent].status == 1) {
                    this.union_data[i].status = 0;
                }
            }
            let z_cnt = 0;
            for (let i in this.union_data) {
                if (this.union_data[i].status == 0) {
                    z_cnt++;
                }
            }
            if (z_cnt == 0) this.optimizeShowTag = !this.optimizeShowTag;
        },
        async showOptimize() {
            this.optimizeShowTag = !this.optimizeShowTag;
            // console.log(tag_info);
            this.optimizeLoading = true;
            const dataStore = useDataStore();
            const data = await dataStore.tagOptimize({
                category: this.dataSource
            });
            this.optimizeLoading = false;
            console.log(data);
            
            let union_data = data.data['change_list'];
            for (let i in union_data) {
                union_data[i]['tag_detail'] = [];
                for (let j in union_data[i].tag_info) {
                    let t_tag = [];
                    let unique_id = union_data[i].tag_info[j].id;
                    for (let k in this.dataSource) {
                        if (this.dataSource[k].id == unique_id) {
                            t_tag = this.dataSource[k];
                            break;
                        }
                        for (let kk in this.dataSource[k].children) {
                            if (this.dataSource[k].children[kk].id == unique_id) {
                                t_tag = this.dataSource[k].children[kk];
                                break;
                            }
                        }
                    }
                    union_data[i]['tag_detail'].push(t_tag);
                }
            }
            // this.union_data = Object.values(union_data);
            this.union_data = union_data;
            // console.log(this.union_data);

        },
        translate(x, y, deg) {
            return `translate(${x}, ${y}) rotate(${deg})`;
        },
        checkStatus() {
            let showTagList = [...this.$refs.treeRef.getCheckedKeys(), ...this.$refs.treeRef.getHalfCheckedKeys()];
            const dataStore = useDataStore();
            dataStore.showTagList = showTagList;
            this.showTagList = showTagList;
        },
        showDialog(tag_type, data) {
            this.tag_name = "";
            this.tag_description = "";
            this.addPoint = true;
            this.selectData = data;

            if (tag_type == 1) {
                this.add_tag_level = '一';
            } else {
                this.add_tag_level = '二';
            }
        },
        addTag() {
            let id_cnt = -1;
            for (const d of this.dataSource) {
                id_cnt = Math.max(id_cnt, d.id);
                for (const dd of d.children) {
                    id_cnt = Math.max(id_cnt, dd.id);
                }
            }
            id_cnt += 1;

            // // this.id_cnt++;
            // let jsonData = {
            //     tag: this.tag_name,
            //     id: id_cnt,
            //     parent_id: this.add_tag_level == '一' ? 0 : this.selectData.id,
            //     level: this.add_tag_level == '一' ? 1 : 2,
            //     category: this.dataSource,
            //     info: this.all_data,
            //     test: 0
            // };
            this.loadingTag = true;
            // const dataStore = useDataStore();
            // const data = await dataStore.queryNewTag(jsonData);
            // console.log(data);
            // let new_data = data.data.info;
            // for (let i in this.all_data) {
            //     for (let j in this.all_data[i].info) {
            //         this.all_data[i].info[j].tag = new_data[i].info[j].tag;
            //         this.all_data[i].info[j].second_tag = new_data[i].info[j].second_tag;
            //     }
            // }
            // this.addPoint = false;
            if (this.add_tag_level == '一') {
                let l_id_cnt = this.dataSource.length + 1;
                this.selectData.push({
                    id: id_cnt,
                    l_id: l_id_cnt,
                    level: 1,
                    label: this.tag_name,
                    description: this.tag_description,
                    disabled: false,
                    children: []
                })
            } else {
                let cnt = this.selectData.children.length + 1;
                this.selectData.children.push({
                    id: id_cnt,
                    l_id: 1,
                    cnt: cnt,
                    level: 2,
                    label: this.tag_name,
                    description: this.tag_description,
                    disabled: false,
                    children: []
                })
            }
            this.noneDisabledTag = this.calcDisabledData(this.all_data);
            this.addPoint = false;

            this.loadingTag = false;
        },
        calcDisabledData(data) {
            let noneDisabledTag = {};
            for (const i in data) {
                if (this.select_video == '' || i == this.select_video) {
                    for (const d of data[i].info) {
                        for (const t of d.tag) {
                            let t1 = this.dataSource[t - 1].id;
                            if (typeof noneDisabledTag[t1] == 'undefined') {
                                noneDisabledTag[t1] = 0;
                            }
                            noneDisabledTag[t1]++;
                            if (typeof d.second_tag[t] != 'undefined') {
                                for (const st of d.second_tag[t]) {
                                    let st1 = this.dataSource[t - 1].children[st - 1].id;
                                    if (typeof noneDisabledTag[st1] == 'undefined') {
                                        noneDisabledTag[st1] = 0;
                                    }
                                    noneDisabledTag[st1]++;
                                }
                            }
                        }
                    }
                }
            }
            // console.log(noneDisabledTag)
            return noneDisabledTag;
        }
    },
    created() {},
    updated() {

    },
    mounted() {
        this.elWidth = this.$refs.wholeWidth.offsetWidth;
        this.elHeight = this.$refs.wholeWidth.offsetHeight;
        const dataStore = useDataStore();
        this.dataSource = dataStore.categorySource;
        let showTagList = [];
        for (const d of this.dataSource) {
            showTagList.push(d.id);
        }
        this.$refs.treeRef.setCheckedKeys(showTagList);
        this.showTagList = showTagList;
        dataStore.showTagList = showTagList;
        this.select_video = dataStore.select_video;
        this.all_data = dataStore.all_data;
        this.noneDisabledTag = this.calcDisabledData(this.all_data);
        /**
         * @description: watch the data changes in the store
         * @return {*}
         */
        dataStore.$subscribe((mutations, state) => {
            this.dataSource = state.categorySource;
            this.select_video = dataStore.select_video;
            this.all_data = dataStore.all_data;
            this.noneDisabledTag = this.calcDisabledData(this.all_data);
            if (this.selectAll) {
                let showTagList = [];
                for (const d of this.dataSource) {
                    showTagList.push(d.id);
                }
                this.$refs.treeRef.setCheckedKeys(showTagList);
                this.showTagList = showTagList;
            }
        });
    },
    watch: {
        select_video: {
            handler() {
                console.log(this.select_video)
                this.info_data = this.all_data[this.select_video]['info'];
            }
        },
        noneDisabledTag: {
            handler() {
                for (const i in this.dataSource) {
                    if (this.noneDisabledTag[this.dataSource[i].id] > 0) {
                        this.dataSource[i].disabled = false;
                    } else {
                        this.dataSource[i].disabled = true;
                    }
                    for (const j in this.dataSource[i].children) {
                        if (this.noneDisabledTag[this.dataSource[i].children[j].id] > 0) {
                            this.dataSource[i].children[j].disabled = false;
                        } else {
                            this.dataSource[i].children[j].disabled = true;
                        }
                    }
                }
            },
            deep: true
        },
        recommendTag: {
            handler() {
                const dataStore = useDataStore();
                this.showTree = false;
                if (this.recommendTag == true) {
                    dataStore.selectShowLevel = 2;
                    this.expandTag = true;
                } else {
                    dataStore.selectShowLevel = 1;
                    this.expandTag = false;
                }
                let showTagList = [...this.$refs.treeRef.getCheckedKeys(), ...this.$refs.treeRef.getHalfCheckedKeys()];

                dataStore.showTagList = showTagList;
                this.showTagList = showTagList
                this.$nextTick(() => {
                    this.showTree = true;
                    this.$nextTick(() => {
                        for (let i in this.showTagList) {
                            this.$refs.treeRef.setChecked(this.showTagList[i], true, true);
                        }
                    })
                })
            }
        },
        selectAll: {
            handler() {
                const dataStore = useDataStore();
                let showTagList = [];
                if (this.selectAll) {
                    for (const d of this.dataSource) {
                        showTagList.push(d.id);
                    }
                    this.$refs.treeRef.setCheckedKeys(showTagList);
                    showTagList = [...this.$refs.treeRef.getCheckedKeys(), ...this.$refs.treeRef.getHalfCheckedKeys()];
                    dataStore.select_all = true;
                } else {
                    this.$refs.treeRef.setCheckedNodes([], false);
                    dataStore.select_all = false;
                }
                this.showTagList = showTagList;
                dataStore.showTagList = showTagList;
            }
        }
    },
};
</script>

<style>
.slide-enter-active,
.slide-leave-active {
    transition: transform 4s;
}

.slide-enter,
.slide-leave-to {
    transform: translateX(100%);
}

.slide-leave,
.slide-enter-to {
    transform: translateX(0);
}

.problem-card {
    width: 100%;
    /* height: 10px; */
    margin-bottom: 10px;
    padding: 10px 10px 10px 20px;
    border-radius: 5px;
    background-color: rgba(0, 0, 0, .3);
    display: flex;
    justify-content: space-between;
}

.problem-card-icon {
    width: 30px;
    padding-top: 3px;
}

.problem-card-time {
    font-size: 18px;
    color: white;
    width: 30%;
    text-align: left;
}

.problem-card-description {
    font-size: 18px;
    color: white;
    width: 70%;
    text-align: left;
}

.tag_description {
    margin-top: -15px;
}

.el-popover__title {
    color: white;
    font-size: 24px;
    font-weight: bold;
}

.el-checkbox__input.is-disabled .el-checkbox__inner {
    background-color: #777;
}

.el-dialog__title {
    color: white;
}

.add_dialog {
    --el-dialog-bg-color: #454647;
    color: white;
    position: absolute;
    right: calc((30vw - 30px) / 2 - 7.5%);
    top: 20%;
    border-radius: 15px;
    /* left: 100px; */
}

.add_dialog .el-dialog__body {
    padding: 3px 20px 3px 20px;
}

.optimize_dialog {
    --el-dialog-bg-color: #454647;
    color: white;
    position: absolute;
    right: calc((30vw - 30px) / 2 - 11%);
    top: 10%;
    border-radius: 15px;
    padding-bottom: 30px
    /* left: 100px; */
}

.optimize_dialog .el-dialog__body {
    padding: 3px 20px 3px 20px;
}

.el-switch__label.is-active {
    text-decoration: underline;
}

.el-switch__label * {
    font-size: 20px;
}

.el-switch__label {
    color: white;
}

.el-checkbox__label {
    color: white;
}

.el-checkbox.el-checkbox--large .el-checkbox__label {
    font-size: 20px;
    font-weight: normal;
}

.el-tree {
    background-color: #222C44;
    --el-tree-node-hover-bg-color: #409eff;
}

.el-tree-node {
    margin-top: 10px;
}

.is-current {
    background-color: #222C44;
}

.el-checkbox {
    --el-checkbox-bg-color: #222C44;
}

.custom-tree-node {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 20px;
    color: white;
    line-height: 1.5;
    padding-right: 8px;
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

<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-01-24 17:02:12
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-03-09 08:29:11
-->
<template>
    <PreviewVideoPlayer :dialogVisible="dialogVisible" :config="preview_config" @showDialog="showDialog" />
    <div class="frameworkBody">
        <div style=" height: 30px;text-align: left; font-size: 24px; color: white; font-weight: bold; justify-content: space-between; display: flex;">
            <span>视频分析</span>
            <span v-show="select_video != ''" style="font-size: 20px;">编号: {{ 'V' + select_video.substr(1) }} 性别:
                                                        {{ user_info.gender }} 年龄: {{ user_info.age }}</span>
        </div>
        <div style="width: 100%; height: calc(100% - 30px); margin-top: 10px;">
            <el-dialog v-model="showInfo" :title="(parseInt(info_data.time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(info_data.time / 60).toString().padStart(2, '0')) + ':' + ((info_data.time % 60).toString().padStart(2, '0'))" width="20%" :append-to="'#mainView'"
                :modal="false" :class="'show_info_dialog'" :show-close="false">
    
                <div v-loading="loadingTag" element-loading-background="rgba(122, 122, 122, 0.8)" id="dialogDiv" ref="dialogDiv" :style="{ width: '100%', height: info_data.status != -1 && info_data.status != 3 ? elHeight * .4 + 'px' : elHeight * .4 + 'px', color: 'white', textAlign: 'left', overflow: 'auto' }">
                    <h2>
                        问题描述
                        <span v-if="info_data.user_said != ''">
                                                                    <el-popover placement="bottom" title="" :width="250" trigger="click"
                                                                        :popper-class="'marker_description'">
                                                                        <template #reference>
                                                                            <a style="position: absolute; margin-top: 1px;"><svg t="1708679239889" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                                                                    xmlns="http://www.w3.org/2000/svg" p-id="1495" width="30" height="30">
                                                                                    <path
                                                                                        d="M536 480v192a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16V480a16 16 0 0 1 16-16h16a16 16 0 0 1 16 16z m-32-128h16a16 16 0 0 1 16 16v32a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16v-32a16 16 0 0 1 16-16z m8 448c159.056 0 288-128.944 288-288s-128.944-288-288-288-288 128.944-288 288 128.944 288 288 288z m0 48c-185.568 0-336-150.432-336-336s150.432-336 336-336 336 150.432 336 336-150.432 336-336 336z"
                                                                                        fill="#ffffff" p-id="1496"></path>
                                                                                </svg></a>
</template>
                                <div :style="{ fontSize: '16px', lineHeight: 1.5, color: 'white' }">
                                    <h3>用户描述</h3>
                                    {{ '"' + info_data.user_said + '"' }}
                                    <h3>AI解释</h3>

                                    {{ '"' + info_data.reason + '"' }}
                                </div>
                            </el-popover>
                        </span>
                    </h2>
                    
                    <div style="margin-bottom: 10px; padding-right: 10px;">
                        <!-- <div style="font-size: 16px;">
                            {{ '"' + info_data.user_said + '"' }}
                        </div> -->
                        <el-input v-model="info_data.description" :autosize="{ minRows: 3, maxRows: 3 }" type="textarea"
                            placeholder="Please input" />
                    </div>
                    <h2>
                        一级标签 (可选)
                    </h2>
                    <div @click="focusTag('main')"
                        :style="{ display: 'flex', flexWrap: 'wrap', backgroundColor: showLevelTag.showFirstTag == true ? '#666666AA' : '#45464700', padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px', cursor: 'pointer' }">
                        <div v-if="info_data.tag.length > 0" style="display: flex; flex-wrap: wrap;">
                            <div v-for="d in info_data.tag" :key="'type_tag' + d" class="align-class"
                                :style="{ backgroundColor: colorMap[dataSource[d - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                                <div
                                    :style="{ backgroundColor: colorMap[dataSource[d - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                                </div>
                                <div>
                                    {{ dataSource[d - 1].label }}
                                </div>
                            </div>
                        </div>
                        <div v-else>
                            <div class="align-class"
                                :style="{ backgroundColor: '#409eff40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                                <div
                                    :style="{ backgroundColor: '#409eff', width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                                </div>
                                <div>
                                    选择一级标签</div>
                            </div>
                        </div>
                    </div>
                    <el-collapse-transition>
                        <div v-if="showLevelTag.showFirstTag"
                            style="background-color: #666666AA; padding: 3px 3px 8px 3px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;">
                            <hr>
                            <div>
                                最多选择2个标签，建议选择一个
                            </div>
                            <div style="display: flex; flex-wrap: wrap;">
                                <div v-for="(d, i) in dataSource" :key="'type_tag' + d" class="align-class"
                                    :style="{ backgroundColor: colorMap[d.id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px', cursor: 'pointer' }"
                                    @click="selectTag(info_data.tag, d.l_id, info_data, d.id, info_data.unique_tag, d.label)">
                                    <div
                                        :style="{ backgroundColor: colorMap[d.id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                                        <svg v-if="info_data.tag.indexOf(d.l_id) != -1" style="position: absolute; top: 0px;"
                                            t="1706630009026" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                            xmlns="http://www.w3.org/2000/svg" p-id="4218" width="15" height="15">
                                            <path
                                                d="M431.47 793.782c-11.365 0-22.332-4.378-30.589-12.286l-235.495-225.535c-17.64-16.894-18.245-44.891-1.35-62.528 16.894-17.64 44.891-18.245 62.532-1.351l201.055 192.552 364.692-443.171c15.519-18.86 43.39-21.567 62.253-6.049 18.861 15.519 21.568 43.39 6.048 62.251l-394.992 479.993c-7.821 9.504-19.248 15.319-31.534 16.047-0.874 0.052-1.748 0.078-2.621 0.078z"
                                                fill="#fff" p-id="4219"></path>
                                        </svg>
                                    </div>
                                    <div>
                                        {{ d.label }}
                                    </div>
                                </div>

                            </div>
                            <el-button style="margin-top: 10px;" type="primary"
                                @click="showAddDialog(1, dataSource)">添加一级标签</el-button>
                        </div>
                    </el-collapse-transition>
                    <h2>
                        二级标签 (可选)
                    </h2>
                    <div
                        :style="{ padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px' }">
                        <div v-for="(d, i) in info_data.tag" :key="'type_first_tag' + d">
                            <hr v-if="i > 0" style="margin-top: 10px;">
                            <div class="align-class"
                                :style="{ padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px', justifyContent: 'left' }">
                                <div
                                    :style="{ backgroundColor: colorMap[dataSource[d - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                                </div>
                                <div>
                                    {{ dataSource[d - 1].label }}
                                </div> &nbsp;
                            </div>
                            <div @click="focusTag(i)"
                                :style="{ display: 'flex', flexWrap: 'wrap', backgroundColor: showLevelTag.showSecondTag[i] == true ? '#666666AA' : '#45464700', padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px', cursor: 'pointer' }">
                                <div v-if="typeof info_data.second_tag[d] != 'undefined' && info_data.second_tag[d].length > 0"
                                    style="display: flex; flex-wrap: wrap;">
                                    <div v-for="(dd, ii) in info_data.second_tag[d]" :key="'type_second_tag' + dd"
                                        class="align-class"
                                        :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                                        <div
                                            :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '0px' }">
                                        </div>
                                        <div>
                                            {{ dataSource[d - 1].children[dd - 1].label }}
                                        </div>
                                    </div>
                                </div>
                                <div v-else>
                                    <div class="align-class"
                                        :style="{ backgroundColor: '#409eff40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                                        <div
                                            :style="{ backgroundColor: '#409eff', width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '0px' }">
                                        </div>
                                        <div>
                                            选择二级标签</div>
                                    </div>
                                </div>
                            </div>

                            <el-collapse-transition>
                                <div v-if="showLevelTag.showSecondTag[i]"
                                    style="background-color: #666666AA; padding: 3px 3px 8px 3px; border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;">
                                    <hr>
                                    <div>
                                        最多选择2个标签，建议选择一个
                                    </div>
                                    <div style="display: flex; flex-wrap: wrap;">
                                        <div v-for="dd in dataSource[d - 1].children" :key="'type_tag' + d"
                                            class="align-class"
                                            :style="{ backgroundColor: colorMap[dd.id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px', cursor: 'pointer' }"
                                            @click="selectTag(info_data.second_tag[d], dd.cnt, 0, dd.id, info_data.unique_tag, dd.label)">
                                            <div
                                                :style="{ backgroundColor: colorMap[dd.id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '0px' }">
                                                <svg v-if="typeof info_data.second_tag[d] != 'undefined' && info_data.second_tag[d].length > 0 && info_data.second_tag[d].indexOf(dd.cnt) != -1"
                                                    style="position: absolute; top: 0px;" t="1706630009026" class="icon"
                                                    viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
                                                    p-id="4218" width="15" height="15">
                                                    <path
                                                        d="M431.47 793.782c-11.365 0-22.332-4.378-30.589-12.286l-235.495-225.535c-17.64-16.894-18.245-44.891-1.35-62.528 16.894-17.64 44.891-18.245 62.532-1.351l201.055 192.552 364.692-443.171c15.519-18.86 43.39-21.567 62.253-6.049 18.861 15.519 21.568 43.39 6.048 62.251l-394.992 479.993c-7.821 9.504-19.248 15.319-31.534 16.047-0.874 0.052-1.748 0.078-2.621 0.078z"
                                                        fill="#fff" p-id="4219"></path>
                                                </svg>
                                            </div>
                                            <div>
                                                {{ dd.label }}
                                            </div>
                                        </div>

                                    </div>
                                    <el-button style="margin-top: 10px;" type="primary"
                                        @click="showAddDialog(2, dataSource[d - 1])">添加二级标签</el-button>
                                </div>
                            </el-collapse-transition>
                        </div>
                    </div>
                    <div v-if="info_data.status != -1 && info_data.status != 3">
                    <h2>
                        其他相同标签问题：
                    </h2>
                    <div>
                        <div v-for="d in info_data.tag" :key="'type_tag' + d">
                            <div class="align-class" style="justify-content: left;">
                                <div
                                    :style="{ backgroundColor: colorMap[dataSource[d - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                                </div>
                                {{ dataSource[d - 1].label }}
                            </div>
                            <div v-if="selectShowLevel == 1">
                                <div v-for="(td, ti) in allTagTimeData[dataSource[d - 1].id]" :key="'time_t' + ti"
                                    style="font-size: 16px;">
                                    {{ 'V' + ti.substr(1) }}: <span v-for="(t_d, t_i) in td" :key="'time_td' + t_i">
                                        <a @click="selectPreview(t_d, ti)"
                                            :style="{ textDecoration: 'underline', color: t_d.vision == 0 ? 'white' : 'blue' }">
                                            {{ (parseInt(t_d.time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(t_d.time / 60).toString().padStart(2, '0')) + ':' + ((t_d.time % 60).toString().padStart(2, '0')) }}
                                        </a>

                                        <!-- <span>{{  t_d.vision }}</span> -->
                                        <span v-if="t_i != td.length - 1">, </span>
                                    </span>
                                </div>
                            </div>
                            <div v-if="selectShowLevel == 2">
                                <div v-for="(txd, txi) in info_data.second_tag[d]" :key="'sec_time_id' + txi">
                                    <div class="align-class" style="justify-content: left;">
                                        <div
                                            :style="{ backgroundColor: colorMap[dataSource[d - 1].children[txd - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '0px' }">
                                        </div>
                                        {{ dataSource[d - 1].children[txd - 1].label }}

                                    </div>
                                    <div v-for="(td, ti) in allTagTimeData[dataSource[d - 1].children[txd - 1].id]"
                                        :key="'time_t' + ti" style="font-size: 16px;">
                                        {{ 'V' + ti.substr(1) }}:
                                        <span v-for="(t_d, t_i) in td" :key="'time_td' + t_i">
                                            <a @click="selectPreview(t_d, ti)"
                                                :style="{ textDecoration: 'underline', color: t_d.vision == 0 ? 'white' : 'blue' }">
                                                {{ (parseInt(t_d.time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(t_d.time / 60).toString().padStart(2, '0')) + ':' + ((t_d.time % 60).toString().padStart(2, '0'))}}
                                            </a>
                                            <!-- <span>{{  t_d.vision }}</span> -->
                                            <span v-if="t_i != td.length - 1">, </span>
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                </div>
                <div style="padding: 5px 0px 10px 0px;">
                    <el-button type="primary" @click="chooseTime(info_data.time)">
                        <div class="align-class">
                            <svg t="1707271687917" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                xmlns="http://www.w3.org/2000/svg" p-id="4224" width="15" height="15">
                                <path
                                    d="M209.92 988.16c-15.36 0-30.72-15.36-30.72-30.72s15.36-30.72 30.72-30.72h471.04c153.6 0 281.6-128 281.6-281.6s-128-281.6-281.6-281.6H102.4l220.16 220.16c5.12 5.12 10.24 10.24 10.24 20.48 0 5.12-5.12 15.36-10.24 20.48-5.12 5.12-10.24 10.24-20.48 10.24-5.12 0-15.36-5.12-20.48-10.24L10.24 353.28c-5.12-5.12-10.24-10.24-10.24-20.48 0-5.12 5.12-15.36 10.24-20.48L281.6 40.96c5.12-5.12 10.24-10.24 20.48-10.24 5.12 0 15.36 5.12 20.48 10.24 0 10.24 5.12 15.36 5.12 25.6 0 5.12-5.12 15.36-10.24 20.48L97.28 307.2h583.68a343.04 343.04 0 0 1 0 686.08H209.92z"
                                    fill="#ffffff" p-id="4225"></path>
                            </svg> &nbsp; 初始位置
                        </div>
                    </el-button>
                    <el-button type="primary" @click="playVideo()">
                        <div v-if="playTag == 1" class="align-class">
                            <svg t="1706253575488" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                xmlns="http://www.w3.org/2000/svg" p-id="4211" width="20" height="20">
                                <path
                                    d="M817.088 484.96l-512-323.744C295.232 154.976 282.752 154.592 272.576 160.224 262.336 165.856 256 176.608 256 188.256l0 647.328c0 11.648 6.336 22.4 16.576 28.032 4.8 2.656 10.112 3.968 15.424 3.968 5.952 0 11.904-1.664 17.088-4.928l512-323.616C826.368 533.184 832 522.976 832 512 832 501.024 826.368 490.816 817.088 484.96z"
                                    fill="#ffffff" p-id="4212"></path>
                            </svg> &nbsp; 播放视频
                        </div>
                        <div v-else class="align-class">
                            <svg t="1706534722560" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                xmlns="http://www.w3.org/2000/svg" p-id="4218" width="20" height="20">
                                <path
                                    d="M304 176h80v672h-80zM712 176h-64c-4.4 0-8 3.6-8 8v656c0 4.4 3.6 8 8 8h64c4.4 0 8-3.6 8-8V184c0-4.4-3.6-8-8-8z"
                                    p-id="4219" fill="#ffffff"></path>
                            </svg> &nbsp; 暂停视频
                        </div>
                    </el-button>
                </div>
                <div v-if="info_data.status != -1 && info_data.status != 3" style="padding: 5px 0px 10px 0px;">
                    <el-button type="success" @click="clickDecision(1)">
                        <svg t="1707272509861" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="11129" width="15" height="15">
                            <path
                                d="M511.6 63.6c-246.9 0-448 201.2-448 448 0 247.3 201.2 448 448 448s448-200.7 448-448c0-246.9-200.7-448-448-448z m259.9 318.5L474.6 699.3c-7 7.3-16.5 12.1-27.4 12.1-10.5 0-20.5-4.7-27.4-12.1L252 520c-7-7.3-11.5-17.8-11.5-29.4 0-23.1 17.5-41.4 38.9-41.4 10.5 0 20.5 4.7 27.4 12.1l140.7 149.9 270-287.8c7-7.3 16.5-12.1 27.4-12.1 21.5 0 38.9 18.3 38.9 41.4-0.8 11.6-5.3 22.1-12.3 29.4z m0 0"
                                p-id="11130" fill="#ffffff"></path>
                        </svg>&nbsp;
                        确认
                    </el-button>
                    <!-- <el-button type="warning" @click="clickDecision(2)">
                        <svg t="1706257862659" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="9466" width="15" height="15">
                            <path
                                d="M512 64c126.677333 3.328 232.192 47.146667 316.501333 131.498667C912.853333 279.808 956.672 385.28 960 512c-3.328 126.677333-47.146667 232.192-131.498667 316.501333C744.192 912.853333 638.72 956.672 512 960c-126.677333-3.328-232.192-47.146667-316.501333-131.498667C111.146667 744.192 67.328 638.72 64 512c3.328-126.677333 47.146667-232.192 131.498667-316.501333C279.808 111.146667 385.28 67.328 512 64zM512 256c-17.322667 0-31.658667 6.357333-43.008 19.029333A58.197333 58.197333 0 0 0 453.973333 320l23.04 256a35.925333 35.925333 0 0 0 11.477334 22.485333 34.048 34.048 0 0 0 23.466666 8.533334 33.621333 33.621333 0 0 0 23.466667-8.533334 36.138667 36.138667 0 0 0 11.52-22.485333l23.04-256a57.984 57.984 0 0 0-15.018667-44.970667A55.381333 55.381333 0 0 0 511.914667 256H512z m0 512c14.677333-0.64 26.88-5.674667 36.522667-15.018667 9.642667-9.344 14.506667-21.333333 14.506666-35.968A49.578667 49.578667 0 0 0 512 665.984a49.493333 49.493333 0 0 0-50.986667 51.029333c0 14.677333 4.821333 26.666667 14.506667 35.968 9.642667 9.301333 21.802667 14.293333 36.48 15.018667z"
                                fill="white" fill-opacity=".96" p-id="9467"></path>
                        </svg>&nbsp;
                        待定
                    </el-button> -->
                    <!-- <el-button type="danger" @click="clickDecision(3)"> -->
                    <el-button type="danger" @click="clickDecision(typeof info_data['humanAdd'] != 'undefined' ? 3 : 9)">
                        <svg t="1707272411978" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="7920" width="15" height="15">
                            <path
                                d="M512 64.5C264.85 64.5 64.5 264.85 64.5 512S264.85 959.5 512 959.5 959.5 759.15 959.5 512 759.15 64.5 512 64.5z m235.21 599.09c16.06 13.81 17.89 38.03 4.08 54.09-7.59 8.83-18.31 13.36-29.1 13.36-8.85 0-17.74-3.05-24.98-9.26L512 562.59 326.79 721.78a38.22 38.22 0 0 1-24.98 9.26c-10.79 0-21.52-4.53-29.1-13.36-13.81-16.06-11.98-40.28 4.08-54.09L453.15 512 276.79 360.42c-16.06-13.81-17.89-38.03-4.08-54.09 13.81-16.07 38.01-17.89 54.09-4.1L512 461.42l185.2-159.19c16.08-13.8 40.29-11.96 54.09 4.1 13.81 16.06 11.98 40.28-4.08 54.09L570.85 512.01l176.36 151.58z"
                                p-id="7921" fill="white"></path>
                        </svg>&nbsp;
                        取消
                    </el-button>
                </div>
                <div v-else style="padding: 5px 0px 10px 0px;">
                    <el-button type="success" @click="submitMarker()">
                        <svg t="1707272509861" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="11129" width="15" height="15">
                            <path
                                d="M511.6 63.6c-246.9 0-448 201.2-448 448 0 247.3 201.2 448 448 448s448-200.7 448-448c0-246.9-200.7-448-448-448z m259.9 318.5L474.6 699.3c-7 7.3-16.5 12.1-27.4 12.1-10.5 0-20.5-4.7-27.4-12.1L252 520c-7-7.3-11.5-17.8-11.5-29.4 0-23.1 17.5-41.4 38.9-41.4 10.5 0 20.5 4.7 27.4 12.1l140.7 149.9 270-287.8c7-7.3 16.5-12.1 27.4-12.1 21.5 0 38.9 18.3 38.9 41.4-0.8 11.6-5.3 22.1-12.3 29.4z m0 0"
                                p-id="11130" fill="#ffffff"></path>
                        </svg>&nbsp;
                        确认
                    </el-button>
                    <el-button type="danger" @click="clickDecision(3)">
                        <svg t="1707272411978" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="7920" width="15" height="15">
                            <path
                                d="M512 64.5C264.85 64.5 64.5 264.85 64.5 512S264.85 959.5 512 959.5 959.5 759.15 959.5 512 759.15 64.5 512 64.5z m235.21 599.09c16.06 13.81 17.89 38.03 4.08 54.09-7.59 8.83-18.31 13.36-29.1 13.36-8.85 0-17.74-3.05-24.98-9.26L512 562.59 326.79 721.78a38.22 38.22 0 0 1-24.98 9.26c-10.79 0-21.52-4.53-29.1-13.36-13.81-16.06-11.98-40.28 4.08-54.09L453.15 512 276.79 360.42c-16.06-13.81-17.89-38.03-4.08-54.09 13.81-16.07 38.01-17.89 54.09-4.1L512 461.42l185.2-159.19c16.08-13.8 40.29-11.96 54.09 4.1 13.81 16.06 11.98 40.28-4.08 54.09L570.85 512.01l176.36 151.58z"
                                p-id="7921" fill="white"></path>
                        </svg>&nbsp;
                        取消
                    </el-button>
                </div>
                <!-- <div v-if="info_data.status != -1 && typeof info_data['humanAdd'] != 'undefined'" style="padding: 5px 0px 10px 0px;"> -->
                    <!-- <el-button type="success" @click="clickDecision(1)">
                        <svg t="1707272509861" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="11129" width="15" height="15">
                            <path
                                d="M511.6 63.6c-246.9 0-448 201.2-448 448 0 247.3 201.2 448 448 448s448-200.7 448-448c0-246.9-200.7-448-448-448z m259.9 318.5L474.6 699.3c-7 7.3-16.5 12.1-27.4 12.1-10.5 0-20.5-4.7-27.4-12.1L252 520c-7-7.3-11.5-17.8-11.5-29.4 0-23.1 17.5-41.4 38.9-41.4 10.5 0 20.5 4.7 27.4 12.1l140.7 149.9 270-287.8c7-7.3 16.5-12.1 27.4-12.1 21.5 0 38.9 18.3 38.9 41.4-0.8 11.6-5.3 22.1-12.3 29.4z m0 0"
                                p-id="11130" fill="#ffffff"></path>
                        </svg>&nbsp;
                        确认
                    </el-button> -->
                    <!-- <el-button type="warning" @click="clickDecision(2)">
                        <svg t="1706257862659" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="9466" width="15" height="15">
                            <path
                                d="M512 64c126.677333 3.328 232.192 47.146667 316.501333 131.498667C912.853333 279.808 956.672 385.28 960 512c-3.328 126.677333-47.146667 232.192-131.498667 316.501333C744.192 912.853333 638.72 956.672 512 960c-126.677333-3.328-232.192-47.146667-316.501333-131.498667C111.146667 744.192 67.328 638.72 64 512c3.328-126.677333 47.146667-232.192 131.498667-316.501333C279.808 111.146667 385.28 67.328 512 64zM512 256c-17.322667 0-31.658667 6.357333-43.008 19.029333A58.197333 58.197333 0 0 0 453.973333 320l23.04 256a35.925333 35.925333 0 0 0 11.477334 22.485333 34.048 34.048 0 0 0 23.466666 8.533334 33.621333 33.621333 0 0 0 23.466667-8.533334 36.138667 36.138667 0 0 0 11.52-22.485333l23.04-256a57.984 57.984 0 0 0-15.018667-44.970667A55.381333 55.381333 0 0 0 511.914667 256H512z m0 512c14.677333-0.64 26.88-5.674667 36.522667-15.018667 9.642667-9.344 14.506667-21.333333 14.506666-35.968A49.578667 49.578667 0 0 0 512 665.984a49.493333 49.493333 0 0 0-50.986667 51.029333c0 14.677333 4.821333 26.666667 14.506667 35.968 9.642667 9.301333 21.802667 14.293333 36.48 15.018667z"
                                fill="white" fill-opacity=".96" p-id="9467"></path>
                        </svg>&nbsp;
                        待定
                    </el-button> -->
                    <!-- <el-button type="danger" @click="clickDecision(3)"> -->
                    <!-- <el-button type="danger" @click="clickDecision(3)">
                        <svg t="1707272411978" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="7920" width="15" height="15">
                            <path
                                d="M512 64.5C264.85 64.5 64.5 264.85 64.5 512S264.85 959.5 512 959.5 959.5 759.15 959.5 512 759.15 64.5 512 64.5z m235.21 599.09c16.06 13.81 17.89 38.03 4.08 54.09-7.59 8.83-18.31 13.36-29.1 13.36-8.85 0-17.74-3.05-24.98-9.26L512 562.59 326.79 721.78a38.22 38.22 0 0 1-24.98 9.26c-10.79 0-21.52-4.53-29.1-13.36-13.81-16.06-11.98-40.28 4.08-54.09L453.15 512 276.79 360.42c-16.06-13.81-17.89-38.03-4.08-54.09 13.81-16.07 38.01-17.89 54.09-4.1L512 461.42l185.2-159.19c16.08-13.8 40.29-11.96 54.09 4.1 13.81 16.06 11.98 40.28-4.08 54.09L570.85 512.01l176.36 151.58z"
                                p-id="7921" fill="white"></path>
                        </svg>&nbsp;
                        删除
                    </el-button>
                </div> -->
            </el-dialog>
            <el-dialog v-model="showDefault" :title="(parseInt(info_data.time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(info_data.time / 60).toString().padStart(2, '0')) + ':' + ((info_data.time % 60).toString().padStart(2, '0'))" width="20%" :append-to="'#mainView'"
                :modal="false" :class="'show_info_dialog'" :show-close="false">
    
                <div v-loading="loadingTag" element-loading-background="rgba(122, 122, 122, 0.8)" id="defaultDialogDiv" ref="defaultDialogDiv" :style="{ width: '100%', height: info_data.status != -1 && info_data.status != 3 ? elHeight * .4 + 'px' : elHeight * .4 + 'px', color: 'white', textAlign: 'left', overflow: 'auto' }">
                    <h2>
                        问题描述
                        <span v-if="info_data.default.user_said != ''">
                    <el-popover placement="bottom" title="" :width="250" trigger="click"
                                                                    :popper-class="'marker_description'">
<template #reference>
    <a style="position: absolute; margin-top: 1px;"><svg t="1708679239889" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                                                                    xmlns="http://www.w3.org/2000/svg" p-id="1495" width="30" height="30">
                                                                                    <path
                                                                                        d="M536 480v192a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16V480a16 16 0 0 1 16-16h16a16 16 0 0 1 16 16z m-32-128h16a16 16 0 0 1 16 16v32a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16v-32a16 16 0 0 1 16-16z m8 448c159.056 0 288-128.944 288-288s-128.944-288-288-288-288 128.944-288 288 128.944 288 288 288z m0 48c-185.568 0-336-150.432-336-336s150.432-336 336-336 336 150.432 336 336-150.432 336-336 336z"
                                                                                        fill="#ffffff" p-id="1496"></path>
                                                                                </svg></a>
</template>
                                <div :style="{ fontSize: '16px', lineHeight: 1.5, color: 'white' }">
                                    <h3>用户描述</h3>
                                    {{ '"' + info_data.default.user_said + '"' }}
                                    <h3>AI解释</h3>

                                    {{ '"' + info_data.default.reason + '"' }}
                                </div>
                            </el-popover>
                        </span>
                    </h2>
                    
                    <div style="margin-bottom: 10px; padding-right: 10px;">
                        <div style="font-size: 18px;">
                            {{ info_data.default.description }}
                        </div>
                        <!-- <el-input v-model="info_data.description" :autosize="{ minRows: 3, maxRows: 3 }" type="textarea"
                            placeholder="Please input" /> -->

                    </div>
                    <!-- <h2>
                        一级标签
                    </h2>
                    <div
                        :style="{ display: 'flex', flexWrap: 'wrap', backgroundColor: showLevelTag.showFirstTag == true ? '#666666AA' : '#45464700', padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px'}">
                        <div v-if="info_data.tag.length > 0" style="display: flex; flex-wrap: wrap;">
                            <div v-for="d in info_data.tag" :key="'type_tag' + d" class="align-class"
                                :style="{ backgroundColor: colorMap[dataSource[d - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                                <div
                                    :style="{ backgroundColor: colorMap[dataSource[d - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                                </div>
                                <div>
                                    {{ dataSource[d - 1].label }}
                                </div>
                            </div>
                        </div> -->
                        <!-- <div v-else>
                            <div class="align-class"
                                :style="{ backgroundColor: '#409eff40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                                <div
                                    :style="{ backgroundColor: '#409eff', width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                                </div>
                                <div>
                                    选择一级标签</div>
                            </div>
                        </div> -->
                    <!-- </div> -->
                    <h2>
                        标签
                    </h2>
                    <div
                        :style="{ padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px' }">
                        <div v-for="(d, i) in info_data.default.tag" :key="'type_first_tag' + d">
                            <hr v-if="i > 0" style="margin-top: 10px;">
                            <div style="display: flex;">
                            <div class="align-class"
                                :style="{ backgroundColor: colorMap[dataSource[d - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px', justifyContent: 'left' }">
                                <div
                                    :style="{ backgroundColor: colorMap[dataSource[d - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                                </div>
                                <div>
                                    {{ dataSource[d - 1].label }}
                                </div> &nbsp;
                            </div>
                        </div>
                            <div 
                                :style="{ display: 'flex', flexWrap: 'wrap', backgroundColor: showLevelTag.showSecondTag[i] == true ? '#666666AA' : '#45464700', padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px', }">
                                <div v-if="typeof info_data.default.second_tag[d] != 'undefined' && info_data.default.second_tag[d].length > 0"
                                    style="display: flex; flex-wrap: wrap;">
                                    <div v-for="(dd, ii) in info_data.default.second_tag[d]" :key="'type_second_tag' + dd"
                                        class="align-class"
                                        :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                                        <div
                                            :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '0px' }">
                                        </div>
                                        <div>
                                            {{ dataSource[d - 1].children[dd - 1].label }}
                                        </div>
                                    </div>
                                </div>
                                <!-- <div v-else>
                                    <div class="align-class"
                                        :style="{ backgroundColor: '#409eff40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                                        <div
                                            :style="{ backgroundColor: '#409eff', width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '0px' }">
                                        </div>
                                        <div>
                                            选择二级标签</div>
                                    </div>
                                </div> -->
                            </div>
                        </div>
                    </div>
                </div>
                <div style="padding: 5px 0px 10px 0px;">
                    <el-button type="primary" @click="chooseTime(info_data.time)">
                        <div class="align-class">
                            <svg t="1707271687917" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                xmlns="http://www.w3.org/2000/svg" p-id="4224" width="15" height="15">
                                <path
                                    d="M209.92 988.16c-15.36 0-30.72-15.36-30.72-30.72s15.36-30.72 30.72-30.72h471.04c153.6 0 281.6-128 281.6-281.6s-128-281.6-281.6-281.6H102.4l220.16 220.16c5.12 5.12 10.24 10.24 10.24 20.48 0 5.12-5.12 15.36-10.24 20.48-5.12 5.12-10.24 10.24-20.48 10.24-5.12 0-15.36-5.12-20.48-10.24L10.24 353.28c-5.12-5.12-10.24-10.24-10.24-20.48 0-5.12 5.12-15.36 10.24-20.48L281.6 40.96c5.12-5.12 10.24-10.24 20.48-10.24 5.12 0 15.36 5.12 20.48 10.24 0 10.24 5.12 15.36 5.12 25.6 0 5.12-5.12 15.36-10.24 20.48L97.28 307.2h583.68a343.04 343.04 0 0 1 0 686.08H209.92z"
                                    fill="#ffffff" p-id="4225"></path>
                            </svg> &nbsp; 初始位置
                        </div>
                    </el-button>
                    <el-button type="primary" @click="playVideo()">
                        <div v-if="playTag == 1" class="align-class">
                            <svg t="1706253575488" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                xmlns="http://www.w3.org/2000/svg" p-id="4211" width="20" height="20">
                                <path
                                    d="M817.088 484.96l-512-323.744C295.232 154.976 282.752 154.592 272.576 160.224 262.336 165.856 256 176.608 256 188.256l0 647.328c0 11.648 6.336 22.4 16.576 28.032 4.8 2.656 10.112 3.968 15.424 3.968 5.952 0 11.904-1.664 17.088-4.928l512-323.616C826.368 533.184 832 522.976 832 512 832 501.024 826.368 490.816 817.088 484.96z"
                                    fill="#ffffff" p-id="4212"></path>
                            </svg> &nbsp; 播放视频
                        </div>
                        <div v-else class="align-class">
                            <svg t="1706534722560" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                xmlns="http://www.w3.org/2000/svg" p-id="4218" width="20" height="20">
                                <path
                                    d="M304 176h80v672h-80zM712 176h-64c-4.4 0-8 3.6-8 8v656c0 4.4 3.6 8 8 8h64c4.4 0 8-3.6 8-8V184c0-4.4-3.6-8-8-8z"
                                    p-id="4219" fill="#ffffff"></path>
                            </svg> &nbsp; 暂停视频
                        </div>
                    </el-button>
                </div>
                <div v-if="info_data.status != -1 && info_data.status != 3" style="padding: 5px 0px 10px 0px;">
                    <el-button v-if="info_data.repeat_status == 0" type="success" @click="clickEdit">
                        <svg t="1707272509861" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="11129" width="15" height="15">
                            <path
                                d="M511.6 63.6c-246.9 0-448 201.2-448 448 0 247.3 201.2 448 448 448s448-200.7 448-448c0-246.9-200.7-448-448-448z m259.9 318.5L474.6 699.3c-7 7.3-16.5 12.1-27.4 12.1-10.5 0-20.5-4.7-27.4-12.1L252 520c-7-7.3-11.5-17.8-11.5-29.4 0-23.1 17.5-41.4 38.9-41.4 10.5 0 20.5 4.7 27.4 12.1l140.7 149.9 270-287.8c7-7.3 16.5-12.1 27.4-12.1 21.5 0 38.9 18.3 38.9 41.4-0.8 11.6-5.3 22.1-12.3 29.4z m0 0"
                                p-id="11130" fill="#ffffff"></path>
                        </svg>&nbsp;
                        复用
                    </el-button>
                    <!-- <el-button type="warning" @click="clickDecision(2)">
                        <svg t="1706257862659" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="9466" width="15" height="15">
                            <path
                                d="M512 64c126.677333 3.328 232.192 47.146667 316.501333 131.498667C912.853333 279.808 956.672 385.28 960 512c-3.328 126.677333-47.146667 232.192-131.498667 316.501333C744.192 912.853333 638.72 956.672 512 960c-126.677333-3.328-232.192-47.146667-316.501333-131.498667C111.146667 744.192 67.328 638.72 64 512c3.328-126.677333 47.146667-232.192 131.498667-316.501333C279.808 111.146667 385.28 67.328 512 64zM512 256c-17.322667 0-31.658667 6.357333-43.008 19.029333A58.197333 58.197333 0 0 0 453.973333 320l23.04 256a35.925333 35.925333 0 0 0 11.477334 22.485333 34.048 34.048 0 0 0 23.466666 8.533334 33.621333 33.621333 0 0 0 23.466667-8.533334 36.138667 36.138667 0 0 0 11.52-22.485333l23.04-256a57.984 57.984 0 0 0-15.018667-44.970667A55.381333 55.381333 0 0 0 511.914667 256H512z m0 512c14.677333-0.64 26.88-5.674667 36.522667-15.018667 9.642667-9.344 14.506667-21.333333 14.506666-35.968A49.578667 49.578667 0 0 0 512 665.984a49.493333 49.493333 0 0 0-50.986667 51.029333c0 14.677333 4.821333 26.666667 14.506667 35.968 9.642667 9.301333 21.802667 14.293333 36.48 15.018667z"
                                fill="white" fill-opacity=".96" p-id="9467"></path>
                        </svg>&nbsp;
                        待定
                    </el-button> -->
                    <el-button type="primary" @click="this.showDefault = !showDefault">
                        <svg t="1707272411978" class="icon" viewBox="0 0 1024 1024" version="1.1"
                            xmlns="http://www.w3.org/2000/svg" p-id="7920" width="15" height="15">
                            <path
                                d="M512 64.5C264.85 64.5 64.5 264.85 64.5 512S264.85 959.5 512 959.5 959.5 759.15 959.5 512 759.15 64.5 512 64.5z m235.21 599.09c16.06 13.81 17.89 38.03 4.08 54.09-7.59 8.83-18.31 13.36-29.1 13.36-8.85 0-17.74-3.05-24.98-9.26L512 562.59 326.79 721.78a38.22 38.22 0 0 1-24.98 9.26c-10.79 0-21.52-4.53-29.1-13.36-13.81-16.06-11.98-40.28 4.08-54.09L453.15 512 276.79 360.42c-16.06-13.81-17.89-38.03-4.08-54.09 13.81-16.07 38.01-17.89 54.09-4.1L512 461.42l185.2-159.19c16.08-13.8 40.29-11.96 54.09 4.1 13.81 16.06 11.98 40.28-4.08 54.09L570.85 512.01l176.36 151.58z"
                                p-id="7921" fill="white"></path>
                        </svg>&nbsp;
                        关闭
                    </el-button>
                </div>
            </el-dialog>
            <el-dialog v-model="tagConfig.addPoint" :title="'添加' + tagConfig.add_tag_level + '级标签'" width="15%" :append-to="'#problems_tag'" :modal="false" :class="'add_main_dialog'">
                <div v-loading="tagConfig.loadingTag"  element-loading-background="rgba(122, 122, 122, 1)" style="width: 100%; height: 160px; margin-top: -35px;">
                    <h3 style="color: white; text-align: left;">标签名称</h3>
                <span>
                                <el-input v-model="tagConfig.tag_name" placeholder="Please input"  :input-style="{ 'font-size': '18px' }"/>
                            </span>
                            <br>
                    <h3 style="color: white; text-align: left;">标签定义</h3>
                            <span>
                                <el-input v-model="tagConfig.description" placeholder="Please input"  :autosize="{ minRows: 3, maxRows: 3 }" type="textarea"/>
                            </span>
                </div>
                <div style="padding: 30px 0px 10px 0px;">
                    <el-button type="primary" @click="addTag()">确定</el-button>
                    <el-button @click="tagConfig.addPoint = false">取消</el-button>
                </div>
            </el-dialog>
            <div id="mainView" ref="mainView" class="align-class" style="height: calc(100% - 105px); width: 100%;">
                <div>
                    <video-player :src="config.src" playsinline :controls="false" :volume="1"
                        :height="1 * config.videoHeight" :playback-rates="[0.7, 1.0, 1.5, 2.0]" @mounted="handleMounted"
                        @ready="handleEvent($event)" @play="handleEvent($event)" @pause="handleEvent($event)"
                        @ended="handleEvent($event)" @loadeddata="handleEvent($event)" @waiting="handleEvent($event)"
                        @playing="handleEvent($event)" @canplay="handleEvent($event)" @canplaythrough="handleEvent($event)"
                        @timeupdate="handleEvent(player?.currentTime())" />
                </div>
            </div>
            <div style="width: 100%; height: 95px; background-color: rgba(83, 83, 83, 0);">
                <div style="height: 50px; width: 100%; padding: 0px 0px 0px 0px;" class="align-class">
                    <div style="height: 0px; width: 100%;" class="align-class">
                        <div @click="clickBar" style="width: 100%; height: 50px; cursor: pointer;" class="align-class">
                            <div id="progressBar" ref="progressBar"
                                style="width: 100%; height: 8px; background-color: #5d5f67; border-radius: 20px;"></div>
                            <div
                                :style="{ position: 'absolute', left: '0px', width: (progressBar) + '%', height: '8px', backgroundColor: '#fff', borderRadius: '20px' }">
                            </div>
                            <div
                                :style="{ backgroundColor: 'white', border: '1px solid #5d5f67', height: '12px', width: '12px', position: 'absolute', borderRadius: '12px', left: 'calc(' + (progressBar) + '% - 6px)' }">
                            </div>
                        </div>

                        <!-- @click="clickMarker(d)" class="progress_marker" -->
                        <div v-for="(d, i) in calcMarkerData" :key="'main_' + i" 
                            :style="{ backgroundColor: '#5a9cf8', height: '12px', width: '8px', position: 'absolute', 'border-radius': '4px', left: 'calc(' + d.percentage + '% - 4px)' }">
                        </div>

                        <div id="playBar"
                            style="position: absolute; left: 0px; top: 8px;width: 100%; height: 3px; background-color: #5d5f67; border-radius: 0px;">
                        </div>
                        <div v-for="(d, i) in already_time.timeSlot" :key="'time_slot' + i"
                            style="width: 100%; position: absolute; left: 0px;">
                            <div
                                :style="{ position: 'absolute', left: 'calc( ' + (d[0] / sumTime * 100) + '% )', top: '8px', width: 'calc(' + ((d[1] - d[0]) / sumTime * 100) + '%)', height: '3px', backgroundColor: '#fff', borderRadius: '0px' }">
                            </div>
                        </div>
                    </div>

                    <div style="width: 100%; position: absolute; top: 1px;">
                        <div v-for="(tag_d, tag_i) in calcHuman" :key="'marker' + tag_i"
                            :style="{ position: 'absolute', left: 'calc(' + tag_d.percentage + '% - 8px)' }">
                            <el-tooltip
                class="box-item"
                effect="dark"
                placement="top"
            >
<template #content>
    <div style="width: 250px; font-size: 16px; padding: 10px;">
        <h2 style="margin-bottom: 10px;">人工建议</h2>
        <h3>问题描述:</h3>
        <div>{{ tag_d.description }}</div>
        <hr style="margin-top: 10px; margin-bottom: 10px;">
        <h3>标签：</h3>
        <div :style="{ padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px' }">
            <div v-for="(d, i) in tag_d.tag" :key="'type_first_tag' + d">
                <!-- <hr v-if="i > 0" style="margin-top: 10px;"> -->
                <div style="display: flex;">
                    <div class="align-class" :style="{ backgroundColor: colorMap[dataSource[d - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px', justifyContent: 'left' }">
                        <div :style="{ backgroundColor: colorMap[dataSource[d - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                        </div>
                        <div>
                            {{ dataSource[d - 1].label }}
                        </div> &nbsp;
                    </div>
                </div>
                <div :style="{ display: 'flex', flexWrap: 'wrap', backgroundColor: showLevelTag.showSecondTag[i] == true ? '#666666AA' : '#45464700', padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px', }">
                    <div v-if="typeof tag_d.second_tag[d] != 'undefined' && tag_d.second_tag[d].length > 0" style="display: flex; flex-wrap: wrap;">
                        <div v-for="(dd, ii) in tag_d.second_tag[d]" :key="'type_second_tag' + dd" class="align-class" :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                            <div :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '0px' }">
                            </div>
                            <div>
                                {{ dataSource[d - 1].children[dd - 1].label }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
                            <div v-if="selectShowLevel == 1">
                                <div v-for="(d, i) in tag_d.tag" :key="'tag' + i"
                                    :style="{ position: 'absolute', top: (-20 * i) + 'px', height: '16px', width: '16px', backgroundColor: colorMap[dataSource[d - 1].id], borderRadius: '10px', border: '1px solid #777', opacity: showTagList.indexOf(dataSource[d - 1].id) != -1 ? 1 : .3, cursor: 'pointer' }" @click="clickMarker(tag_d, 2)">
                                </div>
                            </div>
                            <div v-else>
                                <div v-for="(d, i) in tag_d.tag" :key="'tag' + i"
                                    :style="{ position: 'absolute', top: (0 * i) + 'px', height: '16px', width: '16px', borderRadius: '0px', border: '0px solid #777' }">
                                    <div v-if="typeof tag_d.second_tag[d] != 'undefined' && tag_d.second_tag[d].length > 0">
                                        <div v-for="(dd, ii) in tag_d.second_tag[d]" :key="'sec_tag' + ii"
                                            :style="{ position: 'absolute', top: (-20 * (i * (i == 1 ? tag_d.second_tag[tag_d.tag[i - 1]].length : 0) + ii)) + 'px', left: '0px', height: '16px', width: '16px', borderRadius: '0px', border: '0px solid #777', cursor: 'pointer' }" @click="clickMarker(tag_d, 2)">
                                            <div
                                                :style="{ position: 'absolute', top: '0px', left: '-9px', height: '16px', width: '16px', backgroundColor: colorMap[dataSource[d - 1].id], borderRadius: '10px', border: '1px solid #777', opacity: showTagList.indexOf(dataSource[d - 1].children[dd - 1].id) != -1 ? 1 : .3 }">
                                            </div>
                                            <div
                                                :style="{ position: 'absolute', top: '0px', left: '9px', height: '16px', width: '16px', backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id], borderRadius: '0px', border: '1px solid #777', opacity: showTagList.indexOf(dataSource[d - 1].children[dd - 1].id) != -1 ? 1 : .3 }">
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            </el-tooltip>
                        </div>
                    </div>
                    <div style="width: 100%; position: absolute; top: 40px;">
                        
                        <div v-for="(tag_d, tag_i) in calcMarkerData" :key="'marker' + tag_i"
                            :style="{ position: 'absolute', left: 'calc(' + tag_d.percentage + '% - 8px)' }">
                            <el-tooltip
                class="box-item"
                effect="dark"
                placement="top"
            >
<template #content>
    <div style="width: 250px; font-size: 16px; padding: 10px;">
        <h2 style="margin-bottom: 10px;">AI 建议</h2>
        <h3>问题描述:</h3>
        <div>{{ tag_d.default.description }}</div>
        <hr style="margin-top: 10px; margin-bottom: 10px;">
        <h3>标签：</h3>
        <div :style="{ padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px' }">
            <div v-for="(d, i) in tag_d.default.tag" :key="'type_first_tag' + d">
                <hr v-if="i > 0" style="margin-top: 10px;">
                <div style="display: flex;">
                    <div class="align-class" :style="{ backgroundColor: colorMap[dataSource[d - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px', justifyContent: 'left' }">
                        <div :style="{ backgroundColor: colorMap[dataSource[d - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                        </div>
                        <div>
                            {{ dataSource[d - 1].label }}
                        </div> &nbsp;
                    </div>
                </div>
                <div :style="{ display: 'flex', flexWrap: 'wrap', backgroundColor: showLevelTag.showSecondTag[i] == true ? '#666666AA' : '#45464700', padding: '0px 3px 0px 3px', 'border-top-left-radius': '10px', 'border-top-right-radius': '10px', }">
                    <div v-if="typeof tag_d.default.second_tag[d] != 'undefined' && tag_d.default.second_tag[d].length > 0" style="display: flex; flex-wrap: wrap;">
                        <div v-for="(dd, ii) in tag_d.default.second_tag[d]" :key="'type_second_tag' + dd" class="align-class" :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                            <div :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '0px' }">
                            </div>
                            <div>
                                {{ dataSource[d - 1].children[dd - 1].label }}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
            <!-- <a><svg t="1708679239889" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1495" width="30" height="35"><path d="M536 480v192a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16V480a16 16 0 0 1 16-16h16a16 16 0 0 1 16 16z m-32-128h16a16 16 0 0 1 16 16v32a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16v-32a16 16 0 0 1 16-16z m8 448c159.056 0 288-128.944 288-288s-128.944-288-288-288-288 128.944-288 288 128.944 288 288 288z m0 48c-185.568 0-336-150.432-336-336s150.432-336 336-336 336 150.432 336 336-150.432 336-336 336z" fill="#ffffff" p-id="1496"></path></svg></a> -->
                            <div @click="clickMarker(tag_d, 1)" style=" cursor: pointer" v-if="selectShowLevel == 1">
                                <div v-for="(d, i) in tag_d.default.tag" :key="'tag' + i">
                                <div :style="{ height: '16px', width: '16px', backgroundColor: colorMap[dataSource[d - 1].id], borderRadius: '10px', border: '1px solid #777', opacity: showTagList.indexOf(dataSource[d - 1].id) != -1 ? 1 : .3 }">
                                </div>
                                <div style="margin-top: -20px;">
                                <svg width="12" height="12" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M12.9173 9.58301C12.209 9.58301 11.6673 10.1247 11.6673 10.833C11.6673 11.5413 12.209 12.083 12.9173 12.083C13.6257 12.083 14.1673 11.5413 14.1673 10.833C14.1673 10.1247 13.6257 9.58301 12.9173 9.58301ZM7.08398 9.58301C6.37565 9.58301 5.83398 10.1247 5.83398 10.833C5.83398 11.5413 6.37565 12.083 7.08398 12.083C7.79232 12.083 8.33398 11.5413 8.33398 10.833C8.33398 10.1247 7.79232 9.58301 7.08398 9.58301Z" fill="white"/>
                                    <path d="M2.5 6.25024C2.5 5.79191 2.875 5.41691 3.33333 5.41691H6.66667L5.45833 2.37524C5.29167 1.95858 5.5 1.45858 5.91667 1.29191C6.33333 1.12524 6.83333 1.33358 7 1.75024L8.45833 5.37524H11.5L12.9583 1.75024C13.125 1.33358 13.625 1.12524 14.0417 1.29191C14.4583 1.45858 14.6667 1.95858 14.5 2.37524L13.3333 5.41691H16.6667C17.125 5.41691 17.5 5.79191 17.5 6.25024V17.9169C17.5 18.3752 17.125 18.7502 16.6667 18.7502H3.33333C2.875 18.7502 2.5 18.3752 2.5 17.9169V6.25024ZM4.16667 7.08358V17.0836H15.8333V7.08358H4.16667ZM20 14.1669V10.0002C20 9.54191 19.625 9.16691 19.1667 9.16691C18.7083 9.16691 18.3333 9.54191 18.3333 10.0002V14.1669C18.3333 14.6252 18.7083 15.0002 19.1667 15.0002C19.625 15.0002 20 14.6252 20 14.1669ZM0.833333 15.0002C1.29167 15.0002 1.66667 14.6252 1.66667 14.1669V10.0002C1.66667 9.54191 1.29167 9.16691 0.833333 9.16691C0.375 9.16691 0 9.54191 0 10.0002V14.1669C0 14.6252 0.375 15.0002 0.833333 15.0002Z" fill="white"/>
                                </svg>
                            </div>
                            </div>
                            </div>
                            <div v-else>
                                <div v-for="(d, i) in tag_d.default.tag" :key="'tag' + i"
                                    :style="{ position: 'absolute', top: (-20 * i) + 'px', height: '16px', width: '16px', borderRadius: '0px', border: '0px solid #777' }">
                                    <div v-if="typeof tag_d.default.second_tag[d] != 'undefined' && tag_d.default.second_tag[d].length > 0">
                                        <div v-for="(dd, ii) in tag_d.default.second_tag[d]" :key="'sec_tag' + ii"
                                            :style="{ position: 'absolute', top: (-20 * (i * tag_d.default.second_tag[d].length + ii)) + 'px', left: '0px', height: '16px', width: '16px', borderRadius: '0px', border: '0px solid #777',cursor:'pointer' }" @click="clickMarker(tag_d, 1)">
                                            <div
                                                :style="{ position: 'absolute', top: '0px', left: '-9px', height: '16px', width: '16px', backgroundColor: colorMap[dataSource[d - 1].id], borderRadius: '10px', border: '1px solid #777', opacity: showTagList.indexOf(dataSource[d - 1].children[dd - 1].id) != -1 ? 1 : .3 }">
                                            </div>
                                            <div style="position: absolute; left: -7px; top: -3px;">
                                <svg width="12" height="12" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M12.9173 9.58301C12.209 9.58301 11.6673 10.1247 11.6673 10.833C11.6673 11.5413 12.209 12.083 12.9173 12.083C13.6257 12.083 14.1673 11.5413 14.1673 10.833C14.1673 10.1247 13.6257 9.58301 12.9173 9.58301ZM7.08398 9.58301C6.37565 9.58301 5.83398 10.1247 5.83398 10.833C5.83398 11.5413 6.37565 12.083 7.08398 12.083C7.79232 12.083 8.33398 11.5413 8.33398 10.833C8.33398 10.1247 7.79232 9.58301 7.08398 9.58301Z" fill="white"/>
                                    <path d="M2.5 6.25024C2.5 5.79191 2.875 5.41691 3.33333 5.41691H6.66667L5.45833 2.37524C5.29167 1.95858 5.5 1.45858 5.91667 1.29191C6.33333 1.12524 6.83333 1.33358 7 1.75024L8.45833 5.37524H11.5L12.9583 1.75024C13.125 1.33358 13.625 1.12524 14.0417 1.29191C14.4583 1.45858 14.6667 1.95858 14.5 2.37524L13.3333 5.41691H16.6667C17.125 5.41691 17.5 5.79191 17.5 6.25024V17.9169C17.5 18.3752 17.125 18.7502 16.6667 18.7502H3.33333C2.875 18.7502 2.5 18.3752 2.5 17.9169V6.25024ZM4.16667 7.08358V17.0836H15.8333V7.08358H4.16667ZM20 14.1669V10.0002C20 9.54191 19.625 9.16691 19.1667 9.16691C18.7083 9.16691 18.3333 9.54191 18.3333 10.0002V14.1669C18.3333 14.6252 18.7083 15.0002 19.1667 15.0002C19.625 15.0002 20 14.6252 20 14.1669ZM0.833333 15.0002C1.29167 15.0002 1.66667 14.6252 1.66667 14.1669V10.0002C1.66667 9.54191 1.29167 9.16691 0.833333 9.16691C0.375 9.16691 0 9.54191 0 10.0002V14.1669C0 14.6252 0.375 15.0002 0.833333 15.0002Z" fill="white"/>
                                </svg>
                            </div>
                                            <div
                                                :style="{ position: 'absolute', top: '0px', left: '9px', height: '16px', width: '16px', backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id], borderRadius: '0px', border: '1px solid #777', opacity: showTagList.indexOf(dataSource[d - 1].children[dd - 1].id) != -1 ? 1 : .3 }">
                                            </div>
                                            <div style="position: absolute; left: 11px; top: -3px;">
                                <svg width="12" height="12" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M12.9173 9.58301C12.209 9.58301 11.6673 10.1247 11.6673 10.833C11.6673 11.5413 12.209 12.083 12.9173 12.083C13.6257 12.083 14.1673 11.5413 14.1673 10.833C14.1673 10.1247 13.6257 9.58301 12.9173 9.58301ZM7.08398 9.58301C6.37565 9.58301 5.83398 10.1247 5.83398 10.833C5.83398 11.5413 6.37565 12.083 7.08398 12.083C7.79232 12.083 8.33398 11.5413 8.33398 10.833C8.33398 10.1247 7.79232 9.58301 7.08398 9.58301Z" fill="white"/>
                                    <path d="M2.5 6.25024C2.5 5.79191 2.875 5.41691 3.33333 5.41691H6.66667L5.45833 2.37524C5.29167 1.95858 5.5 1.45858 5.91667 1.29191C6.33333 1.12524 6.83333 1.33358 7 1.75024L8.45833 5.37524H11.5L12.9583 1.75024C13.125 1.33358 13.625 1.12524 14.0417 1.29191C14.4583 1.45858 14.6667 1.95858 14.5 2.37524L13.3333 5.41691H16.6667C17.125 5.41691 17.5 5.79191 17.5 6.25024V17.9169C17.5 18.3752 17.125 18.7502 16.6667 18.7502H3.33333C2.875 18.7502 2.5 18.3752 2.5 17.9169V6.25024ZM4.16667 7.08358V17.0836H15.8333V7.08358H4.16667ZM20 14.1669V10.0002C20 9.54191 19.625 9.16691 19.1667 9.16691C18.7083 9.16691 18.3333 9.54191 18.3333 10.0002V14.1669C18.3333 14.6252 18.7083 15.0002 19.1667 15.0002C19.625 15.0002 20 14.6252 20 14.1669ZM0.833333 15.0002C1.29167 15.0002 1.66667 14.6252 1.66667 14.1669V10.0002C1.66667 9.54191 1.29167 9.16691 0.833333 9.16691C0.375 9.16691 0 9.54191 0 10.0002V14.1669C0 14.6252 0.375 15.0002 0.833333 15.0002Z" fill="white"/>
                                </svg>
                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
            </el-tooltip>
                        </div>
                    </div>
                    
                </div>
                <div
                    style="justify-content: space-between; display: flex; position: absolute; bottom: 0px; height: 30px; width: 100%;">
                    <div>
                        <div style="height: 30px;" class="align-class">
                            <a @click="playVideo()">
                                <svg v-if="playTag == 1" t="1706253575488" class="icon" viewBox="0 0 1024 1024"
                                    version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4211" width="30" height="30">
                                    <path
                                        d="M817.088 484.96l-512-323.744C295.232 154.976 282.752 154.592 272.576 160.224 262.336 165.856 256 176.608 256 188.256l0 647.328c0 11.648 6.336 22.4 16.576 28.032 4.8 2.656 10.112 3.968 15.424 3.968 5.952 0 11.904-1.664 17.088-4.928l512-323.616C826.368 533.184 832 522.976 832 512 832 501.024 826.368 490.816 817.088 484.96z"
                                        fill="#ffffff" p-id="4212"></path>
                                </svg>
                                <svg v-else t="1706534722560" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="4218" width="30" height="30">
                                    <path
                                        d="M304 176h80v672h-80zM712 176h-64c-4.4 0-8 3.6-8 8v656c0 4.4 3.6 8 8 8h64c4.4 0 8-3.6 8-8V184c0-4.4-3.6-8-8-8z"
                                        p-id="4219" fill="#ffffff"></path>
                                </svg>
                            </a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <a @click="chooseTime(currentPlayTime - 10 >= 0 ? currentPlayTime - 10 : 0)">
                                <svg t="1706254098018" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="5623" width="25" height="25">
                                    <path
                                        d="M483.157333 71.466667A32 32 0 0 1 512 53.333333c253.312 0 458.666667 205.354667 458.666667 458.666667S765.312 970.666667 512 970.666667 53.333333 765.312 53.333333 512c0-188.16 113.28-349.738667 275.2-420.48a32 32 0 1 1 25.6 58.624 394.666667 394.666667 0 1 0 229.632-26.325333l38.570667 48.213333a32 32 0 0 1-50.005333 39.978667l-85.333334-106.666667a32 32 0 0 1-3.84-33.877333z m-42.666666 262.357333a32 32 0 0 1 18.176 28.842667v298.666666a32 32 0 0 1-64 0v-232.106666l-54.656 43.776a32 32 0 0 1-40.021334-50.005334l106.666667-85.333333a32 32 0 0 1 33.877333-3.84zM608 394.666667a42.666667 42.666667 0 0 0-42.666667 42.666666v149.333334a42.666667 42.666667 0 1 0 85.333334 0v-149.333334a42.666667 42.666667 0 0 0-42.666667-42.666666z m-106.666667 42.666666a106.666667 106.666667 0 0 1 213.333334 0v149.333334a106.666667 106.666667 0 0 1-213.333334 0v-149.333334z"
                                        p-id="5624" fill="white"></path>
                                </svg></a>&nbsp;
                            <a @click="chooseTime(currentPlayTime + 10 <= sumTime ? currentPlayTime + 10 : sumTime)">
                                <svg t="1706253984610" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="4390" width="25" height="25">
                                    <path
                                        d="M53.333333 512C53.333333 258.688 258.688 53.333333 512 53.333333a32 32 0 0 1 25.002667 52.010667l-85.333334 106.666667a32 32 0 0 1-50.005333-40.021334l38.528-48.128C256.512 157.568 117.333333 318.549333 117.333333 512A394.666667 394.666667 0 1 0 669.866667 150.186667a32 32 0 0 1 25.6-58.666667A458.752 458.752 0 0 1 970.666667 512c0 253.312-205.354667 458.666667-458.666667 458.666667S53.333333 765.312 53.333333 512z m387.2-178.176a32 32 0 0 1 18.133334 28.842667v298.666666a32 32 0 0 1-64 0v-232.106666l-54.656 43.776a32 32 0 0 1-40.021334-50.005334l106.666667-85.333333a32 32 0 0 1 33.877333-3.84zM608 394.666667a42.666667 42.666667 0 0 0-42.666667 42.666666v149.333334a42.666667 42.666667 0 1 0 85.333334 0v-149.333334a42.666667 42.666667 0 0 0-42.666667-42.666666z m-106.666667 42.666666a106.666667 106.666667 0 0 1 213.333334 0v149.333334a106.666667 106.666667 0 0 1-213.333334 0v-149.333334z"
                                        p-id="4391" fill="#ffffff"></path>
                                </svg></a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <div style="color: white;">
                                {{ (parseInt(currentPlayTime / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(currentPlayTime / 60).toString().padStart(2, '0')) + ':' + ((currentPlayTime % 60).toString().padStart(2, '0')) }}&nbsp;/&nbsp;{{
                                    (parseInt(sumTime
                                        / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(sumTime /
                                            60).toString().padStart(2, '0')) + ':' + ((sumTime % 60).toString().padStart(2, '0')) }}
                            </div>
                        </div>
                    </div>
                    <div>
                        <div class="align-class" style="height: 30px;">
                            
                            <el-popover :visible="showPop" placement="top" :width="300" trigger="click">
<template #reference>
    <a @click="showPop = !showPop">
                                    <svg t="1709351288980" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="9658" width="25" height="25"><path d="M276.885468 0h470.228952v73.282434h-470.228952zM41.770992 172.091583h940.457903v73.282434H41.770992zM383.02286 298.259506h73.282434v486.656431h-73.282434zM567.694594 298.259506h73.282434v486.656431h-73.282434z" p-id="9659" fill="#ffffff"></path><path d="M775.267088 298.259506l-47.511445 652.457938H296.305313L248.7328 298.259506h-73.282434l50.381673 691.725109a36.641217 36.641217 0 0 0 36.641217 34.015263h499.602994a36.641217 36.641217 0 0 0 36.641217-34.015263l50.07633-691.725109z" p-id="9660" fill="#ffffff"></path></svg>
                                <div v-if="calcDeleteData.length > 0" style="position: absolute; top: -5px; right: -5px; background-color: red; width: 15px; height: 15px; font-size: 10px; color: white; border-radius: 100px;">
                                    {{ calcDeleteData.length }}
                                </div>
                                </a>
</template>
    <div style="max-height: 300px; width: 100%; padding: 0px 0px; overflow-y: auto;">
        <div v-for="(d_d, d_i) in calcDeleteData" :key="'delete_el' + d_i" style="background-color: rgba(0, 0, 0, .3); height: auto;margin-bottom: 10px; padding: 10px; color: white; font-size: 18px;">
            <!-- {{ d_d }} -->
            <div>
                <span style="font-style: italic; font-weight: bold; text-decoration: underline; color: rgb(64, 158, 255);">时间:</span>&nbsp;{{ (parseInt(d_d.time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(d_d.time / 60).toString().padStart(2, '0')) + ':' + ((d_d.time % 60).toString().padStart(2, '0')) }}
            </div>
            <div>
                <span style="font-style: italic; font-weight: bold; text-decoration: underline; color: rgb(64, 158, 255);">描述:</span>&nbsp;{{ d_d.description }}
            </div>
            <div>
                <span style="font-style: italic; font-weight: bold; text-decoration: underline; color: rgb(64, 158, 255);">标签:</span>
                <div v-for="(d, i) in d_d.tag" :key="'type_first_tag' + d" style="display: flex; flex-wrap: wrap;">
                            <div class="align-class"
                                :style="{backgroundColor: colorMap[dataSource[d - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px', justifyContent: 'left' }">
                                <div
                                    :style="{ backgroundColor: colorMap[dataSource[d - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '20px' }">
                                </div>
                                <div>
                                    {{ dataSource[d - 1].label }}
                                </div> &nbsp;
                            </div>
                            <div :style="{ display: 'flex', flexWrap: 'wrap', backgroundColor: '#45464700', padding: '0px 3px 0px 3px' }">
                                <div v-if="typeof d_d.second_tag[d] != 'undefined' && d_d.second_tag[d].length > 0"
                                    style="display: flex; flex-wrap: wrap;">
                                    <div v-for="(dd, ii) in d_d.second_tag[d]" :key="'type_second_tag' + dd"
                                        class="align-class"
                                        :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id] + '40', padding: '3px 8px 3px 5px', 'border-radius': '100px', marginRight: '10px', marginTop: '5px', 'font-size': '15px' }">
                                        <div
                                            :style="{ backgroundColor: colorMap[dataSource[d - 1].children[dd - 1].id], width: '15px', height: '15px', 'margin': '0px 3px 0px 3px', borderRadius: '0px' }">
                                        </div>
                                        <div>
                                            {{ dataSource[d - 1].children[dd - 1].label }}
                                        </div>
                                    </div>
                                </div>
                            </div>
                            </div>
            </div>
            <div style="width: 100%; justify-content: center; display: flex; margin-top: 10px;">
                <el-button type="success" @click="reviseTag(d_d, 0)">恢复</el-button>
                <el-button type="danger" @click="reviseTag(d_d, 4)">删除</el-button>

            </div>
        </div>
    </div>
    </el-popover>
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            <el-button style="margin-top: -8px;" type="primary" @click="AddMarker(currentPlayTime)">
                                添加可用性问题
                            </el-button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { useDataStore } from "../stores/counter";
import { VideoPlayer } from '@videojs-player/vue'
// import 'video.js/dist/video-js.css'
import 'video.js/dist/video-js.css'
import PreviewVideoPlayer from './utils/PreviewVideoPlayer.vue';

export default {
    name: "PCV",
    props: [],
    data() {
        return {
            all_data: [],
            showPop: false,
            dialogVisible: false,
            selectShowLevel: 1,
            loadingTag: false,
            showDefault: false,
            autoShow: false,
            user_info: {
                name: '',
                gender: '',
                age: ''
            },
            config: {
                src: '',
                videoHeight: 1
            },
            pathSetting: 'http://43.153.168.84:8080/',
            defaultShowTag: 0,
            noneDisabledTag: {},
            select_video: '',
            main_data: [],
            showLevelTag: { showFirstTag: false, showSecondTag: [] },
            elHeight: 0,
            elWidth: 0,
            playTag: 1,
            currentPlayTime: 0,
            repeatTime: -1,
            sumTime: 0,
            marker_data: [],
            marker_time: {},
            player: {},
            state: {},
            progressBar: 0,
            colorMap: ['', '#F6D962', '#D5A138', '#EF753A', '#F08F70', '#EB7D81', '#B76E90', '#986EA4', '#9286B3', '#8796BC', '#A3BFCE', '#B4D3B4', '#D1EFFF', '#89D1FF', '#1B90FF', '#0057D2', '#002A86', '#E2D8FF', '#B894FF', '#7858FF', '#470CED', '#1C0C6E', '#FFDCF3', '#FF8AF0', '#F31DED', '#A100C2', '#510080', '#FFDCE8', '#FEADC8', '#FA4F96', '#BA066C', '#71014B', '#FFD5EA', '#FF8CB2', '#EE3939', '#AA0808', '#5A0404', '#FFF3B8', '#FFC933', '#E76500', '#A93E00', '#6D1900', '#EBF5CB', '#97DD40', '#36A41D', '#256F3A', '#164323', '#C2FCEE', '#2CE0BF', '#049F9A', '#046C7A', '#02414C', '#EAECEE', '#A9B4BE', '#5B738B', '#354A5F', '#1A2733'],
            dataSource: [],
            showInfo: false,
            info_data: {
                tag: []
            },
            already_time: {
                nowTime: -1,
                timeSlot: [],
                lastTime: -1
            },
            showTagList: [],
            allTagTimeData: {},
            preview_config: {},
            tagConfig: {
                addPoint: false,
                loadingTag: false,
                tag_name: '',
                tag_description: '',
                add_tag_level: '',
                selectData: []
            },
            dataSelect: -1,
            previewTime: -1,
            timeChangeTag: 0,
            timeChangeType: 'jump',
            timeBeforeChange: -1
        };
    },
    methods: {
        clickEdit() {
            if (this.showDefault) {
                this.showDefault = false;
            }
            this.showMarkerDialog(this.info_data);

            const dataStore = useDataStore();
            const now = Date.now();

            function formatTimestamp(timestamp) {
                const now = new Date(timestamp);
                // 获取月、日、小时、分钟和秒，并补零
                const month = (now.getMonth() + 1).toString().padStart(2, '0');
                const day = now.getDate().toString().padStart(2, '0');
                const hours = now.getHours().toString().padStart(2, '0');
                const minutes = now.getMinutes().toString().padStart(2, '0');
                const seconds = now.getSeconds().toString().padStart(2, '0');

                // 格式化时间戳
                const formattedTimestamp = `${month}/${day} ${hours}:${minutes}:${seconds}`;

                return formattedTimestamp;
            }
            console.log(formatTimestamp(now), now);
            dataStore.reuse_list.push({ video: this.select_video, time: now, date: formatTimestamp(now), video_time: this.info_data.time });
        },
        reviseTag(data, type) {
            data.status = type;
            if (this.calcDeleteData.length == 0) {
                this.showPop = false;
            }
        },
        showAddDialog(tag_type, data) {
            this.tagConfig.tag_name = "";
            this.tagConfig.description = "";
            this.tagConfig.addPoint = true;
            this.tagConfig.selectData = data;

            if (tag_type == 1) {
                this.tagConfig.add_tag_level = '一';
            } else {
                this.tagConfig.add_tag_level = '二';
            }
            this.player.pause();
            this.timeChangeTag = !this.timeChangeTag;
            this.timeChangeType = 'pause';
            this.playTag = 1;
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
            const dataStore = useDataStore();

            // this.id_cnt++;
            // let jsonData = {
            //     tag: this.tagConfig.tag_name,
            //     id: id_cnt,
            //     parent_id: this.tagConfig.add_tag_level == '一' ? 0 : this.tagConfig.selectData.id,
            //     level: this.tagConfig.add_tag_level == '一' ? 1 : 2,
            //     category: this.dataSource,
            //     info: this.all_data,
            //     test: 0
            // };
            // this.tagConfig.loadingTag = true;
            // const dataStore = useDataStore();
            // const data = await dataStore.queryNewTag(jsonData);
            // let new_data = data.data.info;
            // for (let i in this.all_data) {
            //     for (let j in this.all_data[i].info) {
            //         this.all_data[i].info[j].tag = new_data[i].info[j].tag;
            //         this.all_data[i].info[j].second_tag = new_data[i].info[j].second_tag;
            //     }
            // }

            const now = Date.now();

            function formatTimestamp(timestamp) {
                const now = new Date(timestamp);
                // 获取月、日、小时、分钟和秒，并补零
                const month = (now.getMonth() + 1).toString().padStart(2, '0');
                const day = now.getDate().toString().padStart(2, '0');
                const hours = now.getHours().toString().padStart(2, '0');
                const minutes = now.getMinutes().toString().padStart(2, '0');
                const seconds = now.getSeconds().toString().padStart(2, '0');

                // 格式化时间戳
                const formattedTimestamp = `${month}/${day} ${hours}:${minutes}:${seconds}`;

                return formattedTimestamp;
            }
            console.log(formatTimestamp(now), now);
            console.log(this.tagConfig.selectData, this.tagConfig.selectData.l_id,this.info_data.second_tag);
            let unique_id = id_cnt;
            let label = this.tagConfig.tag_name;
            if (this.tagConfig.add_tag_level == '一') {
                let l_id_cnt = this.dataSource.length + 1;
                this.info_data.tag.push(l_id_cnt);
                this.info_data.second_tag[l_id_cnt] = [];
                this.tagConfig.selectData.push({
                    id: id_cnt,
                    l_id: l_id_cnt,
                    level: 1,
                    label: this.tagConfig.tag_name,
                    description: this.tagConfig.description,
                    disabled: false,
                    children: []
                });

            } else {
                let cnt = this.tagConfig.selectData.children.length + 1;
                this.info_data.second_tag[parseInt(this.tagConfig.selectData.l_id)].push(cnt);
                this.tagConfig.selectData.children.push({
                    id: id_cnt,
                    l_id: 1,
                    cnt: cnt,
                    level: 2,
                    label: this.tagConfig.tag_name,
                    description: this.tagConfig.description,
                    disabled: false,
                    children: []
                })
            }
            this.tagConfig.addPoint = false;
            // this.tagConfig.loadingTag = false;

            dataStore.changeTag_list.push({ video: this.select_video, time: now, date: formatTimestamp(now), video_time: this.info_data.time, event: 'add_tag', tag_id: unique_id, label: label });
        },
        showDialog(data) {
            this.dialogVisible = data;
        },
        selectPreview(data, id) {
            // console.log(data);
            this.player.pause();
            this.timeChangeType = 'pause';
            this.timeChangeTag = !this.timeChangeTag;
            this.playTag = 1;
            const time = data.time;
            const video_id = id;
            const name = id + ' ' + (parseInt(time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(time / 60).toString().padStart(2, '0')) + ':' + ((time % 60).toString().padStart(2, '0'));
            this.preview_config = {
                time: time,
                video_id: video_id,
                name: name
            };
            this.dialogVisible = !this.dialogVisible;
        },
        focusTag(id) {
            if (id == 'main') {
                this.showLevelTag.showFirstTag = !this.showLevelTag.showFirstTag;
                for (let i in this.showLevelTag.showSecondTag) {
                    this.showLevelTag.showSecondTag[i] = false;
                }
            } else {
                this.showLevelTag.showFirstTag = false;
                this.showLevelTag.showSecondTag[id] = !this.showLevelTag.showSecondTag[id];
                for (let i in this.showLevelTag.showSecondTag) {
                    if (i != id)
                        this.showLevelTag.showSecondTag[i] = false;
                }
            }
        },
        selectTag(data, id, info, unique_id, unique_tag, label) {
            console.log(data, id, info, unique_id, unique_tag);
            const dataStore = useDataStore();
            const index = data.indexOf(id);
            const u_index = unique_tag.indexOf(unique_id);


            const now = Date.now();

            function formatTimestamp(timestamp) {
                const now = new Date(timestamp);
                // 获取月、日、小时、分钟和秒，并补零
                const month = (now.getMonth() + 1).toString().padStart(2, '0');
                const day = now.getDate().toString().padStart(2, '0');
                const hours = now.getHours().toString().padStart(2, '0');
                const minutes = now.getMinutes().toString().padStart(2, '0');
                const seconds = now.getSeconds().toString().padStart(2, '0');

                // 格式化时间戳
                const formattedTimestamp = `${month}/${day} ${hours}:${minutes}:${seconds}`;

                return formattedTimestamp;
            }
            console.log(formatTimestamp(now), now);
            // dataStore.reuse_list.push({video: this.select_video, time: now, date: formatTimestamp(now), video_time: this.info_data.time });
            if (index == -1) {
                data.push(id);
                unique_tag.push(unique_id);
                if (typeof info != 'number') {
                    info.second_tag[id] = [];
                    this.showLevelTag.showSecondTag.push(false);
                    if (typeof this.noneDisabledTag[unique_id] == 'undefined') {
                        this.noneDisabledTag[unique_id] = 0;
                    }
                    this.noneDisabledTag[unique_id]++;
                }
                dataStore.changeTag_list.push({ video: this.select_video, time: now, date: formatTimestamp(now), video_time: this.info_data.time, event: 'add_tag', tag_id: unique_id, label: label });
                // if (typeof this.allTagTimeData[this.dataSource])
            } else {
                data.splice(index, 1);
                unique_tag.splice(u_index, 1);
                if (typeof info != "number") {
                    this.showLevelTag.showSecondTag.splice(index, 1);
                    this.noneDisabledTag[unique_id]--;
                }
                dataStore.changeTag_list.push({ video: this.select_video, time: now, date: formatTimestamp(now), video_time: this.info_data.time, event: 'delete_tag', tag_id: unique_id, label: label });
            }
            // console.log()
        },
        clickDecision(tag) {
            if (tag == 9) {
                for (let i in this.info_data.default) {
                    this.info_data[i] = this.info_data.default[i];
                }
                this.info_data.repeat_status = 0;
            } else {
                this.info_data.status = tag
            }
            this.showInfo = false;
            this.showLevelTag.showFirstTag = false;
            for (let i in this.showLevelTag.showSecondTag) {
                this.showLevelTag.showSecondTag[i] = false;
            }
        },
        chooseTime(time) {
            this.timeBeforeChange = this.currentPlayTime;
            this.player.currentTime(time);
            this.timeChangeTag = !this.timeChangeTag;
        },
        clickBar(event) {
            let xPos = event.clientX;
            xPos -= 20;
            let progress_width = this.$refs.progressBar.offsetWidth;
            // console.log(progress_width);
            let changePlayTime = Math.floor(this.sumTime * (xPos / progress_width))
            this.timeBeforeChange = this.currentPlayTime;
            this.player.currentTime(changePlayTime);
            this.timeChangeTag = !this.timeChangeTag;
        },
        clickMarker(data, tag) {
            this.autoShow = tag;
            this.timeBeforeChange = this.currentPlayTime;
            this.player.currentTime(data.time);
            this.timeChangeTag = !this.timeChangeTag;
            if (this.playTag) {
                this.player.play();
                // this.timeChangeTag = !this.timeChangeTag;
                // this.timeChangeType = 'play';
                this.playTag = !this.playTag;
            }
            // this.showMarkerDialog(data);
        },
        // clickDefault(data) {
        //     this.player.currentTime(data.time);
        //     if (this.playTag) {
        //         this.player.play();
        //         this.playTag = !this.playTag;
        //     }
        // },
        showMarkerDialog(data) {
            if (!this.showInfo) {
                this.showInfo = !this.showInfo;
            }
            if (this.showDefault) {
                this.showDefault = !this.showDefault;
            }
            data.repeat_status = 1;
            if (document.getElementById('dialogDiv') != null) {
                this.$nextTick(() => {
                    this.$refs.dialogDiv.scrollTop = 0;
                });
            }
            let showLevelTag = { showFirstTag: false, showSecondTag: [] };
            for (let i in data.tag) {
                showLevelTag.showSecondTag.push(false);
            }
            this.showLevelTag = showLevelTag;
            this.info_data = data;
        },
        showDefaultDialog(data) {
            if (!this.showDefault) {
                this.showDefault = !this.showDefault;
            }
            if (this.showInfo) {
                this.showInfo = !this.showInfo;
            }
            data.vision = 1;
            if (document.getElementById('defaultDialogDiv') != null) {
                this.$nextTick(() => {
                    this.$refs.defaultDialogDiv.scrollTop = 0;
                });
            }
            this.info_data = data;
        },
        AddMarker(time) {
            if (!this.showInfo) {
                this.showInfo = !this.showInfo;
            }
            if (document.getElementById('dialogDiv') != null) {
                this.$nextTick(() => {
                    this.$refs.dialogDiv.scrollTop = 0;
                });
            }
            let data_len = this.main_data.info.length;
            let percentage = time / this.sumTime * 100;
            let add_data = {
                "id": data_len + 1,
                "percentage": percentage,
                "status": -1,
                "time": time,
                "description": "",
                "tag": [],
                "second_tag": {},
                "unique_tag": [],
                "user_said": "",
                "reason": "",
                "vision": 1,
                "repeat_status": 1,
                "humanAdd": 1,
                "default": {
                    "description": "",
                    "tag": [],
                    "second_tag": {},
                    "unique_tag": [],
                    "user_said": "",
                    "reason": "",
                }
            }
            this.main_data.info.push(add_data);
            this.marker_data.push(this.main_data.info[this.main_data.info.length - 1]);
            this.marker_time[time] = this.marker_data[this.marker_data.length - 1];
            this.info_data = this.marker_time[time];
        },
        async submitMarker() {
            if (this.info_data.tag.length == 0) {
                const dataStore = useDataStore();
                let jsonData = {
                    video: this.select_video,
                    id: this.info_data.id,
                    tagtime: this.info_data.time,
                    description: this.info_data.description,
                    category: this.dataSource,
                    info: this.all_data,
                    test: dataStore.dataSelect == 0 ? 1 : 0
                };
                this.loadingTag = true;
                const data = await dataStore.queryRecommendation(jsonData);
                console.log(data);
                this.loadingTag = false;
                let cnt_id = -1;
                for (let i in data.data.info[this.select_video].info) {
                    if (this.info_data.id == data.data.info[this.select_video].info[i].id) {
                        cnt_id = i;
                        break;
                    }
                }
                this.info_data.tag = data.data.info[this.select_video].info[cnt_id].tag;
                this.info_data.second_tag = data.data.info[this.select_video].info[cnt_id].second_tag;
                let unique_tag = new Array();
                for (let i in this.info_data.tag) {
                    if (typeof this.info_data.second_tag[this.info_data.tag[i]] == 'undefined') {
                        this.info_data.second_tag[this.info_data.tag[i]] = [];
                    }
                    unique_tag.push(this.dataSource[this.info_data.tag[i] - 1].id);
                    for (let j in this.info_data.second_tag[this.info_data.tag[i]]) {
                        unique_tag.push(this.dataSource[this.info_data.tag[i] - 1].children[this.info_data.second_tag[this.info_data.tag[i]][j] - 1].id);
                    }
                }
                this.info_data.unique_tag = unique_tag;

                // this.info_data.default.tag = data.data.info[this.select_video].info[cnt_id].tag;
                // this.info_data.default.second_tag = data.data.info[this.select_video].info[cnt_id].second_tag;
                // this.info_data.default.unique_tag = unique_tag;
                // this.info_data.default.description = this.info_data.description;


                console.log(this.info_data);
            }
            this.showLevelTag.showFirstTag = false;
            for (let i in this.showLevelTag.showSecondTag) {
                this.showLevelTag.showSecondTag[i] = false;
            }
            this.info_data.status = 0;
        },
        translate(x, y, deg) {
            return `translate(${x}, ${y}) rotate(${deg})`;
        },
        handleEvent(log) {
            // console.log(log);
        },
        handleMounted(payload) {
            // console.log(payload)
            this.player = payload.player;
            this.state = payload.state;
        },
        playVideo() {
            if (this.playTag) {
                this.player.play();
                this.timeChangeType = 'play';
                this.timeChangeTag = !this.timeChangeTag;
                this.timeChangeType = 'play';
                console.log('play');
            } else {
                this.player.pause();
                this.timeChangeTag = !this.timeChangeTag;
                this.timeChangeType = 'pause';
                console.log('pause');
            }
            this.playTag = !this.playTag;
        },
        calcMarker(data, all_data) {
            // console.log(data);
            let res_data = new Array();
            let time_data = new Object();

            this.user_info = {
                gender: data['gender'],
                age: data['year'],
                name: data['name']
            };
            // console.log(this.user_info)
            for (const d of data['info']) {
                let tmp = d;
                tmp.percentage = d.time / this.sumTime * 100;
                res_data.push(tmp);
                time_data[tmp.time] = res_data[res_data.length - 1];
            }
            // console.log(time_data);
            // console.log(this.dataSource)
            let noneDisabledTag = {};

            for (const d of res_data) {
                for (const t of d.tag) {
                    // console.log(t);
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
            this.noneDisabledTag = noneDisabledTag;
            return [res_data, time_data];
        },
        calcAllTag(data) {
            let res_data = {};
            for (const p in data) {
                const p_code = p;
                for (const d of data[p].info) {
                    for (const t of d.tag) {
                        // console.log(t, d.tag, this.dataSource);
                        if (typeof res_data[this.dataSource[t - 1].id] == 'undefined') {
                            res_data[this.dataSource[t - 1].id] = {};
                        }
                        if (typeof res_data[this.dataSource[t - 1].id][p_code] == 'undefined') {
                            res_data[this.dataSource[t - 1].id][p_code] = [];
                        }
                        res_data[this.dataSource[t - 1].id][p_code].push(d);
                        if (typeof d.second_tag[t] != 'undefined')
                            for (const st of d.second_tag[t]) {
                                if (typeof res_data[this.dataSource[t - 1].children[st - 1].id] == 'undefined') {
                                    res_data[this.dataSource[t - 1].children[st - 1].id] = {};
                                }
                                if (typeof res_data[this.dataSource[t - 1].children[st - 1].id][p_code] == 'undefined') {
                                    res_data[this.dataSource[t - 1].children[st - 1].id][p_code] = [];
                                }
                                res_data[this.dataSource[t - 1].children[st - 1].id][p_code].push(d);
                            }
                    }
                }
            }
            return res_data;
        }
    },
    components: { VideoPlayer, PreviewVideoPlayer },
    created() {},
    computed: {
        calcMarkerData() {
            return this.marker_data.filter(d => d.status != 3 && d.status != 4)
        },
        calcHuman() {
            return this.marker_data.filter(d => d.repeat_status == 1 && d.status != 3 && d.status != 4)
        },
        calcDeleteData() {
            return this.marker_data.filter(d => d.status == 3);
        }
    },
    mounted() {
        this.elHeight = this.$refs.mainView.offsetHeight;
        this.elWidth = this.$refs.mainView.offsetWidth;
        if (this.elHeight * 2 > this.elWidth) {
            this.config.videoHeight = this.elWidth / 2;
        } else {
            this.config.videoHeight = this.elHeight;
        }
        const dataStore = useDataStore();
        this.dataSelect = dataStore.dataSelect;
        this.all_data = dataStore.all_data;
        this.dataSource = dataStore.categorySource;
        this.select_video = dataStore.select_video;
        if (this.dataSource.length != 0) {
            this.allTagTimeData = this.calcAllTag(this.all_data);
        }
        // console.log(this.select_video)
        // if (this.select_video != '')
        //     this.config.src = this.pathSetting + 'AI_Tool/' + this.select_video + '/video.mp4'
        this.main_data = this.all_data[this.select_video];
        if (this.showTagList.length == 0) {
            let tagTmp = [];
            for (let i in this.dataSource) {
                tagTmp.push(this.dataSource[i].id);
            }
            this.showTagList = tagTmp;
        }
        /**
         * @description: watch the data changes in the store
         * @return {*}
         */
        dataStore.$subscribe((mutations, state) => {
            // console.log(this.dataSelect, dataStore.dataSelect);
            this.dataSelect = dataStore.dataSelect;
            this.all_data = state.all_data;
            this.dataSource = state.categorySource;
            // if (this.dataSource.length != 0) {
            //     this.allTagTimeData = this.calcAllTag(this.all_data);
            // }
            this.showTagList = state.showTagList;
            this.selectShowLevel = state.selectShowLevel;
            this.select_video = dataStore.select_video;
            this.previewTime = dataStore.currentPlayTime;

            if (this.showTagList.length == 0) {
                let tagTmp = [];
                for (let i in this.dataSource) {
                    tagTmp.push(this.dataSource[i].id);
                    for (let j in this.dataSource[i].children) {
                        tagTmp.push(this.dataSource[i].children[j].id);
                    }
                }
                this.showTagList = tagTmp;
                this.defaultShowTag = 1;
                // dataStore.showTagList = this.showTagList
            }
        });
    },
    watch: {
        timeChangeTag: {
            handler() {
                const dataStore = useDataStore();
                // 获取当前时间
                const now = Date.now();

                function formatTimestamp(timestamp) {
                    const now = new Date(timestamp);
                    // 获取月、日、小时、分钟和秒，并补零
                    const month = (now.getMonth() + 1).toString().padStart(2, '0');
                    const day = now.getDate().toString().padStart(2, '0');
                    const hours = now.getHours().toString().padStart(2, '0');
                    const minutes = now.getMinutes().toString().padStart(2, '0');
                    const seconds = now.getSeconds().toString().padStart(2, '0');

                    // 格式化时间戳
                    const formattedTimestamp = `${month}/${day} ${hours}:${minutes}:${seconds}`;

                    return formattedTimestamp;
                }
                console.log(formatTimestamp(now), now);
                if (this.timeChangeType == 'jump') {
                    dataStore.time_list.push({ video: this.select_video, time: now, date: formatTimestamp(now), video_time: this.timeBeforeChange, type: 'beforeJump' });
                }
                dataStore.time_list.push({ video: this.select_video, time: now, date: formatTimestamp(now), video_time: this.state.currentTime, type: this.timeChangeType });
                this.timeChangeType = 'jump';
            }
        },
        previewTime: {
            handler() {
                const dataStore = useDataStore();
                if (this.select_video != '') {
                    this.config.src = this.pathSetting + 'AI_Tool/' + this.select_video + '/video.mp4'
                    this.main_data = this.all_data[this.select_video];
                    this.$nextTick(() => {
                        this.timeBeforeChange = this.currentPlayTime;
                        this.player.currentTime(dataStore.currentPlayTime);
                        this.timeChangeTag = !this.timeChangeTag;

                        console.log(dataStore.currentPlayTime);
                    })
                }
            }
        },
        dataSelect: {
            handler(newVal, oldVal) {
                // console.log(newVal, oldVal)
                // Object.assign(this.$data, this.$options.data());
                this.dataSelect = newVal;
                // console.log(this.$data)
            }
        },
        all_data: {
            handler() {
                if (this.dataSource.length != 0) {
                    this.allTagTimeData = this.calcAllTag(this.all_data);
                    // console.log(this.allTagTimeData, this.all_data);
                }
            },
            deep: true
        },
        select_video: {
            handler(newVal, oldVal) {
                this.sumTime = 0;
                this.noneDisabledTag = {};
                this.playTag = 1;
                if (oldVal != '') {
                    if (typeof this.all_data == 'object' && typeof this.all_data[oldVal] != 'undefined') {
                        if (typeof this.all_data[oldVal]['already_time'] == 'undefined') {
                            this.all_data[oldVal]['already_time'] = this.already_time;
                        }
                        this.all_data[oldVal]['already_time'] = this.already_time;
                    }
                }
                if (newVal != '') {
                    if (typeof this.all_data == 'object' && typeof this.all_data[oldVal] != 'undefined') {
                        if (typeof this.all_data[newVal]['already_time'] == 'undefined') {
                            this.all_data[newVal]['already_time'] = {
                                nowTime: -1,
                                timeSlot: [],
                                lastTime: -1
                            };
                        }
                        this.already_time = this.all_data[newVal]['already_time']
                    }
                }
                const dataStore = useDataStore();
                if (this.select_video != '') {
                    this.config.src = this.pathSetting + 'AI_Tool/' + this.select_video + '/video.mp4'
                    this.main_data = this.all_data[this.select_video];
                    this.$nextTick(() => {
                        this.timeBeforeChange = this.currentPlayTime;
                        this.player.currentTime(dataStore.currentPlayTime);
                        this.timeChangeTag = !this.timeChangeTag;
                        console.log(dataStore.currentPlayTime);
                    })
                }
            }
        },
        showTagList: {
            handler() {
                // console.log(this.showTagList)
            }
        },
        state: {
            handler() {
                this.currentPlayTime = parseInt(this.state.currentTime);
                if (!isNaN(this.state.duration))
                    this.sumTime = parseInt(this.state.duration);
                if (this.sumTime != 0) {
                    this.progressBar = (this.currentPlayTime / this.sumTime) * 100;
                }
                if (this.showInfo == true && typeof this.marker_time[this.repeatTime + 1] != 'undefined') {
                    this.showInfo = false;
                }
                if (this.showDefault == true && typeof this.marker_time[this.repeatTime + 1] != 'undefined') {
                    this.showDefault = false;
                }
                if (typeof this.marker_time[this.currentPlayTime] != 'undefined' && this.repeatTime != this.currentPlayTime && this.marker_time[this.currentPlayTime].status != 3) {
                    if (this.autoShow == 0 && this.marker_time[this.currentPlayTime].vision == 0) {
                        this.showDefaultDialog(this.marker_time[this.currentPlayTime]);
                    } else if (this.autoShow == 1) {
                        this.showDefaultDialog(this.marker_time[this.currentPlayTime]);
                    } else if (this.autoShow == 2) {
                        this.showMarkerDialog(this.marker_time[this.currentPlayTime]);
                    }
                    this.autoShow = 0;
                }
                this.repeatTime = this.currentPlayTime;
                if (this.already_time.nowTime == -1) {
                    if (this.currentPlayTime == 1) {
                        this.already_time.timeSlot.push([0, 1]);
                    } else if (this.currentPlayTime > 1) {
                        this.already_time.timeSlot.push([this.currentPlayTime, this.currentPlayTime]);
                    }
                    this.already_time.lastTime = this.currentPlayTime;
                    this.already_time.nowTime = 0;
                } else {
                    if (this.already_time.lastTime == this.currentPlayTime - 1) {
                        this.already_time.lastTime = this.currentPlayTime;
                        this.already_time.timeSlot[this.already_time.nowTime][1] = this.currentPlayTime;
                    } else {
                        let innerTag = -1;
                        for (let i in this.already_time.timeSlot) {
                            if (this.currentPlayTime >= this.already_time.timeSlot[i][0] && this.currentPlayTime <= this.already_time.timeSlot[i][1]) {
                                innerTag = i;
                                break;
                            }
                        }
                        if (innerTag == -1) {
                            this.already_time.timeSlot.push([this.currentPlayTime, this.currentPlayTime]);
                            this.already_time.nowTime = this.already_time.timeSlot.length - 1;
                            this.already_time.lastTime = this.currentPlayTime
                        } else {
                            this.already_time.nowTime = innerTag;
                        }
                    }
                }
            },
            deep: true
        },
        sumTime: {
            handler() {
                if (this.dataSource.length != 0)
                    [this.marker_data, this.marker_time] = this.calcMarker(this.main_data, this.all_data);
            }
        },
        noneDisabledTag: {
            handler() {
                const dataStore = useDataStore();
                dataStore.noneDisabledTag = this.noneDisabledTag;
            },
            deep: true
        }
    },
};
</script>

<style>
.align-class {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* .progress_marker {
    border: 0px solid red;
}

.progress_marker:hover {
    border-width: 0px;
} */

.el-textarea__inner {
    background-color: #45464700;
    color: white;
    font-size: 18px;
}

.show_info_dialog {
    --el-dialog-bg-color: #454647;
    color: white;
    position: absolute;
    /* left: calc(35vw - 12.5%);
    top: calc(5%); */
    right: calc(0px + 25px);
    border-radius: 15px;
    /* left: 100px; */
}

.show_info_dialog_pre {
    --el-dialog-bg-color: #454647;
    color: white;
    position: absolute;
    left: calc(35vw - 12.5%);
    top: calc(5%);
    /* right: calc(0px + 25px); */
    border-radius: 15px;
    /* left: 100px; */
}

.add_main_dialog {
    --el-dialog-bg-color: #454647;
    color: white;
    position: absolute;
    left: calc(35vw - 7.5%);
    top: calc(15%);
    border-radius: 15px;
}

.marker_description {
    background-color: #454647;
    margin-top: -20px;
    margin-left: -0px;
    color: white;
}

.show_info_dialog .el-dialog__body {
    padding: 3px 20px 3px 20px;
}

:deep(.video-js .vjs-big-play-button .vjs-icon-placeholder:before) {
    position: relative;
}

:deep(.vjs-button > .vjs-icon-placeholder:before) {
    position: relative;
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
    background: rgba(201, 201, 202, 1);
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

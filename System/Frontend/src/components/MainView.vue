<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-07-01 00:15:05
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-08-01 19:30:44
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

<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-02-01 19:32:17
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-03-03 22:17:13
-->
<template>
    <div style="width: 100%; height: 100%;">
        <div class="subRect" style="left: 0px; width: 24%">
            <div class="subtitle">
                <span>
                                &nbsp;问题列表
                            </span>
            </div>
            <div class="subContent">
                <div v-for="(problemData, problem_Type) in problemList" :key="'problemList_' + problem_Type" class="container" style="background-color: #ddd;">
                    <div>
                        {{ problem_Type }}
                    </div>
                    <div v-for="(problem, problem_i) in problemData" :key="'s_problem' + problem_i" class="container" :style="{ 'border-color': problem.selectStatus == 1 ? 'rgba(255, 159, 49, 1)' : '#AAA', backgroundColor: 'white' }">
                        <div v-if="problem.selectStatus == 1" :style="{
                                position: 'absolute',
                                right: '-7px',
                                top: 'calc(50% - 15px)',
                                backgroundColor: 'white',
                                borderRadius: '10px',
                            }">
                            <svg t="1721313950720" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="4589" width="20" height="20">
                                <path
                                    d="M448 448H192v128h256v256h128V576h256V448H576V192H448v256z m64 576A512 512 0 1 1 512 0a512 512 0 0 1 0 1024z"
                                    fill="#FF9F31" p-id="4590"></path>
                            </svg>
                        </div>
                        <div class="align-class">
                            <span class="align-class">
                                <span class="title uxButton" @click="selectProblem(problem, 1)">
                                        {{ problem.Video + ' ' + problem.Timestamp }}
                                </span> &nbsp;
                                <div @click="problem.finishTag = !problem.finishTag" class="uxButton">
                                    <svg v-if="problem.finishStatus == 0" t="1722527575157" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7245" width="20" height="20"><path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64z m0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z" p-id="7246" fill="#d81e06"></path><path d="M512 688m-48 0a48 48 0 1 0 96 0 48 48 0 1 0-96 0Z" p-id="7247" fill="#d81e06"></path><path d="M488 576h48c4.4 0 8-3.6 8-8V296c0-4.4-3.6-8-8-8h-48c-4.4 0-8 3.6-8 8v272c0 4.4 3.6 8 8 8z" p-id="7248" fill="#d81e06"></path></svg>&nbsp;

                                    <svg v-else-if="problem.finishStatus == 1" t="1722527087709" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5166" width="20" height="20"><path d="M542.272 64a454.4 454.4 0 1 1-0.704 908.8c-140.608-3.2-261.76-62.912-361.6-177.664a32 32 0 0 1 48.256-42.048c88.32 101.504 192.64 152.96 314.048 155.712a390.4 390.4 0 1 0-388.992-423.872l73.344-73.216a32 32 0 0 1 48.96 40.832l-3.712 4.416L163.2 565.568a32 32 0 0 1-40.832 3.712l-4.48-3.712L9.408 456.96a32 32 0 0 1 40.832-48.96l4.48 3.712 38.336 38.4A454.528 454.528 0 0 1 542.272 64z m0 224.192a32 32 0 0 1 32 32v178.752l162.368 156.352a32 32 0 0 1-44.416 46.08l-172.16-165.76a32 32 0 0 1-9.792-23.04V320.192a32 32 0 0 1 32-32z" fill="#f4ea2a" p-id="5167"></path></svg>&nbsp;
                                    <svg v-else t="1722527413330" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6210" width="18" height="18"><path d="M512 1024a512 512 0 1 1 512-512 512 512 0 0 1-512 512z m0-960a448 448 0 1 0 416.736 611.52A27.552 27.552 0 0 1 928 672a31.424 31.424 0 0 1 10.656-23.36A448 448 0 0 0 512 64z m246.624 342.72l-288 288A32 32 0 0 1 448 704a31.52 31.52 0 0 1-24.256-11.84l-0.32 0.32-160-192 0.32-0.32A31.392 31.392 0 0 1 256 480a32 32 0 0 1 32-32 31.52 31.52 0 0 1 24.256 11.84l0.32-0.32 137.6 165.12 263.232-263.36a32.064 32.064 0 0 1 45.216 45.44z" fill="#1afa29" p-id="6211"></path></svg>
                                </div>
                                &nbsp;
                                <div v-if="problem.finishTag" class="align-class">
                                    | &nbsp;
                                    <svg class="uxButton" @click="changeStatus(problem, 0)" t="1722527575157" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="7245" width="20" height="20"><path d="M512 64C264.6 64 64 264.6 64 512s200.6 448 448 448 448-200.6 448-448S759.4 64 512 64z m0 820c-205.4 0-372-166.6-372-372s166.6-372 372-372 372 166.6 372 372-166.6 372-372 372z" p-id="7246" fill="#d81e06"></path><path d="M512 688m-48 0a48 48 0 1 0 96 0 48 48 0 1 0-96 0Z" p-id="7247" fill="#d81e06"></path><path d="M488 576h48c4.4 0 8-3.6 8-8V296c0-4.4-3.6-8-8-8h-48c-4.4 0-8 3.6-8 8v272c0 4.4 3.6 8 8 8z" p-id="7248" fill="#d81e06"></path></svg>&nbsp;

                                    <svg class="uxButton" @click="changeStatus(problem, 1)" t="1722527087709" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5166" width="20" height="20"><path d="M542.272 64a454.4 454.4 0 1 1-0.704 908.8c-140.608-3.2-261.76-62.912-361.6-177.664a32 32 0 0 1 48.256-42.048c88.32 101.504 192.64 152.96 314.048 155.712a390.4 390.4 0 1 0-388.992-423.872l73.344-73.216a32 32 0 0 1 48.96 40.832l-3.712 4.416L163.2 565.568a32 32 0 0 1-40.832 3.712l-4.48-3.712L9.408 456.96a32 32 0 0 1 40.832-48.96l4.48 3.712 38.336 38.4A454.528 454.528 0 0 1 542.272 64z m0 224.192a32 32 0 0 1 32 32v178.752l162.368 156.352a32 32 0 0 1-44.416 46.08l-172.16-165.76a32 32 0 0 1-9.792-23.04V320.192a32 32 0 0 1 32-32z" fill="#f4ea2a" p-id="5167"></path></svg>&nbsp;
                                    <svg class="uxButton" @click="changeStatus(problem, 2)" t="1722527413330" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6210" width="18" height="18"><path d="M512 1024a512 512 0 1 1 512-512 512 512 0 0 1-512 512z m0-960a448 448 0 1 0 416.736 611.52A27.552 27.552 0 0 1 928 672a31.424 31.424 0 0 1 10.656-23.36A448 448 0 0 0 512 64z m246.624 342.72l-288 288A32 32 0 0 1 448 704a31.52 31.52 0 0 1-24.256-11.84l-0.32 0.32-160-192 0.32-0.32A31.392 31.392 0 0 1 256 480a32 32 0 0 1 32-32 31.52 31.52 0 0 1 24.256 11.84l0.32-0.32 137.6 165.12 263.232-263.36a32.064 32.064 0 0 1 45.216 45.44z" fill="#1afa29" p-id="6211"></path></svg>
                                </div>
                            </span>
                            <span class="icon uxButton">
                                <svg t="1721144591461" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                    xmlns="http://www.w3.org/2000/svg" p-id="1750" width="20" height="20">
                                    <path
                                        d="M509.92 795.84c157.904 0 285.92-128.016 285.92-285.92C795.84 352 667.808 224 509.92 224 352 224 224 352 224 509.92c0 157.904 128 285.92 285.92 285.92z m0 48C325.504 843.84 176 694.32 176 509.92 176 325.504 325.504 176 509.92 176c184.416 0 333.92 149.504 333.92 333.92 0 184.416-149.504 333.92-333.92 333.92z m-2.448-400.704h16a16 16 0 0 1 16 16v201.728a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16V459.136a16 16 0 0 1 16-16z m0-100.176h16a16 16 0 0 1 16 16v23.648a16 16 0 0 1-16 16h-16a16 16 0 0 1-16-16v-23.648a16 16 0 0 1 16-16z"
                                        fill="#6c6c6c" p-id="1751"></path>
                                </svg>

                            </span>
                        </div>
                        <div class="content">
                            {{ problem.Problem }}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="subRect" style="left: calc(24% + 10px); width: calc(35% - 20px)">
            <div class="subtitle">
                <div>
                    &nbsp;起始灵感
                </div>
                <span>
                    <el-popover placement="bottom" :width="100" trigger="click">
                        <template #reference>
                            <!-- 评估指标 -->
                            <span class="uxButton">评估指标</span>
                            
                        </template>
                        <el-checkbox v-for="(d, i) in criterionList" :key="'criterionList_' + i" style="margin-top: 10px;" :value="d.value" v-model="criterionList[i].status">
                            <el-input v-model="criterionList[i].label" style="width: 100px;"></el-input>
                            <!-- {{ d }} -->
                        </el-checkbox>
                        <div>
                            <el-button style="margin-top: 10px;" @click="addMetric()"><svg t="1722493771653" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="12842" width="15" height="15"><path d="M576 64H448v384H64v128h384v384h128V576h384V448H576z" fill="#262626" p-id="12843"></path></svg></el-button>
                        </div>
                    </el-popover>
                    | 
                    <span class="uxButton" @click="compareTag = !compareTag">
                        对比视图
                    </span>
                </span>
            </div>
            <div class="subContent" :style="{height: compareTag == true ? 'calc(58% - 12px)' : 'calc(100% - 30px)'}">
                <div v-for="(problem, problem_i) in startingPoint" :key="'startingPoint_' + problem_i" class="container" :style="{ 'border-color': problem.selectStatus == 1 ? 'rgba(255, 159, 49, 1)' : '#AAA' }">
                    <div class="align-class">
                        <span class="uxButton" @click="selectProblem(problem, 2)" style="display: flex; align-items: center;">
                                    <span class="title">{{ '启发' + (problem_i + 1) }}</span>
                                </span>
                        <span style="display: flex;">
                                    <span @click="editStartingPoint(problem)" class="uxButton">
                                        <svg t="1720712559835" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                            xmlns="http://www.w3.org/2000/svg" p-id="4277" width="20" height="20">
                                            <path
                                                d="M955.2384 1024H40.0896a40.0896 40.0896 0 0 1 0-80.1792h915.1488a40.0896 40.0896 0 0 1 0 80.1792zM745.472 390.2976L559.4112 200.704l102.9632-105.0112 186.6752 189.5424-103.2704 105.0624h-0.3072zM406.3744 735.744l-230.2464 40.704 44.7488-229.6832L503.808 257.4848l186.0608 189.5424-283.4944 288.768z m523.7248-480.9728L692.5312 12.5952A42.7008 42.7008 0 0 0 663.2448 0a41.5744 41.5744 0 0 0-29.2352 12.5952L157.0816 497.3568a39.2192 39.2192 0 0 0-12.288 22.528L88.3712 819.2a39.7824 39.7824 0 0 0 10.8032 35.1232 38.2976 38.2976 0 0 0 34.5088 11.4176L430.08 813.568a39.4752 39.4752 0 0 0 23.9616-11.3664l476.0576-486.5536a43.6224 43.6224 0 0 0 12.288-29.2864 43.3152 43.3152 0 0 0-12.288-29.2352v-2.3552z"
                                                p-id="4278" fill="#6c6c6c"></path>
                                        </svg>
                                    </span> &nbsp;
                        <span @click="deleteStartingPoint(problem.sid)" class="uxButton">
                                        <svg t="1721312041338" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                            xmlns="http://www.w3.org/2000/svg" p-id="2821" width="20" height="20">
                                            <path
                                                d="M608 768c-17.696 0-32-14.304-32-32V384c0-17.696 14.304-32 32-32s32 14.304 32 32v352c0 17.696-14.304 32-32 32zM416 768c-17.696 0-32-14.304-32-32V384c0-17.696 14.304-32 32-32s32 14.304 32 32v352c0 17.696-14.304 32-32 32zM928 224H768v-64c0-52.928-42.72-96-95.264-96H352c-52.928 0-96 43.072-96 96v64H96c-17.696 0-32 14.304-32 32s14.304 32 32 32h832c17.696 0 32-14.304 32-32s-14.304-32-32-32z m-608-64c0-17.632 14.368-32 32-32h320.736C690.272 128 704 142.048 704 160v64H320v-64z"
                                                p-id="2822" fill="#6c6c6c"></path>
                                            <path
                                                d="M736.128 960H288.064c-52.928 0-96-43.072-96-96V383.52c0-17.664 14.336-32 32-32s32 14.336 32 32V864c0 17.664 14.368 32 32 32h448.064c17.664 0 32-14.336 32-32V384.832c0-17.664 14.304-32 32-32s32 14.336 32 32V864c0 52.928-43.072 96-96 96z"
                                                p-id="2823" fill="#6c6c6c"></path>
                                        </svg>
                                    </span>
                        </span>
                    </div>
                    <div class="content">
                        <div v-if="startingPoint[problem_i].editStatus == 0">
                            {{ problem.content }}
                        </div>
    
                        <div v-else class="edit-class">
                            <!-- <div>
                                                    Edit
                                                </div> -->
                            <el-input v-model="startingPoint[problem_i].content" style="width: 100%" :rows="3" type="textarea" placeholder="Please input" />
                            <div class="align-class" style="margin-top: 5px; justify-content: right;">
                                <div class="edit-button" style="background-color: #c6e6f8; cursor: pointer;">
                                    <svg t="1719773054162" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="12918" width="20" height="20">
                                                <path
                                                    d="M939.733333 495.866667c-206.266667-44.266667-367.333333-205.333333-411.6-411.6L512 9.2l-16.533333 77.066667c-44 204.933333-204.266667 365.2-409.2 409.2L9.2 512l76.266667 16.4c205.466667 44.133333 366 204.533333 410 410l16.4 76.4 15.866666-74.133333c44.4-206.8 206-368.4 412.8-412.8L1014.666667 512l-74.933334-16.133333z"
                                                    fill="#ffffff" p-id="12919"></path>
                                            </svg>
                                </div>&nbsp;
                                <div class="edit-button" style="background-color: #11a420; cursor: pointer;">
                                    <svg t="1719773588642" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="13943" width="18" height="18">
                                        <path
                                            d="M887.904 298.208c-12.864-12.064-33.152-11.488-45.216 1.408L415.936 753.984l-233.12-229.696C170.208 511.872 149.952 512 137.536 524.608c-12.416 12.576-12.256 32.864 0.352 45.248l256.48 252.672c0.096 0.096 0.224 0.128 0.32 0.224 0.096 0.096 0.128 0.224 0.224 0.32 2.016 1.92 4.448 3.008 6.784 4.288 1.152 0.672 2.144 1.664 3.36 2.144 3.776 1.472 7.776 2.24 11.744 2.24 4.192 0 8.384-0.832 12.288-2.496 1.312-0.544 2.336-1.664 3.552-2.368 2.4-1.408 4.896-2.592 6.944-4.672 0.096-0.096 0.128-0.256 0.224-0.352 0.064-0.096 0.192-0.128 0.288-0.224l449.184-478.208C901.44 330.592 900.768 310.336 887.904 298.208z"
                                            p-id="13944" fill="#ffffff"></path>
                                    </svg>
                                </div>&nbsp;
                                <div class="edit-button" style="background-color: #b35156; cursor: pointer;">
                                    <svg t="1719773612425" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="16085" width="18" height="18">
                                                <path
                                                    d="M571.733333 512l226.133334-226.133333c17.066667-17.066667 12.8-42.666667-4.266667-59.733334-17.066667-17.066667-42.666667-17.066667-59.733333 0L512 452.266667 285.866667 226.133333c-17.066667-17.066667-42.666667-12.8-59.733334 4.266667-17.066667 17.066667-17.066667 42.666667 0 59.733333l226.133334 226.133334-226.133334 226.133333c-17.066667 17.066667-21.333333 42.666667-4.266666 59.733333 17.066667 17.066667 42.666667 21.333333 59.733333 4.266667l4.266667-4.266667 226.133333-226.133333 226.133333 226.133333c17.066667 17.066667 46.933333 12.8 59.733334-4.266666 12.8-17.066667 12.8-38.4 0-55.466667L571.733333 512z"
                                                    p-id="16086" fill="#ffffff"></path>
                                            </svg>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="info-content" :ref="'info_content' + problem_i">
                        <div class="evaluation-button" @click="showRadar(problem)">评估</div>
                        <div class="evaluation-radar" v-if="problem.showTag == 1">
                            <div class="square-svg" ref="radar">
                                <svg width="100%" :height="radarWidth / zoomTag * .6">
                                    <g :transform="translate(radarWidth / zoomTag / 2, radarWidth / zoomTag * .6 / 2)">
                                        <path v-for="(d, i) in strokePath" :key="'radar_' + i" :d="d.d" :stroke="d.stroke" :stroke-width="d.width" :fill="d.fill" fill-opacity=".3"></path>
                                        <path v-for="(d, i) in problem.radarPath" :key="'radar_' + i" :d="d.d" :stroke="d.stroke" :stroke-width="d.width" :fill="d.fill" fill-opacity=".3"></path>
                                        <g>
                                            <text v-for="(d, i) in problem.radarPoint" :key="'radar_point_' + i" :x="d.x * (radarWidth + 20) / 2" :y="d.y * (radarWidth + 20) / 2" :fill="d.fill" font-size="12px" text-anchor="middle">{{ d.text + ': ' + d.score }}

                                            </text>
                                        </g>
                                    </g>
                                </svg>
                            </div>
                            <div>
                                <div>
                                    <h3>
                                        评估原因
                                    </h3>
                                    <template v-for="(d, i) in problem.score">
                                        <div v-if="criterionList[parseInt(i[i.length - 1]) - 1].status == true">
                                            <strong>{{ criterion[i] }}: <span>{{ d.Score }}</span></strong> &nbsp;
                                            <span>
                                                {{d.Reason}}
                                            </span>
                                        </div>
                                    </template>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <hr v-if="compareTag == true" style="margin: 5px;">
            <div v-if="compareTag == true"  style="width: 100%; height: calc(42% - 30px);">
                <div style="z-index: 100; position: absolute; top: 0px; left: 0px">
                    <el-checkbox v-for="(problem, problem_i) in startingPoint" :key="'startingPoint_radar_' + problem_i" v-model="startingPoint[problem_i].radarStatus">
                        <span class="align-class"><div :style="{width: '10px', height: '10px', backgroundColor: radarColor[problem_i], borderRadius: '50%'}"></div> &nbsp; {{ "启发" + (parseInt(problem.sid) + 1) }}</span>
                    </el-checkbox>
                </div>
                <svg width="100%" height="100%">
                    <g :transform="translate(radarWidth / zoomTag / 2, radarWidth / zoomTag / 2)">
                        <path v-for="(d, i) in strokePath" :key="'radar_' + i" :d="d.d" :stroke="d.stroke" :stroke-width="d.width" :fill="d.fill" fill-opacity=".3"></path>
                        <g v-for="(problem, problem_i) in startingPoint" :key="'startingPoint_radar_' + problem_i">
                            <path v-for="(d, i) in problem.radarPath" :key="'radar_' + i" :d="d.d" :stroke="radarColor[problem_i]" :stroke-width="d.width" :fill="radarColor[problem_i]" fill-opacity=".3" :opacity="problem.radarStatus ? 1 : 0"></path>
                        </g>
                        <text v-for="(d, i) in startingPoint[0].radarPoint" :key="'radar_point_' + i" :x="d.x * (radarWidth + 20) / 2" :y="d.y * (radarWidth + 20) / 2" :fill="d.fill" font-size="12px" text-anchor="middle">{{ d.text }}

                        </text>
                        
                    </g>
                </svg>
            </div>
        </div>
        <div class="subRect" style="left: calc(59% + 0px); width: calc(41% - 0px)">
    
            <div class="subtitle" @click="showText">
                &nbsp;最终方案
            </div>
            <div class="subContent" style="overflow: inherit;">
                <div v-for="(problem, problem_i) in solution" :key="'startingPoint_' + problem_i" class="container" style="height: 100%;">
                    <div class="align-class">
                        <span class="title">
                                    {{ '最终方案' + (problem_i + 1) }}
                                </span>
                        <span v-if="problem.editStatus == 1" @click="editSolution(problem)" class="evaluation-button" style="position: absolute; right: 80px;">保存</span>
    
                        <span style="display: flex;">
                            <span class="uxButton">
                                <svg t="1722488059992" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="6602" width="20" height="20"><path d="M779.410286 789.406476c94.598095-52.565333 157.305905-143.36 157.305904-246.735238 0-65.389714-25.35619-125.610667-67.681523-174.470095 3.023238-19.260952 4.583619-38.66819 4.729904-58.124191 0-9.020952-0.975238-17.846857-1.560381-26.721523C950.51581 347.672381 999.619048 438.174476 999.619048 538.819048c0 112.88381-61.68381 213.089524-157.305905 277.650285v175.884191l-176.323048-107.032381a473.86819 473.86819 0 0 1-75.337143 6.241524c-121.124571 0-198.168381-45.689905-273.066666-117.857524 12.336762 0.682667 24.576 1.560381 37.107809 1.560381 17.554286 0 34.913524-0.828952 52.028953-2.194286 59.14819 40.082286 102.4 64.219429 183.929904 64.219429a403.260952 403.260952 0 0 0 81.383619-8.533334l107.373715 70.558477v-109.860572z m-346.063238-76.166095a933.790476 933.790476 0 0 1-105.813334-8.192l-177.298285 101.180952v-175.835428C68.022857 561.39581 24.380952 465.578667 24.380952 352.743619 24.380952 157.93981 207.189333 0 433.347048 0c188.025905 0 377.514667 157.93981 377.514666 352.743619s-151.649524 360.496762-377.514666 360.496762zM320.512 642.681905c26.136381 5.36381 84.74819 8.533333 112.835048 8.533333 191.146667 0 314.61181-131.900952 314.611809-294.619428 0-162.718476-158.183619-294.570667-314.611809-294.570667-196.510476 0-346.063238 131.900952-346.063238 294.570667 0 103.375238 49.103238 185.344 125.854476 246.735238v109.909333l107.373714-70.558476z m285.891048-239.567238a46.518857 46.518857 0 1 1 47.152762-46.518857 46.811429 46.811429 0 0 1-47.152762 46.518857z m-188.757334 0a46.518857 46.518857 0 1 1 47.152762-46.518857 46.86019 46.86019 0 0 1-47.152762 46.518857z m-188.757333 0a46.518857 46.518857 0 1 1 47.152762-46.518857 46.811429 46.811429 0 0 1-47.152762 46.518857z" p-id="6603" fill="#6c6c6c"></path></svg>
                            </span>&nbsp;
                            <span @click="editSolution(problem)" class="uxButton">
                                <svg t="1720712559835" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                            xmlns="http://www.w3.org/2000/svg" p-id="4277" width="20" height="20">
                                    <path d="M955.2384 1024H40.0896a40.0896 40.0896 0 0 1 0-80.1792h915.1488a40.0896 40.0896 0 0 1 0 80.1792zM745.472 390.2976L559.4112 200.704l102.9632-105.0112 186.6752 189.5424-103.2704 105.0624h-0.3072zM406.3744 735.744l-230.2464 40.704 44.7488-229.6832L503.808 257.4848l186.0608 189.5424-283.4944 288.768z m523.7248-480.9728L692.5312 12.5952A42.7008 42.7008 0 0 0 663.2448 0a41.5744 41.5744 0 0 0-29.2352 12.5952L157.0816 497.3568a39.2192 39.2192 0 0 0-12.288 22.528L88.3712 819.2a39.7824 39.7824 0 0 0 10.8032 35.1232 38.2976 38.2976 0 0 0 34.5088 11.4176L430.08 813.568a39.4752 39.4752 0 0 0 23.9616-11.3664l476.0576-486.5536a43.6224 43.6224 0 0 0 12.288-29.2864 43.3152 43.3152 0 0 0-12.288-29.2352v-2.3552z"
                                                p-id="4278" fill="#6c6c6c"></path>
                                        </svg>
                                    </span> &nbsp;
                        <span @click="deleteStartingPoint(problem.sid)" class="uxButton">
                                        <svg t="1721312041338" class="icon" viewBox="0 0 1024 1024" version="1.1"
                                            xmlns="http://www.w3.org/2000/svg" p-id="2821" width="20" height="20">
                                            <path
                                                d="M608 768c-17.696 0-32-14.304-32-32V384c0-17.696 14.304-32 32-32s32 14.304 32 32v352c0 17.696-14.304 32-32 32zM416 768c-17.696 0-32-14.304-32-32V384c0-17.696 14.304-32 32-32s32 14.304 32 32v352c0 17.696-14.304 32-32 32zM928 224H768v-64c0-52.928-42.72-96-95.264-96H352c-52.928 0-96 43.072-96 96v64H96c-17.696 0-32 14.304-32 32s14.304 32 32 32h832c17.696 0 32-14.304 32-32s-14.304-32-32-32z m-608-64c0-17.632 14.368-32 32-32h320.736C690.272 128 704 142.048 704 160v64H320v-64z"
                                                p-id="2822" fill="#6c6c6c"></path>
                                            <path
                                                d="M736.128 960H288.064c-52.928 0-96-43.072-96-96V383.52c0-17.664 14.336-32 32-32s32 14.336 32 32V864c0 17.664 14.368 32 32 32h448.064c17.664 0 32-14.336 32-32V384.832c0-17.664 14.304-32 32-32s32 14.336 32 32V864c0 52.928-43.072 96-96 96z"
                                                p-id="2823" fill="#6c6c6c"></path>
                                        </svg>
                                    </span>
                        </span>
                    </div>
                    <div class="content" style="height: calc(58% - 20px); overflow-y: auto">
                        <div v-if="problem.editStatus == 0">
                            <v-md-preview :text="finalSolutionContent"></v-md-preview>
                        </div>
                        <div v-else>
                            <v-md-editor mode="edit" v-model="finalSolutionContent"></v-md-editor>
                        </div>
                    </div>
    
                    <hr style="margin: 5px;">
                    <div style="width: 100%; height: calc(42% - 20px);">
                        <span class="title">
                                    设计更新
                                </span>
                        <img src="../assets/figure/redesign1.png" alt="" style="width: 100%;">
                        <h3>Change</h3>
                        <ol>
                            <li>Add a color-coded overlay in the image</li>
                            <li>Add a tooltip next to the “Remove background”</li>
                        </ol>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import problemData from '../assets/problem.json';
export default {
    name: "APP",
    props: ["msgH"],
    data() {
        return {
            msg1: "Hello, main!",
            raw_data: {},
            problemList: [],
            startingPoint: [],
            solution: [],
            editContent: '',
            selectProblemIndexList: [],
            strokePath: [],
            compareTag: false,
            radarColor: ['#C5C2ED', '#96C8ED', '#FFCEBF', '#FFCEEE'],
            criterion: {
                Criterion_1: "Complexity",
                Criterion_2: "Feasibility",
                Criterion_3: "Impact",
                Criterion_4: "Relationally"
            },
            criterionList: [
                {
                    value: "Criterion_1",
                    label: "Complexity",
                    status: true
                },
                {
                    value: "Criterion_2",
                    label: "Feasibility",
                    status: true
                },
                {
                    value: "Criterion_3",
                    label: "Impact",
                    status: true
                },
                {
                    value: 'Criterion_4',
                    label: "Relationally",
                    status: true
                }
            ],
            selectAttributeList: [],
            radarPoint: [],
            radarPath: [],
            radarWidth: 0,
            zoomTag: .5,
            finalSolutionContent: '## Redesign Steps for Interface Updates and Guidance Elements\n### Interface Updates\n1. **Dynamic Feedback Implementation**\n- Design overlays that show real-time changes and effects during the background removal process.\n- Use animations to highlight changes in the image as the user applies different settings.\n2. **Visual Enhancements**\n- Implement color-coded feedback to help users understand success (green) or errors (red) quickly.\n### Guidance Elements\n1. **Placement of Help Icons**\n- Position help icons (e.g., question marks or lightbulbs) next to frequently used tools.\n- Ensure the icons are placed consistently across the interface to maintain user familiarity.\n2. **Design of Help Icons**\n- Choose a design that is easily recognizable and fits within the overall aesthetic of the application.\n- Consider using tooltips that appear on hover to provide immediate help without a click, ensuring a non-intrusive experience.\n3. **Content of Tooltips**\n- Develop tooltips content that provides quick and practical advice tailored to the tool it\'s associated with.\n- Include short descriptions, quick tips, and links to more in-depth tutorials.\n4. **Interactive Elements**\n- Make tooltips interactive, allowing users to access additional resources directly from the tooltip (e.g., video tutorials, step-by-step guides).\nThis revised design plan focuses on enhancing visual feedback and providing context-sensitive guidance without overwhelming the user during the rapid background removal process.'
        };
    },
    methods: {
        changeStatus(data, tag) {
            data.finishStatus = tag;
            data.finishTag = !data.finishTag;
        },
        addMetric() {
            this.criterionList.push({
                value: 'Criterion_' + (this.criterionList.length + 1),
                label: '',
                status: false
            });
            this.criterion['Criterion_' + (this.criterionList.length + 1)] = '';
        },
        showText() {
            console.log(JSON.stringify(this.finalSolutionContent));
        },
        translate(x, y) {
            return `translate(${x}, ${y})`;
        },
        showRadar(data) {
            if (data.showTag == 0) {
                data.showTag = 1;
                
            } else {
                data.showTag = 0;
            }
        },
        calcRadar() {
            for (let data of this.startingPoint) {
                this.radarWidth = (this.$refs.info_content0[0].offsetWidth - 10) * this.zoomTag;
                let radarPoint = [];
                let radarPath = [];
                let strokePath = [];
                let radarCnt = 0;
                for (let i in this.criterionList) {
                    if (this.criterionList[i].status == true) { 
                        radarCnt++;
                    }
                }
                console.log(radarCnt, this.criterionList);
                // let radarAngle = 360 / Object.keys(this.criterion).length;
                let radarAngle = 360 / radarCnt;
                // console.log(radarAngle);
                let selectPath = {
                    d: 'M ',
                    width: 1,
                    fill: '#0057D2',
                    stroke: '#0057D2'
                }
                let tmpCnt = 0;
                // for (let i = 0; i < Object.keys(this.criterion).length; i++) {
                for (let i = 0; i < this.criterionList.length; ++i) {
                    if (this.criterionList[i].status == false) {
                        continue;
                    }
                    selectPath.d += (data['score'][`Criterion_${i + 1}`]['Score'] / 5 * this.radarWidth / 2) * Math.cos((tmpCnt * radarAngle / 180) * Math.PI) + ',' + (data['score'][`Criterion_${i + 1}`]['Score'] / 5 * this.radarWidth / 2) * Math.sin((tmpCnt * radarAngle / 180) * Math.PI) + ' ';
                    // if (i != Object.keys(this.criterion).length - 1) {
                    radarPoint.push({
                        x: Math.cos((tmpCnt * radarAngle / 180) * Math.PI),
                        y: Math.sin((tmpCnt * radarAngle / 180) * Math.PI),
                        text: this.criterion[`Criterion_${i + 1}`],
                        score: data['score'][`Criterion_${i + 1}`]['Score']
                    });
                    strokePath.push({
                        d: 'M 0 0 L ' + Math.cos((tmpCnt * radarAngle / 180) * Math.PI) * this.radarWidth / 2 + ' ' + Math.sin((tmpCnt * radarAngle / 180) * Math.PI) * this.radarWidth / 2,
                        width: .5,
                        stroke: '#ccc',
                        fill: 'none'
                    });
                    tmpCnt++;
                    if (tmpCnt != radarCnt) {
                        selectPath.d += 'L ';
                    } else {
                        selectPath.d += 'Z';
                    }
                }
                // tmpCnt = 0;

                for (let i = 0; i < 6; ++i) {
                    let tmpPath = 'M ';
                    for (let j = 0; j < radarPoint.length; ++j) {
                        tmpPath += (i / 5 * this.radarWidth / 2) * radarPoint[j].x + ',' + (i / 5 * this.radarWidth / 2) * radarPoint[j].y + ' ';
                        if (j != radarPoint.length - 1) {
                            tmpPath += 'L ';
                        } else {
                            tmpPath += 'Z';
                        }
                    }
                    strokePath.push({
                        d: tmpPath,
                        width: .5,
                        stroke: '#ccc',
                        fill: 'none'
                    });
                }

                // console.log(radarPoint, radarPath);
                radarPath.push(selectPath);
                // return [radarPoint, radarPath];
                data.radarPath = radarPath;
                data.radarPoint = radarPoint;
                this.strokePath = strokePath;
            }
        },
        getProblemList() {
            this.problemList = problemData;
        },
        getStartingPoint() {
            this.startingPoint = this.problemList[this.selectProblemIndexList[0]].startingPoint;
        },
        getSolution() {
            this.solution = this.problemList[this.selectProblemIndexList[0]].solution;
            for (const criterion in this.criterion) {
                radarPoint.push({
                    name: this.criterion[criterion],
                    value: this.raw_data[criterion]
                });
            }
            return [];
        },
        selectProblem(data, level) {
            if (level == 1) {
                this.startingPoint = this.startingPointsProcess(this.raw_data.startingPoint, data.pid);
                for (const pi in this.problemList) {
                    for (const d of this.problemList[pi]) {
                        d.selectStatus = 0;
                    }
                }
            }
            if (level == 2) {
                this.solution = this.finalSolutionProcess(this.raw_data.finalSolution, data.sid);
                for (const d of this.startingPoint) {
                    d.selectStatus = 0;
                }

            }
            data.selectStatus = 1;
        },
        editStartingPoint(data) {
            data.editStatus = 1;
        },
        editSolution(data) {
            data.editStatus = !data.editStatus;
        },
        problemProcess(data) {
            let problemData = {};
            for (let i in data) {
                if (typeof problemData[data[i]['problemType']] == 'undefined') {
                    problemData[data[i]['problemType']] = [];
                }
                problemData[data[i]['problemType']].push(data[i]);
            }
            return problemData;
        },
        startingPointsProcess(s_data, pid) {
            let startingPointData = [];
            for (let i in s_data) {
                if (s_data[i].pid == pid) {
                    startingPointData.push(s_data[i]);
                }
            }
            return startingPointData;
        },
        finalSolutionProcess(s_data, sid) {
            let finalSolutionData = [];
            for (let i in s_data) {
                if (s_data[i].sid == sid) {
                    finalSolutionData.push(s_data[i]);
                }
            }
            return finalSolutionData;
        },
        deleteStartingPoint(id) {
            const index = this.startingPoint.findIndex(d => {
                return d.sid == id
            })
            console.log(index);

            if (index > -1) {
                this.startingPoint.splice(index, 1);
            }
        },
        deleteSolution(id) {
            const index = this.solution.indexOf(id);
            console.log(index);
            if (index > -1) {
                this.solution.splice(index, 1);
            }
        }
    },
    created() {},
    mounted() {
        // let dataStore = useDataStore();
        // dataStore.$subscribe(() => {
        //     this.leftShow = dataStore.leftShow;
        //     this.video_select = dataStore.select_video;
        // })
        console.log(problemData)
        this.raw_data = problemData;
        this.problemList = this.problemProcess(problemData.problem);
        this.startingPoint = this.startingPointsProcess(this.raw_data.startingPoint, 1);
        this.solution = this.finalSolutionProcess(this.raw_data.finalSolution, 0);
        // this.radarPoint = this.calcRadarPoint()
        // this.startingPointStatus = [];
        // for (let i = 0; i < this.startingPoint.length; ++i) {
        //     this.startingPointStatus.push(0);
        // }
    },
    updated () {
        if (this.strokePath.length == 0)
            this.calcRadar();
    },
    watch: {
        criterionList: {
            handler () {
                // console.log(this.criterionList);
                for (let d of this.criterionList) {
                    if (d.label != this.criterion[d.value]) {
                        this.criterion[d.value] = d.label;
                    }
                }
                this.calcRadar();
            },
            deep: true
        }
    },
    components: {}
}
</script>

<style>
.square-svg {
    width: 100%;
}

.square-svg::before {
    padding-top: 100%;
}

.uxButton {
    cursor: pointer;
}

.align-class {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.subRect {
    position: absolute;
    top: 0px;
    /* border: 1px solid #AAA; */
    height: 100%;
    border-radius: 3px;
}

.subtitle {
    font-size: 18px;
    font-weight: bold;
    text-align: left;
    height: 25px;
    background-color: #FF9F31;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.subtitle span {
    padding: 3px;
    border-radius: 3px;
}

.subContent {
    height: calc(100% - 25px);
    padding: 5px 0px;
    overflow-y: auto;
}

.subContent .container {
    text-align: left;
    margin-bottom: 5px;
    border: 1px solid #AAA;
    padding: 5px;
    border-radius: 3px;
    /* font-family: giulia; */
}

.subContent .title {
    color: #777;
    text-decoration: underline;
}

.container .icon {
    display: flex;
    align-items: center;
    /* justify-content: space-between; */
}

.edit-class {
    width: 100%;
    background: rgba(255, 159, 49, .7);
    padding: 5px;
}

.edit-button {
    padding: 2px 10px;
    border-radius: 100px;
    border: 0px solid #AAA;
}

.info-content {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: start;
    height: 100%;
    padding: 5px;
    /* background: rgba(255, 159, 49, .7); */
}

.evaluation-button {
    padding: 2px 10px;
    border-radius: 100px;
    border: 0px solid #AAA;
    background: rgba(255, 159, 49, .7);
    color: white;
    cursor: pointer;
}

.evaluation-button:hover {}

.evaluation-radar {
    width: 100%;
    margin-top: 10px;
}
</style>

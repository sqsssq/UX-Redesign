<!--
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2024-01-24 17:02:12
 * @LastEditors: Qing Shi
 * @LastEditTime: 2024-02-21 23:22:40
-->
<template>
    <PreviewVideoPlayer :dialogVisible="dialogVisible" :config="config" @showDialog="showDialog" />
    <div class="frameworkBody">
        <div style=" height: 30px;text-align: left; font-size: 24px; color: white; font-weight: bold; justify-content: space-between; display: flex;">
            <span>总体分析</span>
            <span style="font-size: 20px;">
                    <!-- <el-button type="warning" @click="viewTag = !viewTag">
                        {{ viewTag == false ? '网络图':'旭日图'}}
                    </el-button> -->
                    <el-button type="success" @click="overviewTag = true">
                        概览模式
                    </el-button>
                    <el-button type="primary" @click="overviewTag = false">
                        筛选模式
                    </el-button>
                </span>
        </div>
        <div style="width: 100%; height: calc(100% - 30px); margin-top: 10px;">
            <div id="networkView" ref="networkView" class="align-class" style="height: calc(100% - 20px); width: 100%; border: 0px solid white">
                <svg id="networkSvg" height="100%" width="100%"></svg>
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
            elWidth: 0,
            elHeight: 0,
            viewTag: false,
            select_video: '',
            all_data: [],
            category_data: [],
            pathSetting: '/',
            chart_data: [],
            showTagList: [],
            selectShowLevel: 1,
            dialogVisible: false,
            overviewTag: false,
            config: {},
            colorMap: ['', '#F6D962', '#D5A138', '#EF753A', '#F08F70', '#EB7D81', '#B76E90', '#986EA4', '#9286B3', '#8796BC', '#A3BFCE', '#B4D3B4', '#D1EFFF', '#89D1FF', '#1B90FF', '#0057D2', '#002A86', '#E2D8FF', '#B894FF', '#7858FF', '#470CED', '#1C0C6E', '#FFDCF3', '#FF8AF0', '#F31DED', '#A100C2', '#510080', '#FFDCE8', '#FEADC8', '#FA4F96', '#BA066C', '#71014B', '#FFD5EA', '#FF8CB2', '#EE3939', '#AA0808', '#5A0404', '#FFF3B8', '#FFC933', '#E76500', '#A93E00', '#6D1900', '#EBF5CB', '#97DD40', '#36A41D', '#256F3A', '#164323', '#C2FCEE', '#2CE0BF', '#049F9A', '#046C7A', '#02414C', '#EAECEE', '#A9B4BE', '#5B738B', '#354A5F', '#1A2733'],
        };
    },
    methods: {
        showDialog(data) {
            this.dialogVisible = data;
        },
        calcNetwork(data) {
            // console.log(data);
            let res_data = new Array();
            if (this.selectShowLevel == 1) {
                for (const i in this.all_data) {
                    if (this.overviewTag || this.select_video == '' || this.select_video == i) {
                        for (const j in this.all_data[i].info) {
                            for (const k in this.all_data[i].info[j].tag) {
                                const tag = this.all_data[i].info[j].tag[k] - 1;
                                if (this.overviewTag || this.showTagList.indexOf(this.category_data[tag].id) != -1) {
                                    const time = this.all_data[i].info[j].time;
                                    const source_name = i + ' ' + (parseInt(time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(time / 60).toString().padStart(2, '0')) + ':' + ((time % 60).toString().padStart(2, '0'));
                                    const target_name = this.category_data[tag].label;
                                    const status = this.all_data[i].info[j].status
                                    if (status != 3) {
                                        let status_color = ['#5a9cf8', '#00FF7F', '#ecb050'];
                                        res_data.push({
                                            source: source_name,
                                            source_type: 3,
                                            source_color: status_color[status],
                                            target: target_name,
                                            target_type: 1,
                                            target_color: this.colorMap[this.category_data[tag].id],
                                            type: 0,
                                            config: {
                                                time: time,
                                                video_id: i,
                                                name: source_name
                                            }
                                        });
                                        res_data.push({
                                            source: this.select_video == '' || this.overviewTag ? '所有视频' : this.select_video,
                                            source_type: 0,
                                            source_color: '#222c44',
                                            target: target_name,
                                            target_type: 1,
                                            target_color: this.colorMap[this.category_data[tag].id],
                                            type: 1,
                                            config: {}
                                        })
                                    }
                                }
                            }
                        }
                    }
                }
            } else {
                for (const i in this.all_data) {
                    if (this.overviewTag || this.select_video == '' || this.select_video == i) {
                        for (const j in this.all_data[i].info) {
                            for (const k in this.all_data[i].info[j].tag) {
                                for (const tk in this.all_data[i].info[j].second_tag[this.all_data[i].info[j].tag[k]]) {
                                    const tag = this.all_data[i].info[j].tag[k] - 1;
                                    const sec_tag = this.all_data[i].info[j].second_tag[this.all_data[i].info[j].tag[k]][tk] - 1;
                                    if (this.overviewTag || this.showTagList.indexOf(this.category_data[tag].children[sec_tag].id) != -1) {
                                        const time = this.all_data[i].info[j].time;
                                        const source_name = i + ' ' + (parseInt(time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(time / 60).toString().padStart(2, '0')) + ':' + ((time % 60).toString().padStart(2, '0'));
                                        const target_name = this.category_data[tag].label;
                                        const sec_target_name = this.category_data[tag].children[sec_tag].label;
                                        const status = this.all_data[i].info[j].status
                                        if (status != 3) {
                                            let status_color = ['#5a9cf8', '#00FF7F', '#ecb050'];
                                            res_data.push({
                                                source: source_name,
                                                source_type: 3,
                                                source_color: status_color[status],
                                                target: sec_target_name,
                                                target_type: 2,
                                                target_color: this.colorMap[this.category_data[tag].children[sec_tag].id],
                                                type: 0,
                                                config: {
                                                    time: time,
                                                    video_id: i,
                                                    name: source_name
                                                }
                                            });
                                            res_data.push({
                                                source: target_name,
                                                source_type: 1,
                                                source_color: this.colorMap[this.category_data[tag].id],
                                                target: sec_target_name,
                                                target_type: 2,
                                                target_color: this.colorMap[this.category_data[tag].children[sec_tag].id],
                                                type: 1,
                                                config: {}
                                            });
                                            res_data.push({
                                                source: this.select_video == '' || this.overviewTag ? '所有视频' : this.select_video,
                                                source_type: 0,
                                                source_color: '#222c44',
                                                target: target_name,
                                                target_type: 1,
                                                target_color: this.colorMap[this.category_data[tag].id],
                                                type: 2,
                                                config: {}
                                            })
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
            return res_data;
        },
        paintNetwork(data) {
            function linkArc(d) {
                const r = Math.hypot(d.target.x - d.source.x, d.target.y - d.source.y);
                // A${r},${r} 0 0,1 ${d.target.x},${d.target.y}
                return `
                    M${d.source.x},${d.source.y}
                    L${d.target.x},${d.target.y}
                `;
            }
            let drag = simulation => {
                function dragstarted(event, d) {
                    if (!event.active) simulation.alphaTarget(0.3).restart();
                    d.fx = d.x;
                    d.fy = d.y;
                }

                function dragged(event, d) {
                    d.fx = event.x;
                    d.fy = event.y;
                }

                function dragended(event, d) {
                    if (!event.active) simulation.alphaTarget(0);
                    d.fx = null;
                    d.fy = null;
                }

                return d3.drag()
                    .on("start", dragstarted)
                    .on("drag", dragged)
                    .on("end", dragended);
            }
            const width = this.elWidth;
            const height = this.elHeight;
            const types = Array.from(new Set(data.map(d => d.type)));
            // const nodes = Array.from(new Set(data.flatMap(l => [l.source, l.target])), id => ({ id }));
            let tmp_nodes = new Array();
            for (const d of data) {
                tmp_nodes.push({
                    id: d.source,
                    color: d.source_color,
                    type: d.source_type,
                    config: d.type == 0 ? d.config : {}
                });
                tmp_nodes.push({
                    id: d.target,
                    color: d.target_color,
                    type: d.target_type,
                    config: {}
                });
            }
            const nodes = Array.from(new Set(tmp_nodes.map(JSON.stringify))).map(JSON.parse);
            const links = data.map(d => Object.create(d));
            // console.log(data.flatMap(l => [l.source, l.target]))
            // console.log(nodes)
            const simulation = d3.forceSimulation(nodes)
                .force('link', d3.forceLink(links).id(d => d.id))
                .force('charge', d3.forceManyBody().strength(-300 / 1000 * this.elHeight))
                .force("center", d3.forceCenter(width / 2, height / 2))
                .force("x", d3.forceX())
                .force("y", d3.forceY());

            d3.selectAll('#all-network').remove();

            const svg = d3.select('#networkSvg').append('g').attr('id', 'all-network')

            d3.select('#networkSvg').call(d3.zoom().scaleExtent([1, 10]).on('zoom', zoomed));

            function zoomed({ transform }) {
                // console.log(transform);
                d3.select('#all-network').attr('transform', transform);
            }
            // .attr("viewBox", [-width / 2, -height / 2, width, height]);

            svg.append("defs").selectAll("marker")
                .data(types)
                .join("marker")
                .attr("id", d => `arrow-${d}`)
                .attr("viewBox", "0 -5 10 10")
                .attr("refX", 15)
                .attr("refY", -0.5)
                .attr("markerWidth", 6)
                .attr("markerHeight", 6)
                .attr("orient", "auto")
                .append("path")
                .attr("fill", 'red')
                .attr("d", "M0,-5L10,0L0,5");
            const link = svg.append("g")
                .attr("fill", "none")
                .attr("stroke-width", 1.5)
                .selectAll("path")
                .data(links)
                .join("path")
                .attr("stroke", d => 'white')
            // .attr("marker-end", d => `url(${new URL(`#arrow-${d.type}`, location)})`);

            const node = svg.append("g")
                .attr("fill", "currentColor")
                .attr("stroke-linecap", "round")
                .attr("stroke-linejoin", "round")
                .selectAll("#nodes")
                .attr('id', 'nodes')
                .data(nodes)
                .join("g")
                .on('mouseenter', (e, d) => {
                    d3.select('#text_node' + d.index).attr('display', 'flow');
                })
                .on('mouseout', (e, d) => {
                    d3.select('#text_node' + d.index).attr('display', dd => dd.type != 0 ? 'none' : 'flow');
                })
                .on('click', (e, d) => {
                    // console.log(d.type)
                    if (d.type == 3) {
                        this.dialogVisible = !this.dialogVisible;
                        this.config = d.config;
                    }
                })
                .call(drag(simulation));

            node.append("path")
                .attr("stroke", "white")
                .attr("stroke-width", 1.5)
                .attr('fill', d => d.color)
                .attr('d', d => {
                    // console.log(d)
                    let path_g = ['M-25 -15L-25 15L45 15L45 -15Z', 'M0,0a10,10 0 1, 0 20,0a10,10 0 1,0 -20,0', 'M0 -10L0 10L20 10L20 -10Z', 'M10 -10L5 0L10 10L15 0Z'];
                    let path = path_g[d.type];
                    return path;
                })
            const sentence = svg.append("g")
                .attr("fill", "currentColor")
                .attr("stroke-linecap", "round")
                .attr("stroke-linejoin", "round")
                .selectAll("#sentence")
                .attr('id', 'sentence')
                .data(nodes)
                .join("g")
                .attr('id', (d, i) => {
                    // console.log(i);
                    return 'text_node' + d.index;
                })
                .attr('display', d => d.type == 0 ? 'flex' : 'none')
            // .call(drag(simulation));
            sentence.append("text")
                .attr("x", 10)
                .attr("y", d => d.type == 0 ? '.3em' : "-1em")
                .attr('text-anchor', 'middle')
                .text(d => d.id)
                .clone(true)
                .lower()
                .attr("fill", "none")
                .attr("stroke", "white")
                .attr("stroke-width", 3)

            simulation.on("tick", () => {
                link.attr("d", linkArc);
                node.attr("transform", d => `translate(${d.x - 10},${d.y})`);
                sentence.attr("transform", d => `translate(${d.x - 10},${d.y})`);
            });
            // invalidation.then(() => simulation.stop());
        },
        calcSun(data) {
            // console.log(data);
            let res_data = {
                name: 'all',
                text: '所有视频',
                color: '#222c44',
                children: []
            };
            let t_data = new Object();
            if (this.selectShowLevel == 1) {
                for (const i in this.all_data) {
                    if (this.overviewTag || this.select_video == '' || this.select_video == i) {
                        for (const j in this.all_data[i].info) {
                            for (const k in this.all_data[i].info[j].tag) {
                                const tag = this.all_data[i].info[j].tag[k] - 1;
                                if (this.overviewTag || this.showTagList.indexOf(this.category_data[tag].id) != -1) {
                                    const time = this.all_data[i].info[j].time;
                                    const source_name = i + ' ' + (parseInt(time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(time / 60).toString().padStart(2, '0')) + ':' + ((time % 60).toString().padStart(2, '0'));
                                    const target_name = this.category_data[tag].label;
                                    const target_id = this.category_data[tag].id;
                                    const status = this.all_data[i].info[j].repeat_status;
                                    if (this.all_data[i].info[j].status != 3) {
                                        let status_color = ['#5a9cf8', '#00FF7F', '#ecb050'];
                                        if (typeof t_data[target_id] == 'undefined') {
                                            t_data[target_id] = {
                                                name: target_id,
                                                text: target_name,
                                                children: [],
                                                color: this.colorMap[this.category_data[tag].id],
                                                type: 1
                                            }
                                        }
                                        t_data[target_id].children.push({
                                            name: source_name,
                                            text: source_name,
                                            value: 1,
                                            color: status_color[status],
                                            config: {
                                                time: time,
                                                video_id: i,
                                                name: source_name
                                            },
                                            type: 0
                                        })
                                    }
                                }
                            }
                        }
                    }
                }

                for (const i in t_data) {
                    res_data.children.push(t_data[i]);
                }
                console.log(res_data);
            } else {
                for (const i in this.all_data) {
                    if (this.overviewTag || this.select_video == '' || this.select_video == i) {
                        for (const j in this.all_data[i].info) {
                            for (const k in this.all_data[i].info[j].tag) {
                                for (const tk in this.all_data[i].info[j].second_tag[this.all_data[i].info[j].tag[k]]) {
                                    const tag = this.all_data[i].info[j].tag[k] - 1;
                                    const sec_tag = this.all_data[i].info[j].second_tag[this.all_data[i].info[j].tag[k]][tk] - 1;
                                    if (this.overviewTag || this.showTagList.indexOf(this.category_data[tag].children[sec_tag].id) != -1) {
                                        const time = this.all_data[i].info[j].time;
                                        const source_name = i + ' ' + (parseInt(time / 60 / 60).toString().padStart(2, '0')) + ':' + (parseInt(time / 60).toString().padStart(2, '0')) + ':' + ((time % 60).toString().padStart(2, '0'));
                                        const target_name = this.category_data[tag].label;
                                        const target_id = this.category_data[tag].id;
                                        const sec_target_name = this.category_data[tag].children[sec_tag].label;
                                        const sec_target_id = this.category_data[tag].children[sec_tag].id;
                                        const status = this.all_data[i].info[j].repeat_status;
                                        if (this.all_data[i].info[j].status != 3) {
                                            let status_color = ['#5a9cf8', '#00FF7F'];

                                            if (typeof t_data[target_id] == 'undefined') {
                                                t_data[target_id] = {
                                                    name: target_id,
                                                    text: target_name,
                                                    children: [],
                                                    color: this.colorMap[this.category_data[tag].id],
                                                    type: 1,
                                                    sub: {}
                                                }
                                            }

                                            if (typeof t_data[target_id].sub[sec_target_id] == 'undefined') {
                                                t_data[target_id].sub[sec_target_id] = {
                                                    name: sec_target_id,
                                                    text: sec_target_name,
                                                    children: [],
                                                    color: this.colorMap[this.category_data[tag].children[sec_tag].id],
                                                    type: 2
                                                }
                                            }

                                            t_data[target_id].sub[sec_target_id].children.push({
                                                name: source_name,
                                                text: source_name,
                                                value: 1,
                                                color: status_color[status],
                                                config: {
                                                    time: time,
                                                    video_id: i,
                                                    name: source_name
                                                },
                                                type: 0
                                            })
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                for (let i in t_data) {
                    for (let j in t_data[i].sub) {
                        t_data[i].children.push(t_data[i].sub[j]);
                    }
                    res_data.children.push(t_data[i]);
                }
            }
            return res_data;
        },
        paintSunBurst(data) {
            console.log(data)
            const width = (this.elWidth > this.elHeight ? this.elHeight : this.elWidth) / 2 * .95;
            const height = width;
            const radius = width / (this.selectShowLevel + 2);


            // Compute the layout.
            const hierarchy = d3.hierarchy(data)
                .sum(d => d.value)
                .sort((a, b) => b.value - a.value);
            const root = d3.partition()
                .size([2 * Math.PI, hierarchy.height + 1])
                (hierarchy);
            root.each(d => d.current = d);
            console.log(root, hierarchy)

            // Create the arc generator.
            const arc = d3.arc()
                .startAngle(d => d.x0)
                .endAngle(d => d.x1)
                .padAngle(d => Math.min((d.x1 - d.x0) / 2, 0.005))
                .padRadius(radius * 1.5)
                .innerRadius(d => d.y0 * radius)
                .outerRadius(d => Math.max(d.y0 * radius, d.y1 * radius - 1))


            d3.selectAll('#all-network').remove();

            const svg = d3.select('#networkSvg').append('g').attr('id', 'all-network').attr('transform', `translate(${this.elWidth / 2}, ${this.elHeight / 2})`);
            d3.select('#networkSvg').on('.zoom', null)
            const path = svg.append("g")
                .selectAll("path")
                .data(root.descendants())
                .join("path")
                .attr("fill", d => { return d.data.color; })
                .attr("fill-opacity", d => arcVisible(d.current) ? (d.children ? .6 : .6) : .6)
                .attr("pointer-events", d => arcVisible(d.current) ? "auto" : "none")
                .attr("d", d => {
                    return arc(d.current)
                });

            // Make them clickable if they have children.
            path.filter(d => {
                return d.children
            })
                .style("cursor", "pointer")
                .on("click", clicked);

                path.filter(d => {
                return d.children == undefined
            })
                .style("cursor", "pointer")
                .on("click", (e, d) => {
                    console.log(d);

                    this.dialogVisible = !this.dialogVisible;
                        this.config = d.data.config;
                });
                
            // const format = d3.format(",d");
            // path.append("title")
            //     .text(d => `${d.ancestors().map(d => d.data.name).reverse().join("/")}\n${format(d.value)}`);

            const label = svg.append("g")
                .attr("pointer-events", "none")
                .attr("text-anchor", "middle")
                .style("user-select", "none")
                .selectAll("text")
                .data(root.descendants())
                .join("text")
                .attr("dy", "0.35em")
                .attr("fill-opacity", d => {
                    // console.log(+labelVisible(d.current), labelVisible(d.current))
                    return +labelVisible(d.current)
                })
                .attr("transform", d => labelTransform(d.current))
                .attr('fill', 'white')
                .text(d => {
                    return d.data.text
                });

            const parent = svg.append("circle")
                .datum(root)
                .attr("r", radius)
                .attr("fill", "none")
                .attr("pointer-events", "all")
                .on("click", clicked);

            // Handle zoom on click.
            function clicked(event, p) {
                console.log(p)
                parent.datum(p.parent || root);

                root.each(d => d.target = {
                    x0: Math.max(0, Math.min(1, (d.x0 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
                    x1: Math.max(0, Math.min(1, (d.x1 - p.x0) / (p.x1 - p.x0))) * 2 * Math.PI,
                    y0: Math.max(0, d.y0 - p.depth),
                    y1: Math.max(0, d.y1 - p.depth)
                });

                const t = svg.transition().duration(750);

                // Transition the data on all arcs, even the ones that aren’t visible,
                // so that if this transition is interrupted, entering arcs will start
                // the next transition from the desired position.
                path.transition(t)
                    .tween("data", d => {
                        const i = d3.interpolate(d.current, d.target);
                        return t => d.current = i(t);
                    })
                    .filter(function(d) {
                        return +this.getAttribute("fill-opacity") || arcVisible(d.target);
                    })
                    .attr("fill-opacity", d => arcVisible(d.target) ? (d.children ? .6 : .6) : .6)
                    .attr("pointer-events", d => arcVisible(d.target) ? "auto" : "auto")

                    .attrTween("d", d => () => arc(d.current));

                label.filter(function(d) {
                        return +this.getAttribute("fill-opacity") || labelVisible(d.target);
                    }).transition(t)
                    .attr("fill-opacity", d => {
                        console.log(+labelVisible(d.target), labelVisible(d.target))
                        return +labelVisible(d.target)
                    })
                    .attrTween("transform", d => () => labelTransform(d.current));
            }

            function arcVisible(d) {
                return d.y1 <= 3 && d.y0 >= 1 && d.x1 > d.x0;
            }

            function labelVisible(d) {
                return d.y1 <= 3 && d.y0 >= 1 && (d.y1 - d.y0) * (d.x1 - d.x0) > 0.03;
            }

            function labelTransform(d) {
                const x = (d.x0 + d.x1) / 2 * 180 / Math.PI;
                const y = (d.y0 + d.y1) / 2 * radius;
                return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`;
            }
        }
    },
    components: { PreviewVideoPlayer },
    created() {},
    computed: {},
    mounted() {
        this.elHeight = this.$refs.networkView.offsetHeight;
        this.elWidth = this.$refs.networkView.offsetWidth;
        const dataStore = useDataStore();
        this.all_data = dataStore.all_data;
        this.category_data = dataStore.categorySource;
        this.select_video = dataStore.select_video;
        this.selectShowLevel = dataStore.selectShowLevel;
        this.showTagList = dataStore.showTagList;
        if (this.showTagList.length == 0) {
            let tagTmp = [];
            for (let i in this.category_data) {
                tagTmp.push(this.category_data[i].id);
            }
            this.showTagList = tagTmp;
        }
        if (this.viewTag) {
            this.chart_data = this.calcNetwork(this.all_data);
            this.paintNetwork(this.chart_data);
        } else {
            this.chart_data = this.calcSun(this.all_data);
            this.paintSunBurst(this.chart_data);
        }
        dataStore.$subscribe((mutations, states) => {
            this.all_data = states.all_data;
            this.category_data = states.categorySource;
            this.select_video = dataStore.select_video;
            this.selectShowLevel = dataStore.selectShowLevel;
            this.showTagList = dataStore.showTagList;
            console.log(this.showTagList, this.showTagList.length)
            if (this.showTagList.length == 0) {
                let tagTmp = [];
                for (let i in this.category_data) {
                    tagTmp.push(this.category_data[i].id);
                }
                this.showTagList = tagTmp;
            }
            if (this.viewTag) {
                this.chart_data = this.calcNetwork(this.all_data);
                this.paintNetwork(this.chart_data);
            } else {
                this.chart_data = this.calcSun(this.all_data);
                this.paintSunBurst(this.chart_data);
            }
        });
    },
    watch: {
        overviewTag: {
            handler() {
                if (this.viewTag) {
                    this.chart_data = this.calcNetwork(this.all_data);
                    this.paintNetwork(this.chart_data);
                } else {
                    this.chart_data = this.calcSun(this.all_data);
                    this.paintSunBurst(this.chart_data);
                }
            },
            deep: true
        },
        viewTag: {
            handler() {
                if (this.viewTag) {
                    this.chart_data = this.calcNetwork(this.all_data);
                    this.paintNetwork(this.chart_data);
                } else {
                    this.chart_data = this.calcSun(this.all_data);
                    this.paintSunBurst(this.chart_data);
                }
            }
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

.progress_marker {
    border: 0px solid red;
    /* transition: .1s; */
}

.progress_marker:hover {
    border-width: 4px;
}

.el-textarea__inner {
    background-color: #45464700;
    color: white;
    font-size: 18px;
}

.show_info_dialog {
    --el-dialog-bg-color: #454647AA;
    color: white;
    position: absolute;
    left: calc(35vw - 12.5%);
    top: calc(5%);
    border-radius: 15px;
    /* left: 100px; */
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

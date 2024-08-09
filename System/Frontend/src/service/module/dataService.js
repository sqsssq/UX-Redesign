/*
 * @Description: 
 * @Author: Qing Shi
 * @Date: 2022-11-20 19:23:35
 * @LastEditTime: 2022-11-22 17:18:36
 */

import axios from 'axios';

// axios.defaults.withCredentials = true
const TEST_URL_PREFIX = 'https://43.133.208.67:5000/api/test';

// const TEST_URL_PREFIX = 'http://127.0.0.1:5000/api/test';

export function fetchHello(param, callback) {
    const url = `${TEST_URL_PREFIX}/hello/`;
    axios.post(url, param)
        .then(response => {
            callback(response.data)
        }, errResponse => {
            console.log(errResponse)
        })
}

export function uploadData(param, callback) {
    const url = `${TEST_URL_PREFIX}/upload/`;
    axios.post(url, param)
    .then(response => {
        callback(response.data);
    }, errResponse => {
        console.log(errResponse);
    })
}

export function fetchAllData(param, callback) {
    const url = `${TEST_URL_PREFIX}/fetch/`;
    axios.post(url, param)
    .then(response => {
        callback(response);
    }, errResponse => {
        console.log(errResponse);
    })
}

export async function queryRecommendation(param) {
    const url = `${TEST_URL_PREFIX}/Recommendation`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    })
    return data;
}

export async function queryNewTag(param) {
    const url = `${TEST_URL_PREFIX}/NewTag`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    })
    return data;
}

export async function saveData(param) {
    const url = `${TEST_URL_PREFIX}/Save`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    })
    return data;
}

export async function tagOptimize(param) {
    const url = `${TEST_URL_PREFIX}/TagOp`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    });
    return data;
}

export async function generalChat(param) {
    const url = `${TEST_URL_PREFIX}/GeneralChat`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    });
    return data;
}

export async function addMetric(param) {
    const url = `${TEST_URL_PREFIX}/AddMetric`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    });
    return data;
}

export async function solutionChat(param) {
    const url = `${TEST_URL_PREFIX}/SolutionChat`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    });
    return data;
}

export async function generatePoint(param) {
    const url = `${TEST_URL_PREFIX}/GeneratePoint`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    });
    return data;
}

export async function evaluatePoint(param) {
    const url = `${TEST_URL_PREFIX}/EvaluatePoint`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    });
    return data;
}


export async function save(param) {
    const url = `${TEST_URL_PREFIX}/Save`;
    const jsonString = JSON.stringify(param);
    const data = await axios({
        method: "post",
        url: url,
        headers: {
            "Content-Type": "application/json",
        },
        data: jsonString
    });
    return data;
}
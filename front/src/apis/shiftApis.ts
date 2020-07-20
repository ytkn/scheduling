import axios from "axios";
import { BASE_URL } from "../constants";
import { Instance } from "../types/instance";


export const getInstances = () => {
  return axios({
    method: 'get',
    url: `${BASE_URL}/instances`
  }).then(response => response.data as string[])
}

export const getInstance = (file: string) => {
  return axios({
    method: 'get',
    url: `${BASE_URL}/instances/${file}`
  }).then(response => response.data as Instance)
}

export const getSolutionBySolver = (file: string) => {
  return axios({
    method: 'get',
    url: `${BASE_URL}/instances/${file}/solutions/solver`
  }).then(response => response.data as number[][][])
}

export const getSolutions = (instanceName: string) => {
  return axios({
    method: 'get',
    url: `${BASE_URL}/instances/${instanceName}/solutions`
  }).then(response => response.data as string[])
}

export const getSolution = (instanceName: string, solutionName: string) => {
  return axios({
    method: 'get',
    url: `${BASE_URL}/instances/${instanceName}/solutions/${solutionName}`
  }).then(response => response.data as number[][][])
}
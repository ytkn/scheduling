import axios from "axios";
import { BASE_URL } from "../constants";
import { Instance } from "../types/instance";

export const getInstance = (file: string) => {
  return axios({
    method: 'get',
    url: `${BASE_URL}/instances/${file}`
  }).then(response => response.data as Instance)
}

export const getSolution = (file: string) => {
  return axios({
    method: 'get',
    url: `${BASE_URL}/instances/${file}/solution`
  }).then(response => response.data as number[][][])
}
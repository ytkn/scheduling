import React, { useEffect, useState } from 'react';
import ShiftTable from '../organisms/ShiftTable';
import * as shiftApis from '../apis/shiftApis'
import { Instance } from "../types/instance"
import ShiftPageScss from "../css/ShiftPage.scss"
import classnames from 'classnames'
import Loading from '../atoms/Loading';

const ShiftPage: React.FC = () => {

  const [instanceNames, setInstanceNames] = useState<string[]>([])
  const [solutionNames, setSolutionNames] = useState<string[]>([])
  const [isLoading, setIsLoading] = useState(true)
  const [instanceName, setInstanceName] = useState<string>()
  const [solutionName, setSolutionName] = useState<string>()
  const [instance, setInstance] = useState<Instance>()
  const [solution, setSolution] = useState<number[][][]>()

  const fetchInitialData = async () => {
    const instances = await shiftApis.getInstances()
    setInstanceNames(instances)
    setIsLoading(false)
  }

  const fetchInstance = async () => {
    setIsLoading(true)
    if (instanceName === undefined) return
    const instance = await shiftApis.getInstance(instanceName)
    const solutionNames = await shiftApis.getSolutions(instanceName)
    const solution = await shiftApis.getSolution(instanceName, solutionNames[0])
    setSolutionNames(solutionNames)
    setInstance(instance)
    setSolution(solution)
    setIsLoading(false)
  }

  const fetchSolution = async () => {
    setIsLoading(true)
    if (instanceName === undefined) return
    const solution = await shiftApis.getSolution(instanceName, solutionName)
    setSolutionNames(solutionNames)
    setInstance(instance)
    setSolution(solution)
    setIsLoading(false)
  }

  useEffect(() => {
    fetchInitialData()
  }, [])

  useEffect(() => {
    fetchInstance()
  }, [instanceName])

  useEffect(() => {
    fetchSolution()
  }, [solutionName])

  return (
    <div>
      <h1>shift</h1>
      <div className={ShiftPageScss['selector']}>
        {instanceNames.map(name =>
          <div
            key={name}
            className={
              name === instanceName ?
                classnames([
                  ShiftPageScss['selector__item--selected'],
                  ShiftPageScss['selector__item']
                ]) :
                ShiftPageScss['selector__item']}
            onClick={() => {
              setIsLoading(true)
              setInstanceName(name)
            }}
          >
            {name}
          </div>
        )}
      </div>
      <div className={ShiftPageScss['selector']}>
        {[...solutionNames, "solver"].map(name =>
          <div
            key={name}
            className={
              name === solutionName ?
                classnames([
                  ShiftPageScss['selector__item--selected'],
                  ShiftPageScss['selector__item']
                ]) :
                ShiftPageScss['selector__item']}
            onClick={() => {
              setIsLoading(true)
              setSolutionName(name)
            }}
          >
            {name}
          </div>
        )}
      </div>
      {!isLoading && instanceName && <ShiftTable instance={instance} solution={solution} />}
      {isLoading && <Loading />}
    </div>)
}


export default ShiftPage
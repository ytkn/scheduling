import React, { useEffect, useState } from 'react';
import ShiftTable from '../organisms/ShiftTable';
import * as shiftActions from '../actions/shiftActions'
import { Instance } from "../types/instance"
import ShiftPageScss from "../css/ShiftPage.scss"
import classnames from 'classnames'
import Loading from '../atoms/Loading';

const ShiftPage: React.FC = () => {
  const instanceNames = ['Instance1', 'Instance2', 'Instance3']

  const [isLoading, setIsLoading] = useState(true)
  const [instanceName, setInstanceName] = useState<string>(instanceNames[0])
  const [instance, setInstance] = useState<Instance>()
  const [solution, setSolution] = useState<number[][][]>()

  const fetchInstance = async () => {
    setIsLoading(true)
    const ins = await shiftActions.getInstance(instanceName)
    const sol = await shiftActions.getSolution(instanceName)
    setInstance(ins)
    setSolution(sol)
    setIsLoading(false)
  }

  useEffect(() => {
    fetchInstance()
  }, [instanceName])


  return (
    <div>
      <h1>shift</h1>
      <div className={ShiftPageScss['selector']}>
        {instanceNames.map(name =>
          <div
            key={name}
            className={
              name === instanceName ?
                classnames([ShiftPageScss['selector__item--selected'], ShiftPageScss['selector__item']]) :
                ShiftPageScss['selector__item']}
            onClick={() => setInstanceName(name)}
          >
            {name}
          </div>
        )}
      </div>
      {!isLoading && <ShiftTable instance={instance} solution={solution} />}
      {isLoading && <Loading />}
    </div>)
}


export default ShiftPage
import React from 'react';
import ShiftTablsScss from "../css/ShiftTable.scss"
import classnames from "classnames"

type Props = {
  color: string
  label: string
}

const Legend: React.FC<Props> = (props: Props) =>
  <div className={ShiftTablsScss['legend']}>
    <div className={
      classnames([ShiftTablsScss['legend__box'], ShiftTablsScss[`legend__box--${props.color}`]])}>
    </div>
    <div>{props.label}</div>
  </div>


export default Legend
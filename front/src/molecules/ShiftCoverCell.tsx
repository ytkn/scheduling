import React from 'react';
import ShiftTablsScss from "../css/ShiftTable.scss"
import Balloon from '../atoms/Balloon';

type Props = {
  style: string
  penalty: number
  shiftCover: number
}

const ShiftCoverCell: React.FC<Props> = (props: Props) =>
  <td className={props.style}>
    {props.shiftCover}
    {props.penalty &&
      <div className={ShiftTablsScss['penaltyBox']}>
        <div className={ShiftTablsScss['penalty']}>
          <Balloon text={`penalty:${props.penalty}`} />
        </div>
      </div>}
  </td>


export default ShiftCoverCell
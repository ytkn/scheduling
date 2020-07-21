import React from 'react';
import ShiftTablsScss from "../css/ShiftTable.scss"
import Balloon from '../atoms/Balloon';
import { ShiftRequest } from '../types/instance';

type Props = {
  style: string
  penalty: number
  shiftString: string
  hasOnRequest: boolean
  hasOffRequest: boolean
  onRequest: ShiftRequest
  offRequest: ShiftRequest
}

const ShiftCell: React.FC<Props> = (props: Props) =>
  <td
    className={props.style}
  >
    {`${props.shiftString}`}
    {`${props.hasOnRequest ? '/' + props.onRequest.shift_id : ''}`}
    {`${props.hasOffRequest ? '/!' + props.offRequest.shift_id : ''}`}
    {props.penalty &&
      <div className={ShiftTablsScss['penaltyBox']}>
        <div className={ShiftTablsScss['penalty']}>
          <Balloon text={`penalty:${props.penalty}`} />
        </div>
      </div>}
  </td>


export default ShiftCell